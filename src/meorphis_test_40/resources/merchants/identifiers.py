# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ...types.merchants.identifier_list_response import IdentifierListResponse

__all__ = ["IdentifiersResource", "AsyncIdentifiersResource"]


class IdentifiersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IdentifiersResourceWithRawResponse:
        return IdentifiersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IdentifiersResourceWithStreamingResponse:
        return IdentifiersResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentifierListResponse:
        """
        Return several identifiers for the merchant, such as public IDs, publishable
        keys, signing secrets, etc...
        """
        return self._get(
            "/merchant/identifiers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IdentifierListResponse,
        )


class AsyncIdentifiersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIdentifiersResourceWithRawResponse:
        return AsyncIdentifiersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIdentifiersResourceWithStreamingResponse:
        return AsyncIdentifiersResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentifierListResponse:
        """
        Return several identifiers for the merchant, such as public IDs, publishable
        keys, signing secrets, etc...
        """
        return await self._get(
            "/merchant/identifiers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IdentifierListResponse,
        )


class IdentifiersResourceWithRawResponse:
    def __init__(self, identifiers: IdentifiersResource) -> None:
        self._identifiers = identifiers

        self.list = to_raw_response_wrapper(
            identifiers.list,
        )


class AsyncIdentifiersResourceWithRawResponse:
    def __init__(self, identifiers: AsyncIdentifiersResource) -> None:
        self._identifiers = identifiers

        self.list = async_to_raw_response_wrapper(
            identifiers.list,
        )


class IdentifiersResourceWithStreamingResponse:
    def __init__(self, identifiers: IdentifiersResource) -> None:
        self._identifiers = identifiers

        self.list = to_streamed_response_wrapper(
            identifiers.list,
        )


class AsyncIdentifiersResourceWithStreamingResponse:
    def __init__(self, identifiers: AsyncIdentifiersResource) -> None:
        self._identifiers = identifiers

        self.list = async_to_streamed_response_wrapper(
            identifiers.list,
        )
