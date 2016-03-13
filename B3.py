from game_delay import delay
import A3
import B4
import overall
import sys
nothing = 0

def B3(command, subject, player_input):
    global success
    if command == 1:
        history.append('visited')
        B4.B4_text(B4.history)
        success = True
    elif command == 2 or command == 4:
        print
        delay("A wall blocks your way.")
        print
        success = False
    elif command == 3:
        history.append('visited')
        A3.A3_text(A3.history)
    elif command == 5:
        if subject.lower() in B3_inventory:
            overall.main_character.inventory[subject] = B3_inventory[subject]
            del B3_inventory[subject]
            print
            delay("%s has been added to inventory" %(subject))
        elif subject.lower() in overall.final_enemy.inventory and overall.final_enemy.is_alive == False:
            overall.main_character.inventory[subject] = overall.final_enemy.inventory[subject]
            del overall.final_enemy.inventory[subject]
            print
            delay("%s added to inventory" %(subject))
        elif subject.lower() in overall.final_enemy.inventory and overall.final_enemy.is_alive == True and overall.final_enemy.is_asleep == True:
            print
            delay("The ENEMY is still, you can not take items from it.")
        elif subject.lower() in overall.main_character.inventory:
            print
            delay('%s already in inventory' %(subject))
        else:
            print
            delay("Can not pick up %s" %(subject))
        print
        sucess = False
    elif command == 6:
        print
        if subject.lower() in overall.main_character.inventory:
            B3_inventory[subject] = overall.main_character.inventory[subject]
            del overall.main_character.inventory[subject]
            delay('%s has been removed from inventory' %(subject))
        else:
            delay('%s not in inventory' %(subject))
        print
        success = False
    elif command == 7:
        if subject.lower() == 'enemy' and overall.if_empty(overall.final_enemy.inventory) == False and overall.final_enemy.is_alive == False:
            print
            delay("The body of the enemy contains a: ")
            print
            for item in overall.final_enemy.inventory:
                print
                delay(item)
                print
            print
        elif subject.lower() == 'enemy' and overall.if_empty(overall.final_enemy.inventory) == True and overall.final_enemy.is_alive == False:
            print
            delay("This body carries nothing on it.")
            print
        elif subject.lower() == 'enemy' and overall.final_enemy.is_alive == True and overall.final_enemy.is_asleep == True:
            print
            delay("This ENEMY is still alive. You can not search it.")
            print
        else:
            print
            delay("Cannot search %s" %(subject))
            print
            print
        success = False
    elif command == 8:
        print
        if subject.lower() in overall.main_character.inventory and overall.main_character.inventory[subject.lower()].form == 'weapon' and overall.final_enemy.is_asleep == True:
            print
            delay("As you attack the ENEMY stirs from its slumber.")
            print
            overall.final_enemy.is_asleep = False
            B3_combat(command, subject, 0)   
        elif subject.lower() in overall.main_character.inventory:
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
        B3_reit(nothing) 

def B3_reit(success):
    print
    while success == False:
        player_input = raw_input("What do you want to do?: ")
        overall.action(player_input)
        new_command = overall.command
        new_subject = overall.subject
        B3(new_command, new_subject, player_input)

history = []
B3_inventory = {}

def B3_text(history):
    print
    print
    print
    if 'visited' not in history:
        overall.final_enemy.is_alive = True
        overall.final_enemy.is_asleep = False
    else:
        pass
    delay("You enter a large stone cavern lit by a ring of torches.")
    print
    print
    delay("There are doors at the EAST and NORTH ends of the room.")
    print
    print
    if overall.final_enemy.is_alive == True:
        if overall.final_enemy.is_asleep == True:
            delay("A great large slumbering hound sleeps curled up in the middle of the room.")
            print
        elif overall.final_enemy.is_asleep == False:
            delay("A great large hound the size of a small house stands in the center of the room. It catches sight of you as you enter and snarls.")
            print
            print
            delay("The ENEMY moves to attack!")
            print
        else:
            pass
        if overall.if_empty(B3_inventory) == False:
            print
            delay("On the floor lies a: ")
            for item in B3_inventory:
                print
                delay(item)
                print
        print      
    else:
        delay("On the floor lies the body of a slain ENEMY")
        print
        if overall.if_empty(B3_inventory) == False:
            print
            delay("On the floor also lies a: ")
            for item in B3_inventory:
                print
                delay(item)
                print
        print
    player_input = raw_input("What do you want to do?: ")
    overall.action(player_input)
    new_command = overall.command
    if overall.final_enemy.is_alive == True and overall.final_enemy.is_asleep == False:
        B3_combat(new_command, overall.subject, player_input)
    else:
        B3(new_command, overall.subject, player_input)

def B3_combat_reit(success):
    print
    while overall.final_enemy.is_alive == True and overall.final_enemy.is_asleep == False:
        player_input = raw_input("What do you want to do?: ")
        overall.action(player_input)
        new_command = overall.command
        new_subject = overall.subject
        B3_combat(new_command, new_subject, player_input)

def B3_combat(command, subject, player_input):
    if command == 1 or command == 2 or command == 3 or command == 4:
        print
        delay("You try to flee, but the ENEMY hound catches you first")
        print
    elif command == 5:
        if subject.lower() in A3_inventory:
            print
            delay("You move to pick up the %s, but the ENEMY hound blocks your way.")
            print
        else:
            print
            delay("There is no %s to pick up.")
            print
    elif command == 6:
        print
        if subject.lower() in overall.main_character.inventory and subject.lower() == 'dried meat':
            delay("dried meat has been removed from inventory")
            print
            print
            delay("The hound stops and sniffs the air. It questioningly walks over to the dried meat and in one bite snaps it up and swallows. It looks at you and licks your face, then turns and walks away to lie down.")
            print
            print
            delay("The ENEMY is now asleep")
            print
            overall.final_enemy.is_asleep = True
            del overall.main_character.inventory[subject.lower()]
        elif subject.lower() in overall.main_character.inventory:
            B3_inventory[subject] = overall.main_character.inventory[subject]
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
            delay("You attack the ENEMY hound with your %s. You deal %s damage." %(subject.lower(), overall.main_character.inventory[subject.lower()].value)) 
            print
            overall.final_enemy.health -= overall.main_character.inventory[subject.lower()].value
            overall.final_enemy.enemy_death()
        elif subject.lower() in overall.main_character.inventory and overall.main_character.inventory[subject.lower()].form == 'instrument':
            overall.main_character.inventory[subject].use()
            print
            delay("The hound stops and tilts its head. It then lets out a humongous yawn, lays down, rests its head on its paws, and closes its eyes.")
            print
            print
            delay("The ENEMY is now asleep.")
            print
            print
            overall.final_enemy.is_asleep = True
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
    if overall.final_enemy.is_alive == True and overall.final_enemy.is_asleep == False:
        print
        delay("The ENEMY hound runs over and attacks, taking you in its mouth and violently shaking you, then throwing you to the opposite side of the room.")
        print
        overall.final_enemy.enemy_attack()
        B3_combat_reit(nothing)
    else:
        player_input = raw_input("What do you want to do?: ")
        overall.action(player_input)
        new_command = overall.command
        B3(new_command, overall.subject, player_input)

