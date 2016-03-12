from game_delay import delay
import A1
import B2
import A3
import overall
import sys
nothing = 0

def A2(command, subject, player_input):
    global success
    if command == 1:
        if 'unlocked' in history:
            print
            history.append('visited')
            A3.A3_text(A3.history)
            success = True
        else:
            print
            delay('This door is locked')
            print
            success = False
    elif command == 2:
        history.append('visited')
        B2.B2_text(B2.history)
    elif command == 3:
        print
        delay("A wall blocks your way")
        print
        success = False
    elif command == 4:
        history.append("visited")
        A1.A1_text(A1.history)
    elif command == 5:
        if subject.lower() in A2_inventory:
            overall.main_character.inventory[subject] = A2_inventory[subject]
            del A2_inventory[subject]
            print
            delay('%s has been added to inventory' %(subject))
        elif subject.lower() in overall.main_character.inventory:
            print
            delay('%s already in inventory' %(subject))
        else:
            print
            delay("Can not pick up %s" %(subject))
        print
        success = False
    elif command == 6:
        print
        if subject.lower() in overall.main_character.inventory:
            A2_inventory[subject] = overall.main_character.inventory[subject]
            del overall.main_character.inventory[subject]
            delay('%s has been removed from inventory' %(subject))
        else:
            delay('%s not in inventory' %(subject))
        print
        success = False
    elif command == 7:
        print
        delay('Nothing here to search')
        print
        success = False
    elif command == 8:
        print
        if subject.lower() == 'iron key' and subject.lower() in overall.main_character.inventory:
            history.append('unlocked')
            delay("IRON KEY unlocks the NORTH door")
            print

        elif subject.lower() in overall.main_character.inventory:
            overall.main_character.inventory[subject].use()
            if overall.main_character.inventory[subject.lower()].form == 'food':
                del overall.main_character.inventory[subject.lower()]
        else:
            delay('No %s in inventory' %(subject))
            print
        success = False
    elif command == 9:
        for item in overall.main_character.inventory:
            print
            delay(item)
            print
        if overall.if_empty(overall.main_character.inventory) == True:
            print
            delay("You have nothing in your inventory!")
            print
        success = False
    elif command == 10:
        print
        if subject.lower() in overall.main_character.inventory:
            overall.main_character.inventory[subject].describe()
        else:
            delay('%s not in inventory' %(subject))
        print
        success = False
    elif command == 11:
        print
        overall.main_character.death()
        success = False
    else:
        success = False
    if success == False:
        A2_reit(nothing)
            

def A2_reit(success):
    print
    while success == False:
        player_input = raw_input("What do you want to do?: ")
        overall.action(player_input)
        new_command = overall.command
        new_subject = overall.subject
        A2(new_command, new_subject, player_input)


history = []
A2_inventory = {}

def A2_text(history):
    print
    print
    print
    if overall.if_empty(A2_inventory) == True:
        print
        delay("You enter an empty room")
        print
    elif overall.if_empty(A2_inventory) == False:
        print
        delay("You enter a room. On the floor lies a: ")
        print
        for item in A2_inventory:
            print
            delay(item)
        print
    if 'visited' in history:
        pass
    else:
        print
        delay("TUTORIAL: To check your health type 'health'. Don't let your health get too low!")
        print
        print
        delay("TUTORIAL: To view what you have in your inventory, type 'inventory'")
        print
    print
    delay("At the NORTH, SOUTH, and WEST sides of the room are doors.")
    print
    print
    player_input = raw_input("What do you want to do?: ")
    overall.action(player_input)
    new_command = overall.command
    A2(new_command, overall.subject, player_input)

