# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "PaymentMethodAccountAddPaymentMethodParams",
    "BillingAddress",
    "BillingAddressAddressReferenceID",
    "BillingAddressAddressReferenceExplicit",
]


class PaymentMethodAccountAddPaymentMethodParams(TypedDict, total=False):
    token: Required[str]
    """The Bolt token associated to the credit card."""

    tag: Required[Annotated[Literal["credit_card"], PropertyInfo(alias=".tag")]]

    billing_address: Required[BillingAddress]
    """The credit card's billing address"""

    bin: Required[str]
    """The Bank Identification Number for the credit card.

    This is typically the first 4-6 digits of the credit card number.
    """

    expiration: Required[str]
    """The expiration date of the credit card. TODO TO MAKE EXPIRATION REUSABLE"""

    last4: Required[str]
    """The last 4 digits of the credit card number."""

    network: Required[Literal["visa", "mastercard", "amex", "discover", "jcb", "unionpay", "alliancedata", "citiplcc"]]
    """The credit card network."""

    type: Required[object]


class BillingAddressAddressReferenceID(TypedDict, total=False):
    id: Required[str]
    """The address's ID"""

    tag: Required[Annotated[Literal["id"], PropertyInfo(alias=".tag")]]
    """The type of address reference"""


class BillingAddressAddressReferenceExplicit(TypedDict, total=False):
    tag: Required[Annotated[Literal["explicit"], PropertyInfo(alias=".tag")]]
    """The type of address reference"""

    country_code: Required[str]

    first_name: Required[str]

    last_name: Required[str]

    locality: Required[str]

    postal_code: Required[str]

    street_address1: Required[str]

    company: str

    email: str

    phone: str

    region: str

    street_address2: str


BillingAddress = Union[BillingAddressAddressReferenceID, BillingAddressAddressReferenceExplicit]
