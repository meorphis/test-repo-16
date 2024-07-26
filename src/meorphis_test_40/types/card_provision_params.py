# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Annotated, Literal

from typing import Union

from .._types import Base64FileInput

from .._utils import PropertyInfo

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["CardProvisionParams"]

class CardProvisionParams(TypedDict, total=False):
    certificate: Annotated[Union[str, Base64FileInput], PropertyInfo(format = "base64")]
    """Only applicable if `digital_wallet` is `APPLE_PAY`.

    Omit to receive only `activationData` in the response. Apple's public leaf
    certificate. Base64 encoded in PEM format with headers
    `(-----BEGIN CERTIFICATE-----)` and trailers omitted. Provided by the device's
    wallet.
    """

    digital_wallet: Literal["APPLE_PAY", "GOOGLE_PAY", "SAMSUNG_PAY"]
    """Name of digital wallet provider."""

    nonce: Annotated[Union[str, Base64FileInput], PropertyInfo(format = "base64")]
    """Only applicable if `digital_wallet` is `APPLE_PAY`.

    Omit to receive only `activationData` in the response. Base64 cryptographic
    nonce provided by the device's wallet.
    """

    nonce_signature: Annotated[Union[str, Base64FileInput], PropertyInfo(format = "base64")]
    """Only applicable if `digital_wallet` is `APPLE_PAY`.

    Omit to receive only `activationData` in the response. Base64 cryptographic
    nonce provided by the device's wallet.
    """

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]