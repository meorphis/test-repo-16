# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ExistListParams", "Identifier"]


class ExistListParams(TypedDict, total=False):
    identifier: Required[Identifier]
    """
    A type and value combination that defines the identifier used to detect the
    existence of an account.
    """


class Identifier(TypedDict, total=False):
    identifier_type: Required[Literal["email", "email_sha256"]]
    """The type of identifier"""

    identifier_value: Required[str]
    """The value of the identifier.

    The value must be valid for the specified `identifier_type`
    """
