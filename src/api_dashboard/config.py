"""
Configuration utilities for API Dashboard.

Reads API keys and configuration from environment variables.
"""

from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass
class AppConfig:
    news_api_key: str 
    weather_api_key: str | None
    crypto_api_key: str | None
    city: str
    base_currency: str


def load_config() -> AppConfig:
    """
    Load configuration from environment variables.

    For security, keys are not hardcoded. This is production best practice.
    """
    print(os.getenv("NEWS_API_KEY"))
    return AppConfig(
        weather_api_key=os.getenv("WEATHER_API_KEY"),
        crypto_api_key=os.getenv("CRYPTO_API_KEY"),
        news_api_key=os.getenv("NEWS_API_KEY"),
        city=os.getenv("DASHBOARD_CITY", "Delhi"),
        base_currency=os.getenv("BASE_CURRENCY", "USD"),
    )
