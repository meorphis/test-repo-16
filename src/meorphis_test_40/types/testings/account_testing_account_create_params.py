# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AccountTestingAccountCreateParams"]


class AccountTestingAccountCreateParams(TypedDict, total=False):
    deactivate_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    email_state: Required[Literal["missing", "unverified", "verified"]]

    phone_state: Required[Literal["missing", "unverified", "verified"]]

    has_address: bool

    is_migrated: bool
