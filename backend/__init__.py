import logging
proj_name = 'SubscribePro'
# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.getLogger('httpx').setLevel(logging.ERROR)
# Initialize the bot
