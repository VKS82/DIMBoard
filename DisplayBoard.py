import config
from trello import TrelloClient
from LoadJSON import LoadJSON
from DraftPicks import draft_picks

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

year = '2022'

for team in DIM_board.all_lists():
    for pick in draft_picks:
        card_name = pick+' '+year+' '+team.name
        if '_' in card_name:
            team.add_card(name=card_name)

