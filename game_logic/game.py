from  utils.deck import create_deck
from  utils.deck import shuffle
from utils.deck import compare_cards

def create_player(name: str) -> dict:
    if name == "":
        name = "AI"
    else:
        name = name

    card_list_of_player = []

    won_pile = []

    player_status = {}
    player_status["name"] = name
    player_status["hand"] = card_list_of_player
    player_status["won_pile"] = won_pile

    return player_status


def init_game(p1 ,p2) :
    player_1= create_player(p1)
    player_2 = create_player(p2)
    new_shuffle_deck = shuffle(create_deck())
    count = 0

    for for_card in new_shuffle_deck:
        if count <= 25:
            player_1["hand"].append(for_card)
            count += 1
        else:
            player_2["hand"].append(for_card)

    game_dict = {"deck": new_shuffle_deck,
                 "player_1": player_1,
                 "player_2": player_2


                 }

    return game_dict

# print(init_game("meir",""))

def play_round(player_1: dict, player_2: dict)-> None:
        compare_cards(player_1,player_2)





