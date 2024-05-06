# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["AddressAccountAddressCreateResponse"]


class AddressAccountAddressCreateResponse(BaseModel):
    id: str

    country_code: str

    first_name: str

    last_name: str

    locality: str

    postal_code: str

    street_address1: str

    company: Optional[str] = None

    email: Optional[str] = None

    is_default: Optional[bool] = None

    phone: Optional[str] = None

    region: Optional[str] = None

    street_address2: Optional[str] = None
