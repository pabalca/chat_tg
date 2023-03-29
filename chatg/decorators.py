import logging


authorized_users = [716400002, 8006572, 7547655, 5331343045, 354206380]


def authorized_users_only(func):
    async def wrapper(update, context):
        user_id = update.effective_user.id
        if user_id in authorized_users:
            # If user is authorized, run the original function
            return await func(update, context)
        else:
            # If user is not authorized, do nothing
            error = f"Unauthorized access denied for user {user_id}"
            logging.info(error)
            return await update.message.reply_text(error)

    return wrapper
