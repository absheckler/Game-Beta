from game_delay import delay
import A2
import overall
nothing = 0


def A1(command, subject, player_input):
    global success
    if command == 1:
        history.append("visited")
        A2.A2_text(A2.history)
        success = True
    elif command == 2 or command == 3:
        print
        delay("A wall blocks your way")
        print
        success = False
    elif command == 4:
        print
        delay("This door is closed and sealed.")
        print
        success = False
    elif command == 5:
        if subject.lower() in A1_inventory:
            overall.main_character.inventory[subject] = A1_inventory[subject]
            del A1_inventory[subject]
            print
            delay("%s has been added to inventory" %(subject))
        elif subject.lower() in overall.main_character.inventory:
            print
            delay('%s already in inventory' %(subject))
        else:
            print
            delay("Can not pick up %s"%(subject))
        print
        success = False
    elif command == 6:
        print
        if subject.lower() in overall.main_character.inventory:
            A1_inventory[subject] = overall.main_character.inventory[subject]
            del overall.main_character.inventory[subject]
            delay('%s has been removed from inventory'%(subject))
        else:
            delay('%s not in inventory'%(subject))
        print
        success = False
    elif command == 7:
        print
        delay("Nothing here to search")
        print
        success = False
    elif command == 8:
        print
        if subject.lower() in overall.main_character.inventory:
            overall.main_character.inventory[subject].use()
            if overall.main_character.inventory[subject.lower()].form == 'food':
                del overall.main_character.inventory[subject.lower()]
        else:
            delay("No %s in inventory" %(subject))
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
            delay("%s not in inventory" %(subject))
        print
        success = False
    elif command == 11:
        print
        overall.main_character.death()
        success = False
    else:
        success = False
    if success == False:
        A1_reit(nothing)


def A1_reit(success):
    print
    while success == False:
        player_input = raw_input("What do you want to do?: ")
        overall.action(player_input)
        new_command = overall.command
        new_subject = overall.subject
        A1(new_command, new_subject, player_input)      

history = []
A1_inventory = {}
note = overall.Object("Ah, so you have been chosen. I do not envy you, the fact that you are here means many before you have tried and failed. Ah well, I guess you have no choice but to continue. Godspeed.", "passive", 0)
A1_inventory['note'] = note

def A1_text(history):
    print
    print
    print
    global player_input
    delay("You enter a room lit by a single torch.")
    print
    if 'visited' not in history:
        print
        delay("The door behind you closes and seals.")
        print
    else:
        pass
    if 'note' not in A1_inventory:
        if overall.if_empty(A1_inventory) == True:
            print
            delay("The room is empty except for a barren alter standing at its center.")
            print
        elif overall.if_empty(A1_inventory) == False:
            print
            delay("The room is empty except for an alter standing at its center. Upon the alter sits a: ")
            print
            for item in A1_inventory:
                print
                delay(item)
            print           
    if 'note' in A1_inventory:
        print
        delay("The room is empty except for an alter standing at its center. Upon the alter is a NOTE.")
        print
        print
        if overall.if_empty(A1_inventory) == False and overall.count > 1:
            delay("On the alter there also sits a: ")
            for item in A1_inventory:
                print
                delay(item)
            print
            print
        delay("The NOTE reads: ")
        print
        note.describe()
    else:
        pass
    if 'visited' in history:
        pass
    else:
        print
        delay("TUTORIAL: To pick up an item, type 'pick up' and the name of the item you want to pick up. For example, if you wanted to pick up an apple, you would type 'Pick up apple'")
        print
        print
        delay("TUTORIAL: If you want to get rid of an item, type 'drop' and the name of the item you want to get rid of. Remember, if you drop an item you can always come back and pick it up!")
        print
    print
    delay("There is a door on the NORTH side of the room")
    print
    print
    if 'visited' in history:
        delay("There is a closed and sealed door at the SOUTH side of the room")
        print
        print
    player_input = raw_input("What do you want to do?: ")
    overall.action(player_input)
    new_command = overall.command
    A1(new_command, overall.subject, player_input)

