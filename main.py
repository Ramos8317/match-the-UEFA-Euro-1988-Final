# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

#part 1
#Players who scored
Player1 = 'Gullit'
player2 = 'Van_Basten'

#time stamp of a goal
Goal_0 = 32
Goal_1 = 54

#use +-operator
scorers = 'Gullit + Goal_0' , 'Van_Basten + Goal_1'

#Use f-strings or the +-operator/who scored+ when 
Report = f'{Player1} scored in the {Goal_0}nd minute\n{player2} scored in the {Goal_1}th minute'
print(Report)

#part 2
#Random player in a variable
Player = 'Ronald_Koeman'
first_name = Player.find('Ronald')
last_name_len= Player[7:len(Player)]                #Koeman
name_short = (Player[0]) +'.'+ f'{last_name_len}'   #R. Koeman

print(name_short)


chant = 'Koeman(!)'*6
(chant!=3)
(chant!=2)

print(chant)
