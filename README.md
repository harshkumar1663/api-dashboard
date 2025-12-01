# API Dashboard (CLI)

Author: Harsh Kumar

A command-line dashboard that fetches:

- Current **weather**
- **Crypto** prices (BTC, ETH vs base currency)
- Top **technology news** headlines

The design is modular: a config loader, separate HTTP clients, and a
simple rendering layer. This structure is production friendly and easy to test.

---

## Tech Stack

- Python 3.11+
- `requests`
- `.env`-based configuration

---

## Setup

```bash
git clone https://github.com/harshkumar1663/api-dashboard.git
cd api-dashboard

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
cp .env.example .env  # and fill in your keys
