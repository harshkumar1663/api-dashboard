"""
HTTP clients that talk to external APIs.

These functions are small and pure, so they are easy to unit test by mocking `requests`.
"""

from __future__ import annotations

import logging
from typing import Any, Dict, List

import requests  # type: ignore

from .config import AppConfig

logger = logging.getLogger(__name__)


class APIError(RuntimeError):
    """Generic API error for dashboard clients."""


def _handle_response(response: requests.Response) -> Dict[str, Any]:
    """Validate HTTP response and return JSON or raise APIError."""
    try:
        response.raise_for_status()
        return response.json()
    except requests.RequestException as exc:  # network / HTTP issues
        logger.exception("API request failed.")
        raise APIError(str(exc)) from exc


def get_weather(config: AppConfig) -> Dict[str, Any]:
    """
    Fetch current weather for a configured city.

    Uses a public-style endpoint (replace with actual provider).
    """
    logger.info("Fetching weather for %s", config.city)
    # Example URL pattern; replace with your chosen provider.
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": "28.6139",  # Delhi approx
        "longitude": "77.2090",
        "current_weather": "true",
    }
    response = requests.get(url, params=params, timeout=10)
    return _handle_response(response)


def get_crypto_prices(config: AppConfig, symbols: List[str]) -> Dict[str, Any]:
    """
    Fetch crypto prices for selected symbols (e.g., ['BTC', 'ETH']).

    Uses a public demo endpoint for demonstration.
    """
    logger.info("Fetching crypto prices for %s", ", ".join(symbols))
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": ",".join(["bitcoin", "ethereum"]),
        "vs_currencies": config.base_currency.lower(),
    }
    response = requests.get(url, params=params, timeout=10)
    return _handle_response(response)


def get_top_headlines(config: AppConfig, limit: int = 5) -> List[Dict[str, Any]]:
    """
    Fetch top news headlines (technology category example).

    Uses a demo-like structure; in real usage, plug in a news provider.
    """
    logger.info("Fetching top news headlines.")
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "country": "in",
        "category": "technology",
        "pageSize": limit,
        "apiKey": config.news_api_key ,
    }
    response = requests.get(url, params=params, timeout=10)
    data = _handle_response(response)
    return data.get("articles", [])
