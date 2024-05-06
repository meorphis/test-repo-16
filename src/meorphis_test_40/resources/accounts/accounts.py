# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .exists import (
    ExistsResource,
    AsyncExistsResource,
    ExistsResourceWithRawResponse,
    AsyncExistsResourceWithRawResponse,
    ExistsResourceWithStreamingResponse,
    AsyncExistsResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from .addresses import (
    AddressesResource,
    AsyncAddressesResource,
    AddressesResourceWithRawResponse,
    AsyncAddressesResourceWithRawResponse,
    AddressesResourceWithStreamingResponse,
    AsyncAddressesResourceWithStreamingResponse,
)
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
from .payment_methods import (
    PaymentMethodsResource,
    AsyncPaymentMethodsResource,
    PaymentMethodsResourceWithRawResponse,
    AsyncPaymentMethodsResourceWithRawResponse,
    PaymentMethodsResourceWithStreamingResponse,
    AsyncPaymentMethodsResourceWithStreamingResponse,
)
from ...types.account_account_get_response import AccountAccountGetResponse

__all__ = ["AccountsResource", "AsyncAccountsResource"]


class AccountsResource(SyncAPIResource):
    @cached_property
    def addresses(self) -> AddressesResource:
        return AddressesResource(self._client)

    @cached_property
    def exists(self) -> ExistsResource:
        return ExistsResource(self._client)

    @cached_property
    def payment_methods(self) -> PaymentMethodsResource:
        return PaymentMethodsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AccountsResourceWithRawResponse:
        return AccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountsResourceWithStreamingResponse:
        return AccountsResourceWithStreamingResponse(self)

    def account_get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountAccountGetResponse:
        """Retrieve a shopper's account details, such as addresses and payment information"""
        return self._get(
            "/account",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountAccountGetResponse,
        )


class AsyncAccountsResource(AsyncAPIResource):
    @cached_property
    def addresses(self) -> AsyncAddressesResource:
        return AsyncAddressesResource(self._client)

    @cached_property
    def exists(self) -> AsyncExistsResource:
        return AsyncExistsResource(self._client)

    @cached_property
    def payment_methods(self) -> AsyncPaymentMethodsResource:
        return AsyncPaymentMethodsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAccountsResourceWithRawResponse:
        return AsyncAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountsResourceWithStreamingResponse:
        return AsyncAccountsResourceWithStreamingResponse(self)

    async def account_get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountAccountGetResponse:
        """Retrieve a shopper's account details, such as addresses and payment information"""
        return await self._get(
            "/account",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountAccountGetResponse,
        )


class AccountsResourceWithRawResponse:
    def __init__(self, accounts: AccountsResource) -> None:
        self._accounts = accounts

        self.account_get = to_raw_response_wrapper(
            accounts.account_get,
        )

    @cached_property
    def addresses(self) -> AddressesResourceWithRawResponse:
        return AddressesResourceWithRawResponse(self._accounts.addresses)

    @cached_property
    def exists(self) -> ExistsResourceWithRawResponse:
        return ExistsResourceWithRawResponse(self._accounts.exists)

    @cached_property
    def payment_methods(self) -> PaymentMethodsResourceWithRawResponse:
        return PaymentMethodsResourceWithRawResponse(self._accounts.payment_methods)


class AsyncAccountsResourceWithRawResponse:
    def __init__(self, accounts: AsyncAccountsResource) -> None:
        self._accounts = accounts

        self.account_get = async_to_raw_response_wrapper(
            accounts.account_get,
        )

    @cached_property
    def addresses(self) -> AsyncAddressesResourceWithRawResponse:
        return AsyncAddressesResourceWithRawResponse(self._accounts.addresses)

    @cached_property
    def exists(self) -> AsyncExistsResourceWithRawResponse:
        return AsyncExistsResourceWithRawResponse(self._accounts.exists)

    @cached_property
    def payment_methods(self) -> AsyncPaymentMethodsResourceWithRawResponse:
        return AsyncPaymentMethodsResourceWithRawResponse(self._accounts.payment_methods)


class AccountsResourceWithStreamingResponse:
    def __init__(self, accounts: AccountsResource) -> None:
        self._accounts = accounts

        self.account_get = to_streamed_response_wrapper(
            accounts.account_get,
        )

    @cached_property
    def addresses(self) -> AddressesResourceWithStreamingResponse:
        return AddressesResourceWithStreamingResponse(self._accounts.addresses)

    @cached_property
    def exists(self) -> ExistsResourceWithStreamingResponse:
        return ExistsResourceWithStreamingResponse(self._accounts.exists)

    @cached_property
    def payment_methods(self) -> PaymentMethodsResourceWithStreamingResponse:
        return PaymentMethodsResourceWithStreamingResponse(self._accounts.payment_methods)


class AsyncAccountsResourceWithStreamingResponse:
    def __init__(self, accounts: AsyncAccountsResource) -> None:
        self._accounts = accounts

        self.account_get = async_to_streamed_response_wrapper(
            accounts.account_get,
        )

    @cached_property
    def addresses(self) -> AsyncAddressesResourceWithStreamingResponse:
        return AsyncAddressesResourceWithStreamingResponse(self._accounts.addresses)

    @cached_property
    def exists(self) -> AsyncExistsResourceWithStreamingResponse:
        return AsyncExistsResourceWithStreamingResponse(self._accounts.exists)

    @cached_property
    def payment_methods(self) -> AsyncPaymentMethodsResourceWithStreamingResponse:
        return AsyncPaymentMethodsResourceWithStreamingResponse(self._accounts.payment_methods)
