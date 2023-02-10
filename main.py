# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

#part 1 EUFA Euro 1988 Final

scorer1 = 'Ruud Gullit'    #1
scorer2 = 'Marco van Basten'

# time mark of a goal 
goal_0 = 32       #2
goal_1 = 54

scorers = scorer1  + ' ' + str(goal_0) +',' + ' ' + scorer2 + ' ' + str(goal_1)

report = f'{scorer1} scored in the {goal_0}nd minute\n{scorer2} scored in the {goal_1}th minute'  

#part 2 #1
player = 'Ronald Koeman'
first_name = player[:player.find(' ')]
last_name_len = len(player[0:6])                    #koeman   
name_short = (player[0]) +'.'+ ' ' + (player[7:13]) #R. Koeman

chant = ('Ronald! '* 6).rstrip()
good_chant = bool(chant)
