import sys
sys.path.append("/home/ejvlf/personal/adventofcode2021")
print(sys.path)

from common.text_manipulations import TextParser

NUMBER_OF_COLUMNS = 5
NUMBER_OF_ROWS = 5

# Create a bingo card with number as key for fast evaluation and tuple as prize and line number
def generate_card (source_data : list) -> dict:

    card = {}    

    for i, line in enumerate(source_data):
        
        col_counter = 1

        for number in line:

            if number == "":
                continue
                        
            card[int(number)] = (False, i + 1, col_counter)
            col_counter += 1

    return card
    
def parse_source_file(source: list):

    withdrawn_numbers = []
    card_number_list = []
    current_card = []

    withdrawn_numbers = source[0]

    for row in source[2:]:

        if row == "":
            card_number_list.append(current_card)
            current_card = []
            continue

        current_card.append(row.split(" "))

    return withdrawn_numbers, card_number_list

def card_checker (number : int, cards : list):

    for card in cards:

        if number in card:

            card[number] = (True, card[number][1], card[number][2])

    return cards
        
def victory_checker (cards : list) -> list:

    winners = []

    def card_filter(card, callback) -> list:
        list_of_rows = []
        list_of_cols = []
        
        for (key, value) in card.items():
            
            if callback(value):
                list_of_rows.append(value[1])
                list_of_cols.append(value[2])        
        
        return set(list_of_rows), set(list_of_cols)

    for card in cards:

        # Return rows and columns that don't have a hit
        loser_rows, loser_cols = card_filter(card, lambda val : val[0] == False)        

        if len(loser_rows) < NUMBER_OF_ROWS or len(loser_cols) < NUMBER_OF_COLUMNS:            

            winners.append(card)

    if len(winners) > 0:

        return winners
                   
    return


#Run the numbers and tag the cards as numbers come out. Return the winning card
def run_the_numbers(numbers: list, cards: list, part="") -> dict:

    total_cards = len(cards)

    for number in numbers:

        print(f"Number: {number}")

        card_checker(int(number), cards)

        winning_card = victory_checker(cards)

        if winning_card is not None and part == "":

            print("We have a winner")

            return winning_card[0], number

        elif winning_card is not None and part == "part2":

            for card in winning_card:
                
                # Remnove from all the cards
                cards.remove(card)
                current_size = len(cards)

                print(f"We have a winner. Removed {card}. We still have {current_size} out of {total_cards}")

                if len(cards) == 0:

                    print(f"Last winner: {card}")
                    return card, number

    return winning_card, number

def score_calculator(victory_number : int, victory_card : dict) -> int:

        list_of_numbers = []
        
        for (key, value) in victory_card.items():

            if value[0] == False:

                list_of_numbers.append(key)

        return sum(list_of_numbers) * victory_number
        

def run():

    #source file loading
    source_list = TextParser("day4.txt", parse_to_ints=False).load_file_as_list()
    numbers, cards_list = parse_source_file(source_list)
    numbers = [ int(number) for number in numbers.split(",")]

    list_of_cards_to_eval = []
    part_2_cards = []

    for card in cards_list:

        list_of_cards_to_eval.append(generate_card(card))

    # Part 1 
    winner_card, winner_number = run_the_numbers(numbers, list_of_cards_to_eval)

    score = score_calculator(winner_number, winner_card)
    print(f"Part 1 score: {score}")

    # Part 2

    for card in cards_list:

        part_2_cards.append(generate_card(card))

    winner_card, winner_number = run_the_numbers(numbers, part_2_cards, "part2")
    score = score_calculator(winner_number, winner_card)
    print(f"Part 2 score: {score}")


        
if __name__ == "__main__":

    run()