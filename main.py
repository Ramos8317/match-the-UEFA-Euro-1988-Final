# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

#part 1 EUFA Euro 1988 Final

scorer1 = 'Ruud Gullit'    #1
scorer2 = 'Marco Van Basten'

# time mark of a goal 
goal_0 = 32       #2
goal_1 = 54

scorers = 'Ruud Gullit'+' 32, Marco van Basten '+'54'

Report = f'{scorer1} scored in the {goal_0}nd minute\n{scorer2} scored in the {goal_1}th minute'  #4

#part 2 #1
player = 'Ronald_Koeman'
first_name = player.find('ronald')  
last_name_len = player[7:len(player)]               #koeman   
name_short = (player[0]) +'.'+ f'{last_name_len}'   #R. Koeman

chant = 'Koeman! '*6
good_chant = (chant!=6)
