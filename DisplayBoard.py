import config
from trello import TrelloClient
from LoadJSON import LoadJSON

DIM_params = LoadJSON()

search_id = DIM_params['id']


client = TrelloClient(api_key=config.TRELLO_API_KEY,
                      api_secret=config.TRELLO_API_SECRET,
                      token=config.TOKEN)

all_boards = client.list_boards()

for i in all_boards:
    if i.id == search_id:
        DIM_board = i
        break

print(DIM_board.id)
print(DIM_board.all_lists())

for team in DIM_board.all_lists():
    print(team.list_cards())


