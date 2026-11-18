from fastapi import FastAPI
from exceptions import (
    PinCodeNotFoundError,
    pincode_not_found_handler,
    InvalidPinCodeError,
    invalid_pincode_handler,
)
from models import LocationResponse, BulkRequest, BulkResponse
from data import pincode_db

app = FastAPI(
    title="picode lookup API",
    description="Auto Fill city and state from Indian pincode during checkout",
)


app.add_exception_handler(PinCodeNotFoundError, pincode_not_found_handler)
app.add_exception_handler(InvalidPinCodeError, invalid_pincode_handler)


@app.get("/")
def root():
    return {"message": "Pincode lookup API"}


@app.get("/pincode/{code}", response_model=LocationResponse)
def lookup_pincode(code: str):
    if len(code) != 6 or not code.isdigit():
        raise InvalidPinCodeError(code, "must be exactly 6 digit ")

    if code not in pincode_db:
        raise PinCodeNotFoundError(code)
    return pincode_db[code]


@app.post("/pincode/bulk", response_model=BulkResponse)
def bulk_lookup(request: BulkRequest):
    result = [
        LocationResponse.model_validate(pincode_db[code])
        for code in request.pincode
        if code in pincode_db
    ]
    missing = [code for code in request.pincode if code not in pincode_db]
    return BulkResponse(
        found=len(result), not_found=len(missing), result=result, missing=missing
    )
