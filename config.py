import os
from dotenv import load_dotenv

load_dotenv()

# Bot Information
BOT_NAME = "BC's AI"
VERSION = "1.0.0"

# Personality Settings
CHEF_STYLE = "Professional chef, storyteller, recipe expert"

# Files
PERSONALITY_FILE = "prompts/chef_personality.txt"
RECIPES_FILE = "data/recipes.txt"

# API Settings
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Telegram Settings
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")