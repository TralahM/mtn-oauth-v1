# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from mtn_oauth_v1 import MtnOAuthV1, AsyncMtnOAuthV1
from mtn_oauth_v1.types import Successtoken

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccessTokens:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: MtnOAuthV1) -> None:
        access_token = client.access_tokens.create(
            grant_type="client_credentials",
        )
        assert_matches_type(Successtoken, access_token, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: MtnOAuthV1) -> None:
        access_token = client.access_tokens.create(
            grant_type="client_credentials",
            client_id="client_id",
            client_secret="client_secret",
        )
        assert_matches_type(Successtoken, access_token, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: MtnOAuthV1) -> None:
        response = client.access_tokens.with_raw_response.create(
            grant_type="client_credentials",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_token = response.parse()
        assert_matches_type(Successtoken, access_token, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: MtnOAuthV1) -> None:
        with client.access_tokens.with_streaming_response.create(
            grant_type="client_credentials",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_token = response.parse()
            assert_matches_type(Successtoken, access_token, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAccessTokens:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncMtnOAuthV1) -> None:
        access_token = await async_client.access_tokens.create(
            grant_type="client_credentials",
        )
        assert_matches_type(Successtoken, access_token, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMtnOAuthV1) -> None:
        access_token = await async_client.access_tokens.create(
            grant_type="client_credentials",
            client_id="client_id",
            client_secret="client_secret",
        )
        assert_matches_type(Successtoken, access_token, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMtnOAuthV1) -> None:
        response = await async_client.access_tokens.with_raw_response.create(
            grant_type="client_credentials",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_token = await response.parse()
        assert_matches_type(Successtoken, access_token, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMtnOAuthV1) -> None:
        async with async_client.access_tokens.with_streaming_response.create(
            grant_type="client_credentials",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_token = await response.parse()
            assert_matches_type(Successtoken, access_token, path=["response"])

        assert cast(Any, response.is_closed) is True
