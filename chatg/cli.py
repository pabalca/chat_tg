import click
import logging
import os
import sys

from telegram import __version__ as TG_VER

try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

if __version_info__ < (20, 0, 0, "alpha", 1):
    raise RuntimeError(
        f"This example is not compatible with your current PTB version {TG_VER}. To view the "
        f"{TG_VER} version of this example, "
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
    )

from telegram import ForceReply, Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)
from chatg.decorators import authorized_users_only
from chatg.functions import (
    start,
    help_command,
    price_command,
    userid_command,
    echo,
    chat_command,
    menu_command,
    key_command,
)


@click.command()
def cli():
    """Start the bot."""

    # Create the Application and pass it your bot's token.
    bot_token = os.getenv("TG_TOKEN")
    if not bot_token:
        logging.error("Not TG_TOKEN defined")
        return
    application = Application.builder().token(bot_token).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("price", price_command))
    application.add_handler(CommandHandler("userid", userid_command))
    application.add_handler(CommandHandler("menu", menu_command))
    application.add_handler(CommandHandler("key", key_command))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, chat_command)
    )

    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    cli()
