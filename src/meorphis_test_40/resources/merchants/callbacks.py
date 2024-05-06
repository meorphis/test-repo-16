# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import (
    make_request_options,
)
from ...types.merchants import callback_merchant_callbacks_update_params
from ...types.merchants.callback_list_response import CallbackListResponse
from ...types.merchants.callback_merchant_callbacks_update_response import CallbackMerchantCallbacksUpdateResponse

__all__ = ["CallbacksResource", "AsyncCallbacksResource"]


class CallbacksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CallbacksResourceWithRawResponse:
        return CallbacksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CallbacksResourceWithStreamingResponse:
        return CallbacksResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CallbackListResponse:
        """Return callback URLs configured on the merchant such as OAuth URLs."""
        return self._get(
            "/merchant/callbacks",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallbackListResponse,
        )

    def merchant_callbacks_update(
        self,
        *,
        account_page: str | NotGiven = NOT_GIVEN,
        base_domain: str | NotGiven = NOT_GIVEN,
        confirmation_redirect: str | NotGiven = NOT_GIVEN,
        create_order: str | NotGiven = NOT_GIVEN,
        debug: str | NotGiven = NOT_GIVEN,
        get_account: str | NotGiven = NOT_GIVEN,
        mobile_app_domain: str | NotGiven = NOT_GIVEN,
        oauth_logout: str | NotGiven = NOT_GIVEN,
        oauth_redirect: str | NotGiven = NOT_GIVEN,
        privacy_policy: str | NotGiven = NOT_GIVEN,
        product_info: str | NotGiven = NOT_GIVEN,
        remote_api: str | NotGiven = NOT_GIVEN,
        shipping: str | NotGiven = NOT_GIVEN,
        support_page: str | NotGiven = NOT_GIVEN,
        tax: str | NotGiven = NOT_GIVEN,
        terms_of_service: str | NotGiven = NOT_GIVEN,
        universal_merchant_api: str | NotGiven = NOT_GIVEN,
        update_cart: str | NotGiven = NOT_GIVEN,
        validate_additional_account_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CallbackMerchantCallbacksUpdateResponse:
        """
        Update and configure callback URLs on the merchant such as OAuth URLs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            "/merchant/callbacks",
            body=maybe_transform(
                {
                    "account_page": account_page,
                    "base_domain": base_domain,
                    "confirmation_redirect": confirmation_redirect,
                    "create_order": create_order,
                    "debug": debug,
                    "get_account": get_account,
                    "mobile_app_domain": mobile_app_domain,
                    "oauth_logout": oauth_logout,
                    "oauth_redirect": oauth_redirect,
                    "privacy_policy": privacy_policy,
                    "product_info": product_info,
                    "remote_api": remote_api,
                    "shipping": shipping,
                    "support_page": support_page,
                    "tax": tax,
                    "terms_of_service": terms_of_service,
                    "universal_merchant_api": universal_merchant_api,
                    "update_cart": update_cart,
                    "validate_additional_account_data": validate_additional_account_data,
                },
                callback_merchant_callbacks_update_params.CallbackMerchantCallbacksUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallbackMerchantCallbacksUpdateResponse,
        )


class AsyncCallbacksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCallbacksResourceWithRawResponse:
        return AsyncCallbacksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCallbacksResourceWithStreamingResponse:
        return AsyncCallbacksResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CallbackListResponse:
        """Return callback URLs configured on the merchant such as OAuth URLs."""
        return await self._get(
            "/merchant/callbacks",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallbackListResponse,
        )

    async def merchant_callbacks_update(
        self,
        *,
        account_page: str | NotGiven = NOT_GIVEN,
        base_domain: str | NotGiven = NOT_GIVEN,
        confirmation_redirect: str | NotGiven = NOT_GIVEN,
        create_order: str | NotGiven = NOT_GIVEN,
        debug: str | NotGiven = NOT_GIVEN,
        get_account: str | NotGiven = NOT_GIVEN,
        mobile_app_domain: str | NotGiven = NOT_GIVEN,
        oauth_logout: str | NotGiven = NOT_GIVEN,
        oauth_redirect: str | NotGiven = NOT_GIVEN,
        privacy_policy: str | NotGiven = NOT_GIVEN,
        product_info: str | NotGiven = NOT_GIVEN,
        remote_api: str | NotGiven = NOT_GIVEN,
        shipping: str | NotGiven = NOT_GIVEN,
        support_page: str | NotGiven = NOT_GIVEN,
        tax: str | NotGiven = NOT_GIVEN,
        terms_of_service: str | NotGiven = NOT_GIVEN,
        universal_merchant_api: str | NotGiven = NOT_GIVEN,
        update_cart: str | NotGiven = NOT_GIVEN,
        validate_additional_account_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CallbackMerchantCallbacksUpdateResponse:
        """
        Update and configure callback URLs on the merchant such as OAuth URLs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            "/merchant/callbacks",
            body=await async_maybe_transform(
                {
                    "account_page": account_page,
                    "base_domain": base_domain,
                    "confirmation_redirect": confirmation_redirect,
                    "create_order": create_order,
                    "debug": debug,
                    "get_account": get_account,
                    "mobile_app_domain": mobile_app_domain,
                    "oauth_logout": oauth_logout,
                    "oauth_redirect": oauth_redirect,
                    "privacy_policy": privacy_policy,
                    "product_info": product_info,
                    "remote_api": remote_api,
                    "shipping": shipping,
                    "support_page": support_page,
                    "tax": tax,
                    "terms_of_service": terms_of_service,
                    "universal_merchant_api": universal_merchant_api,
                    "update_cart": update_cart,
                    "validate_additional_account_data": validate_additional_account_data,
                },
                callback_merchant_callbacks_update_params.CallbackMerchantCallbacksUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallbackMerchantCallbacksUpdateResponse,
        )


class CallbacksResourceWithRawResponse:
    def __init__(self, callbacks: CallbacksResource) -> None:
        self._callbacks = callbacks

        self.list = to_raw_response_wrapper(
            callbacks.list,
        )
        self.merchant_callbacks_update = to_raw_response_wrapper(
            callbacks.merchant_callbacks_update,
        )


class AsyncCallbacksResourceWithRawResponse:
    def __init__(self, callbacks: AsyncCallbacksResource) -> None:
        self._callbacks = callbacks

        self.list = async_to_raw_response_wrapper(
            callbacks.list,
        )
        self.merchant_callbacks_update = async_to_raw_response_wrapper(
            callbacks.merchant_callbacks_update,
        )


class CallbacksResourceWithStreamingResponse:
    def __init__(self, callbacks: CallbacksResource) -> None:
        self._callbacks = callbacks

        self.list = to_streamed_response_wrapper(
            callbacks.list,
        )
        self.merchant_callbacks_update = to_streamed_response_wrapper(
            callbacks.merchant_callbacks_update,
        )


class AsyncCallbacksResourceWithStreamingResponse:
    def __init__(self, callbacks: AsyncCallbacksResource) -> None:
        self._callbacks = callbacks

        self.list = async_to_streamed_response_wrapper(
            callbacks.list,
        )
        self.merchant_callbacks_update = async_to_streamed_response_wrapper(
            callbacks.merchant_callbacks_update,
        )
