# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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
from ...types.accounts import exist_list_params

__all__ = ["ExistsResource", "AsyncExistsResource"]


class ExistsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExistsResourceWithRawResponse:
        return ExistsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExistsResourceWithStreamingResponse:
        return ExistsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        identifier: exist_list_params.Identifier,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Determine whether or not an identifier is associated with an existing Bolt
        account.

        Args:
          identifier: A type and value combination that defines the identifier used to detect the
              existence of an account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/account/exists",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"identifier": identifier}, exist_list_params.ExistListParams),
            ),
            cast_to=NoneType,
        )


class AsyncExistsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExistsResourceWithRawResponse:
        return AsyncExistsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExistsResourceWithStreamingResponse:
        return AsyncExistsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        identifier: exist_list_params.Identifier,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Determine whether or not an identifier is associated with an existing Bolt
        account.

        Args:
          identifier: A type and value combination that defines the identifier used to detect the
              existence of an account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/account/exists",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"identifier": identifier}, exist_list_params.ExistListParams),
            ),
            cast_to=NoneType,
        )


class ExistsResourceWithRawResponse:
    def __init__(self, exists: ExistsResource) -> None:
        self._exists = exists

        self.list = to_raw_response_wrapper(
            exists.list,
        )


class AsyncExistsResourceWithRawResponse:
    def __init__(self, exists: AsyncExistsResource) -> None:
        self._exists = exists

        self.list = async_to_raw_response_wrapper(
            exists.list,
        )


class ExistsResourceWithStreamingResponse:
    def __init__(self, exists: ExistsResource) -> None:
        self._exists = exists

        self.list = to_streamed_response_wrapper(
            exists.list,
        )


class AsyncExistsResourceWithStreamingResponse:
    def __init__(self, exists: AsyncExistsResource) -> None:
        self._exists = exists

        self.list = async_to_streamed_response_wrapper(
            exists.list,
        )
