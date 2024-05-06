# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from meorphis_test_40 import MeorphisTest40, AsyncMeorphisTest40
from meorphis_test_40.types import (
    WebhookListResponse,
    WebhookCreateResponse,
    WebhookRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebhooks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_create(self, client: MeorphisTest40) -> None:
        webhook = client.webhooks.create(
            event={
                "tag": "group",
                "event_group": "all",
            },
            url="https://www.example.com/webhook",
        )
        assert_matches_type(WebhookCreateResponse, webhook, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_create(self, client: MeorphisTest40) -> None:
        response = client.webhooks.with_raw_response.create(
            event={
                "tag": "group",
                "event_group": "all",
            },
            url="https://www.example.com/webhook",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookCreateResponse, webhook, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_create(self, client: MeorphisTest40) -> None:
        with client.webhooks.with_streaming_response.create(
            event={
                "tag": "group",
                "event_group": "all",
            },
            url="https://www.example.com/webhook",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookCreateResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: MeorphisTest40) -> None:
        webhook = client.webhooks.retrieve(
            "wh_za7VbYcSQU2zRgGQXQAm-g",
        )
        assert_matches_type(WebhookRetrieveResponse, webhook, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: MeorphisTest40) -> None:
        response = client.webhooks.with_raw_response.retrieve(
            "wh_za7VbYcSQU2zRgGQXQAm-g",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookRetrieveResponse, webhook, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: MeorphisTest40) -> None:
        with client.webhooks.with_streaming_response.retrieve(
            "wh_za7VbYcSQU2zRgGQXQAm-g",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookRetrieveResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: MeorphisTest40) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.webhooks.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: MeorphisTest40) -> None:
        webhook = client.webhooks.list()
        assert_matches_type(WebhookListResponse, webhook, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: MeorphisTest40) -> None:
        response = client.webhooks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookListResponse, webhook, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: MeorphisTest40) -> None:
        with client.webhooks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookListResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: MeorphisTest40) -> None:
        webhook = client.webhooks.delete(
            "wh_za7VbYcSQU2zRgGQXQAm-g",
        )
        assert webhook is None

    @parametrize
    def test_raw_response_delete(self, client: MeorphisTest40) -> None:
        response = client.webhooks.with_raw_response.delete(
            "wh_za7VbYcSQU2zRgGQXQAm-g",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert webhook is None

    @parametrize
    def test_streaming_response_delete(self, client: MeorphisTest40) -> None:
        with client.webhooks.with_streaming_response.delete(
            "wh_za7VbYcSQU2zRgGQXQAm-g",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert webhook is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: MeorphisTest40) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.webhooks.with_raw_response.delete(
                "",
            )


class TestAsyncWebhooks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_create(self, async_client: AsyncMeorphisTest40) -> None:
        webhook = await async_client.webhooks.create(
            event={
                "tag": "group",
                "event_group": "all",
            },
            url="https://www.example.com/webhook",
        )
        assert_matches_type(WebhookCreateResponse, webhook, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMeorphisTest40) -> None:
        response = await async_client.webhooks.with_raw_response.create(
            event={
                "tag": "group",
                "event_group": "all",
            },
            url="https://www.example.com/webhook",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookCreateResponse, webhook, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMeorphisTest40) -> None:
        async with async_client.webhooks.with_streaming_response.create(
            event={
                "tag": "group",
                "event_group": "all",
            },
            url="https://www.example.com/webhook",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookCreateResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMeorphisTest40) -> None:
        webhook = await async_client.webhooks.retrieve(
            "wh_za7VbYcSQU2zRgGQXQAm-g",
        )
        assert_matches_type(WebhookRetrieveResponse, webhook, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMeorphisTest40) -> None:
        response = await async_client.webhooks.with_raw_response.retrieve(
            "wh_za7VbYcSQU2zRgGQXQAm-g",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookRetrieveResponse, webhook, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMeorphisTest40) -> None:
        async with async_client.webhooks.with_streaming_response.retrieve(
            "wh_za7VbYcSQU2zRgGQXQAm-g",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookRetrieveResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMeorphisTest40) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.webhooks.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncMeorphisTest40) -> None:
        webhook = await async_client.webhooks.list()
        assert_matches_type(WebhookListResponse, webhook, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMeorphisTest40) -> None:
        response = await async_client.webhooks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookListResponse, webhook, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMeorphisTest40) -> None:
        async with async_client.webhooks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookListResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncMeorphisTest40) -> None:
        webhook = await async_client.webhooks.delete(
            "wh_za7VbYcSQU2zRgGQXQAm-g",
        )
        assert webhook is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncMeorphisTest40) -> None:
        response = await async_client.webhooks.with_raw_response.delete(
            "wh_za7VbYcSQU2zRgGQXQAm-g",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert webhook is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncMeorphisTest40) -> None:
        async with async_client.webhooks.with_streaming_response.delete(
            "wh_za7VbYcSQU2zRgGQXQAm-g",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert webhook is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncMeorphisTest40) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.webhooks.with_raw_response.delete(
                "",
            )
