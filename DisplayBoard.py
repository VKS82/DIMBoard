import config
from trello import TrelloClient



client = TrelloClient(api_key=config.TRELLO_API_KEY,
                      api_secret=config.TRELLO_API_SECRET,
                      token=config.TOKEN)

all_boards = client.list_boards()

print(all_boards)