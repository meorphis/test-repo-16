# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal

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
from ...types.testings import account_testing_account_create_params
from ...types.testings.account_testing_account_create_response import AccountTestingAccountCreateResponse

__all__ = ["AccountsResource", "AsyncAccountsResource"]


class AccountsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccountsResourceWithRawResponse:
        return AccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountsResourceWithStreamingResponse:
        return AccountsResourceWithStreamingResponse(self)

    def testing_account_create(
        self,
        *,
        deactivate_at: Union[str, datetime],
        email_state: Literal["missing", "unverified", "verified"],
        phone_state: Literal["missing", "unverified", "verified"],
        has_address: bool | NotGiven = NOT_GIVEN,
        is_migrated: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountTestingAccountCreateResponse:
        """
        Create a Bolt shopper account for testing purposes.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/testing/accounts",
            body=maybe_transform(
                {
                    "deactivate_at": deactivate_at,
                    "email_state": email_state,
                    "phone_state": phone_state,
                    "has_address": has_address,
                    "is_migrated": is_migrated,
                },
                account_testing_account_create_params.AccountTestingAccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountTestingAccountCreateResponse,
        )


class AsyncAccountsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccountsResourceWithRawResponse:
        return AsyncAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountsResourceWithStreamingResponse:
        return AsyncAccountsResourceWithStreamingResponse(self)

    async def testing_account_create(
        self,
        *,
        deactivate_at: Union[str, datetime],
        email_state: Literal["missing", "unverified", "verified"],
        phone_state: Literal["missing", "unverified", "verified"],
        has_address: bool | NotGiven = NOT_GIVEN,
        is_migrated: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountTestingAccountCreateResponse:
        """
        Create a Bolt shopper account for testing purposes.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/testing/accounts",
            body=await async_maybe_transform(
                {
                    "deactivate_at": deactivate_at,
                    "email_state": email_state,
                    "phone_state": phone_state,
                    "has_address": has_address,
                    "is_migrated": is_migrated,
                },
                account_testing_account_create_params.AccountTestingAccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountTestingAccountCreateResponse,
        )


class AccountsResourceWithRawResponse:
    def __init__(self, accounts: AccountsResource) -> None:
        self._accounts = accounts

        self.testing_account_create = to_raw_response_wrapper(
            accounts.testing_account_create,
        )


class AsyncAccountsResourceWithRawResponse:
    def __init__(self, accounts: AsyncAccountsResource) -> None:
        self._accounts = accounts

        self.testing_account_create = async_to_raw_response_wrapper(
            accounts.testing_account_create,
        )


class AccountsResourceWithStreamingResponse:
    def __init__(self, accounts: AccountsResource) -> None:
        self._accounts = accounts

        self.testing_account_create = to_streamed_response_wrapper(
            accounts.testing_account_create,
        )


class AsyncAccountsResourceWithStreamingResponse:
    def __init__(self, accounts: AsyncAccountsResource) -> None:
        self._accounts = accounts

        self.testing_account_create = async_to_streamed_response_wrapper(
            accounts.testing_account_create,
        )
