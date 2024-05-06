# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CallbackMerchantCallbacksUpdateParams"]


class CallbackMerchantCallbacksUpdateParams(TypedDict, total=False):
    account_page: str

    base_domain: str

    confirmation_redirect: str

    create_order: str

    debug: str

    get_account: str

    mobile_app_domain: str

    oauth_logout: str

    oauth_redirect: str

    privacy_policy: str

    product_info: str

    remote_api: str

    shipping: str

    support_page: str

    tax: str

    terms_of_service: str

    universal_merchant_api: str

    update_cart: str

    validate_additional_account_data: str
