import os

from config import BOT_NAME, PERSONALITY_FILE, RECIPES_FILE


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
            with open(file_path, "r", encoding="utf-8") as file:
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
                "I am your culinary assistant by Chef Chepkwony. "
                "Ask me about Kenyan cuisines, African cuisines, "
                "International cuisines, recipes, and cooking tips."
            )


        return (
            "🤖 I am BC's AI, the official culinary assistant by Chef Chepkwony.\n\n"
            "Ask me about recipes, cooking techniques, food knowledge, "
            "or cuisines from Kenya, Africa, and around the world."
        )


    def run(self):

        print("🤖 BC's AI is ready!")

        while True:

            user = input("\nYou: ")

            if user.lower() == "exit":

                print("Goodbye Chef! 👨🏾‍🍳")
                break


            answer = self.chat(user)

            print("\nBC's AI:", answer)



if __name__ == "__main__":

    bot = ChefChepkwonyBot()

    bot.run()