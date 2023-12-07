#Part 2 Day 3 2023
file = open("input3.txt", "r")
lines = file.readlines()

def get_star_loc(lines):
    star_loc = []
    for row_index in range(len(lines)):
        star_index = [i for i, letter in enumerate(lines[row_index]) if letter == "*"]
        for i in star_index:
            star_loc.append((row_index, i))
    return star_loc

# Get complete numbers adjacent with a position on a row, in both directions
def get_number_by_loc(row, col, lines):
    n_cols = len(lines[row])
    start_col = col
    while start_col >= 0 and lines[row][start_col].isnumeric():
        start_col -=1
    start_col +=1
    end_col = col
    while end_col < n_cols and lines[row][end_col].isnumeric():
        end_col +=1
    end_col -=1
    return (int(lines[row][start_col:end_col+1]), start_col, end_col, row)
            

def get_gear_ratio_of_star(star_row, star_col, lines):
    adjacent_number_pairs = []
    line = lines[star_row].strip()
    n_cols = len(line)
    n_rows = len(lines)

    for row_incre in range(-1,2):
        for col_incre in range(-1,2):
            row_index = star_row + row_incre
            col_index = star_col + col_incre
            if (row_incre !=0 or col_incre !=0) and col_index >= 0 and col_index < n_cols and row_index >= 0 and row_index < n_rows and lines[row_index][col_index].isnumeric():
                number = get_number_by_loc(row_index, col_index, lines) 
                if number not in adjacent_number_pairs:
                    adjacent_number_pairs.append(number) 
                               
    if len(adjacent_number_pairs) == 2:
        return adjacent_number_pairs[0][0] * adjacent_number_pairs[1][0]
    else:
        return 0
        
def get_total_gear_ratios(lines):
    total_gear_ratios = 0
    star_indexes = get_star_loc(lines)
    for star_i in star_indexes:
        total_gear_ratios += get_gear_ratio_of_star(star_i[0], star_i[1], lines)
    return total_gear_ratios


print(get_total_gear_ratios(lines))
#84907174
file.close()


