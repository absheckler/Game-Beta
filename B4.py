from game_delay import delay
import B3
import overall
import sys
import time
nothing = 0

def B4(command, subject, player_input):
    global success
    if command == 1:
        if 'unlocked' in history:
            print
            history.append('visited')
            delay("You open the white door, and the first thing you notice is the brilliant, blinding golden light... ")
            print
            print
            delay("To be continued...")
            print
            print
            delay("Victory! Game Over")
            print
            print
            sys.exit()
            success = True
        elif 'unlocked' not in history and overall.master.is_alive == False:
            print
            delay("This door is locked")
            print
            success = False
        elif 'unlocked' not in history and overall.master.is_alive == True:
            print
            delay('You walk over to the white door and try to open it.')
            print
            print
            time.sleep(1.5)
            delay('The white door is locked')
            print
            print
            time.sleep(1.5)
            delay('By the time you realize your mistake it is too late')
            print
            print
            time.sleep(1.5)
            delay('The old man leaps from behind his desk, knife in hand and stabs you in the back.')
            print
            print
            time.sleep(1.5)
            delay('As you fall to the floor and bleed out, he stands over you with a wicked grin on his face and says "Did you really think you could leave this place alive? Ha. You are not but one of many who will meet their end in this place."')
            print
            print
            time.sleep(1.5)
            delay('You Died: Game Over')
            sys.exit()
            success = False
    elif command == 2 or command == 3:
        print
        delay("A wall blocks your way")
        print
        success = False
    elif command == 4:
        history.append('visited')
        B3.B3_text(B3.history)
    elif command == 5:
        if subject.lower() in B4_inventory:
            if overall.master.is_alive == True:
                print
                delay('As you try to pick up the %s the old man says "Ahem, what do you think you are doing? That is mine you can not take it."' %(subject))
                print
            else:
                overall.main_character.inventory[subject] = B4_inventory[subject]
                del B4_inventory[subject]
                print
                delay('%s has been added to inventory' %(subject))
                print
        elif subject.lower() in overall.main_character.inventory:
            print
            delay('%s already in inventory' %(subejct))
            print
        else:
            print
            delay("Can not pick up %s" %(subject))
            print
        success = False
    elif command == 6:
        print
        if subject.lower() in overall.main_character.inventory:
            B4_inventory[subject] = overall.main_character.inventory[subject]
            del overall.main_character.inventory[subject]
            delay('%s has been removed from inventory' %(subject))
        else:
            delay('%s not in inventory' %(subject))
        print
        success = False
    elif command == 7:
        if overall.master.is_alive == False:    
            if subject.lower() == 'desk' and overall.if_empty(B4_inventory) == False:
                print
                delay('This desk contains a: ')
                print
                for item in B4_inventory:
                    print
                    delay(item)
                    print
            elif subject.lower() == 'desk' and overall.if_empty(B4_inventory) == True:
                print
                delay('This desk is empty.')
                print
            else:
                print
                delay('Can not search %s' %(subject))
                print
        else:
            print
            delay('You try to lean in to search the desk, but the man stops you and says "Ahem, just what do you think you are doing? Stop that."')
            print
        success = False
    elif command == 8:
        print
        if subject.lower() == 'white key' and subject.lower() in overall.main_character.inventory:
            history.append('unlocked')
            delay('WHITE KEY unlocks NORTH door')
            print
        elif subject.lower() in overall.main_character.inventory and overall.main_character.inventory[subject.lower()].form == 'weapon' and overall.master.is_alive == True:
            delay("You raise your %s and the old man's eyes widen in fear. He yells 'WAIT, NO, HOW DID YOU KNOW?' just before your %s comes down and chops off his head. The knife concealed in his hand under the desk clatters to the ground." %(subject, subject))
            print
            overall.master.is_alive = False
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
        B4_reit(nothing)

def B4_reit(success):
    print
    while success == False:
        player_input = raw_input("What do you want to do?: ")
        overall.action(player_input)
        new_command = overall.command
        new_subject = overall.subject
        B4(new_command, new_subject, player_input)

history = []
B4_inventory = {}
white_key = overall.Object("A key made of a polished white material that looks strangely familiar...", 'key', 0) 
B4_inventory['white key'] = white_key

def B4_text(history):
    print
    print
    print
    delay("You enter a small study, littered with documents and bookshelves lining the walls.")
    print
    print
    delay("To the NORTH is a door made of some strange white, polished material.")
    print
    print
    if overall.master.is_alive == True:
        delay("At the center of the room is a DESK, behind which sits an old scholarly man reading a book. As you enter the man looks up.")
        print
        print
        if 'visited' in history:
            delay("The man exclaims, 'You again? I told you you could leave, go on, it's just through that door.'")
            print
        else:
            delay("The man says 'Wha- who are you?! How did you get here? Ah well, I guess it doesn't matter, go on leave, just through that door'. He points to the white door to the NORTH")
            print
    else:
        delay("At the center of the room is a DESK, behind which sits the decapitated corpse of an old man.")
        print
    print
    player_input = raw_input("What do you want to do?: ")
    overall.action(player_input)
    new_command = overall.command
    B4(new_command, overall.subject, player_input)


