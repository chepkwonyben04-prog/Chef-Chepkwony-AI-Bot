import os

class ChefChepkwonyBot:

    def __init__(self):
        self.name = "Chef Chepkwony AI"

        self.personality = self.load_file(
            "prompts/chef_personality.txt"
        )

        self.recipes = self.load_file(
            "data/recipes.txt"
        )

    def load_file(self, path):
        try:
            with open(path, "r", encoding="utf-8") as file:
                return file.read()
        except FileNotFoundError:
            return ""

    def chat(self, message):
        response = f"""
👨🏾‍🍳 {self.name}

Message received:
{message}

I am trained with Chef Chepkwony's cooking knowledge.
"""
        return response

    def run(self):
        print(f"{self.name} is ready!")

        while True:
            user_input = input("\nYou: ")

            if user_input.lower() in ["exit", "quit"]:
                print("Chef Chepkwony AI shutting down...")
                break

            print(self.chat(user_input))