from setuptools import setup

setup(
    name="chatg",
    version=1.0,
    packages=["chatg"],
    install_requires=["click", "asyncio", "openai", "python-telegram-bot", "requests", "yfinance", "qrcode", "bip32utils", "bip39"],
    entry_points={"chatgsole_scripts": ["chatg = chatg.cli:cli"]},
)
