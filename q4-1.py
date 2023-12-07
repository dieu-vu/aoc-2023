def string_to_number_list(s):
    return s.strip().split()

def get_card_points(lines):
    total_point = 0
    for line in lines:
        numbers = line.strip().split(':')[1]
        winning_numbers = string_to_number_list(numbers.split('|')[0])
        own_numbers = string_to_number_list(numbers.split('|')[1])
        number_of_winning_numbers = list(set(own_numbers) & set(winning_numbers))
        if len(number_of_winning_numbers) >=1:
            total_point += 2**(len(number_of_winning_numbers)-1)
    return total_point

def main():
    file = open("input4.txt")
    lines = file.readlines()
    print(get_card_points(lines))

if __name__ == "__main__":
    main()
    
