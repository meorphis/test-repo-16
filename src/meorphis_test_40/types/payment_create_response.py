# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PaymentCreateResponse", "Action"]


class Action(BaseModel):
    method: Optional[Literal["GET", "POST"]] = None

    type: Optional[Literal["redirect", "finalize"]] = None

    url: Optional[str] = None


class PaymentCreateResponse(BaseModel):
    id: Optional[str] = None

    action: Optional[Action] = None

    status: Optional[Literal["awaiting_user_confirmation", "payment_ready", "update_payment_method", "success"]] = None
