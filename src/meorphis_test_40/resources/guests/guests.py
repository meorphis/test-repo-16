# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .payments import (
    PaymentsResource,
    AsyncPaymentsResource,
    PaymentsResourceWithRawResponse,
    AsyncPaymentsResourceWithRawResponse,
    PaymentsResourceWithStreamingResponse,
    AsyncPaymentsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["GuestsResource", "AsyncGuestsResource"]


class GuestsResource(SyncAPIResource):
    @cached_property
    def payments(self) -> PaymentsResource:
        return PaymentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> GuestsResourceWithRawResponse:
        return GuestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GuestsResourceWithStreamingResponse:
        return GuestsResourceWithStreamingResponse(self)


class AsyncGuestsResource(AsyncAPIResource):
    @cached_property
    def payments(self) -> AsyncPaymentsResource:
        return AsyncPaymentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncGuestsResourceWithRawResponse:
        return AsyncGuestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGuestsResourceWithStreamingResponse:
        return AsyncGuestsResourceWithStreamingResponse(self)


class GuestsResourceWithRawResponse:
    def __init__(self, guests: GuestsResource) -> None:
        self._guests = guests

    @cached_property
    def payments(self) -> PaymentsResourceWithRawResponse:
        return PaymentsResourceWithRawResponse(self._guests.payments)


class AsyncGuestsResourceWithRawResponse:
    def __init__(self, guests: AsyncGuestsResource) -> None:
        self._guests = guests

    @cached_property
    def payments(self) -> AsyncPaymentsResourceWithRawResponse:
        return AsyncPaymentsResourceWithRawResponse(self._guests.payments)


class GuestsResourceWithStreamingResponse:
    def __init__(self, guests: GuestsResource) -> None:
        self._guests = guests

    @cached_property
    def payments(self) -> PaymentsResourceWithStreamingResponse:
        return PaymentsResourceWithStreamingResponse(self._guests.payments)


class AsyncGuestsResourceWithStreamingResponse:
    def __init__(self, guests: AsyncGuestsResource) -> None:
        self._guests = guests

    @cached_property
    def payments(self) -> AsyncPaymentsResourceWithStreamingResponse:
        return AsyncPaymentsResourceWithStreamingResponse(self._guests.payments)
