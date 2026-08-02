from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

from config import (
    BOT_NAME,
    PERSONALITY_FILE,
    RECIPES_FILE,
    TELEGRAM_TOKEN
)


class ChefChepkwonyBot:

    def __init__(self):

        self.name = "BC's AI"

        self.personality = self.load_file(
            PERSONALITY_FILE
        )

        self.recipes = self.load_file(
            RECIPES_FILE
        )


    def load_file(self, file_path):

        try:
            with open(
                file_path,
                "r",
                encoding="utf-8"
            ) as file:

                return file.read()

        except FileNotFoundError:

            return "File not found."


    def chat(self, message):

        message = message.lower()


        if "recipe" in message or "cook" in message:

            return (
                "👨🏾‍🍳 Here is some culinary knowledge from BC's AI:\n\n"
                + self.recipes[:1000]
            )


        if "who are you" in message or "name" in message:

            return self.personality


        if "hello" in message or "hi" in message:

            return (
                "👋 Welcome to BC's AI!\n\n"
                "I am the official culinary assistant by Chef Chepkwony.\n\n"
                "Ask me about Kenyan cuisines, African cuisines, "
                "International cuisines, recipes, and cooking tips."
            )


        return (
            "🤖 I am BC's AI, the official culinary assistant by Chef Chepkwony.\n\n"
            "Ask me about recipes, cooking techniques, food knowledge, "
            "or cuisines from Kenya, Africa, and around the world."
        )


    async def start(
        self,
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
    ):

        await update.message.reply_text(
            "👋 Welcome to BC's AI!\n\n"
            "I am the official culinary assistant by Chef Chepkwony.\n\n"
            "Ask me about recipes, cooking tips, "
            "Kenyan cuisines, African cuisines, "
            "and global cuisines."
        )


    async def message_handler(
        self,
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
    ):

        user_message = update.message.text

        answer = self.chat(user_message)

        await update.message.reply_text(answer)



if __name__ == "__main__":

    bot = ChefChepkwonyBot()


    app = Application.builder().token(
        TELEGRAM_TOKEN
    ).build()


    app.add_handler(
        CommandHandler(
            "start",
            bot.start
        )
    )


    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            bot.message_handler
        )
    )


    print("🤖 BC's AI Telegram Bot is running...")


    app.run_polling()