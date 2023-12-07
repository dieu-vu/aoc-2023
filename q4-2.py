def string_to_number_list(s):
    return s.strip().split()

def get_winning_number_count(card_number_str):
    winning_numbers = string_to_number_list(card_number_str.split('|')[0])
    own_numbers = string_to_number_list(card_number_str.split('|')[1])
    return len(list(set(own_numbers) & set(winning_numbers)))

def get_card_result(card):
    numbers = card.strip().split(':')[1]
    card_number = int(card.strip().split(':')[0].strip().split()[1])
    win_count = get_winning_number_count(numbers)
    win_card_numbers = [i for i in range(card_number+1, card_number+win_count+1)]
    return {card_number: win_card_numbers}

def get_card_results_dict(cards):
    card_results_dict = {}
    for card in cards:
        card_result = get_card_result(card)
        card_results_dict.update(card_result)
    return card_results_dict

def get_winning_card_list(cards):
    card_results_dict = get_card_results_dict(cards)
    return [k for k, v in card_results_dict.items() if len(v) > 0]
      

def main():
    file = open("input4.txt")
    lines = file.readlines()
    card_results_dict = get_card_results_dict(lines)
    winning_list = get_winning_card_list(lines)
    not_winning_card_count = len(lines) - len(winning_list)
    ind = 0
    while ind < len(winning_list):
        winning_list += card_results_dict.get(winning_list[ind])
        ind += 1
    print(len(winning_list) + not_winning_card_count)
        

if __name__ == "__main__":
    main()
    