def get_number_from_line(line):
    res = [i for i in line if i.isdigit()]
    return int(f"{res[0]}{res[-1]}")

file = open("input1.txt", "r")
lines = file.readlines()

num_list = [get_number_from_line(line) for line in lines]
print(sum(num_list))




