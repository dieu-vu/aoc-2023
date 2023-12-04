file = open("input3.txt", "r")
lines = file.readlines()

def is_symbol(s):
    return not(s == '.' or  s.isalnum())

def check_number_in_line(line_index):
    line = lines[line_index].strip()
    start_i = 0
    end_i = 0
    in_a_number = False
    number_value = ''
    number_list = []
    for i in range(len(line)):
        if line[i].isnumeric():
            number_value += line[i]
            if not in_a_number:
                in_a_number = True
                start_i = i
        else:
            if in_a_number:
                end_i = i-1
                in_a_number = False
                is_special_number = check_adjacent_symbol(start_i, end_i, line_index)
                if is_special_number:
                    number_list.append(int(number_value))
                number_value = ''
                    
    if in_a_number:
        end_i = i-1
        is_special_number = check_adjacent_symbol(start_i, end_i, line_index)
        if is_special_number:
            number_list.append(int(number_value))
    print(number_list)                
    return number_list


def check_adjacent_symbol(start_i, end_i, line_i):

    start_check_i = start_i-1 if start_i > 0 else start_i
    end_check_i = end_i+1 if end_i < len(lines[line_i])-1 else end_i
    if is_symbol(lines[line_i][start_check_i]) or is_symbol(lines[line_i][end_check_i]):
        return True

    if line_i > 0 and line_i < len(lines)-1:
        for i in range(start_check_i, end_check_i+1):
            if is_symbol(lines[line_i-1][i]):
                return True
            if is_symbol(lines[line_i+1][i]):
                return True
    if line_i == 0:
        for i in range(start_check_i, end_check_i+1):
            if len(lines) > 1 and is_symbol(lines[line_i+1][i]):
                return True 

    if line_i == len(lines)-1 and len(lines) > 1:   
       for i in range(start_check_i, end_check_i+1):
            if is_symbol(lines[line_i-1][i]):
                return True              
    return False       


# lines = [
# "............394.........................*........650...637....695......*.....................................586....-...735..154.....423*344",
# "........458..%.....*...728..+..........488.435......................241........795.552.....9.&...............................#..............",
# "...........*....86.981....*..633.........../................762.700.....70*.........../....*.837......-.........20..................%......."]

# lines = ["........458..%.....*...728..+..........488.435......................241........795.552.....9.&...............................#.............."]

sum_numbers = 0
for i in range(len(lines)):
    sum_line = sum(check_number_in_line(i))
    print(sum_line)
    sum_numbers += sum_line
print(sum_numbers)



