# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AccessTokenCreateParams"]


class AccessTokenCreateParams(TypedDict, total=False):
    grant_type: Required[Literal["client_credentials"]]
    """Type of grant i.e client credentials"""

    client_id: str
    """The client identifier / username."""

    client_secret: str
    """The client secret / password."""
