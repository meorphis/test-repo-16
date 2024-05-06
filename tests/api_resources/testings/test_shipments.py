# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from meorphis_test_40 import MeorphisTest40, AsyncMeorphisTest40
from meorphis_test_40._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestShipments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_testing_shipment_tracking_create(self, client: MeorphisTest40) -> None:
        shipment = client.testings.shipments.testing_shipment_tracking_create(
            status="in_transit",
            tracking_details=[{}, {}, {}],
            tracking_number="MockBolt-143292",
        )
        assert shipment is None

    @parametrize
    def test_method_testing_shipment_tracking_create_with_all_params(self, client: MeorphisTest40) -> None:
        shipment = client.testings.shipments.testing_shipment_tracking_create(
            status="in_transit",
            tracking_details=[
                {
                    "event_date": "2014-08-21:T14:24:00Z",
                    "status": "pre_transit",
                    "message": "Billing information received",
                    "locality": "San Francisco",
                    "region": "CA",
                    "postal_code": "string",
                    "country_code": "US",
                },
                {
                    "event_date": "2014-08-21:T14:24:00Z",
                    "status": "pre_transit",
                    "message": "Billing information received",
                    "locality": "San Francisco",
                    "region": "CA",
                    "postal_code": "string",
                    "country_code": "US",
                },
                {
                    "event_date": "2014-08-21:T14:24:00Z",
                    "status": "pre_transit",
                    "message": "Billing information received",
                    "locality": "San Francisco",
                    "region": "CA",
                    "postal_code": "string",
                    "country_code": "US",
                },
            ],
            tracking_number="MockBolt-143292",
            delivery_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert shipment is None

    @parametrize
    def test_raw_response_testing_shipment_tracking_create(self, client: MeorphisTest40) -> None:
        response = client.testings.shipments.with_raw_response.testing_shipment_tracking_create(
            status="in_transit",
            tracking_details=[{}, {}, {}],
            tracking_number="MockBolt-143292",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shipment = response.parse()
        assert shipment is None

    @parametrize
    def test_streaming_response_testing_shipment_tracking_create(self, client: MeorphisTest40) -> None:
        with client.testings.shipments.with_streaming_response.testing_shipment_tracking_create(
            status="in_transit",
            tracking_details=[{}, {}, {}],
            tracking_number="MockBolt-143292",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shipment = response.parse()
            assert shipment is None

        assert cast(Any, response.is_closed) is True


class TestAsyncShipments:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_testing_shipment_tracking_create(self, async_client: AsyncMeorphisTest40) -> None:
        shipment = await async_client.testings.shipments.testing_shipment_tracking_create(
            status="in_transit",
            tracking_details=[{}, {}, {}],
            tracking_number="MockBolt-143292",
        )
        assert shipment is None

    @parametrize
    async def test_method_testing_shipment_tracking_create_with_all_params(
        self, async_client: AsyncMeorphisTest40
    ) -> None:
        shipment = await async_client.testings.shipments.testing_shipment_tracking_create(
            status="in_transit",
            tracking_details=[
                {
                    "event_date": "2014-08-21:T14:24:00Z",
                    "status": "pre_transit",
                    "message": "Billing information received",
                    "locality": "San Francisco",
                    "region": "CA",
                    "postal_code": "string",
                    "country_code": "US",
                },
                {
                    "event_date": "2014-08-21:T14:24:00Z",
                    "status": "pre_transit",
                    "message": "Billing information received",
                    "locality": "San Francisco",
                    "region": "CA",
                    "postal_code": "string",
                    "country_code": "US",
                },
                {
                    "event_date": "2014-08-21:T14:24:00Z",
                    "status": "pre_transit",
                    "message": "Billing information received",
                    "locality": "San Francisco",
                    "region": "CA",
                    "postal_code": "string",
                    "country_code": "US",
                },
            ],
            tracking_number="MockBolt-143292",
            delivery_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert shipment is None

    @parametrize
    async def test_raw_response_testing_shipment_tracking_create(self, async_client: AsyncMeorphisTest40) -> None:
        response = await async_client.testings.shipments.with_raw_response.testing_shipment_tracking_create(
            status="in_transit",
            tracking_details=[{}, {}, {}],
            tracking_number="MockBolt-143292",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shipment = await response.parse()
        assert shipment is None

    @parametrize
    async def test_streaming_response_testing_shipment_tracking_create(self, async_client: AsyncMeorphisTest40) -> None:
        async with async_client.testings.shipments.with_streaming_response.testing_shipment_tracking_create(
            status="in_transit",
            tracking_details=[{}, {}, {}],
            tracking_number="MockBolt-143292",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shipment = await response.parse()
            assert shipment is None

        assert cast(Any, response.is_closed) is True
