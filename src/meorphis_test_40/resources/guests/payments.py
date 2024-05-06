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
from ...types.guests import payment_guest_payments_initialize_params
from ...types.guests.payment_guest_payments_initialize_response import PaymentGuestPaymentsInitializeResponse

__all__ = ["PaymentsResource", "AsyncPaymentsResource"]


class PaymentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PaymentsResourceWithRawResponse:
        return PaymentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PaymentsResourceWithStreamingResponse:
        return PaymentsResourceWithStreamingResponse(self)

    def guest_payments_initialize(
        self,
        *,
        cart: payment_guest_payments_initialize_params.Cart,
        payment_method: payment_guest_payments_initialize_params.PaymentMethod,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentGuestPaymentsInitializeResponse:
        """
        Initialize a Bolt payment token that will be used to reference this payment to
        Bolt when it is updated or finalized for guest shoppers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/guest/payments",
            body=maybe_transform(
                {
                    "cart": cart,
                    "payment_method": payment_method,
                },
                payment_guest_payments_initialize_params.PaymentGuestPaymentsInitializeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentGuestPaymentsInitializeResponse,
        )


class AsyncPaymentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPaymentsResourceWithRawResponse:
        return AsyncPaymentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPaymentsResourceWithStreamingResponse:
        return AsyncPaymentsResourceWithStreamingResponse(self)

    async def guest_payments_initialize(
        self,
        *,
        cart: payment_guest_payments_initialize_params.Cart,
        payment_method: payment_guest_payments_initialize_params.PaymentMethod,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentGuestPaymentsInitializeResponse:
        """
        Initialize a Bolt payment token that will be used to reference this payment to
        Bolt when it is updated or finalized for guest shoppers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/guest/payments",
            body=await async_maybe_transform(
                {
                    "cart": cart,
                    "payment_method": payment_method,
                },
                payment_guest_payments_initialize_params.PaymentGuestPaymentsInitializeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentGuestPaymentsInitializeResponse,
        )


class PaymentsResourceWithRawResponse:
    def __init__(self, payments: PaymentsResource) -> None:
        self._payments = payments

        self.guest_payments_initialize = to_raw_response_wrapper(
            payments.guest_payments_initialize,
        )


class AsyncPaymentsResourceWithRawResponse:
    def __init__(self, payments: AsyncPaymentsResource) -> None:
        self._payments = payments

        self.guest_payments_initialize = async_to_raw_response_wrapper(
            payments.guest_payments_initialize,
        )


class PaymentsResourceWithStreamingResponse:
    def __init__(self, payments: PaymentsResource) -> None:
        self._payments = payments

        self.guest_payments_initialize = to_streamed_response_wrapper(
            payments.guest_payments_initialize,
        )


class AsyncPaymentsResourceWithStreamingResponse:
    def __init__(self, payments: AsyncPaymentsResource) -> None:
        self._payments = payments

        self.guest_payments_initialize = async_to_streamed_response_wrapper(
            payments.guest_payments_initialize,
        )
