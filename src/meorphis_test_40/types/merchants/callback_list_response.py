# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["CallbackListResponse"]


class CallbackListResponse(BaseModel):
    account_page: Optional[str] = None

    base_domain: Optional[str] = None

    confirmation_redirect: Optional[str] = None

    create_order: Optional[str] = None

    debug: Optional[str] = None

    get_account: Optional[str] = None

    mobile_app_domain: Optional[str] = None

    oauth_logout: Optional[str] = None

    oauth_redirect: Optional[str] = None

    privacy_policy: Optional[str] = None

    product_info: Optional[str] = None

    remote_api: Optional[str] = None

    shipping: Optional[str] = None

    support_page: Optional[str] = None

    tax: Optional[str] = None

    terms_of_service: Optional[str] = None

    universal_merchant_api: Optional[str] = None

    update_cart: Optional[str] = None

    validate_additional_account_data: Optional[str] = None
