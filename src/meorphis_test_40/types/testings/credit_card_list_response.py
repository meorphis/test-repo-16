# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["CreditCardListResponse"]


class CreditCardListResponse(BaseModel):
    expiration: str
    """The expiration date of the credit card. TODO TO MAKE EXPIRATION REUSABLE"""

    last4: str
    """The last 4 digits of the credit card number."""

    network: Literal["visa", "mastercard", "amex", "discover", "jcb", "unionpay", "alliancedata", "citiplcc"]
    """The credit card network."""
