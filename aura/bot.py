from . import client

bot = client.Client()

import sys
sys.modules["bot"] = bot