# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from .callbacks import (
    CallbacksResource,
    AsyncCallbacksResource,
    CallbacksResourceWithRawResponse,
    AsyncCallbacksResourceWithRawResponse,
    CallbacksResourceWithStreamingResponse,
    AsyncCallbacksResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .identifiers import (
    IdentifiersResource,
    AsyncIdentifiersResource,
    IdentifiersResourceWithRawResponse,
    AsyncIdentifiersResourceWithRawResponse,
    IdentifiersResourceWithStreamingResponse,
    AsyncIdentifiersResourceWithStreamingResponse,
)

__all__ = ["MerchantsResource", "AsyncMerchantsResource"]


class MerchantsResource(SyncAPIResource):
    @cached_property
    def callbacks(self) -> CallbacksResource:
        return CallbacksResource(self._client)

    @cached_property
    def identifiers(self) -> IdentifiersResource:
        return IdentifiersResource(self._client)

    @cached_property
    def with_raw_response(self) -> MerchantsResourceWithRawResponse:
        return MerchantsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MerchantsResourceWithStreamingResponse:
        return MerchantsResourceWithStreamingResponse(self)


class AsyncMerchantsResource(AsyncAPIResource):
    @cached_property
    def callbacks(self) -> AsyncCallbacksResource:
        return AsyncCallbacksResource(self._client)

    @cached_property
    def identifiers(self) -> AsyncIdentifiersResource:
        return AsyncIdentifiersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMerchantsResourceWithRawResponse:
        return AsyncMerchantsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMerchantsResourceWithStreamingResponse:
        return AsyncMerchantsResourceWithStreamingResponse(self)


class MerchantsResourceWithRawResponse:
    def __init__(self, merchants: MerchantsResource) -> None:
        self._merchants = merchants

    @cached_property
    def callbacks(self) -> CallbacksResourceWithRawResponse:
        return CallbacksResourceWithRawResponse(self._merchants.callbacks)

    @cached_property
    def identifiers(self) -> IdentifiersResourceWithRawResponse:
        return IdentifiersResourceWithRawResponse(self._merchants.identifiers)


class AsyncMerchantsResourceWithRawResponse:
    def __init__(self, merchants: AsyncMerchantsResource) -> None:
        self._merchants = merchants

    @cached_property
    def callbacks(self) -> AsyncCallbacksResourceWithRawResponse:
        return AsyncCallbacksResourceWithRawResponse(self._merchants.callbacks)

    @cached_property
    def identifiers(self) -> AsyncIdentifiersResourceWithRawResponse:
        return AsyncIdentifiersResourceWithRawResponse(self._merchants.identifiers)


class MerchantsResourceWithStreamingResponse:
    def __init__(self, merchants: MerchantsResource) -> None:
        self._merchants = merchants

    @cached_property
    def callbacks(self) -> CallbacksResourceWithStreamingResponse:
        return CallbacksResourceWithStreamingResponse(self._merchants.callbacks)

    @cached_property
    def identifiers(self) -> IdentifiersResourceWithStreamingResponse:
        return IdentifiersResourceWithStreamingResponse(self._merchants.identifiers)


class AsyncMerchantsResourceWithStreamingResponse:
    def __init__(self, merchants: AsyncMerchantsResource) -> None:
        self._merchants = merchants

    @cached_property
    def callbacks(self) -> AsyncCallbacksResourceWithStreamingResponse:
        return AsyncCallbacksResourceWithStreamingResponse(self._merchants.callbacks)

    @cached_property
    def identifiers(self) -> AsyncIdentifiersResourceWithStreamingResponse:
        return AsyncIdentifiersResourceWithStreamingResponse(self._merchants.identifiers)
