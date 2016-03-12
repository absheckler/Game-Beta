import sys
from game_delay import delay

class Character(object):
    def __init__(self, health, inventory, is_alive):
        self.health = health
        self.inventory = inventory
        self.is_alive = is_alive
    def view_inventory(self):
        for thing in self.inventory:
            delay(thing)
    def death(self):
        if self.health < 1:
            self.is_alive = False
            print
            delay("You Died: Game Over")
            sys.exit()            
        else:
            delay("Your health is now %s" %(self.health))
            print


main_character = Character(5, {}, True)

class Enemy(object):
    is_asleep = False
    def __init__(self, health, inventory, attack, is_alive, is_asleep):
        self.health = health
        self.inventory = inventory
        self.attack = attack
        self.is_alive = is_alive
    def enemy_attack(self):
        print
        delay("The ENEMY deals %s damage to you" %(self.attack))
        print
        print
        main_character.health -= self.attack
        main_character.death()
    def enemy_death(self):
        if self.health < 1:
            self.is_alive = False
            print
            delay("The ENEMY falls to the ground, dead.")
            print
            print
        else:
            print
            delay("The ENEMY's health is now %s" %(self.health))
            print
        
enemy1 = Enemy(5, {}, 2, False, True)
final_enemy = Enemy(15, {}, 10, False, True)
master = Character(1, {}, True)

def action(player_input):
    global command
    global subject
    command = 0
    if player_input.lower() == "go north":
        command = 1
        subject = 0
        return True
    elif player_input.lower() == "go west":
        command = 2
        subject = 0
        return True
    elif player_input.lower() == "go east":
        command = 3
        subject = 0
        return True
    elif player_input.lower() == "go south":
        command = 4
        subject = 0
        return True
    elif player_input.lower()[0:7] == "pick up":
        command = 5
        subject = player_input[8:]
        return True
    elif player_input.lower()[0:4] == "drop":
        command = 6
        subject = player_input.lower()[5:]
        return True
    elif player_input.lower()[0:6] == "search":
        command = 7
        subject = player_input.lower()[7:]
        return True
    elif player_input.lower()[0:3] == "use":
        command = 8
        subject = player_input.lower()[4:]
        return True
    elif player_input.lower()[0:9] == "inventory":
        command = 9
        subject = 0
    elif player_input.lower()[0:7] == "analyze":
        command = 10
        subject = player_input.lower()[8:]
    elif player_input.lower()[0:6] == "health":
        command = 11
        subject = 0
    else:
        print
        delay("You can not %s at this time." %(player_input))
        print
        return False
    return command
    return subject

class Object(object):
    def __init__(self, description, form, value):
        self.description = description
        self.form = form
        self.value = value
    def describe(self):
        print
        delay(self.description)
        print
    def use(self):
        if self.form == 'food':
            main_character.health += self.value
            delay("This food added + %s to your health." %(self.value))
            print
            print
            main_character.death()
        elif self.form == 'weapon':
            if enemy1.is_alive == False and final_enemy.is_alive == False or final_enemy.is_asleep == True:
                suicide_choice = raw_input("There are no enemies here. Do you want to kill yourself? Yes/No: ")
                if suicide_choice.lower() == 'yes':
                    delay('You Died: Game Over')
                    sys.exit()
                elif suicide_choice.lower() == 'no':
                    choice = True
                else:
                    print
                    delay("Type yes or no")
                    print
                    print
                    choice = False
                while choice != True:
                    suicide_choice = raw_input("Do you want to kill yourself? Yes/No: ")
                    if suicide_choice.lower == 'yes':
                        print
                        delay('You Died: Game Over')
                        choice = True
                    elif suicide_choice.lower() == 'no':
                        choice = True
                    else:
                        print
                        delay("Type yes or no")
                        print
                        print
                        choice = False
        elif self.form == 'passive':
            delay("You can not use this item")
            print
        elif self.form == 'key':
            delay("This key can not be used here")
            print
        elif self.form == 'instrument':
            delay("You play the instrument and it lets out a soft, soulful melody.")
            print


def if_empty(dictionary):
    global count
    count = 0
    for item in dictionary:
        count += 1
    if count == 0:
        return True
    else:
        return False
        return count


