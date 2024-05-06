# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from meorphis_test_40 import MeorphisTest40, AsyncMeorphisTest40
from meorphis_test_40._utils import parse_datetime
from meorphis_test_40.types.testings import AccountTestingAccountCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccounts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_testing_account_create(self, client: MeorphisTest40) -> None:
        account = client.testings.accounts.testing_account_create(
            deactivate_at=parse_datetime("2017-07-21T17:32:28Z"),
            email_state="unverified",
            phone_state="verified",
        )
        assert_matches_type(AccountTestingAccountCreateResponse, account, path=["response"])

    @parametrize
    def test_method_testing_account_create_with_all_params(self, client: MeorphisTest40) -> None:
        account = client.testings.accounts.testing_account_create(
            deactivate_at=parse_datetime("2017-07-21T17:32:28Z"),
            email_state="unverified",
            phone_state="verified",
            has_address=True,
            is_migrated=True,
        )
        assert_matches_type(AccountTestingAccountCreateResponse, account, path=["response"])

    @parametrize
    def test_raw_response_testing_account_create(self, client: MeorphisTest40) -> None:
        response = client.testings.accounts.with_raw_response.testing_account_create(
            deactivate_at=parse_datetime("2017-07-21T17:32:28Z"),
            email_state="unverified",
            phone_state="verified",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountTestingAccountCreateResponse, account, path=["response"])

    @parametrize
    def test_streaming_response_testing_account_create(self, client: MeorphisTest40) -> None:
        with client.testings.accounts.with_streaming_response.testing_account_create(
            deactivate_at=parse_datetime("2017-07-21T17:32:28Z"),
            email_state="unverified",
            phone_state="verified",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountTestingAccountCreateResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAccounts:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_testing_account_create(self, async_client: AsyncMeorphisTest40) -> None:
        account = await async_client.testings.accounts.testing_account_create(
            deactivate_at=parse_datetime("2017-07-21T17:32:28Z"),
            email_state="unverified",
            phone_state="verified",
        )
        assert_matches_type(AccountTestingAccountCreateResponse, account, path=["response"])

    @parametrize
    async def test_method_testing_account_create_with_all_params(self, async_client: AsyncMeorphisTest40) -> None:
        account = await async_client.testings.accounts.testing_account_create(
            deactivate_at=parse_datetime("2017-07-21T17:32:28Z"),
            email_state="unverified",
            phone_state="verified",
            has_address=True,
            is_migrated=True,
        )
        assert_matches_type(AccountTestingAccountCreateResponse, account, path=["response"])

    @parametrize
    async def test_raw_response_testing_account_create(self, async_client: AsyncMeorphisTest40) -> None:
        response = await async_client.testings.accounts.with_raw_response.testing_account_create(
            deactivate_at=parse_datetime("2017-07-21T17:32:28Z"),
            email_state="unverified",
            phone_state="verified",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountTestingAccountCreateResponse, account, path=["response"])

    @parametrize
    async def test_streaming_response_testing_account_create(self, async_client: AsyncMeorphisTest40) -> None:
        async with async_client.testings.accounts.with_streaming_response.testing_account_create(
            deactivate_at=parse_datetime("2017-07-21T17:32:28Z"),
            email_state="unverified",
            phone_state="verified",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountTestingAccountCreateResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True
