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
player = 'Jan Wouters'
first_name = player[:player.find(' ')]
last_name = player[player.find(' '):]
last_name_len = len(last_name)-1
name_short = player[0] + '.' + last_name

first_name_len = len(first_name)
chant = ((first_name + '! ') * first_name_len)[:-1]         #ik wilde de .rstrip weer gebruiken maar ik kreeg dit keer een error, vroeg me af waarom, 
good_chant = chant[-1]  != ' '                              #en wat moet ik aan de code veranderen als ik het wil gebruiken.

