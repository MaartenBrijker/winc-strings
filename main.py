# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

player_0 = "Ruud Gullit"
player_1 = "Marco van Basten"

goal_0 = 32
goal_1 = 54

scorers = player_0 + ' ' + str(goal_0) + ', ' + player_1 + ' ' + str(goal_1)

report = f"{player_0} scored in the {goal_0}nd minute\n{player_1} scored in the {goal_1}th minute"

print(scorers)
print(report)

player = 'Berry van Aerle'
first_name = player[:player.find(' ')]
last_name_len = len(player[player.find(' ')+1:])
name_short = player[0] + '.' + player[player.find(' '):]

chant = (first_name + '! ') * (len(first_name)-1) + first_name + '!'
good_chant = chant[-1] != ' '

print(first_name)
print(last_name_len)
print(name_short)
print(chant)
print(good_chant)