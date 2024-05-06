# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from meorphis_test_40 import MeorphisTest40, AsyncMeorphisTest40
from meorphis_test_40.types.testings import CreditCardListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCreditCards:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: MeorphisTest40) -> None:
        credit_card = client.testings.credit_cards.list()
        assert_matches_type(CreditCardListResponse, credit_card, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: MeorphisTest40) -> None:
        response = client.testings.credit_cards.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_card = response.parse()
        assert_matches_type(CreditCardListResponse, credit_card, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: MeorphisTest40) -> None:
        with client.testings.credit_cards.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_card = response.parse()
            assert_matches_type(CreditCardListResponse, credit_card, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCreditCards:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncMeorphisTest40) -> None:
        credit_card = await async_client.testings.credit_cards.list()
        assert_matches_type(CreditCardListResponse, credit_card, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMeorphisTest40) -> None:
        response = await async_client.testings.credit_cards.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_card = await response.parse()
        assert_matches_type(CreditCardListResponse, credit_card, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMeorphisTest40) -> None:
        async with async_client.testings.credit_cards.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_card = await response.parse()
            assert_matches_type(CreditCardListResponse, credit_card, path=["response"])

        assert cast(Any, response.is_closed) is True
