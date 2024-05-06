# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from meorphis_test_40 import MeorphisTest40, AsyncMeorphisTest40
from meorphis_test_40.types.accounts import (
    AddressUpdateResponse,
    AddressAccountAddressCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAddresses:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: MeorphisTest40) -> None:
        address = client.accounts.addresses.update(
            "D4g3h5tBuVYK9",
            country_code="US",
            first_name="Alice",
            last_name="Baker",
            locality="San Francisco",
            postal_code="94105",
            street_address1="535 Mission St, Ste 1401",
        )
        assert_matches_type(AddressUpdateResponse, address, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: MeorphisTest40) -> None:
        address = client.accounts.addresses.update(
            "D4g3h5tBuVYK9",
            country_code="US",
            first_name="Alice",
            last_name="Baker",
            locality="San Francisco",
            postal_code="94105",
            street_address1="535 Mission St, Ste 1401",
            company="ACME Corporation",
            email="alice@example.com",
            is_default=True,
            phone="+14155550199",
            region="CA",
            street_address2="c/o Shipping Department",
        )
        assert_matches_type(AddressUpdateResponse, address, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: MeorphisTest40) -> None:
        response = client.accounts.addresses.with_raw_response.update(
            "D4g3h5tBuVYK9",
            country_code="US",
            first_name="Alice",
            last_name="Baker",
            locality="San Francisco",
            postal_code="94105",
            street_address1="535 Mission St, Ste 1401",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address = response.parse()
        assert_matches_type(AddressUpdateResponse, address, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: MeorphisTest40) -> None:
        with client.accounts.addresses.with_streaming_response.update(
            "D4g3h5tBuVYK9",
            country_code="US",
            first_name="Alice",
            last_name="Baker",
            locality="San Francisco",
            postal_code="94105",
            street_address1="535 Mission St, Ste 1401",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address = response.parse()
            assert_matches_type(AddressUpdateResponse, address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: MeorphisTest40) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.accounts.addresses.with_raw_response.update(
                "",
                country_code="US",
                first_name="Alice",
                last_name="Baker",
                locality="San Francisco",
                postal_code="94105",
                street_address1="535 Mission St, Ste 1401",
            )

    @parametrize
    def test_method_delete(self, client: MeorphisTest40) -> None:
        address = client.accounts.addresses.delete(
            "D4g3h5tBuVYK9",
        )
        assert address is None

    @parametrize
    def test_raw_response_delete(self, client: MeorphisTest40) -> None:
        response = client.accounts.addresses.with_raw_response.delete(
            "D4g3h5tBuVYK9",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address = response.parse()
        assert address is None

    @parametrize
    def test_streaming_response_delete(self, client: MeorphisTest40) -> None:
        with client.accounts.addresses.with_streaming_response.delete(
            "D4g3h5tBuVYK9",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address = response.parse()
            assert address is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: MeorphisTest40) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.accounts.addresses.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_account_address_create(self, client: MeorphisTest40) -> None:
        address = client.accounts.addresses.account_address_create(
            country_code="US",
            first_name="Alice",
            last_name="Baker",
            locality="San Francisco",
            postal_code="94105",
            street_address1="535 Mission St, Ste 1401",
        )
        assert_matches_type(AddressAccountAddressCreateResponse, address, path=["response"])

    @parametrize
    def test_method_account_address_create_with_all_params(self, client: MeorphisTest40) -> None:
        address = client.accounts.addresses.account_address_create(
            country_code="US",
            first_name="Alice",
            last_name="Baker",
            locality="San Francisco",
            postal_code="94105",
            street_address1="535 Mission St, Ste 1401",
            company="ACME Corporation",
            email="alice@example.com",
            is_default=True,
            phone="+14155550199",
            region="CA",
            street_address2="c/o Shipping Department",
        )
        assert_matches_type(AddressAccountAddressCreateResponse, address, path=["response"])

    @parametrize
    def test_raw_response_account_address_create(self, client: MeorphisTest40) -> None:
        response = client.accounts.addresses.with_raw_response.account_address_create(
            country_code="US",
            first_name="Alice",
            last_name="Baker",
            locality="San Francisco",
            postal_code="94105",
            street_address1="535 Mission St, Ste 1401",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address = response.parse()
        assert_matches_type(AddressAccountAddressCreateResponse, address, path=["response"])

    @parametrize
    def test_streaming_response_account_address_create(self, client: MeorphisTest40) -> None:
        with client.accounts.addresses.with_streaming_response.account_address_create(
            country_code="US",
            first_name="Alice",
            last_name="Baker",
            locality="San Francisco",
            postal_code="94105",
            street_address1="535 Mission St, Ste 1401",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address = response.parse()
            assert_matches_type(AddressAccountAddressCreateResponse, address, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAddresses:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncMeorphisTest40) -> None:
        address = await async_client.accounts.addresses.update(
            "D4g3h5tBuVYK9",
            country_code="US",
            first_name="Alice",
            last_name="Baker",
            locality="San Francisco",
            postal_code="94105",
            street_address1="535 Mission St, Ste 1401",
        )
        assert_matches_type(AddressUpdateResponse, address, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncMeorphisTest40) -> None:
        address = await async_client.accounts.addresses.update(
            "D4g3h5tBuVYK9",
            country_code="US",
            first_name="Alice",
            last_name="Baker",
            locality="San Francisco",
            postal_code="94105",
            street_address1="535 Mission St, Ste 1401",
            company="ACME Corporation",
            email="alice@example.com",
            is_default=True,
            phone="+14155550199",
            region="CA",
            street_address2="c/o Shipping Department",
        )
        assert_matches_type(AddressUpdateResponse, address, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncMeorphisTest40) -> None:
        response = await async_client.accounts.addresses.with_raw_response.update(
            "D4g3h5tBuVYK9",
            country_code="US",
            first_name="Alice",
            last_name="Baker",
            locality="San Francisco",
            postal_code="94105",
            street_address1="535 Mission St, Ste 1401",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address = await response.parse()
        assert_matches_type(AddressUpdateResponse, address, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncMeorphisTest40) -> None:
        async with async_client.accounts.addresses.with_streaming_response.update(
            "D4g3h5tBuVYK9",
            country_code="US",
            first_name="Alice",
            last_name="Baker",
            locality="San Francisco",
            postal_code="94105",
            street_address1="535 Mission St, Ste 1401",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address = await response.parse()
            assert_matches_type(AddressUpdateResponse, address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncMeorphisTest40) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.accounts.addresses.with_raw_response.update(
                "",
                country_code="US",
                first_name="Alice",
                last_name="Baker",
                locality="San Francisco",
                postal_code="94105",
                street_address1="535 Mission St, Ste 1401",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncMeorphisTest40) -> None:
        address = await async_client.accounts.addresses.delete(
            "D4g3h5tBuVYK9",
        )
        assert address is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncMeorphisTest40) -> None:
        response = await async_client.accounts.addresses.with_raw_response.delete(
            "D4g3h5tBuVYK9",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address = await response.parse()
        assert address is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncMeorphisTest40) -> None:
        async with async_client.accounts.addresses.with_streaming_response.delete(
            "D4g3h5tBuVYK9",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address = await response.parse()
            assert address is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncMeorphisTest40) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.accounts.addresses.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_account_address_create(self, async_client: AsyncMeorphisTest40) -> None:
        address = await async_client.accounts.addresses.account_address_create(
            country_code="US",
            first_name="Alice",
            last_name="Baker",
            locality="San Francisco",
            postal_code="94105",
            street_address1="535 Mission St, Ste 1401",
        )
        assert_matches_type(AddressAccountAddressCreateResponse, address, path=["response"])

    @parametrize
    async def test_method_account_address_create_with_all_params(self, async_client: AsyncMeorphisTest40) -> None:
        address = await async_client.accounts.addresses.account_address_create(
            country_code="US",
            first_name="Alice",
            last_name="Baker",
            locality="San Francisco",
            postal_code="94105",
            street_address1="535 Mission St, Ste 1401",
            company="ACME Corporation",
            email="alice@example.com",
            is_default=True,
            phone="+14155550199",
            region="CA",
            street_address2="c/o Shipping Department",
        )
        assert_matches_type(AddressAccountAddressCreateResponse, address, path=["response"])

    @parametrize
    async def test_raw_response_account_address_create(self, async_client: AsyncMeorphisTest40) -> None:
        response = await async_client.accounts.addresses.with_raw_response.account_address_create(
            country_code="US",
            first_name="Alice",
            last_name="Baker",
            locality="San Francisco",
            postal_code="94105",
            street_address1="535 Mission St, Ste 1401",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address = await response.parse()
        assert_matches_type(AddressAccountAddressCreateResponse, address, path=["response"])

    @parametrize
    async def test_streaming_response_account_address_create(self, async_client: AsyncMeorphisTest40) -> None:
        async with async_client.accounts.addresses.with_streaming_response.account_address_create(
            country_code="US",
            first_name="Alice",
            last_name="Baker",
            locality="San Francisco",
            postal_code="94105",
            street_address1="535 Mission St, Ste 1401",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address = await response.parse()
            assert_matches_type(AddressAccountAddressCreateResponse, address, path=["response"])

        assert cast(Any, response.is_closed) is True
