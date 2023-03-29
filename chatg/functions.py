import logging
from telegram import ForceReply, Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)
from telegram import ReplyKeyboardMarkup, KeyboardButton

from chatg.decorators import authorized_users_only
from chatg.chat import question
from chatg.finance import get_price
from chatg.bitcoin import generate_key


@authorized_users_only
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    photo_url = "https://cdn.dribbble.com/users/1117770/screenshots/2626626/welcome.gif"
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        # reply_markup=ForceReply(selective=False),
    )
    await context.bot.send_photo(chat_id=update.message.chat_id, photo=photo_url)


@authorized_users_only
async def price_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    token_list = context.args
    if not token_list:
        token_list = ["btc-usd", "eth-usd"]
    message = ""
    for token in token_list:
        data = get_price(token)
        message += f"{token} = {data['price']} {data['currency']} \n"
    await update.message.reply_text(message)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "\nAvailable commands:\n\n"
        "* /start : Say hi to the bot.\n"
        "* /userid : Get you user_id.\n"
        "* /price <price> : Get token prices.\n"
        "* /key <secret> : Get bitcoin private key.\n"
        "* /help : Show available commands."
    )


async def userid_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(update.effective_user.id)


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    await update.message.reply_text(update.message.text)


@authorized_users_only
async def chat_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user.id
    answer = question(update.message.text)
    logging.info(f"user={user}; question={update.message.text}; answer={answer}")
    await update.message.reply_text(answer)


@authorized_users_only
async def menu_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Create a list of button labels
    button_list = [
        [KeyboardButton("/start")],
        [KeyboardButton("/price")],
        [KeyboardButton("/key")],
        [KeyboardButton("/help")],
    ]

    # Create a reply keyboard markup object
    reply_markup = ReplyKeyboardMarkup(button_list, resize_keyboard=True)

    # Send a message with the button menu
    await update.message.reply_text(
        "Please choose an option:",
        reply_markup=reply_markup,
    )


async def key_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    secret = " ".join(context.args)
    logging.info(f"secret = {secret}")
    seed, qr = generate_key(secret)
    await context.bot.send_photo(chat_id=update.message.chat_id, photo=qr)
    await update.message.reply_text(seed)
