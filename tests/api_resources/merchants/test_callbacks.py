# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from meorphis_test_40 import MeorphisTest40, AsyncMeorphisTest40
from meorphis_test_40.types.merchants import (
    CallbackListResponse,
    CallbackMerchantCallbacksUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCallbacks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: MeorphisTest40) -> None:
        callback = client.merchants.callbacks.list()
        assert_matches_type(CallbackListResponse, callback, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: MeorphisTest40) -> None:
        response = client.merchants.callbacks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        callback = response.parse()
        assert_matches_type(CallbackListResponse, callback, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: MeorphisTest40) -> None:
        with client.merchants.callbacks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            callback = response.parse()
            assert_matches_type(CallbackListResponse, callback, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_merchant_callbacks_update(self, client: MeorphisTest40) -> None:
        callback = client.merchants.callbacks.merchant_callbacks_update()
        assert_matches_type(CallbackMerchantCallbacksUpdateResponse, callback, path=["response"])

    @parametrize
    def test_method_merchant_callbacks_update_with_all_params(self, client: MeorphisTest40) -> None:
        callback = client.merchants.callbacks.merchant_callbacks_update(
            account_page="https://www.example.com/account",
            base_domain="https://www.example.com/",
            confirmation_redirect="https://www.example.com/bolt/redirect",
            create_order="https://www.example.com/bolt/order",
            debug="https://www.example.com/bolt/debug",
            get_account="https://www.example.com/bolt/account",
            mobile_app_domain="https://m.example.com/",
            oauth_logout="https://www.example.com/bolt/logout",
            oauth_redirect="https://www.example.com/bolt/oauth",
            privacy_policy="https://www.example.com/privacy-policy",
            product_info="https://www.example.com/bolt/product",
            remote_api="https://www.example.com/bolt/remote-api",
            shipping="https://www.example.com/bolt/shipping",
            support_page="https://www.example.com/help",
            tax="https://www.example.com/bolt/tax",
            terms_of_service="https://www.example.com/terms-of-service",
            universal_merchant_api="https://www.example.com/bolt/merchant-api",
            update_cart="https://www.example.com/bolt/cart",
            validate_additional_account_data="https://www.example.com/bolt/validate-account",
        )
        assert_matches_type(CallbackMerchantCallbacksUpdateResponse, callback, path=["response"])

    @parametrize
    def test_raw_response_merchant_callbacks_update(self, client: MeorphisTest40) -> None:
        response = client.merchants.callbacks.with_raw_response.merchant_callbacks_update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        callback = response.parse()
        assert_matches_type(CallbackMerchantCallbacksUpdateResponse, callback, path=["response"])

    @parametrize
    def test_streaming_response_merchant_callbacks_update(self, client: MeorphisTest40) -> None:
        with client.merchants.callbacks.with_streaming_response.merchant_callbacks_update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            callback = response.parse()
            assert_matches_type(CallbackMerchantCallbacksUpdateResponse, callback, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCallbacks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncMeorphisTest40) -> None:
        callback = await async_client.merchants.callbacks.list()
        assert_matches_type(CallbackListResponse, callback, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMeorphisTest40) -> None:
        response = await async_client.merchants.callbacks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        callback = await response.parse()
        assert_matches_type(CallbackListResponse, callback, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMeorphisTest40) -> None:
        async with async_client.merchants.callbacks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            callback = await response.parse()
            assert_matches_type(CallbackListResponse, callback, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_merchant_callbacks_update(self, async_client: AsyncMeorphisTest40) -> None:
        callback = await async_client.merchants.callbacks.merchant_callbacks_update()
        assert_matches_type(CallbackMerchantCallbacksUpdateResponse, callback, path=["response"])

    @parametrize
    async def test_method_merchant_callbacks_update_with_all_params(self, async_client: AsyncMeorphisTest40) -> None:
        callback = await async_client.merchants.callbacks.merchant_callbacks_update(
            account_page="https://www.example.com/account",
            base_domain="https://www.example.com/",
            confirmation_redirect="https://www.example.com/bolt/redirect",
            create_order="https://www.example.com/bolt/order",
            debug="https://www.example.com/bolt/debug",
            get_account="https://www.example.com/bolt/account",
            mobile_app_domain="https://m.example.com/",
            oauth_logout="https://www.example.com/bolt/logout",
            oauth_redirect="https://www.example.com/bolt/oauth",
            privacy_policy="https://www.example.com/privacy-policy",
            product_info="https://www.example.com/bolt/product",
            remote_api="https://www.example.com/bolt/remote-api",
            shipping="https://www.example.com/bolt/shipping",
            support_page="https://www.example.com/help",
            tax="https://www.example.com/bolt/tax",
            terms_of_service="https://www.example.com/terms-of-service",
            universal_merchant_api="https://www.example.com/bolt/merchant-api",
            update_cart="https://www.example.com/bolt/cart",
            validate_additional_account_data="https://www.example.com/bolt/validate-account",
        )
        assert_matches_type(CallbackMerchantCallbacksUpdateResponse, callback, path=["response"])

    @parametrize
    async def test_raw_response_merchant_callbacks_update(self, async_client: AsyncMeorphisTest40) -> None:
        response = await async_client.merchants.callbacks.with_raw_response.merchant_callbacks_update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        callback = await response.parse()
        assert_matches_type(CallbackMerchantCallbacksUpdateResponse, callback, path=["response"])

    @parametrize
    async def test_streaming_response_merchant_callbacks_update(self, async_client: AsyncMeorphisTest40) -> None:
        async with async_client.merchants.callbacks.with_streaming_response.merchant_callbacks_update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            callback = await response.parse()
            assert_matches_type(CallbackMerchantCallbacksUpdateResponse, callback, path=["response"])

        assert cast(Any, response.is_closed) is True
