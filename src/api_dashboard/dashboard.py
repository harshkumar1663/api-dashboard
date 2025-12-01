"""
CLI dashboard to show weather, crypto prices, and news in a neat table.

Author: Harsh Kumar
"""

from __future__ import annotations

import argparse
import logging
from textwrap import shorten

from .clients import get_crypto_prices, get_top_headlines, get_weather
from .config import AppConfig, load_config

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] [%(levelname)s] %(name)s - %(message)s",
)


def render_dashboard(config: AppConfig) -> None:
    """Fetch data from APIs and pretty-print to console."""
    weather = get_weather(config)
    crypto = get_crypto_prices(config, ["BTC", "ETH"])
    news = get_top_headlines(config, limit=5)

    print("=" * 60)
    print(f" API Dashboard - Harsh Kumar ".center(60, "="))
    print("=" * 60)
    print("\n[Weather]")
    current = weather.get("current_weather", {})
    print(f"City: {config.city}")
    print(f"Temperature: {current.get('temperature', 'N/A')}°C")
    print(f"Wind: {current.get('windspeed', 'N/A')} km/h")

    print("\n[Crypto]")
    for coin_id, price_data in crypto.items():
        price = price_data.get(config.base_currency.lower(), "N/A")
        print(f"{coin_id.title():<10} {price} {config.base_currency}")

    print("\n[Top Tech News]")
    for idx, article in enumerate(news, start=1):
        title = shorten(article.get("title", "Untitled"), width=70, placeholder="...")
        print(f"{idx}. {title}")

    print("\n" + "=" * 60)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="API Dashboard CLI")
    parser.add_argument(
        "--city",
        type=str,
        help="Override default city for weather.",
    )
    parser.add_argument(
        "--currency",
        type=str,
        help="Override base currency for crypto prices.",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    config = load_config()

    if args.city:
        config.city = args.city
    if args.currency:
        config.base_currency = args.currency

    render_dashboard(config)


if __name__ == "__main__":
    main()
