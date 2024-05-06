# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .accounts import (
    AccountsResource,
    AsyncAccountsResource,
    AccountsResourceWithRawResponse,
    AsyncAccountsResourceWithRawResponse,
    AccountsResourceWithStreamingResponse,
    AsyncAccountsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .shipments import (
    ShipmentsResource,
    AsyncShipmentsResource,
    ShipmentsResourceWithRawResponse,
    AsyncShipmentsResourceWithRawResponse,
    ShipmentsResourceWithStreamingResponse,
    AsyncShipmentsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .credit_cards import (
    CreditCardsResource,
    AsyncCreditCardsResource,
    CreditCardsResourceWithRawResponse,
    AsyncCreditCardsResourceWithRawResponse,
    CreditCardsResourceWithStreamingResponse,
    AsyncCreditCardsResourceWithStreamingResponse,
)

__all__ = ["TestingsResource", "AsyncTestingsResource"]


class TestingsResource(SyncAPIResource):
    __test__ = False

    @cached_property
    def accounts(self) -> AccountsResource:
        return AccountsResource(self._client)

    @cached_property
    def credit_cards(self) -> CreditCardsResource:
        return CreditCardsResource(self._client)

    @cached_property
    def shipments(self) -> ShipmentsResource:
        return ShipmentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> TestingsResourceWithRawResponse:
        return TestingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TestingsResourceWithStreamingResponse:
        return TestingsResourceWithStreamingResponse(self)


class AsyncTestingsResource(AsyncAPIResource):
    @cached_property
    def accounts(self) -> AsyncAccountsResource:
        return AsyncAccountsResource(self._client)

    @cached_property
    def credit_cards(self) -> AsyncCreditCardsResource:
        return AsyncCreditCardsResource(self._client)

    @cached_property
    def shipments(self) -> AsyncShipmentsResource:
        return AsyncShipmentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTestingsResourceWithRawResponse:
        return AsyncTestingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTestingsResourceWithStreamingResponse:
        return AsyncTestingsResourceWithStreamingResponse(self)


class TestingsResourceWithRawResponse:
    __test__ = False

    def __init__(self, testings: TestingsResource) -> None:
        self._testings = testings

    @cached_property
    def accounts(self) -> AccountsResourceWithRawResponse:
        return AccountsResourceWithRawResponse(self._testings.accounts)

    @cached_property
    def credit_cards(self) -> CreditCardsResourceWithRawResponse:
        return CreditCardsResourceWithRawResponse(self._testings.credit_cards)

    @cached_property
    def shipments(self) -> ShipmentsResourceWithRawResponse:
        return ShipmentsResourceWithRawResponse(self._testings.shipments)


class AsyncTestingsResourceWithRawResponse:
    def __init__(self, testings: AsyncTestingsResource) -> None:
        self._testings = testings

    @cached_property
    def accounts(self) -> AsyncAccountsResourceWithRawResponse:
        return AsyncAccountsResourceWithRawResponse(self._testings.accounts)

    @cached_property
    def credit_cards(self) -> AsyncCreditCardsResourceWithRawResponse:
        return AsyncCreditCardsResourceWithRawResponse(self._testings.credit_cards)

    @cached_property
    def shipments(self) -> AsyncShipmentsResourceWithRawResponse:
        return AsyncShipmentsResourceWithRawResponse(self._testings.shipments)


class TestingsResourceWithStreamingResponse:
    __test__ = False

    def __init__(self, testings: TestingsResource) -> None:
        self._testings = testings

    @cached_property
    def accounts(self) -> AccountsResourceWithStreamingResponse:
        return AccountsResourceWithStreamingResponse(self._testings.accounts)

    @cached_property
    def credit_cards(self) -> CreditCardsResourceWithStreamingResponse:
        return CreditCardsResourceWithStreamingResponse(self._testings.credit_cards)

    @cached_property
    def shipments(self) -> ShipmentsResourceWithStreamingResponse:
        return ShipmentsResourceWithStreamingResponse(self._testings.shipments)


class AsyncTestingsResourceWithStreamingResponse:
    def __init__(self, testings: AsyncTestingsResource) -> None:
        self._testings = testings

    @cached_property
    def accounts(self) -> AsyncAccountsResourceWithStreamingResponse:
        return AsyncAccountsResourceWithStreamingResponse(self._testings.accounts)

    @cached_property
    def credit_cards(self) -> AsyncCreditCardsResourceWithStreamingResponse:
        return AsyncCreditCardsResourceWithStreamingResponse(self._testings.credit_cards)

    @cached_property
    def shipments(self) -> AsyncShipmentsResourceWithStreamingResponse:
        return AsyncShipmentsResourceWithStreamingResponse(self._testings.shipments)
