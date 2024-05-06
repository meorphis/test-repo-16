# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

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
from ...types.accounts import payment_method_account_add_payment_method_params
from ...types.accounts.payment_method_account_add_payment_method_response import (
    PaymentMethodAccountAddPaymentMethodResponse,
)

__all__ = ["PaymentMethodsResource", "AsyncPaymentMethodsResource"]


class PaymentMethodsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PaymentMethodsResourceWithRawResponse:
        return PaymentMethodsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PaymentMethodsResourceWithStreamingResponse:
        return PaymentMethodsResourceWithStreamingResponse(self)

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Delete an existing payment method.

        Deleting a payment method does not invalidate
        transactions or orders that are associated with it.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/account/payment-methods/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def account_add_payment_method(
        self,
        *,
        token: str,
        tag: Literal["credit_card"],
        billing_address: payment_method_account_add_payment_method_params.BillingAddress,
        bin: str,
        expiration: str,
        last4: str,
        network: Literal["visa", "mastercard", "amex", "discover", "jcb", "unionpay", "alliancedata", "citiplcc"],
        type: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentMethodAccountAddPaymentMethodResponse:
        """Add a payment method to a shopper's Bolt account Wallet.

        For security purposes,
        this request must come from your backend because authentication requires the use
        of your private key.<br /> **Note**: Before using this API, the credit card
        details must be tokenized using Bolt's JavaScript library function, which is
        documented in
        [Install the Bolt Tokenizer](https://help.bolt.com/developers/references/bolt-tokenizer).

        Args:
          token: The Bolt token associated to the credit card.

          billing_address: The credit card's billing address

          bin: The Bank Identification Number for the credit card. This is typically the first
              4-6 digits of the credit card number.

          expiration: The expiration date of the credit card. TODO TO MAKE EXPIRATION REUSABLE

          last4: The last 4 digits of the credit card number.

          network: The credit card network.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/account/payment-methods",
            body=maybe_transform(
                {
                    "token": token,
                    "tag": tag,
                    "billing_address": billing_address,
                    "bin": bin,
                    "expiration": expiration,
                    "last4": last4,
                    "network": network,
                    "type": type,
                },
                payment_method_account_add_payment_method_params.PaymentMethodAccountAddPaymentMethodParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentMethodAccountAddPaymentMethodResponse,
        )


class AsyncPaymentMethodsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPaymentMethodsResourceWithRawResponse:
        return AsyncPaymentMethodsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPaymentMethodsResourceWithStreamingResponse:
        return AsyncPaymentMethodsResourceWithStreamingResponse(self)

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Delete an existing payment method.

        Deleting a payment method does not invalidate
        transactions or orders that are associated with it.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/account/payment-methods/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def account_add_payment_method(
        self,
        *,
        token: str,
        tag: Literal["credit_card"],
        billing_address: payment_method_account_add_payment_method_params.BillingAddress,
        bin: str,
        expiration: str,
        last4: str,
        network: Literal["visa", "mastercard", "amex", "discover", "jcb", "unionpay", "alliancedata", "citiplcc"],
        type: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentMethodAccountAddPaymentMethodResponse:
        """Add a payment method to a shopper's Bolt account Wallet.

        For security purposes,
        this request must come from your backend because authentication requires the use
        of your private key.<br /> **Note**: Before using this API, the credit card
        details must be tokenized using Bolt's JavaScript library function, which is
        documented in
        [Install the Bolt Tokenizer](https://help.bolt.com/developers/references/bolt-tokenizer).

        Args:
          token: The Bolt token associated to the credit card.

          billing_address: The credit card's billing address

          bin: The Bank Identification Number for the credit card. This is typically the first
              4-6 digits of the credit card number.

          expiration: The expiration date of the credit card. TODO TO MAKE EXPIRATION REUSABLE

          last4: The last 4 digits of the credit card number.

          network: The credit card network.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/account/payment-methods",
            body=await async_maybe_transform(
                {
                    "token": token,
                    "tag": tag,
                    "billing_address": billing_address,
                    "bin": bin,
                    "expiration": expiration,
                    "last4": last4,
                    "network": network,
                    "type": type,
                },
                payment_method_account_add_payment_method_params.PaymentMethodAccountAddPaymentMethodParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentMethodAccountAddPaymentMethodResponse,
        )


class PaymentMethodsResourceWithRawResponse:
    def __init__(self, payment_methods: PaymentMethodsResource) -> None:
        self._payment_methods = payment_methods

        self.delete = to_raw_response_wrapper(
            payment_methods.delete,
        )
        self.account_add_payment_method = to_raw_response_wrapper(
            payment_methods.account_add_payment_method,
        )


class AsyncPaymentMethodsResourceWithRawResponse:
    def __init__(self, payment_methods: AsyncPaymentMethodsResource) -> None:
        self._payment_methods = payment_methods

        self.delete = async_to_raw_response_wrapper(
            payment_methods.delete,
        )
        self.account_add_payment_method = async_to_raw_response_wrapper(
            payment_methods.account_add_payment_method,
        )


class PaymentMethodsResourceWithStreamingResponse:
    def __init__(self, payment_methods: PaymentMethodsResource) -> None:
        self._payment_methods = payment_methods

        self.delete = to_streamed_response_wrapper(
            payment_methods.delete,
        )
        self.account_add_payment_method = to_streamed_response_wrapper(
            payment_methods.account_add_payment_method,
        )


class AsyncPaymentMethodsResourceWithStreamingResponse:
    def __init__(self, payment_methods: AsyncPaymentMethodsResource) -> None:
        self._payment_methods = payment_methods

        self.delete = async_to_streamed_response_wrapper(
            payment_methods.delete,
        )
        self.account_add_payment_method = async_to_streamed_response_wrapper(
            payment_methods.account_add_payment_method,
        )
