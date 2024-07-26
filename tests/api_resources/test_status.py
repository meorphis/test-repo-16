# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from meorphis_test_40 import MeorphisTest40, AsyncMeorphisTest40

from meorphis_test_40.types import StatusListResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from meorphis_test_40 import MeorphisTest40, AsyncMeorphisTest40
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

class TestStatus:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    def test_method_list(self, client: MeorphisTest40) -> None:
        status = client.status.list()
        assert_matches_type(StatusListResponse, status, path=['response'])

    @parametrize
    def test_raw_response_list(self, client: MeorphisTest40) -> None:

        response = client.status.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        status = response.parse()
        assert_matches_type(StatusListResponse, status, path=['response'])

    @parametrize
    def test_streaming_response_list(self, client: MeorphisTest40) -> None:
        with client.status.with_streaming_response.list() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            status = response.parse()
            assert_matches_type(StatusListResponse, status, path=['response'])

        assert cast(Any, response.is_closed) is True
class TestAsyncStatus:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    async def test_method_list(self, async_client: AsyncMeorphisTest40) -> None:
        status = await async_client.status.list()
        assert_matches_type(StatusListResponse, status, path=['response'])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMeorphisTest40) -> None:

        response = await async_client.status.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        status = await response.parse()
        assert_matches_type(StatusListResponse, status, path=['response'])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMeorphisTest40) -> None:
        async with async_client.status.with_streaming_response.list() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            status = await response.parse()
            assert_matches_type(StatusListResponse, status, path=['response'])

        assert cast(Any, response.is_closed) is True