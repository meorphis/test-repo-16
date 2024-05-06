# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "PaymentGuestPaymentsInitializeParams",
    "Cart",
    "CartAmounts",
    "CartDiscount",
    "CartDiscountAmounts",
    "CartItem",
    "CartShipment",
    "CartShipmentAddress",
    "CartShipmentAddressAddressReferenceID",
    "CartShipmentAddressAddressReferenceExplicit",
    "CartShipmentCost",
    "PaymentMethod",
]


class PaymentGuestPaymentsInitializeParams(TypedDict, total=False):
    cart: Required[Cart]

    payment_method: Required[PaymentMethod]


class CartAmounts(TypedDict, total=False):
    currency: Required[str]

    total: Required[int]
    """The total amount, in cents, including its items and taxes (if applicable)."""

    tax: int
    """The total tax amount, in cents for all of the items associated with the cart."""


class CartDiscountAmounts(TypedDict, total=False):
    currency: Required[str]

    total: Required[int]
    """The total amount, in cents, including its items and taxes (if applicable)."""

    tax: int
    """The total tax amount, in cents for all of the items associated with the cart."""


class CartDiscount(TypedDict, total=False):
    amounts: Required[CartDiscountAmounts]

    code: str
    """Discount code."""

    details_url: str
    """
    Used to provide a link to additional details, such as a landing page, associated
    with the discount offering.
    """


class CartItem(TypedDict, total=False):
    name: Required[str]
    """The name of a given item."""

    quantity: Required[int]
    """The number of units that comprise this cart item."""

    reference: Required[str]
    """This value is used by Bolt as an external reference to a given item."""

    total_amount: Required[int]
    """The total amount, in cents, of the item including its taxes if applicable."""

    unit_price: Required[int]
    """The price of one unit of the item; for example, the price of one pack of socks."""

    description: str
    """A human-readable description of this cart item."""

    image_url: str
    """Used to provide a link to the image associated with the item."""


class CartShipmentAddressAddressReferenceID(TypedDict, total=False):
    id: Required[str]
    """The address's ID"""

    tag: Required[Annotated[Literal["id"], PropertyInfo(alias=".tag")]]
    """The type of address reference"""


class CartShipmentAddressAddressReferenceExplicit(TypedDict, total=False):
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


CartShipmentAddress = Union[CartShipmentAddressAddressReferenceID, CartShipmentAddressAddressReferenceExplicit]


class CartShipmentCost(TypedDict, total=False):
    currency: Required[str]

    total: Required[int]
    """The total amount, in cents, including its items and taxes (if applicable)."""

    tax: int
    """The total tax amount, in cents for all of the items associated with the cart."""


class CartShipment(TypedDict, total=False):
    address: CartShipmentAddress
    """The Address object is used for shipping, and physical store address use cases."""

    carrier: str
    """The name of the carrier selected."""

    cost: CartShipmentCost


class Cart(TypedDict, total=False):
    amounts: Required[CartAmounts]

    order_reference: Required[str]
    """This value is used by Bolt as an external reference to a given order.

    This reference must be unique per successful transaction.
    """

    discounts: Iterable[CartDiscount]

    display_id: str
    """
    This field corresponds to the merchant's order reference associated with this
    Bolt transaction.
    """

    items: Iterable[CartItem]

    order_description: str
    """
    Used optionally to pass additional information like order numbers or other IDs
    as needed.
    """

    shipments: Iterable[CartShipment]


class PaymentMethod(TypedDict, total=False):
    tag: Required[Annotated[Literal["paypal"], PropertyInfo(alias=".tag")]]

    cancel: Required[str]
    """Redirect URL for canceled PayPal transaction."""

    success: Required[str]
    """Redirect URL for successful PayPal transaction."""
