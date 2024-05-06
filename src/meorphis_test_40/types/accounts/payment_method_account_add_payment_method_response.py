# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "PaymentMethodAccountAddPaymentMethodResponse",
    "BillingAddress",
    "BillingAddressAddressReferenceID",
    "BillingAddressAddressReferenceExplicit",
]


class BillingAddressAddressReferenceID(BaseModel):
    id: str
    """The address's ID"""

    tag: Literal["id"] = FieldInfo(alias=".tag")
    """The type of address reference"""


class BillingAddressAddressReferenceExplicit(BaseModel):
    id: str

    tag: Literal["explicit"] = FieldInfo(alias=".tag")
    """The type of address reference"""

    country_code: str

    first_name: str

    last_name: str

    locality: str

    postal_code: str

    street_address1: str

    company: Optional[str] = None

    email: Optional[str] = None

    phone: Optional[str] = None

    region: Optional[str] = None

    street_address2: Optional[str] = None


BillingAddress = Union[BillingAddressAddressReferenceID, BillingAddressAddressReferenceExplicit]


class PaymentMethodAccountAddPaymentMethodResponse(BaseModel):
    tag: Literal["credit_card"] = FieldInfo(alias=".tag")

    expiration: str
    """The expiration date of the credit card. TODO TO MAKE EXPIRATION REUSABLE"""

    last4: str
    """The last 4 digits of the credit card number."""

    network: Literal["visa", "mastercard", "amex", "discover", "jcb", "unionpay", "alliancedata", "citiplcc"]
    """The credit card network."""

    type: object

    id: Optional[str] = None

    billing_address_id: Optional[str] = None
    """The ID of credit card's billing address"""
