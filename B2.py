from game_delay import delay
import A2
import overall
nothing = 0

def B2(command, subject, player_input):
    global success
    if command == 1 or command == 2 or command == 4:
        print
        delay("A wall blocks your way.")
        print
        success = False
    elif command == 3:
        history.append('visited')
        A2.A2_text(A2.history)
    elif command == 5:
        if subject.lower() in B2_inventory:
            overall.main_character.inventory[subject] = B2_inventory[subject]
            del B2_inventory[subject]
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
            B2_inventory[subject] = overall.main_character.inventory[subject]
            del overall.main_character.inventory[subject]
            delay('%s has been removed from inventory' %(subject))
        else:
            delay('%s not in inventory' %(subject))
        print
        success = False
    elif command == 7:
        if subject.lower() == 'chest' and overall.if_empty(B2_inventory) == False:
            print
            delay("The chest contains a: ")
            print
            for item in B2_inventory:
                print
                delay(item)
                print
            if overall.if_empty(B2_inventory) == True:
                print
                delay("This chest is empty")
                print
            print
            if 'searched' not in history:
                delay("TUTORIAL: To use an item, type 'use' and the name of the item you want to use.")
                print
                print
                delay("TUTORIAL: To view the description of an object in your inventory type 'analyze' and the name of the object.")
                print
                print
            history.append('searched')
        elif subject.lower() == 'chest' and overall.if_empty(B2_inventory) == True:
            print
            delay("This chest is empty")
            print
        else:
            print
            delay("Can not search %s" %(subject))
            print
        success = False
    elif command == 8:
        print
        if subject.lower() in overall.main_character.inventory:
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
        B2_reit(nothing)

def B2_reit(success):
    print
    while success == False:
        player_input = raw_input("What do you want to do?: ")
        overall.action(player_input)
        new_command = overall.command
        new_subject = overall.subject
        B2(new_command, new_subject, player_input)

history = []
B2_inventory = {}
iron_key = overall.Object("An old, rusted iron key.", "key", 0)
B2_inventory["iron key"] = iron_key
sword = overall.Object("An ordinary, slightly worn bastard sword.", "weapon", 3)
B2_inventory['sword'] = sword
dried_meat = overall.Object("A wrapped package of tender meats that it appears someone took great care in preparing, perhaps as a snack.", "food", 3)
B2_inventory['dried meat'] = dried_meat

def B2_text(history):
    print
    print
    print
    delay("You enter a dimly lit storage room with a CHEST in the back corner.")
    print
    print
    if 'visited' not in history:
        delay("TUTORIAL: To search a container or a body, type 'search' and the name of the thing you want to search. For example, if you wanted to search a cabinet, you would type 'search cabinet'.")
        print
        print
    delay("The only door in the room is the one on the EAST side through which you just entered.")
    print
    print
    player_input = raw_input("What do you want to do?: ")
    overall.action(player_input)
    new_command = overall.command
    B2(new_command, overall.subject, player_input)

