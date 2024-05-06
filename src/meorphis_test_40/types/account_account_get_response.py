# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "AccountAccountGetResponse",
    "Address",
    "PaymentMethod",
    "PaymentMethodBillingAddress",
    "PaymentMethodBillingAddressAddressReferenceID",
    "PaymentMethodBillingAddressAddressReferenceExplicit",
    "Profile",
]


class Address(BaseModel):
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


class PaymentMethodBillingAddressAddressReferenceID(BaseModel):
    id: str
    """The address's ID"""

    tag: Literal["id"] = FieldInfo(alias=".tag")
    """The type of address reference"""


class PaymentMethodBillingAddressAddressReferenceExplicit(BaseModel):
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


PaymentMethodBillingAddress = Union[
    PaymentMethodBillingAddressAddressReferenceID, PaymentMethodBillingAddressAddressReferenceExplicit
]


class PaymentMethod(BaseModel):
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


class Profile(BaseModel):
    email: Optional[str] = None
    """An email address."""

    first_name: Optional[str] = None
    """The given name of the person associated with this record."""

    last_name: Optional[str] = None
    """The last name of the person associated with this record."""

    phone: Optional[str] = None
    """A phone number following E164 standards, in its globalized format, i.e.

    prepended with a plus sign.
    """


class AccountAccountGetResponse(BaseModel):
    addresses: List[Address]

    payment_methods: List[PaymentMethod]

    profile: Optional[Profile] = None
