def create_card(rank: str, suite: str) -> dict:
                list_of_cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

                suite_of_cards = ["H", "C", "D", "S"]

                card_create = {}

                for i in list_of_cards:
                    if i == rank:
                        card_create["rank"] = i

                for i in suite_of_cards:
                    if i == suite:
                        card_create["suite"] = i

                for i in range(len(list_of_cards)):
                    if list_of_cards[i] == rank:
                        card_create["value"] = i + 2


                return card_create


print(create_card("A", "S"))

def compare_cards(p1_card: dict, p2_card: dict) -> str:

                    if p1_card["value"] > p2_card["value"]:
                        return 'p1'

                    elif p1_card["value"] < p2_card["value"]:
                        return 'p2'

                    elif p1_card["value"] == p2_card["value"]:
                        return 'WAR'

print(compare_cards(create_card("10", "S"), create_card("10", "H")))

def create_deck() -> list[dict]:

    deck_of_cards = []







