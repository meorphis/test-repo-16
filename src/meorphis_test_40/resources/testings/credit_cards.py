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
from ...types.testings.credit_card_list_response import CreditCardListResponse

__all__ = ["CreditCardsResource", "AsyncCreditCardsResource"]


class CreditCardsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CreditCardsResourceWithRawResponse:
        return CreditCardsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CreditCardsResourceWithStreamingResponse:
        return CreditCardsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreditCardListResponse:
        """Retrieve test credit card information.

        This includes its token, which is
        generated against the `4111 1111 1111 1004` test card.
        """
        return self._get(
            "/testing/credit-cards",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditCardListResponse,
        )


class AsyncCreditCardsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCreditCardsResourceWithRawResponse:
        return AsyncCreditCardsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCreditCardsResourceWithStreamingResponse:
        return AsyncCreditCardsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreditCardListResponse:
        """Retrieve test credit card information.

        This includes its token, which is
        generated against the `4111 1111 1111 1004` test card.
        """
        return await self._get(
            "/testing/credit-cards",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditCardListResponse,
        )


class CreditCardsResourceWithRawResponse:
    def __init__(self, credit_cards: CreditCardsResource) -> None:
        self._credit_cards = credit_cards

        self.list = to_raw_response_wrapper(
            credit_cards.list,
        )


class AsyncCreditCardsResourceWithRawResponse:
    def __init__(self, credit_cards: AsyncCreditCardsResource) -> None:
        self._credit_cards = credit_cards

        self.list = async_to_raw_response_wrapper(
            credit_cards.list,
        )


class CreditCardsResourceWithStreamingResponse:
    def __init__(self, credit_cards: CreditCardsResource) -> None:
        self._credit_cards = credit_cards

        self.list = to_streamed_response_wrapper(
            credit_cards.list,
        )


class AsyncCreditCardsResourceWithStreamingResponse:
    def __init__(self, credit_cards: AsyncCreditCardsResource) -> None:
        self._credit_cards = credit_cards

        self.list = async_to_streamed_response_wrapper(
            credit_cards.list,
        )
