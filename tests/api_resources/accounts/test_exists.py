# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from meorphis_test_40 import MeorphisTest40, AsyncMeorphisTest40

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExists:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: MeorphisTest40) -> None:
        exist = client.accounts.exists.list(
            identifier={
                "identifier_type": "email",
                "identifier_value": "alice@example.com",
            },
        )
        assert exist is None

    @parametrize
    def test_raw_response_list(self, client: MeorphisTest40) -> None:
        response = client.accounts.exists.with_raw_response.list(
            identifier={
                "identifier_type": "email",
                "identifier_value": "alice@example.com",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exist = response.parse()
        assert exist is None

    @parametrize
    def test_streaming_response_list(self, client: MeorphisTest40) -> None:
        with client.accounts.exists.with_streaming_response.list(
            identifier={
                "identifier_type": "email",
                "identifier_value": "alice@example.com",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exist = response.parse()
            assert exist is None

        assert cast(Any, response.is_closed) is True


class TestAsyncExists:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncMeorphisTest40) -> None:
        exist = await async_client.accounts.exists.list(
            identifier={
                "identifier_type": "email",
                "identifier_value": "alice@example.com",
            },
        )
        assert exist is None

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMeorphisTest40) -> None:
        response = await async_client.accounts.exists.with_raw_response.list(
            identifier={
                "identifier_type": "email",
                "identifier_value": "alice@example.com",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exist = await response.parse()
        assert exist is None

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMeorphisTest40) -> None:
        async with async_client.accounts.exists.with_streaming_response.list(
            identifier={
                "identifier_type": "email",
                "identifier_value": "alice@example.com",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exist = await response.parse()
            assert exist is None

        assert cast(Any, response.is_closed) is True
