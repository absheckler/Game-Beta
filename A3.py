from game_delay import delay
import A2
import B3
import overall
import sys
nothing = 0

def A3(command, subject, player_input):
    global success
    if command == 1 or command == 3:
        print
        delay("A wall blocks your way.")
        print
        success = False
    elif command == 2:
        history.append('visited')
        B3.B3_text(B3.history)
        success = True
    elif command == 4:
        history.append('visited')
        A2.A2_text(A2.history)
    elif command == 5:
        if subject.lower() in A3_inventory:
            overall.main_character.inventory[subject] = A3_inventory[subject]
            del A3_inventory[subject]
            print
            delay("%s has been added to inventory" %(subject))
        elif subject.lower() in overall.enemy1.inventory:
            overall.main_character.inventory[subject] = overall.enemy1.inventory[subject]
            del overall.enemy1.inventory[subject]
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
            A3_inventory[subject] = overall.main_character.inventory[subject]
            del overall.main_character.inventory[subject]
            delay('%s has been removed from inventory' %(subject))
        else:
            delay('%s not in inventory' %(subject))
        print
        success = False
    elif command == 7:
        if subject.lower() == 'enemy' and overall.if_empty(overall.enemy1.inventory) == False:
            print
            delay("The body of the enemy contains a: ")
            print
            for item in overall.enemy1.inventory:
                print
                delay(item)
                print
            print
        elif subject.lower() == 'enemy' and overall.if_empty(overall.enemy1.inventory) == True:
            print
            delay("This body carries nothing on it")
            print
        else:
            print
            delay("Cannot search %s" %(subject))
            print
            print
        success = False
    elif command == 8:
        print
        if subject.lower() in overall.main_character.inventory:
            overall.main_character.inventory[subject.lower()].use()
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
        A3_reit(nothing)

def A3_reit(success):
    print
    while success == False:
        player_input = raw_input("What do you want to do?: ")
        overall.action(player_input)
        new_command = overall.command
        new_subject = overall.subject
        A3(new_command, new_subject, player_input)

history = []
A3_inventory = {}
longknife = overall.Object("A wicked, twisted longknife stained red from the flesh of many enemies.", "weapon", 2)
overall.enemy1.inventory["longknife"] = longknife
flute = overall.Object("A small flute carved from smooth wood. Its mouthpiece is worn from use, perhaps its owner was a musician... ", "instrument", 0)
overall.enemy1.inventory['flute'] = flute


def A3_text(history):
    print
    print
    print
    if 'visited' not in history:
        overall.enemy1.is_alive = True
    else:
        pass
    delay('You enter a large circular room with a soaring ceiling, supported by a ring of pillars and lit by flaming braziers. The floor is a a sand pit, littered with human bones and skulls.')
    print
    print
    delay("There are doors at the WEST and SOUTH sides of the room")
    print
    print
    if overall.enemy1.is_alive == True:
        delay("At the center of the room stands a masked ENEMY, armed with a viciously long knife")
        print
        if overall.if_empty(A3_inventory) == False:
            print
            delay("On the floor lies a: ")
            for item in A3_inventory:
                print
                delay(item)
                print
        print
        delay("The ENEMY moves to attack!")
        print
        print
    else:
        delay("On the floor lies the body of a slain ENEMY")
        print
        if overall.if_empty(A3_inventory) == False:
            print
            delay("On the floor also lies a: ")
            for item in A3_inventory:
                print
                delay(item)
                print
        print
    player_input = raw_input("What do you want to do?: ")
    overall.action(player_input)
    new_command = overall.command
    if overall.enemy1.is_alive == True:
        A3_combat(new_command, overall.subject, player_input)
    else:
        A3(new_command, overall.subject, player_input)



def A3_combat_reit(success):
    print
    while overall.enemy1.is_alive == True:
        player_input = raw_input("What do you want to do?: ")
        overall.action(player_input)
        new_command = overall.command
        new_subject = overall.subject
        A3_combat(new_command, new_subject, player_input)
        

def A3_combat(command, subject, player_input):
    if command == 1 or command == 2 or command == 3 or command == 4:
        print
        delay("You try to flee, but the ENEMY warrior catches you first")
        print
    elif command == 5:
        if subject.lower() in A3_inventory:
            print
            delay("You move to pick up the %s, but the ENEMY warrior blocks your way.")
            print
        else:
            print
            delay("There is no %s to pick up.")
            print
    elif command == 6:
        print
        if subject.lower() in overall.main_character.inventory:
            A3_inventory[subject] = overall.main_character.inventory[subject]
            del overall.main_character.inventory[subject]
            delay('%s has been removed from inventory' %(subject))
        else:
            delay('%s not in inventory' %(subject))
        print
    elif command == 7:
        print
        delay("Nothing here to search.")
        print
    elif command == 8:
        print
        if subject.lower() in overall.main_character.inventory and overall.main_character.inventory[subject.lower()].form == 'weapon':
            delay("You attack the ENEMY warrior with your %s. You deal %s damage." %(subject.lower(), overall.main_character.inventory[subject.lower()].value)) 
            print
            overall.enemy1.health -= overall.main_character.inventory[subject.lower()].value
            overall.enemy1.enemy_death()
        elif subject.lower() in overall.main_character.inventory:
            overall.main_character.inventory[subject].use()
            if overall.main_character.inventory[subject.lower()].form == 'food':
                del overall.main_character.inventory[subject.lower()]       
        else:
            delay('No %s in inventory' %(subject))
            print
    elif command == 9:
        for item in overall.main_character.inventory:
            print
            delay(item)
            print
        if overall.if_empty(overall.main_character.inventory) == True:
            print
            delay("You have nothing in your inventory!")
            print
    elif command == 10:
        print
        if subject.lower() in overall.main_character.inventory:
            overall.main_character.inventory[subject].describe()
        else:
            delay('%s not in inventory' %(subject))
        print
    elif command == 11:
        print
        overall.main_character.death()
    else:
        pass
    if overall.enemy1.is_alive == True:
        print
        delay("The ENEMY warrior attacks with a lacerating cut from its knife.")
        print
        overall.enemy1.enemy_attack()
        A3_combat_reit(nothing)
    else:
        player_input = raw_input("What do you want to do?: ")
        overall.action(player_input)
        new_command = overall.command
        A3(new_command, overall.subject, player_input)

