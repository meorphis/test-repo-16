# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
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
from ...types.testings import shipment_testing_shipment_tracking_create_params

__all__ = ["ShipmentsResource", "AsyncShipmentsResource"]


class ShipmentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ShipmentsResourceWithRawResponse:
        return ShipmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ShipmentsResourceWithStreamingResponse:
        return ShipmentsResourceWithStreamingResponse(self)

    def testing_shipment_tracking_create(
        self,
        *,
        status: Literal["in_transit", "cancelled", "failure", "delivered"],
        tracking_details: Iterable[shipment_testing_shipment_tracking_create_params.TrackingDetail],
        tracking_number: str,
        delivery_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Simulate a shipment tracking update, such as those that Bolt would ingest from
        third-party shipping providers that would allow updating tracking and delivery
        information to shipments associated with orders.

        Args:
          status: The shipment's status.

          tracking_details: A list of tracking updates that contain the shipment's status, location, and any
              unique messages.

          tracking_number: The carrier's tracking number for the shipment. Must be prefixed with
              `MockBolt`.

          delivery_date: The shipment's actual or estimated delivery date.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/testing/shipments",
            body=maybe_transform(
                {
                    "status": status,
                    "tracking_details": tracking_details,
                    "tracking_number": tracking_number,
                    "delivery_date": delivery_date,
                },
                shipment_testing_shipment_tracking_create_params.ShipmentTestingShipmentTrackingCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncShipmentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncShipmentsResourceWithRawResponse:
        return AsyncShipmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncShipmentsResourceWithStreamingResponse:
        return AsyncShipmentsResourceWithStreamingResponse(self)

    async def testing_shipment_tracking_create(
        self,
        *,
        status: Literal["in_transit", "cancelled", "failure", "delivered"],
        tracking_details: Iterable[shipment_testing_shipment_tracking_create_params.TrackingDetail],
        tracking_number: str,
        delivery_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Simulate a shipment tracking update, such as those that Bolt would ingest from
        third-party shipping providers that would allow updating tracking and delivery
        information to shipments associated with orders.

        Args:
          status: The shipment's status.

          tracking_details: A list of tracking updates that contain the shipment's status, location, and any
              unique messages.

          tracking_number: The carrier's tracking number for the shipment. Must be prefixed with
              `MockBolt`.

          delivery_date: The shipment's actual or estimated delivery date.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/testing/shipments",
            body=await async_maybe_transform(
                {
                    "status": status,
                    "tracking_details": tracking_details,
                    "tracking_number": tracking_number,
                    "delivery_date": delivery_date,
                },
                shipment_testing_shipment_tracking_create_params.ShipmentTestingShipmentTrackingCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ShipmentsResourceWithRawResponse:
    def __init__(self, shipments: ShipmentsResource) -> None:
        self._shipments = shipments

        self.testing_shipment_tracking_create = to_raw_response_wrapper(
            shipments.testing_shipment_tracking_create,
        )


class AsyncShipmentsResourceWithRawResponse:
    def __init__(self, shipments: AsyncShipmentsResource) -> None:
        self._shipments = shipments

        self.testing_shipment_tracking_create = async_to_raw_response_wrapper(
            shipments.testing_shipment_tracking_create,
        )


class ShipmentsResourceWithStreamingResponse:
    def __init__(self, shipments: ShipmentsResource) -> None:
        self._shipments = shipments

        self.testing_shipment_tracking_create = to_streamed_response_wrapper(
            shipments.testing_shipment_tracking_create,
        )


class AsyncShipmentsResourceWithStreamingResponse:
    def __init__(self, shipments: AsyncShipmentsResource) -> None:
        self._shipments = shipments

        self.testing_shipment_tracking_create = async_to_streamed_response_wrapper(
            shipments.testing_shipment_tracking_create,
        )
