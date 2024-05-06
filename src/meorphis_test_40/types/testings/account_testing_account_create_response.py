# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AccountTestingAccountCreateResponse"]


class AccountTestingAccountCreateResponse(BaseModel):
    deactivate_at: datetime

    email: str

    email_state: Literal["missing", "unverified", "verified"]

    oauth_code: str

    otp_code: str

    phone: str

    phone_state: Literal["missing", "unverified", "verified"]
