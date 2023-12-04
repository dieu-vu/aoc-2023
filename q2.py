
def convert_to_dict(line):
    game_title, game_sets = line.strip().split(':')
    game_id = game_title.split()[1]

    sets = game_sets.strip().split(';')

    for game in sets:
        result = game.strip().split(',')
        color_max = {'red': 12, 'green': 13, 'blue': 14}
        for r in result:
            count, color = r.strip().split()
            if int(count) > color_max.get(color):
                return 0
    return int(game_id)


file = open("input2.txt", "r")
lines = file.readlines()
print(lines)

sum_game_id = sum([convert_to_dict(line) for line in lines])
print(sum_game_id)

