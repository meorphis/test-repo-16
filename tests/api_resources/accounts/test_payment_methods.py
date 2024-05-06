# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from meorphis_test_40 import MeorphisTest40, AsyncMeorphisTest40
from meorphis_test_40.types.accounts import (
    PaymentMethodAccountAddPaymentMethodResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPaymentMethods:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_delete(self, client: MeorphisTest40) -> None:
        payment_method = client.accounts.payment_methods.delete(
            "D4g3h5tBuVYK9",
        )
        assert payment_method is None

    @parametrize
    def test_raw_response_delete(self, client: MeorphisTest40) -> None:
        response = client.accounts.payment_methods.with_raw_response.delete(
            "D4g3h5tBuVYK9",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_method = response.parse()
        assert payment_method is None

    @parametrize
    def test_streaming_response_delete(self, client: MeorphisTest40) -> None:
        with client.accounts.payment_methods.with_streaming_response.delete(
            "D4g3h5tBuVYK9",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_method = response.parse()
            assert payment_method is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: MeorphisTest40) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.accounts.payment_methods.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_account_add_payment_method(self, client: MeorphisTest40) -> None:
        payment_method = client.accounts.payment_methods.account_add_payment_method(
            token="a1B2c3D4e5F6G7H8i9J0k1L2m3N4o5P6Q7r8S9t0",
            tag="credit_card",
            billing_address={
                "tag": "id",
                "id": "D4g3h5tBuVYK9",
            },
            bin="411111",
            expiration="2025-03",
            last4="1004",
            network="visa",
            type={},
        )
        assert_matches_type(PaymentMethodAccountAddPaymentMethodResponse, payment_method, path=["response"])

    @parametrize
    def test_method_account_add_payment_method_with_all_params(self, client: MeorphisTest40) -> None:
        payment_method = client.accounts.payment_methods.account_add_payment_method(
            token="a1B2c3D4e5F6G7H8i9J0k1L2m3N4o5P6Q7r8S9t0",
            tag="credit_card",
            billing_address={
                "tag": "id",
                "id": "D4g3h5tBuVYK9",
            },
            bin="411111",
            expiration="2025-03",
            last4="1004",
            network="visa",
            type={},
        )
        assert_matches_type(PaymentMethodAccountAddPaymentMethodResponse, payment_method, path=["response"])

    @parametrize
    def test_raw_response_account_add_payment_method(self, client: MeorphisTest40) -> None:
        response = client.accounts.payment_methods.with_raw_response.account_add_payment_method(
            token="a1B2c3D4e5F6G7H8i9J0k1L2m3N4o5P6Q7r8S9t0",
            tag="credit_card",
            billing_address={
                "tag": "id",
                "id": "D4g3h5tBuVYK9",
            },
            bin="411111",
            expiration="2025-03",
            last4="1004",
            network="visa",
            type={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_method = response.parse()
        assert_matches_type(PaymentMethodAccountAddPaymentMethodResponse, payment_method, path=["response"])

    @parametrize
    def test_streaming_response_account_add_payment_method(self, client: MeorphisTest40) -> None:
        with client.accounts.payment_methods.with_streaming_response.account_add_payment_method(
            token="a1B2c3D4e5F6G7H8i9J0k1L2m3N4o5P6Q7r8S9t0",
            tag="credit_card",
            billing_address={
                "tag": "id",
                "id": "D4g3h5tBuVYK9",
            },
            bin="411111",
            expiration="2025-03",
            last4="1004",
            network="visa",
            type={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_method = response.parse()
            assert_matches_type(PaymentMethodAccountAddPaymentMethodResponse, payment_method, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPaymentMethods:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_delete(self, async_client: AsyncMeorphisTest40) -> None:
        payment_method = await async_client.accounts.payment_methods.delete(
            "D4g3h5tBuVYK9",
        )
        assert payment_method is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncMeorphisTest40) -> None:
        response = await async_client.accounts.payment_methods.with_raw_response.delete(
            "D4g3h5tBuVYK9",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_method = await response.parse()
        assert payment_method is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncMeorphisTest40) -> None:
        async with async_client.accounts.payment_methods.with_streaming_response.delete(
            "D4g3h5tBuVYK9",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_method = await response.parse()
            assert payment_method is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncMeorphisTest40) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.accounts.payment_methods.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_account_add_payment_method(self, async_client: AsyncMeorphisTest40) -> None:
        payment_method = await async_client.accounts.payment_methods.account_add_payment_method(
            token="a1B2c3D4e5F6G7H8i9J0k1L2m3N4o5P6Q7r8S9t0",
            tag="credit_card",
            billing_address={
                "tag": "id",
                "id": "D4g3h5tBuVYK9",
            },
            bin="411111",
            expiration="2025-03",
            last4="1004",
            network="visa",
            type={},
        )
        assert_matches_type(PaymentMethodAccountAddPaymentMethodResponse, payment_method, path=["response"])

    @parametrize
    async def test_method_account_add_payment_method_with_all_params(self, async_client: AsyncMeorphisTest40) -> None:
        payment_method = await async_client.accounts.payment_methods.account_add_payment_method(
            token="a1B2c3D4e5F6G7H8i9J0k1L2m3N4o5P6Q7r8S9t0",
            tag="credit_card",
            billing_address={
                "tag": "id",
                "id": "D4g3h5tBuVYK9",
            },
            bin="411111",
            expiration="2025-03",
            last4="1004",
            network="visa",
            type={},
        )
        assert_matches_type(PaymentMethodAccountAddPaymentMethodResponse, payment_method, path=["response"])

    @parametrize
    async def test_raw_response_account_add_payment_method(self, async_client: AsyncMeorphisTest40) -> None:
        response = await async_client.accounts.payment_methods.with_raw_response.account_add_payment_method(
            token="a1B2c3D4e5F6G7H8i9J0k1L2m3N4o5P6Q7r8S9t0",
            tag="credit_card",
            billing_address={
                "tag": "id",
                "id": "D4g3h5tBuVYK9",
            },
            bin="411111",
            expiration="2025-03",
            last4="1004",
            network="visa",
            type={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_method = await response.parse()
        assert_matches_type(PaymentMethodAccountAddPaymentMethodResponse, payment_method, path=["response"])

    @parametrize
    async def test_streaming_response_account_add_payment_method(self, async_client: AsyncMeorphisTest40) -> None:
        async with async_client.accounts.payment_methods.with_streaming_response.account_add_payment_method(
            token="a1B2c3D4e5F6G7H8i9J0k1L2m3N4o5P6Q7r8S9t0",
            tag="credit_card",
            billing_address={
                "tag": "id",
                "id": "D4g3h5tBuVYK9",
            },
            bin="411111",
            expiration="2025-03",
            last4="1004",
            network="visa",
            type={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_method = await response.parse()
            assert_matches_type(PaymentMethodAccountAddPaymentMethodResponse, payment_method, path=["response"])

        assert cast(Any, response.is_closed) is True
