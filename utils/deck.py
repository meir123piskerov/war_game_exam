from random import randint



def create_card(rank: str, suite: str) -> dict:
                list_of_cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

                suite_of_cards = ["H", "C", "D", "S"]

                card_create = {}

                for card in list_of_cards:
                    if card == rank:
                        card_create["rank"] = card

                for suite_card in suite_of_cards:
                    if suite_card == suite:
                        card_create["suite"] = suite_card

                for valuue_caed in range(len(list_of_cards)):
                    if list_of_cards[valuue_caed] == rank:
                        card_create["value"] = valuue_caed + 2


                return card_create


# print(create_card("A", "S"))

def compare_cards(p1_card: dict, p2_card: dict) -> str:

                    if p1_card["value"] > p2_card["value"]:
                        return 'p1'

                    elif p1_card["value"] < p2_card["value"]:
                        return 'p2'

                    elif p1_card["value"] == p2_card["value"]:
                        return 'WAR'

# print(compare_cards(create_card("10", "S"), create_card("10", "H")))

def create_deck() -> list[dict]:

    list_of_cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    suite_of_cards = ["H", "C", "D", "S"]

    deck_of_cards = []
    for suite in suite_of_cards:
        for card in list_of_cards:
            deck_of_cards.append(create_card(card, suite))
    return deck_of_cards

# print(len(create_deck()))


def shuffle(deck: list[dict]) -> list[dict]:
        for card in range(len(deck)):
            if deck[card] != deck[randint(0,51)]:
                 deck[card] = deck[randint(0, 51)]
            else:
                continue



        return deck

# print(shuffle(create_deck()))
# print(len(shuffle(create_deck())))
#
# d = create_deck()
# e = shuffle(d)
# print(len(e))






