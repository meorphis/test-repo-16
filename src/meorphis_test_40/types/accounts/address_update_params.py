# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AddressUpdateParams"]


class AddressUpdateParams(TypedDict, total=False):
    country_code: Required[str]

    first_name: Required[str]

    last_name: Required[str]

    locality: Required[str]

    postal_code: Required[str]

    street_address1: Required[str]

    company: str

    email: str

    is_default: bool

    phone: str

    region: str

    street_address2: str
