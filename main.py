# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
Gullit = "Ruud Gullit"
vanBasten ="Marco van Basten"

goal_0 = 32
goal_1 = 54

scorers = f"{Gullit} {goal_0}, {vanBasten} {goal_1}"
report = f"{Gullit} scored in the {goal_0}nd minute\n{vanBasten} scored in the {goal_1}th minute"

print(scorers+"\n"+report)

player  = "Hans van Breukelen"
first_name = player[0:player.find(' ')] 
last_name_len = len(player[player.find(" ")+1:len(player)])

name_short =player[0]+". "+player[player.find(" ")+1:len(player)]

str= f"{first_name}! "*len(first_name) # copy times the length in the firstname
chant = str[0:len(str)-1]  # remove whitespace at the end of str
good_chant =chant[len(chant)-1]!=" "

print(name_short)
print(chant)