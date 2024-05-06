# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["IdentifierListResponse", "MerchantDivision"]


class MerchantDivision(BaseModel):
    publishable_key: str


class IdentifierListResponse(BaseModel):
    merchant_divisions: List[MerchantDivision]

    merchant_id: str

    signing_secret: str
