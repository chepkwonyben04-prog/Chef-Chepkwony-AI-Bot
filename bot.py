class ChefChepkwonyBot:

    def __init__(self):
        self.name = "Chef Chepkwony AI"

        self.personality = self.load_file(
            "prompts/chef_personality.txt"
        )

        self.recipes = self.load_file(
            "data/recipes.txt"
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
            return self.recipes[:500]

        if "who are you" in message or "name" in message:
            return self.personality

        return (
            "👨🏾‍🍳 I am Chef Chepkwony AI. "
            "Ask me about recipes, cooking tips, or food knowledge."
        )

    def run(self):

        print("👨🏾‍🍳 Chef Chepkwony AI is ready!")

        while True:
            user = input("\nYou: ")

            if user.lower() == "exit":
                print("Goodbye Chef!")
                break

            answer = self.chat(user)
            print("\nBot:", answer)