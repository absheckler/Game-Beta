from game_delay import delay
from room_modules import A1
from room_modules import A2
import overall
import time
nothing = 0

delay("You wake.")
print
print
delay("You are at the end of a windowless, damp, dark, cobblestone hallway, lit by a series of torches.")
print
print
delay("You can't remember how you got here.")
print
print
delay("At the NORTH end of the hallway is a door.")
print
print
delay("TUTORIAL: To move in a certain direction type 'go' and the direction you want to go in. For example, if you wanted to move WEST, you would type in 'Go West'.")
print
print
player_input = raw_input("What do you want to do?:  ")


while overall.action(player_input) == False:
    player_input = raw_input("What do you want to do?: ")


overall.action(player_input)

if overall.command == 1:
    disembark = True
elif overall.command == 2 or overall.command == 3 or overall.command == 4:
    print
    delay("A wall blocks your way")
    print
    disembark = False
else:
    print
    print
    delay("You can not %s at this time" %(player_input))
    print
    disembark = False

while disembark != True:
    print
    player_input = raw_input("What do you want to do?: ")
    overall.action(player_input)
    if overall.command == 1:
        disembark = True
    elif overall.command == 2 or overall.command == 3 or overall.command == 4:
        print
        delay("A wall blocks your way")
        print
        print
        disembark = False
    else:
        disembark = False

A1.A1_text(A1.history)
