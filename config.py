import os

# Bot Information
BOT_NAME = "Chef Chepkwony AI"
VERSION = "1.0.0"

# Personality Settings
CHEF_STYLE = "Professional chef, storyteller, recipe expert"

# Files
PERSONALITY_FILE = "prompts/chef_personality.txt"
RECIPES_FILE = "data/recipes.txt"

# API Settings (ongeza key baadaye)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")