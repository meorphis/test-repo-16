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
from ...types.accounts import address_update_params, address_account_address_create_params
from ...types.accounts.address_update_response import AddressUpdateResponse
from ...types.accounts.address_account_address_create_response import AddressAccountAddressCreateResponse

__all__ = ["AddressesResource", "AsyncAddressesResource"]


class AddressesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AddressesResourceWithRawResponse:
        return AddressesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AddressesResourceWithStreamingResponse:
        return AddressesResourceWithStreamingResponse(self)

    def update(
        self,
        id: str,
        *,
        country_code: str,
        first_name: str,
        last_name: str,
        locality: str,
        postal_code: str,
        street_address1: str,
        company: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        is_default: bool | NotGiven = NOT_GIVEN,
        phone: str | NotGiven = NOT_GIVEN,
        region: str | NotGiven = NOT_GIVEN,
        street_address2: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AddressUpdateResponse:
        """Edit an existing address on the shopper's account.

        This does not edit addresses
        that are already associated with other resources, such as transactions or
        shipments.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._put(
            f"/account/addresses/{id}",
            body=maybe_transform(
                {
                    "country_code": country_code,
                    "first_name": first_name,
                    "last_name": last_name,
                    "locality": locality,
                    "postal_code": postal_code,
                    "street_address1": street_address1,
                    "company": company,
                    "email": email,
                    "is_default": is_default,
                    "phone": phone,
                    "region": region,
                    "street_address2": street_address2,
                },
                address_update_params.AddressUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddressUpdateResponse,
        )

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
        """Delete an existing address.

        Deleting an address does not invalidate transactions
        or shipments that are associated with it.

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
            f"/account/addresses/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def account_address_create(
        self,
        *,
        country_code: str,
        first_name: str,
        last_name: str,
        locality: str,
        postal_code: str,
        street_address1: str,
        company: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        is_default: bool | NotGiven = NOT_GIVEN,
        phone: str | NotGiven = NOT_GIVEN,
        region: str | NotGiven = NOT_GIVEN,
        street_address2: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AddressAccountAddressCreateResponse:
        """
        Add an address to the shopper's account

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/account/addresses",
            body=maybe_transform(
                {
                    "country_code": country_code,
                    "first_name": first_name,
                    "last_name": last_name,
                    "locality": locality,
                    "postal_code": postal_code,
                    "street_address1": street_address1,
                    "company": company,
                    "email": email,
                    "is_default": is_default,
                    "phone": phone,
                    "region": region,
                    "street_address2": street_address2,
                },
                address_account_address_create_params.AddressAccountAddressCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddressAccountAddressCreateResponse,
        )


class AsyncAddressesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAddressesResourceWithRawResponse:
        return AsyncAddressesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAddressesResourceWithStreamingResponse:
        return AsyncAddressesResourceWithStreamingResponse(self)

    async def update(
        self,
        id: str,
        *,
        country_code: str,
        first_name: str,
        last_name: str,
        locality: str,
        postal_code: str,
        street_address1: str,
        company: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        is_default: bool | NotGiven = NOT_GIVEN,
        phone: str | NotGiven = NOT_GIVEN,
        region: str | NotGiven = NOT_GIVEN,
        street_address2: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AddressUpdateResponse:
        """Edit an existing address on the shopper's account.

        This does not edit addresses
        that are already associated with other resources, such as transactions or
        shipments.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._put(
            f"/account/addresses/{id}",
            body=await async_maybe_transform(
                {
                    "country_code": country_code,
                    "first_name": first_name,
                    "last_name": last_name,
                    "locality": locality,
                    "postal_code": postal_code,
                    "street_address1": street_address1,
                    "company": company,
                    "email": email,
                    "is_default": is_default,
                    "phone": phone,
                    "region": region,
                    "street_address2": street_address2,
                },
                address_update_params.AddressUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddressUpdateResponse,
        )

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
        """Delete an existing address.

        Deleting an address does not invalidate transactions
        or shipments that are associated with it.

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
            f"/account/addresses/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def account_address_create(
        self,
        *,
        country_code: str,
        first_name: str,
        last_name: str,
        locality: str,
        postal_code: str,
        street_address1: str,
        company: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        is_default: bool | NotGiven = NOT_GIVEN,
        phone: str | NotGiven = NOT_GIVEN,
        region: str | NotGiven = NOT_GIVEN,
        street_address2: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AddressAccountAddressCreateResponse:
        """
        Add an address to the shopper's account

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/account/addresses",
            body=await async_maybe_transform(
                {
                    "country_code": country_code,
                    "first_name": first_name,
                    "last_name": last_name,
                    "locality": locality,
                    "postal_code": postal_code,
                    "street_address1": street_address1,
                    "company": company,
                    "email": email,
                    "is_default": is_default,
                    "phone": phone,
                    "region": region,
                    "street_address2": street_address2,
                },
                address_account_address_create_params.AddressAccountAddressCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddressAccountAddressCreateResponse,
        )


class AddressesResourceWithRawResponse:
    def __init__(self, addresses: AddressesResource) -> None:
        self._addresses = addresses

        self.update = to_raw_response_wrapper(
            addresses.update,
        )
        self.delete = to_raw_response_wrapper(
            addresses.delete,
        )
        self.account_address_create = to_raw_response_wrapper(
            addresses.account_address_create,
        )


class AsyncAddressesResourceWithRawResponse:
    def __init__(self, addresses: AsyncAddressesResource) -> None:
        self._addresses = addresses

        self.update = async_to_raw_response_wrapper(
            addresses.update,
        )
        self.delete = async_to_raw_response_wrapper(
            addresses.delete,
        )
        self.account_address_create = async_to_raw_response_wrapper(
            addresses.account_address_create,
        )


class AddressesResourceWithStreamingResponse:
    def __init__(self, addresses: AddressesResource) -> None:
        self._addresses = addresses

        self.update = to_streamed_response_wrapper(
            addresses.update,
        )
        self.delete = to_streamed_response_wrapper(
            addresses.delete,
        )
        self.account_address_create = to_streamed_response_wrapper(
            addresses.account_address_create,
        )


class AsyncAddressesResourceWithStreamingResponse:
    def __init__(self, addresses: AsyncAddressesResource) -> None:
        self._addresses = addresses

        self.update = async_to_streamed_response_wrapper(
            addresses.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            addresses.delete,
        )
        self.account_address_create = async_to_streamed_response_wrapper(
            addresses.account_address_create,
        )
