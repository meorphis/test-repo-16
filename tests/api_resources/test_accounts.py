# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from meorphis_test_40 import MeorphisTest40, AsyncMeorphisTest40
from meorphis_test_40.types import AccountAccountGetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccounts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_account_get(self, client: MeorphisTest40) -> None:
        account = client.accounts.account_get()
        assert_matches_type(AccountAccountGetResponse, account, path=["response"])

    @parametrize
    def test_raw_response_account_get(self, client: MeorphisTest40) -> None:
        response = client.accounts.with_raw_response.account_get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountAccountGetResponse, account, path=["response"])

    @parametrize
    def test_streaming_response_account_get(self, client: MeorphisTest40) -> None:
        with client.accounts.with_streaming_response.account_get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountAccountGetResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAccounts:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_account_get(self, async_client: AsyncMeorphisTest40) -> None:
        account = await async_client.accounts.account_get()
        assert_matches_type(AccountAccountGetResponse, account, path=["response"])

    @parametrize
    async def test_raw_response_account_get(self, async_client: AsyncMeorphisTest40) -> None:
        response = await async_client.accounts.with_raw_response.account_get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountAccountGetResponse, account, path=["response"])

    @parametrize
    async def test_streaming_response_account_get(self, async_client: AsyncMeorphisTest40) -> None:
        async with async_client.accounts.with_streaming_response.account_get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountAccountGetResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True
