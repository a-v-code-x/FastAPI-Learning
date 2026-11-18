from pydantic import BaseModel, field_validator


class PincodeRequest(BaseModel):
    pincode: str

    @field_validator("pincode")
    @classmethod
    def validate_pincode(cls, value: str):
        if len(value) != 6 or not value.isdigit():
            raise ValueError("Pincode must be exactly 6 digits")
        return value


class LocationResponse(BaseModel):
    pincode: str
    city: str
    state: str
    district: str


class BulkRequest(BaseModel):
    pincode: list[str]

    @field_validator("pincode")
    @classmethod
    def validate_pincodes(cls, values: list[str]):
        if not values:
            raise ValueError("At least one pincode is required")

        if len(values) > 20:
            raise ValueError("Maximum 20 pincodes allowed")

        for code in values:
            if len(code) != 6 or not code.isdigit():
                raise ValueError("Each pincode must be exactly 6 digits")

        return values


class BulkResponse(BaseModel):
    status: str = "success"
    found: int
    not_found: int
    result: list[LocationResponse]
    missing: list[str]
