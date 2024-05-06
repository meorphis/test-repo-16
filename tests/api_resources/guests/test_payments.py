# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from meorphis_test_40 import MeorphisTest40, AsyncMeorphisTest40
from meorphis_test_40.types.guests import (
    PaymentGuestPaymentsInitializeResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPayments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_guest_payments_initialize(self, client: MeorphisTest40) -> None:
        payment = client.guests.payments.guest_payments_initialize(
            cart={
                "amounts": {
                    "total": 10000,
                    "currency": "USD",
                },
                "order_reference": "order_100",
            },
            payment_method={
                "tag": "paypal",
                "success": "https://example.com",
                "cancel": "https://example.com",
            },
        )
        assert_matches_type(PaymentGuestPaymentsInitializeResponse, payment, path=["response"])

    @parametrize
    def test_method_guest_payments_initialize_with_all_params(self, client: MeorphisTest40) -> None:
        payment = client.guests.payments.guest_payments_initialize(
            cart={
                "amounts": {
                    "total": 10000,
                    "currency": "USD",
                    "tax": 1000,
                },
                "order_reference": "order_100",
                "order_description": "Order #1234567890",
                "display_id": "215614191",
                "shipments": [
                    {
                        "address": {
                            "tag": "id",
                            "id": "D4g3h5tBuVYK9",
                        },
                        "cost": {
                            "total": 10000,
                            "currency": "USD",
                            "tax": 900,
                        },
                        "carrier": "FedEx",
                    }
                ],
                "discounts": [
                    {
                        "amounts": {
                            "total": 10000,
                            "currency": "USD",
                            "tax": 900,
                        },
                        "code": "SUMMER10DISCOUNT",
                        "details_url": "https://www.example.com/SUMMER-SALE",
                    }
                ],
                "items": [
                    {
                        "name": "Bolt Swag Bag",
                        "reference": "item_100",
                        "description": "Large tote with Bolt logo.",
                        "total_amount": 9000,
                        "unit_price": 1000,
                        "quantity": 9,
                        "image_url": "https://www.example.com/products/123456/images/1.png",
                    }
                ],
            },
            payment_method={
                "tag": "paypal",
                "success": "https://example.com",
                "cancel": "https://example.com",
            },
        )
        assert_matches_type(PaymentGuestPaymentsInitializeResponse, payment, path=["response"])

    @parametrize
    def test_raw_response_guest_payments_initialize(self, client: MeorphisTest40) -> None:
        response = client.guests.payments.with_raw_response.guest_payments_initialize(
            cart={
                "amounts": {
                    "total": 10000,
                    "currency": "USD",
                },
                "order_reference": "order_100",
            },
            payment_method={
                "tag": "paypal",
                "success": "https://example.com",
                "cancel": "https://example.com",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(PaymentGuestPaymentsInitializeResponse, payment, path=["response"])

    @parametrize
    def test_streaming_response_guest_payments_initialize(self, client: MeorphisTest40) -> None:
        with client.guests.payments.with_streaming_response.guest_payments_initialize(
            cart={
                "amounts": {
                    "total": 10000,
                    "currency": "USD",
                },
                "order_reference": "order_100",
            },
            payment_method={
                "tag": "paypal",
                "success": "https://example.com",
                "cancel": "https://example.com",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = response.parse()
            assert_matches_type(PaymentGuestPaymentsInitializeResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPayments:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_guest_payments_initialize(self, async_client: AsyncMeorphisTest40) -> None:
        payment = await async_client.guests.payments.guest_payments_initialize(
            cart={
                "amounts": {
                    "total": 10000,
                    "currency": "USD",
                },
                "order_reference": "order_100",
            },
            payment_method={
                "tag": "paypal",
                "success": "https://example.com",
                "cancel": "https://example.com",
            },
        )
        assert_matches_type(PaymentGuestPaymentsInitializeResponse, payment, path=["response"])

    @parametrize
    async def test_method_guest_payments_initialize_with_all_params(self, async_client: AsyncMeorphisTest40) -> None:
        payment = await async_client.guests.payments.guest_payments_initialize(
            cart={
                "amounts": {
                    "total": 10000,
                    "currency": "USD",
                    "tax": 1000,
                },
                "order_reference": "order_100",
                "order_description": "Order #1234567890",
                "display_id": "215614191",
                "shipments": [
                    {
                        "address": {
                            "tag": "id",
                            "id": "D4g3h5tBuVYK9",
                        },
                        "cost": {
                            "total": 10000,
                            "currency": "USD",
                            "tax": 900,
                        },
                        "carrier": "FedEx",
                    }
                ],
                "discounts": [
                    {
                        "amounts": {
                            "total": 10000,
                            "currency": "USD",
                            "tax": 900,
                        },
                        "code": "SUMMER10DISCOUNT",
                        "details_url": "https://www.example.com/SUMMER-SALE",
                    }
                ],
                "items": [
                    {
                        "name": "Bolt Swag Bag",
                        "reference": "item_100",
                        "description": "Large tote with Bolt logo.",
                        "total_amount": 9000,
                        "unit_price": 1000,
                        "quantity": 9,
                        "image_url": "https://www.example.com/products/123456/images/1.png",
                    }
                ],
            },
            payment_method={
                "tag": "paypal",
                "success": "https://example.com",
                "cancel": "https://example.com",
            },
        )
        assert_matches_type(PaymentGuestPaymentsInitializeResponse, payment, path=["response"])

    @parametrize
    async def test_raw_response_guest_payments_initialize(self, async_client: AsyncMeorphisTest40) -> None:
        response = await async_client.guests.payments.with_raw_response.guest_payments_initialize(
            cart={
                "amounts": {
                    "total": 10000,
                    "currency": "USD",
                },
                "order_reference": "order_100",
            },
            payment_method={
                "tag": "paypal",
                "success": "https://example.com",
                "cancel": "https://example.com",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = await response.parse()
        assert_matches_type(PaymentGuestPaymentsInitializeResponse, payment, path=["response"])

    @parametrize
    async def test_streaming_response_guest_payments_initialize(self, async_client: AsyncMeorphisTest40) -> None:
        async with async_client.guests.payments.with_streaming_response.guest_payments_initialize(
            cart={
                "amounts": {
                    "total": 10000,
                    "currency": "USD",
                },
                "order_reference": "order_100",
            },
            payment_method={
                "tag": "paypal",
                "success": "https://example.com",
                "cancel": "https://example.com",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = await response.parse()
            assert_matches_type(PaymentGuestPaymentsInitializeResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True
