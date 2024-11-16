# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import access_token_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.successtoken import Successtoken

__all__ = ["AccessTokensResource", "AsyncAccessTokensResource"]


class AccessTokensResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccessTokensResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/TralahM/mtn-oauth-v1#accessing-raw-response-data-eg-headers
        """
        return AccessTokensResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccessTokensResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/TralahM/mtn-oauth-v1#with_streaming_response
        """
        return AccessTokensResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        grant_type: Literal["client_credentials"],
        client_id: str | NotGiven = NOT_GIVEN,
        client_secret: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Successtoken:
        """
        OAuth2 endpoint that provides an access token for consumers of other endpoints.

        Args:
          grant_type: Type of grant i.e client credentials

          client_id: The client identifier / username.

          client_secret: The client secret / password.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/access_token",
            body=maybe_transform(
                {
                    "client_id": client_id,
                    "client_secret": client_secret,
                },
                access_token_create_params.AccessTokenCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"grant_type": grant_type}, access_token_create_params.AccessTokenCreateParams),
            ),
            cast_to=Successtoken,
        )


class AsyncAccessTokensResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccessTokensResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/TralahM/mtn-oauth-v1#accessing-raw-response-data-eg-headers
        """
        return AsyncAccessTokensResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccessTokensResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/TralahM/mtn-oauth-v1#with_streaming_response
        """
        return AsyncAccessTokensResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        grant_type: Literal["client_credentials"],
        client_id: str | NotGiven = NOT_GIVEN,
        client_secret: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Successtoken:
        """
        OAuth2 endpoint that provides an access token for consumers of other endpoints.

        Args:
          grant_type: Type of grant i.e client credentials

          client_id: The client identifier / username.

          client_secret: The client secret / password.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/access_token",
            body=await async_maybe_transform(
                {
                    "client_id": client_id,
                    "client_secret": client_secret,
                },
                access_token_create_params.AccessTokenCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"grant_type": grant_type}, access_token_create_params.AccessTokenCreateParams
                ),
            ),
            cast_to=Successtoken,
        )


class AccessTokensResourceWithRawResponse:
    def __init__(self, access_tokens: AccessTokensResource) -> None:
        self._access_tokens = access_tokens

        self.create = to_raw_response_wrapper(
            access_tokens.create,
        )


class AsyncAccessTokensResourceWithRawResponse:
    def __init__(self, access_tokens: AsyncAccessTokensResource) -> None:
        self._access_tokens = access_tokens

        self.create = async_to_raw_response_wrapper(
            access_tokens.create,
        )


class AccessTokensResourceWithStreamingResponse:
    def __init__(self, access_tokens: AccessTokensResource) -> None:
        self._access_tokens = access_tokens

        self.create = to_streamed_response_wrapper(
            access_tokens.create,
        )


class AsyncAccessTokensResourceWithStreamingResponse:
    def __init__(self, access_tokens: AsyncAccessTokensResource) -> None:
        self._access_tokens = access_tokens

        self.create = async_to_streamed_response_wrapper(
            access_tokens.create,
        )
