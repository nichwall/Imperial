import random
import math

print 'START GAME'
name = raw_input('Character name: ')
print "Hello, {}. Welcome to the Empire.".format(name)
char = {'name':name, 'credit': 1000, 'health':130, 'damage': 25, 'medpacs': 25, 'melee' : '', 'ranged':'', 'm_off':'',
        'ranged_off': '', 'lightside': 20, 'neutral':20, 'darkside':20}
##########################################################################################################################################################
def FactionAndClass():
    char['faction'] = 'Empire'
    print "(1) Sith Marauder: medium DPS, medium health"
    print "(2) Sith Assassin: high DPS, low health"
    print "(3) Sith Juggernaut: low DPS, high health"
    classtype = int(raw_input("Input your chosen class type: "))
    if classtype == 1:
        classname = 'Marauder'
        char['health'] = char['health'] + 70
        char['damage'] = char['damage'] + 60
        char['maxhealth'] = 170
    if classtype == 2:
        classname = 'Assassin'
        credit = char['credit'] + 500
        char['damage'] = char['damage'] + 75
        char['health'] = char['health'] + 20
        char['maxhealth'] = 120
    if classtype == 3:
        classname = 'Juggernaut'
        char['damage'] = char['damage'] + 45
        char['maxhealth'] = 265
        char['health'] = char['health'] + 165
    char['classname'] = classname
    char['classtype'] = classtype
    return char

def PrintHoloEntry(order):
    for entry in order:
        if entry == '1':
            print """DARTH ADEGA was a notorious Sith Sorceror during the Great Hyperspace War. He used both the Light and the Dark Side
to acheive his ends, and was known as the Lord of Balance. He was presumed missing in the Battle for Raxus, and was presumed dead
sometime later."""
        elif entry == '2':
            print """MARKA RAGNOS..............."""
        elif entry == '3':
            print """THE CODE OF THE SITH is the code that all Sith live by:
Peace is a lie; there is only passion.
From passion, I gain strength.
From strength, I gain power.
From power, I gain victory.
Through victory, my chains are broken.
The Force shall free me."""
        elif entry == '4':
            print """THE SITH EMPIRE (PRE-HYPERSPACE WAR) was started by rogue Jedi who came to Korriban after their defeat and exile from Tython. Ajunta Pall
lead these Jedi, and they would eventually become the first Sith Lords."""
        elif entry == '5':
            print """THE SITH EMPIRE (POST-HYPERSPACE WAR) beaten by the REpublic"""
        elif entry == '6':
            print """THE GALACTIC REPUBLIC...."""
        elif entry == '7':
            print """THE SITH ORDER....."""
        elif entry == '8':
            print """LOLA SAYU......"""
        elif entry == '9':
            print """DARTH IMPERIUS was a former slave, risen to power through careful execution of her enemies. She is
more given to mercy than the rest of her Sith brethren, but she has used such tendencies to create an army of loyal followers.
Head of the Sphere of Ancient Mysteries, she commands the search for ancient Sith relics, keeping the powerful ones to increase
her own strength.

The Lethan Twi'lek has specialized in the path of a Sorceror, utilizing the Force to create massive lightning storms. She's capable of using Force Lightning to
annihilate small groups of enemies, or poisioning them through Dark means. A pragmatic woman, she has been hailed as the Lord of the People, a title she
uses to great affect. While the old guard hates her, the up and coming nobility in the Empire has been quick to ally with whom they see as the next Head of the
Council."""
        elif entry == '10':
            print """DARTH ANCINA is Head of the Sphere of Technology. She is Imperius's rival for control over the Council, and adheres strictly to the
old ways of the Sith. As a staunch traditionalist, her rise to power threatens Imperius who, as an alien, is vulnerable to attacks on her heritage."""
        elif entry == '11':
            print """THE GREAT HYPERSPACE WAR....."""
        elif entry == '12':
            print """NAGA SADOW......"""
        elif entry == '13':
            print """LUDO KRESSH....."""
        elif entry == '14':
            print """ZIOST....."""
        elif entry == '15':
            print """RAXUS PRIME....."""

def HealChoice(char):
    healchoice = raw_input("Enter 1 to heal: ")
    if healchoice == '1':
        if char['medpacs'] > 0:
            char['health'] = char['health'] + 30
            if char['health'] > char['maxhealth']:
                char['health'] = char['maxhealth']
            char['medpacs'] = char['medpacs'] - 1
            print "Your health is up to {}.".format(char['health'])
            print "You have {} medpacs.".format(char['medpacs'])
        else:
            print "You have no more medpacs!"
    print "You chose not to heal."

def AnimalAttack(char):
    print "A wild animal! It attacks!"
    animalattack = 10
    animalhealth = math.floor(70 * random.random())
    while animalhealth > 0:
        hit = random.random() * 4
        if hit > 3:
            print "It claws you for", animalattack, "damage!"
            char['health'] = char['health'] - animalattack
            print "Your health is now {}.".format(char['health'])
        else:
            print "It missed you."
        att = random.random() * 10
        if att > 4:
            print "You got it for {} damage!".format(char['damage'])
            animalhealth = animalhealth - char['damage']
            print "The animal now has {} health.".format(animalhealth)
            if animalhealth < 0:
                animalhealth = 0
                print "It's dead."
        else:
            print "You missed it."
        if char['health'] < 0:
            char['health'] = 0
            print "Sorry, but you died."
            print "GAME OVER"
            quit()
    print "You win!"
    print "Here's a reward: 100 credits."
    char['credit'] = char['credit'] + 100
    print "You have {} credits.".format(char['credit'])

def TarentatekAttack(char):
    thealth = 250
    print "The tarentatek attacks!"
    while thealth > 0:
        print "You attack first!"
        print "Try for a headshot or just attack?"
        print "You might miss of you go for a headshot, but there's higher damage."
        atype = raw_input("1 for headshot, 2 for attack: ")
        if atype == '1':
            acc = 100 * random.random()
            if acc > 50:
                headshot = char['damage'] + math.floor(random.random() * 70)
                thealth = thealth - (headshot)
                print "You hit for {} damage!".format(headshot)
                print "The tarentatek now has {} health.".format(thealth)
            else:
                print 'You missed.'
        if atype == '2':
            thealth  = thealth - char['damage']
            print "The tarentatek takes {} damage and now has {} health.".format(char['damage'], thealth)
        if thealth < 0:
                thealth = 0
                print "It's dead."
                HealChoice(char)
        else:
            tattack = math.floor(random.random() * 55)
            char['health'] = char['health'] - tattack
            if char['health'] < 0:
                char['health'] = 0
                print "Sorry, but you died."
                print "GAME OVER"
                exit()
            print "The tarentatek attacks you for {} damage, leaving you with {} health.".format(tattack, char['health'])
        HealChoice(char)

def TukataAttack(char):
    thealth = 150
    print "The tuk'ata attacks!"
    while char['health'] > 0 or thealth > 0:
        print "You attack first!"
        print "Try for a headshot or just attack?"
        print "You might miss of you go for a headshot, but there's higher damage."
        atype = raw_input("1 for headshot, 2 for attack: ")
        if atype == '1':
            acc = 100 * random.random()
            if acc > 50:
                headshot = char['damage'] + math.floor(random.random() * 70)
                thealth = thealth - (headshot)
                print "You hit for {} damage!".format(headshot)
                print "The tuk'ata now has {} health.".format(thealth)
            else:
                print 'You missed.'
        if atype == '2':
            thealth  = thealth - char['damage']
            print "The tuk'ata takes {} damage and now has {} health.".format(char['damage'], thealth)
        if thealth < 0:
                thealth = 0
                print "It's dead."
                HealChoice(char)
        else:
            tattack = math.floor(random.random() * 75)
            char['health'] = char['health'] - tattack
            if char['health'] < 0:
                char['health'] = 0
                print "Sorry, but you died."
                print "GAME OVER"
                exit()
            print "The tuk'ata attacks you for {} damage, leaving you with {} health.".format(tattack, char['health'])
        HealChoice(char)

def MercBandAttack(char, amount, affiliation):
    for merc in range(amount):
        thealth = math.floor(random.random * 100)
        while thealth > 0:
            print "You attack first!"
            print "Try for a headshot or just attack?"
            print "You might miss of you go for a headshot, but there's higher damage."
            atype = raw_input("1 for headshot, 2 for attack: ")
            if atype == '1':
                acc = 100 * random.random()
                if acc > 50:
                    headshot = char['damage'] + math.floor(random.random() * 70)
                    thealth = thealth - (headshot)
                    print "You hit for {} damage!".format(headshot)
                    print "The {} now has {} health.".format(affiliation,thealth)
                else:
                    print 'You missed.'
            if atype == '2':
                thealth  = thealth - char['damage']
                print "The {} takes {} damage and now has {} health.".format(affiliation, char['damage'], thealth)
            if thealth < 0:
                thealth = 0
                print "It's dead."
                HealChoice(char)
            else:
                tattack = random.random() * 75
                char['health'] = char['health'] - tattack
                if char['health'] < 0:
                    char['health'] = 0
                    print "Sorry, but you died."
                    print "GAME OVER"
                    exit()
                print "The {} attacks you for {} damage, leaving you with {} health.".format(affiliation,tattack, char['health'])
            HealChoice(char)
            
def SithFight(char, enemyname, amountenemies, enemyhealth):
    for enemy in range(amountenemies):
        ehealth = math.floor(enemyhealth * random.random())
        while ehealth > 0:
            print 'You attack first!'
            if char['lightside'] >= 40 or char['darkside'] >= 40 or char['neutral'] >= 70:
                if char['darkside'] >= 40 or char['neutral'] >= 70:
                    print "1A: You can attack for 170 damage with lightning!"
                if char['lightside'] >= 40 or char['neutral'] >= 70:
                    print "1B: You may attack with a telekinetic throw for 170 damage."
                if char['darkside'] >= 100 or char['neutral'] >= 150:
                    print "2A: You may use a Force Repulse, for 300 damage!"
                if char['lightside'] >= 100 or char['neutral'] >= 150:
                    print "2B: You can attack for 300 damage with a Force Wave."
                if char['darkside'] >= 250 or char['neutral'] >= 325:
                    print "3A: You can use a Death Field to do 400 damage!"
                if char['lightside'] >= 250 or char['neutral'] >= 325:
                    print "3B You may unleash a Stasis Field for 400 damage!"
                if char['darkside'] >= 500 or char['neutral'] >= 700:
                    print "4A: You can Drain Force for 750 damage!"
                if char ['lightside'] >= 500 or char['neutral'] >= 700:
                    print "4B: You may Mind Warp the enemy for 750 damage."
                if char['darkside'] >= 750 or char['neutral'] >= 970:
                    print "5A: You may devastate the enemy with a Force Storm for 1200 damage."
                if char['lightside'] >= 750 or char['neutral'] >= 970:
                    print "5B: You could unleash the power of the Force to do 1200 damage with a Force Quake."
                chosen = raw_input("Enter the number of your chosen Force attack: ")
                while chosen == '':
                    raw_input("Enter the number of your chosen Force attack: ")
                if chosen[0] == '1':
                    damage = 170
                elif chosen[0] == '2':
                    damage = 300
                elif chosen[0] == '3':
                    damage = 400
                elif chosen[0] == '4':
                    damage = 750
                elif chosen[0] == '5':
                    damage = 1200
                ehealth = ehealth - damage
                if ehealth < 0:
                    ehealth = 0
                print "You hit {} for {}, leaving it with {} health.".format(enemyname, damage, ehealth)
            else:
                print "You use a normal attack for {} damage".format(char['damage'])
                ehealth = ehealth - char['damage']
                if ehealth < 0:
                    ehealth = 0
                    print "It's dead."
                else:    
                    print "{} now has {} health.".format(enemyname, ehealth)
                    print "{} attacks!".format(enemyname)
                    eattack = 50 + math.floor(50 * random.random())
                    char['health'] = char['health'] - eattack
                    if char['health'] < 0:
                        char['health'] = 0
                        print "Sorry, but you died."
                        print "GAME OVER"
                        exit()
                    print "{} attacks you for {} damage, leaving you with {} health.".format(enemyname, eattack,char['health'])
            HealChoice(char)

def LDNpoints(char, LS, DS, NS):
    char['lightside'] = char['lightside'] + LS
    char['darkside'] = char['darkside'] + DS
    char['neutral'] = char['neutral'] + NS
    print "You now have {} Light Side points, {} Dark Side points, and {} Neutral Force points.".format(char['lightside'], char['darkside'], char['neutral'])

def Credits(char, amount):
    char['credit'] = char['credit'] + amount
    print "You gain {} credits, and now have {} credits.".format(amount, char['credit'])

#############################################################################################################################################################
def KorribanTomb(char):
    print """You enter the tomb cautiously. As you do, something stirs in your gut. Hmm.
This place is filled with darkness. Do you embrace it?"""
    print "Choose your side(You can change later):"
    print "1: Light Side"
    print "2: Neutral Side"
    print "3: Dark Side"
    choice = int(raw_input("You choose: "))
    if choice == 1:
        LDNpoints(char, 40, 0, 15)
    if choice == 2:
        LDNpoints(char, 0, 0, 55)
    if choice == 3:
        LDNpoints(char, 0, 40, 15)
    print """You continue on through the tomb. A shyrack perches on top of a statue.
You come to a fork in the road. 3 tunnels gape in front of you."""
    print "Take your pick:"
    print "1: The left tunnel"
    print "2: The middle tunnel"
    print "3: The right tunnel"
    pick = int(raw_input("You go down tunnel: "))
    if pick == 1:
        print "You head down the left tunnel."
        print "Three shyracks attack you!"
        AnimalAttack(char)
        HealChoice(char)
        AnimalAttack(char)
        HealChoice(char)
        AnimalAttack(char)
        HealChoice(char)
        print "Ugh. If you never see another Shyrack it'll be too soon."
        print "..."
        print "Darn."
        print "Another shyrack flies out."
        AnimalAttack(char)
        print
        HealChoice(char)
        print """They seem to get fiercer as you battle your way down the twisting tunnel, lit by residual Force Energy.
They might be protecting something. Or course, the Dark Side in the tomb could have made them stronger and fiercer.
You wonder if it could do the same for you. The tomb's power is... alluring."""
        print "Stop to soak up the dark side?"
        yaynay = int(raw_input("1 for Yes, 2 for No: "))
        if yaynay == 2:
            LDNpoints(char, 0, 30, 10)
        else:
            LDNpoints(char, 30, 0, 10)
        print "..."
        print "You continue down the tomb."
        print "There. A moldering crypt lies before you."
        print "Loot the crypt?"
        loot = int(raw_input("1 for looting, 2 for leaving, and 3 to continue looking around: "))
        if loot == 1:
            print "Naughty, naughty."
            LDNpoints(char, 0, 20, 10)
            print "You now have {} Light Side points, {} Dark Side points, and {} Neutral Force points.".format(char['lightside'], char['darkside'], char['neutral'])
            print "Well, you find an old lightsaber."
            print "You turn it on, and the red blade gleams anrily against the darkness of the tomb."
            char['damage'] = char['damage'] + 50
            print "You turn to leave, and a gate you hadn't noticed before opens."
            print "An animalistic screech echos out."
            print "..."
            print "A terentatek."
            run = int(raw_input("1 to RUN, 2 to FIGHT: "))
            if run == 2:
                TarentatekAttack(char)
                print "You won..."
                print "You pry a blade from the harness on the beast."
                print "The shoto is a good match for the blade you got from the tomb."
                char['damage'] = char['damage'] + 20
        elif loot == 2:
            LDNpoints(char, 20, 0, 10)
            print "A ghost, shimmering red with Dark Side energy appears, blocking your exit."
            print '"You did not disturb my tomb," it muses.'
            print '"I am Lord Dartian. Answer my questions and I shall end you, or reward you."'
            countright = 0
            countwrong = 0
            print '"What is the reward of power?"'
            ans1 = int(raw_input("1: Victory; 2: Power is its own reward; 3: Respect; 4: Influence "))
            if ans1 == 1:
                countright = 1
            else:
                countwrong = 1
            print '''"What is the Jedi's greatest weakness?"'''
            ans2 = int(raw_input("1: Compassion; 2: The Republic; 3: Detachment; 4: The Light "))
            if ans2 == 3:
                countright = countright + 1
            else:
                countwrong = countwrong + 1
            print '"What is Death?"'
            ans3 = int(raw_input("1: Failure; 2: Yourself; 3: The cessation of a heartbeat; 4: Weakness "))
            if ans3 == 1:
                countright = countright + 1
            else:
                countwrong = countwrong + 1
            if countwrong > countright:
                print "The ghost turns and gestures at a gate hidden in shadows, and then moves to block your way out"
                print "He laughs, eager to see you die fighting his... Tarentatek."
                print "Your day just keeps getting better and better."
                TarentatekAttack(char)
                print "You won..."
                print "You pry a blade from the harness on the beast."
                print "A red shoto-- an offhand weapon used in tandem with another blade."
                char['melee_off'] = "Old Sith Shoto"
                char['damage'] = char['damage'] + 20
            if countright > countwrong or countright == countwrong:
                print "Lord Dartian looks genuinely surprised."
                print '"Here: A saberstaff. I have no need of it."'
                char['damage'] = char['damage'] + 65
                repent = int(raw_input("Do you want to try and redeem the ghost? 1: YES 2: NO "))
                if repent == 1:
                    if char['lightside'] > 39:
                        print "Dartian nods. He agrees with you."
                        print "He turns blue, and a smile, a gentle one, crosses his face."
                        print "You have redeemed a Sith Lord!"
                        LDNpoints(char, 40, 0, 0)
                    else:
                        print 'He smiles sadly. "My place is here. This... is my punishment."'
                        print '"I wish you luck. I forsee a hard path ahead of you."'
                        LDNpoints(char, 0, 0, 30)
                    print "Thanks for your efforts towards cleansing the tombs."
                if repent == 2:
                    print "You turn to leave, nodding at Lord Dartian."
                    print "The red glow fades behind you as you walk out of the tomb and back to the fork."
                    print "You leave the tomb. You've had enough of this place anyway."
    if pick == 2:
        print "You walk until you see a Dark Side shrine."
        print "A tuk'ata lies in front of it."
        atta = raw_input("Enter 1 to attack the tuk'ata, and any other key to continue: ")
        if atta == '1':
            TukataAttack(char)
            LDNpoints(char, 0, 30, 10)
        else:
            print "As you get closer, it looks different from any tuk'ata you've seen."
            print "It raises its head and growls as you come close."
            print "You see it's bones through it's skin, and see an injury on it's leg."
            helper = raw_input("Enter 1 to help the tu'kata: ")
            if helper == '1':
                print "You go find a shyrack to feed the tu'kata."
                found = 'false'
                while found == 'false':
                    if random.random() * 100 > 80:
                        print "There's one."
                        AnimalAttack(char)
                        found = 'true'
                    else:
                        print "You keep looking."
                print "You feed the tuk'ata. Now it doesn't want to eat you."
                print "In fact, it looks quite appreciative."
                print "Now, it needs that injury healed."
                healer = raw_input("Enter 1 to heal the tu'kata: ")
                if healer == '1':
                    if char['lightside'] > 44:
                        print "You channel the light side of the Force to heal its wounds."
                        print "It nuzzles you gratefully."
                    else:
                        print "You'll need to use a medpac."
                        if char['medpacs'] > 0:
                             print "You have {} medpacs.".format(char['medpacs'])
                             use = raw_input("Enter 1 to use a medpac: ")
                             if use == '1':
                                 print "You used a medpac!"
            else:
                TukataAttack(char)
                print "Picking on the injured, are we? Tsk tsk tsk."
                LDNpoints(char, 0, 70, 0)
        print "You continue on."
        print "There! At the shrine you see a Sith Holocron."
        print "As you step closer, it seems to thrum with Force Energy."
        print '"{}."'.format(char['name'])
        print "Creepy."
        print "..."
        print "Red tendrils of mist start to reach out for you, and you start to feel faint."
        run = raw_input("Enter 1 to run: ")
        if run ==  '1':
            print "Time to go!"
            print "You run back out of the tomb, promising yourself you will never enter that Force-forsaken tomb again."
        else:
            print "The Dark Side swirls around you."
            print "Its power is... intoxicating."
            LDNpoints(char, 0, 30, 0)
    if pick == 3:
        print "You meander down the right tunnel."
        print "There's two holocrons on either side of the tunnel."
        print "One is a red pyramid, thrumming angrily-- a Sith Holocron."
        print "The other is a gentle blue dodecahedron, a Jedi Holocron."
        print "Which do you take?"
        take = raw_input("Enter 1 for the Jedi Holocron or 2 for the Sith Holocron: ")
        if take == '1':
            LDNpoints(char, 150, 0, 0)
            print "The holocron pulses quietly in your palm, infusing you with a sense of peace."
        elif take == '2':
            LDNpoints(char, 0, 150, 0)
            print "The holocron gleams blood, red, and you feel your rage begin to build."
        else:
            print "You don't take either of the holocrons, continuing on."
            LDNpoints(char, 0, 0, 250)
        print "You continue on down the tomb."
        print "The Force builds in strength as you approach the western-most side of the ruins."
        explore = raw_input("Enter 1 to continue exploring the tunnels or 2 to move on towards the Force Nexus: ")
        while explore == '1':
            luck = (100 * random.random())
            if luck > 98:
                print "Well fierfek."
                print "A shabla terentatek."
                TarentatekAttack(char)
            elif luck < 98 and luck > 94:
                print "A tuk'ata? This day just keeps getting better and better."
                TukataAttack(char)
            elif luck < 94 and luck > 70:
                print "Nothing. At this point, you're kind of relieved."
                print "There's plenty more tunnels, though."
            elif luck < 70 and luck > 50:
                print "A bunch of shyracks squawk angrily."
                AnimalAttack(char)
                HealChoice(char)
                AnimalAttack(char)
                HealChoice(char)
                AnimalAttack(char)
                HealChoice(char)
            elif luck < 50 and luck > 20:
                print "You found a stash of medpacs!"
                char['medpacs'] = char['medpacs'] + 7
            elif luck < 20:
                print "Hmph."
                print "A small stash of holocrons. You snatch them all."
                LDNpoints(char, 20, 20, 20)
            explore = raw_input("Enter 1 to keep exploring: ")
        print "You continue on towards the Force Nexus."
        print "A group of Sith Ghosts waits for you, and they don't look too happy."
        SithFight(char, 'Sith Ghost', 3, 150)
        print "You look around the chamber."
        crypt = raw_input("Enter 1 to enter the crypt, or 2 to look around the chamber: ")
        while crypt == '2':
            loot = random.random() * 100
            if loot > 80:
                print "You found some credits!"
                Credits(char, math.floor(1250 * random.random()))
            elif loot < 80 and loot > 70:
                print "Oh look, a shyrack."
                AnimalAttack(char)
            elif loot < 70 and loot > 35:
                print "You found a small stash of credits!"
                Credits(char, math.floor(random.random() * 70))
            elif loot < 35 and loot > 30:
                print "You found a large stash of goods."
                char['credit'] = char['credit'] + math.floor(random.random() * 10000)
                char['medpacs'] = char['medpacs'] + 15
                char['maxhealth'] = char['maxhealth'] + 40
                char['damage'] = char['damage'] + 30
                print "You receive armor upgrades as well as holos of old Sith fighting techniques, raising your damage and maximum health."
                print "You also now have {} credits and {} medpacs.".format(char['credit'], char['medpacs'])
            elif loot < 30 and loot > 15:
                print "You found some Sith and Jedi holocrons, rasing your Light side and Dark Side points."
                LDNpoints(char, 30, 30, 0)
            else:
                print "You found some Grey Jedi Holocrons!"
                print "These are rare."
                LDNpoints(char, 0, 0, math.floor(random.random() * 300))
            crypt = raw_input("Enter 2 to keep looking around, and any other key to continue: ")
        print "You cautiously enter the crypt."
        print "And there's nothing."
        print "Literally nothing."
        print "Fekking tomb robbers."
        print "You aren't getting paid for this type of osik."

def Beginning(char):
    print """{}, you have been chosen to defend the {} using your skills as a {}.
You have {} credits to your name, and no weapons. How you go from here is up to you.
You may want to find a mentor in the nearby village, or test your skills in the nearby wilds.
You may also want to look in the town's cantina.
You could find a friend, or you may find some information that could be useful.""".format(char['name'],char['faction'], char['classname'], char['credit'])
    print "1: Find a mentor."
    print '2: Head to the wilds.'
    print '3: Enter the cantina.'
    print '4: Keep looking around town.'
    path = raw_input("Which way do you go? ")
    return path

def FindMentor1(char):
    print "You chose to find a mentor!"
    print "You wander around town, looking for someone who knows a thing or two about the ongoing wars."
    print "Dreshdae is a horrid place, but you have little choice. This is where possible Sith must come to prove themselves."
    print "Not for the last time, you wish that Sith had never realized you were an Adept, a Forceling, whatever."
    print "But this is the way the dice fall."
    raw_input("Enter any key to continue: ")
    print "There's the Academy not too far from here."
    print "You sigh, resigning yourself to dealing with more Sith."
    print "Yep."
    print "There's some now, and they don't look cheerful."
    print "..."
    print "Not that Sith ever do, though, to be honest."
    raw_input("Enter any key to continue: ")
    print "Oh look, it seems the Acolytes decided to attack you."
    print "..... What a surprise."
    SithFight(char, 'Acoloyte', 4, 70)
    print "You collect the credits from their bodies."
    Credits(char, math.floor(random.random() * 5000))
    raw_input("Enter any key to continue: ")
    print "You enter the Academy cautiously."
    print "You've heard all about the ruthlessness and cunning of the Sith."
    print "Several Acolytes eye you as you walk in."
    raw_input("Enter any key to continue: ")
    print "You keep looking around, but the Sith Masters are all out fighting the Republic."
    print "You head back to town, dissapointed."

def ExploreWilds1(char):
    print "You head off to the wilds."
    planet = 'Korriban'
    description = """Pretty sure you're in Hell right now. Dry sand scrapes against your skin, and a tuk'ata howls somewhere in the distance.
A shyrack screeches overhead, and you tense, wishing you had a blaster, or maybe a cannon.
If that's not enough, giant statues, their heads bowed lean over you, hundreds of feet tall.
You can see a massive building in the distance."""
    print "{}. {}.".format(planet, description)
    print "Well, thats interesting."
    choice = raw_input("1 to head towards, 2 to keep exploring: ")
    while choice == '2':
        print "Alright. You decide to keep looking around."
        explore = 100 * random.random()
        if explore < 55:
            print "You found some rubble!"
            luck = 100 * random.random()
            if luck < 25:
                print "You found a couple credits. Nice."
                Credits(char, 2)
            if luck < 70 and luck > 40:
                AnimalAttack(char)
        choice = raw_input("1 to move on, 2 to keep exploring: ")
    print "Who knew {} could be so big?".format(planet)
    print
    print "..."
    print
    print "..."
    print
    print "Finally, you arrive."
    KorribanTomb(char)

def EnterCantina1(char):
    print "A drink sounds good right now."
    print "Imperial propaganda blares from the speakers."
    print """It's got a rather catchy tune, and you start humming, "Bum Bum bum dum da dum dum da dum....."""""
    print "A recruiter looks up at you, sizing you up. The waitress gestures at a table."
    print "A 'treasure hunter' flails wildly, in the middle of telling some tale to his friends."
    print "And there's....."
    print "That's impossible, you think."
    raw_input("Hit any key to continue.")
    print "That's Darth Imperius."
    print "The Twi'lek sits in a booth next to a Togruta. She seems rather more cheerful than her position would allow."
    print "Your jaw drops and you stare at the Dark Lord."
    print "Unfortunately, this catches Imperius's eye."
    print "She waves you over, her features hardening into ice."
    runner = raw_input("Enter 1 to run and any other key to continue: ")
    if runner == '1':
        print "You barely make it out of the Cantina, before a voice slashes through the air"
        print '"Get them!"'
        print "Your day is just fantastic so far."
        SithFight(char, 'Darth Imperius', 1, 1500)
        print "You stand over the Twi'lek's body, shocked."
        print "GAME OVER"
        print
        print "You heard me. GAME OVER. Imperius was your ride off Korriban, genius."
        quit()
    else:
        print "You nervously walk towards the Sith."
        print "Imperius leans forward as you slide into the booth, steepling her fingers."
        print '"Risky business, approaching a Dark Lord," the Togruta drawls, twin lightsabers flashing at her hip.'
        print '"Well, I cannot run quickly enough to escape," you stammer out.'
        print '"Relax," Imperius orders."'
        print "She leans forward, and tells about a mission."
        accept = raw_input("Enter 1 to accept the mission: ")
        if accept == '1':
            char['missionaccept'] = 'yes'
        else:
            print "She frowns angrily."
            print '"Is there any I could change your mind?"'
            print "You still have a chance to accept the mission."
            print "You sigh, and accept the mission, since you have no real choice."
            char['missionaccept'] = 'yes'
        print "Your mission is to hunt down the source of the rumors surrounding the Holocron of Darth Adega and the Blade of Ragnos."
        print "You must also search out the hidden Sith facility-- it is worrying Imperius, but she cannot look for it herself."
        print "While your search for the Sith facilty must be last, do you want to search for the Holocron or the Blade, first?"
        search = raw_input("Enter 1 for the Blade or 2 for the Holocron: ")
        if search == '1':
            char['priorityone'] = 'Blade of Ragnos'
            char['prioritytwo'] = 'Holocron of Adega'
        elif search == '2':
            char['priorityone'] = 'Holocron of Adega'
            char['prioritytwo'] = 'Blade of Ragnos'
        else:
            char['priorityone'] = 'Blade of Ragnos'
            char['prioritytwo'] = 'Holocron of Adega'
        print "You'll need to head to Dromund Kaas first though. This mission is your alone."
        print "You must be trained in the ways of the Sith."
        print "Imperius hands you a keycard, giving you access to one of her ships."
        print "You can now leave Korriban."
        char['ship'] = 'true'
            
############################################################################################################################################    
def ExploreTown1(char):
    print "Hmm. The markets, the hospital or the training arena?"
    choose = raw_input("1 for the markets, 2 for the hospital, 3 for the training arena or 4 to go somewhere else: ")
    while choose != '4':
        if choose == '1':
            print "Alright. You head to the markets."
            print "A seller approaches you with holocron and artifacts for sale."
            buyer = raw_input("Enter 1 to buy something: ")
            while buyer == '1':
                sale = {'200 LS Jedi Holocron':5000, '200 DS Sith Holocron': 5000, '100 LS Jedi Artifact': 2500, '100 DS Sith Artifact': 2500, '50 LS Jedi Holocron': 500,
                        '500 LS Jedi Holocron': 7000, '50 LS Jedi Holocron': 500, '20 LS Jedi Holocron': 200, '40 LS Jedi Holocron': 400,
                        '5 DS Sith Holocron': 50,'500 DS Sith Holocron': 7000, '50 DS Sith Holocron': 500, '20 DS Sith Holocron': 200, '40 DS Sith Holocron': 400,
                        '5 LS Jedi Holocron': 50, '50 DS Sith Holocron': 500}
                for item in sale:
                    print item, 'for', sale[item], 'credits.'
                key = raw_input("Enter the name of the item you wish to purchase: ")
                if key not in sale:
                    print "Sorry, that isn't availavble for purchase here."
                else:
                    if char['credit'] < sale[key]:
                        print "You need more credits to buy that."
                    else:
                        char['credit'] = char['credit'] - sale[key]
                        lst = key.split()
                        if lst[1] == 'LS':
                            char['lightside'] = char['lightside'] + int(lst[0])
                        elif lst[1] == 'DS':
                            char['darkside'] = char['darkside'] + int(lst[0])
                        print "You bought {} for {} credits, leaving you with {} credits.".format(key, sale[key], char['credit'])
                        del sale[key]
                buyer = raw_input("Enter 1 to continue shopping: ")
        if choose == '2':
            print "You head to the hospital."
            print "Do you wish to upgrade your maximum health or buy medpacs?"
            print "10 credits for each maximum health point."
            print "20 credits for each medpac."
            print "You may also restore yourself to full health for 30 credits."
            med = raw_input("Enter the number of medpacs you wish to buy: ")
            heal = raw_input("Enter the number of maximum health points you wish to gain: ")
            full = raw_input("Enter 1 to fully heal yourself: ")
            if med.isdigit() and heal.isdigit():
                med = int(med)
                heal = int(heal)
                medcost = med * 20
                healcost = heal * 10
                total = healcost + medcost
                if medcost + healcost > char['credit']:
                    print "You don't have enough credits for that."
                else:
                    char['credit'] = char['credit'] - total
                    char['maxhealth'] = char['maxhealth'] + heal
                    char['medpacs'] = char['medpacs'] + med
                    print "You bought {} medpacs and {} maximum health points for {} credits, leaving you with {} credits.".format(med, heal, total, char['credit'])
                if full == '1':
                    fullcost = 30
                    char['health'] = char['maxhealth']
                    char['credit'] = char['credit'] - fullcost
                    print "You healed yourself fully!"
            else:
                print "You did not enter a number."
        if choose == '3':
            print "Welcome to the training arena!"
            train = raw_input("Enter 1 to train: ")
            if train == '1':
                number = raw_input("Enter the number of enemies you wish to fight: ")
                hp = raw_input("Enter the health for each enemy: ")
                try:
                    SithFight(char, 'Training Dummy', int(number), int(hp))
                    HealChoice(char)
                    print "You gain 30 LS points, 30 DS points, and 30 NS points."
                    LDNpoints(char, 30, 30, 30)
                    print "You also gain +10 to damage"
                    char['damage'] = char['damage'] + 10
                except:
                    print "Please enter numbers for the health and number of enemies."
        choose = raw_input("Merchant = 1, Hospital = 2, Training = 3, Elsewhere = 4. What next: ")
      
###########################################################################################################################################
def FirstPlanet():
    char = FactionAndClass()
    path = Beginning(char)
    while path != '5':
        if path == '1':
            FindMentor1(char)
        if path == '2':
            ExploreWilds1(char)
        if path == '3':
            EnterCantina1(char)
        if path == '4':
            ExploreTown1(char)
        path = raw_input("What next? Remember, Mentor(1), Wilds(2), Cantina(3), Town(4), Done(5)")
    if char['ship'] == 'true':
        print "You may now leave Korriban."
        print "If you're done here, you may leave for Dromund Kaas."
        leave = raw_input("Enter 1 to leave: ")
        if leave == '1':
            print "Your new ship thrums as her powerful engines warm up."
            print "She needs a name, you muse."
            char['shipname'] = raw_input("Enter ship name: ")
            print "The {} takes off, screaming through the atmosphere.".format(char['shipname'])
            print "The navicomputer beeps."
            hyperspace = raw_input("Enter 1 to engage the hyperdrive: ")
            if hyperspace == '1':
                print "The stars turn into streaks as the {} exits realspace.".format(char['shipname'])
                print "YOU HAVE LEFT KORRIBAN!"
                print
                print "CONGRATULATIONS!"
                print
        else:
            path = raw_input("What next? Remember, Mentor(1), Wilds(2), Cantina(3), Town(4), Done(5)")
            while path != '5':
                if path == '1':
                    FindMentor1(char)
                if path == '2':
                    ExploreWilds1(char)
                if path == '3':
                    EnterCantina1(char)
                if path == '4':
                    ExploreTown1(char)
                path = raw_input("What next? Remember, Mentor(1), Wilds(2), Cantina(3), Town(4), Done(5)")
    else:
        print "You'll need access to a ship to leave Korriban."
################################################################################################################################        


def KaasPort(char):
    print "The markets, the hospital?"
    choose = raw_input("1 for the shop, 2 for the clinic, or 3 to continue to Kaas City: ")
    while choose != '3':
        if choose == '1':
            print "Alright. You head to the shop."
            print "You see a bunch of artifacts and holocrons for sale."
            print "They're cheaper due to the high levels of Sith on this planet."
            buyer = raw_input("Enter 1 to buy something: ")
            while buyer == '1':
                sale = {'250 LS Jedi Holocron':5000, '250 DS Sith Holocron': 5000, '130 LS Jedi Artifact': 2500, '130 DS Sith Artifact': 2500,
                        '60 LS Jedi Holocron': 500,
                        '600 LS Jedi Holocron': 7000, '70 LS Jedi Holocron': 500, '30 LS Jedi Holocron': 200, '50 LS Jedi Holocron': 400,
                        '10 DS Sith Holocron': 50,'600 DS Sith Holocron': 7000, '60 DS Sith Holocron': 500, '30 DS Sith Holocron': 200, '50 DS Sith Holocron': 400,
                        '10 DS Sith Holocron': 50, '70 DS Sith Holocron': 500}
                for item in sale:
                    print item, 'for', sale[item], 'credits.'
                key = raw_input("Enter the name of the item you wish to purchase: ")
                if key not in sale:
                    print "We don't have that here in Dromund Kaas."
                else:
                    if char['credit'] < sale[key]:
                        print "You need more credits to buy that."
                    else:
                        char['credit'] = char['credit'] - sale[key]
                        lst = key.split()
                        if lst[1] == 'LS':
                            char['lightside'] = char['lightside'] + int(lst[0])
                        elif lst[1] == 'DS':
                            char['darkside'] = char['darkside'] + int(lst[0])
                        print "You bought {} for {} credits, leaving you with {} credits.".format(key, sale[key], char['credit'])
                        del sale[key]
                buyer = raw_input("Enter 1 to continue shopping: ")
        if choose == '2':
            print "You head to the clinic."
            print "Do you wish to upgrade your maximum health or buy medpacs?"
            print "20 credits for each maximum health point."
            print "30 credits for each medpac."
            print "You may also restore yourself to full health for 35 credits."
            med = raw_input("Enter the number of medpacs you wish to buy: ")
            heal = raw_input("Enter the number of maximum health points you wish to gain: ")
            full = raw_input("Enter 1 to fully heal yourself: ")
            try:
                med = int(med)
                heal = int(heal)
                medcost = med * 30
                healcost = heal * 20
                total = healcost + medcost
                if medcost + healcost > char['credit']:
                    print "You don't have enough credits for that."
                else:
                    char['credit'] = char['credit'] - total
                    char['maxhealth'] = char['maxhealth'] + heal
                    char['medpacs'] = char['medpacs'] + med
                    print "You bought {} medpacs and {} maximum health points for {} credits, leaving you with {} credits.".format(med, heal, total, char['credit'])
                if full == '1':
                    fullcost = 35
                    char['health'] = char['maxhealth']
                    char['credit'] = char['credit'] - fullcost
                    print "The cranky old nurse slowly heals you back to full health, then shoos you away"
            except:
                print "You did not enter a number."
            
def KaasWilds(char):
    minleft = 50
    for steps in range(50):
        print "You're {} minutes away from Kaas City.".format(minleft)
        minleft = minleft - 1
        encounter = random.random() * 100
        if encounter > 98:
            print "You find a cave, and your curiosity gets the better of you."
            print 'Too late, you remember the saying, "Curiosity killed the nexu."'
            print "The Terentatek you disturbed attacks you."
            TarentatekAttack(char)
        elif encounter > 60 and encounter < 98:
            print "One of the many animals in Dromund Kaas's wilds decided you would be a good dinner."
            AnimalAttack(char)
        elif encounter > 40 and encounter < 60:
            print "A few Sith decide you're a good way to pass the time."
            print "Naturally, you're against the idea."
            print "Crispy deep lightning-fried {} is not the way to go.".format(char['name'])
            SithFight(char, 'Sith', 3, 110)
        elif encounter > 25 and encounter < 40:
            print "You found a stash of holocrons!"
            LDNpoints(char, 10, 10, 10)
        elif encounter > 15 and encounter < 25:
            print "You found a decent stash of credits!"
            char['credit'] = char['credit'] + math.floor(random.random() * 500)
        elif encounter > 5 and encounter < 15:
            print "You found a small stash of credits!"
            char['credit'] = char['credit'] + math.floor(random.random() * 250)
        else:
            print "You found a massive stash of credits!"
            char['credit'] = char['credit'] + math.floor(random.random() * 5000)
################################################################################
def KaasCity(char):
    print "You finally reach Kaas City."
    print "The city has instituted a clinic at the entrance to the city."
    print "You're now fully healed!"
    char['health'] = char['maxhealth']
    print "Your comm lights up."
    raw_input("Enter any key to accept the call: ")
    print "Imperius stares at you, intimidating even through a holo."
    print '''"I've got a lead for you to investigate," she announces.'''
    print "She tells you about the lead, and you grimace."
    raw_input("Enter any key to continue: ")
    print "Imperial Intelligence."
    print "You sigh and head towards the tallest spires in the city."
    loiter = raw_input("Enter 1 to loiter, disregarding Imperius's request to hurry, or 2 to go straight to Intelligence: ")
    if loiter == '1':
        LDNpoints(char, 0, 5, 10)
        print "As you loiter in Kaas City, several drunken cantina patrons decide you seem like good target practice."
        SithFight(char,'Drunken Patron', 5, 75)
        print "You loot their bodies for credits."
        char['credit'] = char['credit'] + math.floor(random.random() * 1000)
    else:
        LDNpoints(char, 5, 0, 10)
        print "You grimace as rain seeps into your clothes."
        print "You grab a cheap secondhand jacket, since you won't need it for very long."
        print "You find a nice sum of credits in the pocket."
        char['credit'] = char['credit'] + math.floor(random.random() * 2000)
    print "You arrive at Imperial Intelligence HQ."
    raw_input("Enter any key to continue: ")
    print '"Ah, {}. We have been expecting you."'.format(char['name'])
    print "A stout dark haired man nods at you as you apparoach the conference table."
    print '"Imperius sends you her regards."'
    print '"Now, down to business. I am Minister Feros, head of Sith Intelligence."'
    query1 = raw_input("(1)Ask about old Intelligence Agency, (2)Ask about new Agency, (3) Continue: ")
    if query1 == '1':
        print '''"Ah, Imperial Intelligence." Feros frowns and strokes his mustache.
"Now that is the question, isn't it? We're not entirely sure what happened, after all. The
Minister though, he was in the thick of it. No one knows where he is, now, of course. Him and Cipher Nine,
Watcher Two, the Remnants, we like to call them. They've escaped. The Republic knows nothing, we know nothing.
Nothig but a name. The Star Cabal. They brought the old Intelligence down."

"Anyways, no time for ghost tales. They're likely all dead. So, what have you come for?"'''
    elif query1 == '2':
        print '''"We're tasked with intelligence operations, of course, but we also...
solve problems within and outside the Empire. Assassination, investigation, information disemination..."

"In short, we ensure Imperial galactic domination, by any means necessary."

A shiver goes down your spine. Despite his jovial exterior, there's a glint in his eyes
that suggests a spine of military-grade durasteel. This man is not someone to cross."'''
    else:
        print '"Down to business, then. Good!"'
    print '''"Darth Imperius herself seems to be overseeing your investigation. This means the investigation has been blacklisted.
Only those working directly under her command may see your efforts." Feros leaned forward, and rumbled, "This means from now on,
your actions reflect on Darth Imperius. You must be careful."'''
    print "You leave Feros and get busy reading records and studying up on the Sith Empire"
    print "Eventually, your chrono beeps, and you get up to leave and head to your apartment."
    print "......"
    print "Of course."
    print "Some sneering Sith block the walkway to your rental speeder."
    print '"Lord Nazarra sent us, schutta."'
    choice = raw_input("Enter 1 to go ahead and attack, or 2 to keep tallking: ")
    if choice == '1':
        print "You leap forward and attack!"
        LDNpoints(0, 40, 40)
        SithFight(char, "Sith Apprentice", 4, 120)
    elif choice == '2':
        LDNpoints(40, 0, 40)
        print '"Lord Nazarra?" You cross your arms and stare at the Sith, unimpressed.'
        print '"Imperius will die," they state, "So join us-- or die."'
        print '"How cliche," you mutter.'
        print "They attack, tired of talking."
        SithFight(char, 'Sith Apprentice', 3, 120)
    raw_input("Enter any key to continue: ")
    print "You sigh, and step over their bodies."
    print '''........

........

"THOSE SHAB'LA SONS OF HUT'TUUNE, STOOPA SCHUTTA, FROG-BRAIN,
DROOLING BO'MARR CAST OFF, PIECE OF POODOO GOOD FOR NOTHING SITH SCUM WEAKLINGS!!!"

Your yell echoes through the parking lot. The intelligent bystanders duck into
their homes or cars.

They fierfekking KEYYED your speeder!

"THAT WAS AN OSIK'LA RENTAL!!!"
'''
    print "You leave early in the morning to meet with Imperius."
    print "You glower as you get out of your (keyyed)(RENTAL) speeder."
    print "One of Imperius's aides hand you a large cup of caf as you slouch in, and you slowly start to feel human again."
    print "Imperius sits down, and asks if you found anything interesting."
    print """You can mention:
(1) Lord Nazarra and his attack
(2) The investigation being blacklisted
(3) Possible locations for the Holocron and the Blade
"""
    mention = raw_input("Enter the topic to discuss: ")
    mentioncount = 0
    while mentioncount != 3:
        if mention == '1':
            print "Imperius sighs."
            print '''"Lord Nazzara has been a pain in my shebs ever since I joined the Dark Council."
    Her mouth twitched, and then she grinned, revealing the sharp fangs common to all Twi'leks. "He's out
    of his league, and besides, I'm head of the Sphere of Ancient Knowledge. It's just dusty old tombs, some say, but
    I've got all the ancient relics under my command, AND I killed Thanoton to get here.
    He has no idea what he's trying to get himself into."

    "If he's out of his league, then why does he challenge you?" You shift in the high backed chair. Sith
    do not keep ergonomics in mind when designing furniture.

    Imperius leans back in her chair, her expression pensieve. "And that is the problem. I
    have no idea why he would do such a thing. Maybe his hate for aliens has made him reckless."'''
            guess = raw_input("Motive could be (1)Anti-alien, (2)Another Dark Lord's urging, or (3)Unknown: ")
            if guess == '1':
                print "Imperius agrees with you about the anti-alien tendencies."
                print "If it's anti-alien hate though, it doesn't explain the attack on you."
                print "It doesn't matter- Imperius will probably.... take care... of the problem herself."
            if guess == '2':
                print "Imperius acknowledges that she's thought of that possibility."
                print "She has little idea beyond 'the entire Sith Order', though, when it comes to her enemies."
                print "She promises to keep looking, as she would have anyway."
            if guess == '3':
                print "Imperius nods, accepting the possibility of some as of yet unknown motive."
                print "He will die anyway, if he chooses to face her, so she shrugs."
                print '''"The motive doesn't matter, only his death."'''
            mentioncount = mentioncount + 1
        if mention == '2':
            print "Imperius explains that the less other Sith know, the better."
            print "She remarks that one could simply be buying new clothes, and that the buying of new clothes could be turned into treason."
            print "Sith are paranoid, in short."
            print '...'
            print "As they must be, to survive."
            mentioncount = mentioncount + 1
        if mention == '3':
            print "Down to the task at hand, good."
            print "She reveals she has little idea where to find the Blade and the Holocron."
            print "There may be a clue in the Ancient Temple to the west of Kaas City."
            print "Imperius instructs you to head there, with all due haste."
            print """ "{}." You turn back as you start to head out the door.

"Be careful. The tomb will try to claim your sanity and your power. Do not linger there, whatever you do."

You stare at the Dark Lord. Her lekku are stiff, and the ends are quivering, and you realize she is afraid.
"You've been there, my lord. Haven't you?"

Her eyes close, and her expression twists. "Yes. And I stayed overlong. Sometimes, I can still hear the dead.
They scream, and rage, and it is a fate I would wish on no one. So do hurry, {}."

"I will. Tombs are not my favorite resort destination."
""".format(char['name'], char['name'])
        mention = raw_input("Enter the topic to discuss: ")
    print "You leave for the tomb, grimacing."
    print "....."
    print "You though you were done with tombs once you left Korriban."
    print "Damn it."
###########################################################################################################
def KaasTemple(char):
    print "You blunder through the Dromund Kaas undergrowth, cursing the planet with every footstep."
    for steps in range(25):
        print "You've walked for {} minutes out of the 25 minute long hike.".format(steps)
        hahasucker = math.floor(random.random() * 100)
        if hahasucker > 90:
            print "One of the crazy reseach teams Imperius warned you about spots you."
            print "...."
            print "Osik."
            print "You decide not to let them research your dead body."
            SithFight(char, 'Crazed Research Team-Member', 7, 110)
        elif hahasucker > 60 and hahasucker < 90:
            print "One of the many animals in Dromund Kaas's wilds decided you would be a good dinner."
            AnimalAttack(char)
        elif hahasucker > 40 and hahasucker < 60:
            print "A few Sith decide you really don't need to get to the tomb."
            print "Of course, you're against the idea."
            print "Crispy deep lightning-fried {} is neither tasty nor profitable.".format(char['name'])
            SithFight(char, 'Sith', 3, 110)
        elif hahasucker > 25 and hahasucker < 40:
            print "You found a stash of holocrons!"
            LDNpoints(char, 30, 30, 30)
        elif hahasucker > 15 and hahasucker < 25:
            print "You found a sweet stash of credits!"
            char['credit'] = char['credit'] + math.floor(random.random() * 5000)
        elif hahasucker > 5 and hahasucker < 15:
            print "You found a small stash of credits!"
            char['credit'] = char['credit'] + math.floor(random.random() * 250)
        else:
            print "You found a wicked stash of credits!"
            char['credit'] = char['credit'] + math.floor(random.random() * 50000)
        print
        raw_input("Enter any key to continue: ")
    print "The temple gives off a dull gleam, almost purple in the neverending twilight of Dromund Kaas."
    print "The ruins dotting the courtyard are magnificent-- the evil radiating from this place does little to mask their former glory."
    print "The maddened researchers though, might, and you decide that the Empire has no business in archeology."
    SithFight(char, 'Crazy Researcher', 7, 120)
    print "Ugh."
    raw_input("Enter any key to continue into the temple: ")
    print "You cautiously enter into the cavernous temple, an eiree green glow permeating the massive spaces within."
    print "Demented shrieks and cries echo through the halls."
    print "You hold on tighter to your weapon."
    raw_input("Enter any key to creep around the first corner: ")
    print "The source of some of the animalistic wails stares at you."
    print "One of the maddened Sith Imperius warned you about bares its teeth."
    SithFight(char, 'Maddened Sith Lord', 1, 450)
    print "Some of the, well, zombies amble towards you, alerted by the sound of your fight."
    SithFight(char, 'Crazed Research Team Members', 7, 120)
    print "You attempt to wipe the guts off your pants, but really only succeed in smearing it more."
    print "Fierfek, what a brilliant day."
    print "There's five tombs on your map, and unfortunately, you have no idea which is which."
    print "They all might contain useful information."
    print "The first tomb on the map has notes about a cult centered there."
    print "The second has the remains of dozens of Sith Lords who rebelled against the Emporer."
    print "The third, a Sith Alchemist. You shudder, thinking of the Sithspawn that might lie within."
    print "The fourth has notes about a Kallig, but that's it. There's very little."
    print "The last, the fifth, has no notes at all."
    tomborder = []
    for tomb in range(5):
        tomborder = tomborder + raw_input("Enter the number of the tomb to visit: ")
    print "Is this order satisfactory?"
    for item in tomborder:
        print "Tomb {}".format(item)
    orderTrue = raw_input("Enter 1 to continue with this order: ")
    while orderTrue != '1':
        for entry in range(5):
            tomborder.append(raw_input("Enter entry number here: "))
        print "Is the following order satisfactory?"
        for item in tomborder:
            print "Tomb {}".format(item)
        orderTrue = raw_input("Enter 1 to continue with this order: ")
    for order in tomborder:
        if order == '1':
            print "You hate cults with a burning passion, having lost your father to one."
            print "The Dark Side oils within you as rage ignites, turning your heart into a furnace."
            print "A few guards seee you coming and attack."
            SithFight(char, 'Cult Guard', 3, 180)
            raw_input("Enter any key to continue into the cult's tomb: ")
            print "Shrines to a long dead Sith dot the halls."
            print "The screaming of the guards must have awakened the rest of the cult to your presence, and several stand in your way, blocking the path to the central chamber."
            SithFight(char, 'Cult Member', 15, 350)
            print "You head into the central chamber."
            raw_input("Enter any key to continue: ")
            print "You strike down the guards, and stalk towards the Sith in the center."
            print '"End this," you snarl with clenched teeth.'
            print "The Sith simply chuckles, igniting a saber."
            print '''In a sickly sweet childlike-tone, he murmurs, "But the power. You want it. You crave it."

You hiss at him, but before you can say anything, the Sith leaps at you, suddenly full of rage. "You killed my children!"'''
            print "You briefly reflect you didn't exactly have this on your agenda for the day before parrying away the first swipe."
            SithFight(char, "Cult Leader", 1, 950)
            print "You stalk back out, having finished off the cult."
            print "You halt at the entrance to the tomb, and turn back."
            print '''"That was for my father, hut'tuune."'''
        elif order == '2':
            print "This is the first quiet tomb you've been in."
            print "You take a moment to breathe and admire the architecture."
            char['health'] = char['maxhealth']
            print "You're now at full health."
        elif order == '3':
            print "You were right, unfortunately."
            print "Hordes of Sithspawn meander about in the crypt."
            print "Frakking alchemist."
            SithFight(char, "Tuk'ata Sithspawn", 4, 300)
            print "You griamce, some unidentifiable fluid and blood and..... motor oil on your clothes."
            print "You sniff at it, immediately wishing you hadn't."
            print "But yes, that is indeed motor oil."
            print "You eye the mechanical joints of the mutated tuk'ata."
            print "Well. As long as it isn't too poisonous."
            raw_input("Enter any key to continue further into the crypt: ")
            print "You shiver, a disturbance in the Force making the hair on the back of your neck stand up."
            print "The ghost of a Sith Pureblood stalks apst you, turnig to face you as he reaches the stone coffin."
            print '''"I am Lord Alcim. I meld the unliving and the living. I have conquered death, and I have created life.'''
            print "He continues in this vain for sometime."
            leave = raw_input("Enter 1 to talk to him, and any other key to leave: ")
            if leave == '1':
                if char['lightside'] > 500:
                    print "You can't help but want to redeem this lost soul."
                    print'''"This isn't life," you whisper. "And these animals: They can't hunt, can't feel the sun's rays throgh their fur, can't find a mate...
They aren't alive, just mutated."

The Sith pauses. "Yes, I have considered this, but you cannot change my mind."

"What would change your mind? A Force-Honest plea?"

"A sith would never beg," he muses. His eyes open wide, and he frowns. "You are not Sith. But you have survived the tomb, and the voices do not sing
to you. Our doctrine states that only one who obtain power could defeat this temple.... but that is not your doctrine."

"I am Sith," you assert, "Just... a different kind. I don't believe in power for power's sake, and the dark is not stronger than the light."

He looks pensive. "Then you have confirmed my doubts about our order."

He begins to glow, and the Sithspawn begin to drop, one by one.

"Change the order. Make us stronger."

And Lord Alcim disappears.'''
                    print "You look around, Sithspawn dissolving into puddles of.... goo."
                    print "..."
                    print "Damn, but you are NOT getting paid enough for this."
                else:
                    print "You stand there a while, but you really can't get a word in edge wise with Lord Chatterbox."
        elif order == '4':
            print "Imperius's notes only say 'Kallig'."
            print "Ergo, you know next to nothing about this tomb."
            print "And so, you are suitable shocked when a ghost appears."
            print "You briefly wish for a triple shot of expresso."
            print '"You seek to aid Darth Imperius," the masked ghost intones.'
            print '''"Well, yes. She got me off Korriban, and I'm curious abou this jaunt of hers. Would have ccome alog anyway to find out what was going on."

The ghost grumbles, then states, "If you turn your back on her, I will have my revenge."

You shrug, "You're dead, and I've got nothing planned. So far, I'm her loyal ally. But if someone stronger coes along,
I may join them."

"I can ask nothing less," the ghost says.

He then gives you the choice of strength in the Force, increased health, or increased fighting prowess."'''
            choice = raw_input("(1)Force Points, (2)Health, (3)Damage: ")
            if choice == '1':
                LDNpoints(char, 100, 100, 100)
            elif choice == '2':
                char['maxhealth'] = char['maxhealth'] + 50
                char['health'] = char['maxhealth']
            elif choice == '3':
                char['damage'] = char['damage'] + 50
        elif order == '5':
            print "You stalk into the tomb, blade at the ready."
            for steps in range(15):
                luck = random.random()
                if luck > .75:
                    print "You fall victim to one of the traps in the tomb."
                    if char['classname'] == 'Juggernaut':
                        print "As a Juggernaut, you easily shake off any damage you may have taken."
                    else:
                        char['health'] = char['health'] - 20
                        print "You take 20 damage."
                        HealChoice(char)
                elif luck < .75 and luck > .5:
                    print "A dwarf shyrack dive bombs you, then flies away in a hurry."
                    print "Your footsteps must have disturbed it."
                    print "The only damage you take is to your dignity, which you feel has been rather questionable of late."
                elif luck < .5 and luck > .2:
                    print "You're attacked by a bunch of overlarge spiders."
                    AnimalAttack(char)
                    AnimalAttack(char)
                    AnimalAttack(char)
                else:
                    print "You creep along and water falls on your face."
                    print "It must be raining again outside."
                raw_input("Enter any key to continue: ")
            print "You head into the central chamber, and snag the Holocron."
            print "However, it triggers a trap."
            print "A terentatek lurches out of the dank tomb corridors."
            SithFight(char, "Terentatek Mauler", 1, 1700)
            print "You clean off your blade, and head out, holocron in hand."
    print "You sigh, stepping out of the tomb."
    print "You shake off the ghosts, and prepare to tread back to Kaas City."
    print "...."
    print "Shab, but you did not sign up for this much exercise."
    print "When you get back to Kaas City,  you discover the map is in a language no one loyal to Imperius knows."
    print "...."
    print "An enraged howl echoed though Kaas City that day."
    raw_input("Enter any key to continue: ")
        
def ChasingGhosts(char):
    print "Your search leads you through Kaas City, through it's underbelly and glittering spires."
    print "You track down leads, hunt through Archives, and shake down anyone who might know how to translate that map."
    print "Eventually, this leads you to the estates of Lord Nazarra."
    print "You sigh, resolving yourself to cutting through another Sith fortress."
    stock = raw_input("Enter any key to head over to Nazarra's estate, or 1 to head to the clinic: ")
    if stock == '1':
        med = raw_input("Enter the number of medpacs you wish to buy for 40 credits each: ")
        heal = raw_input("Enter the number of maximum health points you wish to gain for 30 credits each: ")
        full = raw_input("Enter 1 to fully heal yourself for 45 credits: ")
        try:
            med = int(med)
            heal = int(heal)
            medcost = med * 40
            healcost = heal * 30
            total = healcost + medcost
            if medcost + healcost > char['credit']:
                print "You don't have enough credits for that."
            else:
                char['credit'] = char['credit'] - total
                char['maxhealth'] = char['maxhealth'] + heal
                char['medpacs'] = char['medpacs'] + med
                print "You bought {} medpacs and {} maximum health points for {} credits, leaving you with {} credits.".format(med, heal, total, char['credit'])
            if full == '1':
                fullcost = 45
                char['health'] = char['maxhealth']
                char['credit'] = char['credit'] - fullcost
                print "The cranky old nurse slowly heals you back to full health, then shoos you away"
        except:
            print "You did not enter a number."
    print "You trudge towards the palace."
    print "That better be a solid lead."
    print "Two guards stand outside the gates. There's definitely more inside, but you might be able to mind-trick these two."
    if char['lightside'] > 100 or char['darkside'] > 100:
        if char['lightside'] > char['darkside']:
            print "You use a Jedi Mind Trick to get by the guards."
            LDNpoints(char, 30, 0, 0)
        else:
            print "You summon the Dark Side of the Force to warp their minds."
            print "You pass by their shells, their minds burnt out by your will."
    else:
        print "You'll have to do this the old fashioned way."
        print "You unclip your saber from your belt."
        SithFight(char, 'Guard', 2, 150)
    print "You continue on into the compound."
    check = raw_input("Enter 1 to check the high security vault first, and any other key to continue towards the archves: ")
    if check == '1':
        print "You stalk into the vault, slicing through the two droids guarding it."
        keycode = raw_input("Enter the key code: ")
        tries = 0
        while keycode != '1138':
            tries = tries + 1
            print "The pad blinks angrily at you."
            keycode = raw_input("Enter the key code: ")
            if tries > 4:
                print "Enter the title of Lord Lucaas's first film."
                print "You sigh, wondering who this Jeorj Lucaas is."
            if tries > 10:
                print "Alarms ring out."
                print "You must have triggered an alert."
                print "You swear and drop to your knees, tearing panels out, trying to cross the wires, and if you're honest, do anything mildly helpful, really."
                print "A code flickers on the screen: 1138"
                keycode = raw_input("Enter the key code: ")
        print "You grimace, slipping inside the vault."
        print "Your heart sinks as a massive turret whirls to target you."
        SithFight(char, 'Turret', 1, 400)
        print "You stare at the wreckage, intruiged."
        print "There better be some good loot here for a turret like that."
        raw_input("Enter any key to continue on: ")
        print "You slip into the vault."
        Credits(char, 75000)
        print "You see two Holocrons. The security on them ensures you'll only be able to get to one of them."
        print "Which do you take: the Jedi or Sith Holocron?"
        take = raw_input("(1)Sith or (2)Jedi: ")
        if take == '1':
            LDNpoints(char, 100, 0, 0)
            print "You snatch the blue fractal-patterns device."
        elif take == '2':
            LDNpoints(char, 0, 100, 0)
            print "You snatch the red pyramid."
    print "You continue slipping through the fortress."
    print "You execute or Mind-trick guards, sneaking through without opposition."
    print "..."
    print "It's almost too easy."
    print "You come to the door, and eye the code Imperius gave you: 1977."
    code = raw_input("The keycode prompts you for the key: ")
    while code != '1977':
        code = raw_input("The keycode prompts you for the key: ")
    print "You enter nervously into the Archives."
    print "It seems you were right to be nervous..."
    raw_input("Enter any key to continue: ")
    print "Fierfek."
    print "Lord Nazarra stands, juggling the Ancient Holocron you need."
    print 'He smirks, "Looking for this?"'
    print "You unholster your weapons in reply."
    raw_input("Enter any key to continue: ")
    print "Lightning crackles from his fingers."
    print "You receive 30 damage!"
    char['health'] = char['health'] - 30
    SithFight(char, 'Lord Nazarra', 1, 750)
    print "You grab the holocron from the Sith corpse."
    print "It's time to return to Imperius."
    print "You make sure to pillage the di'kut's Archives for some Jedi and Sith holocrons."
    LDNpoints(char, 40, 40, 40)
    print "You also disover a stash of creds."
    Credits(char, math.floor(random.random() * 10000))
    raw_input("Enter any key to continue: ")
    print "You trudge back into the Citadel where Imperius makes her lair."
    print "She smiles, thanking you for your service, and you recive your next mission."
    print "You're heading to find the {}, and then the {}.".format(char['priorityone'], char['prioritytwo'])

##########################################################################################                    
def SecondPlanet(char):
    print
    print "You, {}, look around as the {} enters realspace.".format(char['name'], char['shipname'])
    print "Flashes of lightning flicker across the planets surface."
    print "The Dark side churns around this planet, and you feel yourself begin to seethe."
    LDNpoints(char, 0, 30, 10)
    print "Dromund Kaas air control waves you through, and you exit the {}." .format(char['shipname'])
    print "You must get through the wilds to get to Kaas City."
    print "However, you may stock up at the spaceport Hospital and Shops."
    spaceport = raw_input("Enter 1 to stick around the airport: ")
    if spaceport == '1':
        KaasPort(char)
    KaasWilds(char)
    KaasCity(char)
    KaasTemple(char)
    ChasingGhosts(char)
###############################################################

def LostTemple(char):
    print "A frozen tundra awaits you."
    print "........"
    print "You go to the *best* places."
    print "The map showed the way to the Temple of Filaro, Lord Ragnos's secret apprentice."
    print "But it also warns of swarms of massive Sithspawn."
    raw_input("Enter any key to continue: ")
    print "You trudge through snowdrifts, headed for the tomb."
    print "A massive Sithspawn bursts out of the snow ahead."
    print "It looks like a mutated Karshaa-wrym."
    if char['classname'] == 'Assassin':
        print "You use your skills as an Assassin to sneak past the beast, cloaked in the Force."
    if char['classname'] == 'Marauder':
        print "You race past the beast, using the inborn speed of the Marauder to race past."
    if char['classname'] == 'Juggernaut':
        print "You curse your inability for subterfuge and blinding speed."
        print "The Sithspawn roars, and you ready your blade for the fight."
        raw_input("Enter any key to continue: ")
        SithFight(char, 'Karshaa-wyrm Sithspawn', 1, 2275)
    print "You stalk into the cave."
    print "Set into the back of the cave is a doorway flanked by etheral red torches."
    print "...."
    raw_input("Enter any key to enter the cave: ")
    print "After exploring the cave, you discover the Ancient writings of Filaro."
    print "There's one that blinks onto the screen, seemingly left opened from the last reader:"
    print '''The Sith Code is applicable only to pursuits in life. It creates a society that continually strives for power, and when it gains that power,
it does not know what to do expcept keep struggling to attin more.

"Peace is a lie; there is only passion."

Peace is a lie only as long as the Sith Code is followed. It is possible to gain a sense of contentment in one's actions. However, this encourages complacency,
and therefore the Sith Code rules out contentment in order to get rid of any possibility of complacency in its Empire.

"Through passion, I gain strength.
Through strength, I gain power."

These are true, but they are only applicable to ambition. One may also find strength in purpose, which does not require passion. One may also find strength in peace,
but that is a trait ascribed to Jedi, whose strength is often denied or minimized throughout the Empire in order to dismiss the teachings of the Light.

However, when one is passionate about something they desire, that passion gives them strength to follow that passion. that strength turns them into a powerhouse, and the more
passion one has for a cause, the more power the cause gains.

"Through power, I gain victory."

This is true, and I cannot find fault with this line of the code. Someone who exemplifies weakness rarely attains anything in their life.

"Through victory, my chains are broken.
The Force shall free me."

These are flawed statements. The Sith Empire conditions its denizens to continually hunt for power and influence. Since they are continually  hunting,
this line turns into cahins around their neck. The Imperials are forced to continue hunting, while the Force bends them tihter to it through their deepening dependence
on the Force and their 'victories'.'''
    raw_input("Enter any key to continue: ")
    print "Among a dusty stack of holocrons, you find the coordinates."
    print "The blue glow of the holocron lights up the grin on your face."
    print "You exit the cave, heading into the Valley."

def ValleyOfTheDead(char):
    for steps in range(40):
        print "You've walked for {} minutes out of the 40 minute Valley hike.".format(steps)
        hahasucker = math.floor(random.random() * 100)
        if hahasucker > 90:
            print "A horde of Sithspawn lies in front of you."
            SithFight(char, 'Sithspawn', 7, 240)
        elif hahasucker > 60 and hahasucker < 90:
            print "One of the many animals in Ziost's Valley attacks, driven mad by the Dark Side imbuing the planet."
            AnimalAttack(char)
        elif hahasucker > 40 and hahasucker < 60:
            print "A few anceint war-droids attack you for trespassing on ancient lands."
            SithFight(char, 'Ancient War-Droid', 3, 110)
        elif hahasucker > 25 and hahasucker < 40:
            print "You travel on, unbothered."
        elif hahasucker > 15 and hahasucker < 25:
            print "Dead Sith warriors from ages past, resurrected by the Dark energy of the Valley, attack."
            SithFight(char, 'Sith Zombie', 5, 295)
        elif hahasucker > 5 and hahasucker < 15:
            print "A minefield lies in front of you."
            print "You may sneak around(1), Force jump and speed your way acoss(2), or use the Force to shake off the damage(3)."
            action = raw_input("Enter the number of your chosen action: ")
            if action == '1':
                if char['classname'] == 'Assassin':
                    print "You successfully sneak around!"
                elif char['classname'] == 'Marauder':
                    luck = random.random()
                    if luck > .5:
                        print "It's a close thing, but you successfully sneak around."
                    else:
                        print "You almost manage it, but Marauders aren't too brilliant at sneaking."
                        char['health'] = char['heatlh'] - 30
                        print "You lost 30 health to the minefield."
                else:
                    print "Juggernauts are in no way meant for sneaking."
                    char['health'] = char['heatlh'] - 40
                    print "You lost 40 health to the minefield."
            elif action == '2':
                if char['classname'] == 'Marauder':
                    print "You successfully leap around the minefield!"
                elif char['classname'] == 'Assassin':
                    luck = random.random()
                    if luck > .5:
                        print "It's a close thing, but you successfully leap around."
                        print "Maybe you shouldn't try to speed though next time."
                        print "Speed and jumping around aren't an Assassin's style."
                    else:
                        print "You almost manage it, but Assassins aren't meant for blatant speed and jumpiness."
                        char['health'] = char['heatlh'] - 20
                        print "You lost 20 health to the minefield."
                else:
                    print "Juggernauts aren't trained with speed in mind."
                    char['health'] = char['heatlh'] - 20
                    print "You lost 20 health to the minefield."
            else:
                if char['classname'] == 'Juggernaut':
                    print "Your skills as a Juggernaut let you shrug off the damage from the minefield."
                    print "Fierfek, but you're a better tank than tanks themselves."
                elif char['classname'] == 'Marauder':
                    luck = random.random()
                    if luck > .85:
                        print "It's a close thing, but you successfully walk through."
                    else:
                        print "You almost manage it, but Marauders aren't too brilliant at taking damage."
                        char['health'] = char['heatlh'] - 30
                        print "You lost 30 health to the minefield."
                else:
                    print "Assassins are in no way meant for taking damage."
                    char['health'] = char['heatlh'] - 30
                    print "You lost 30 health to the minefield."
        else:
            print "A Sithspawn, once a rancor, storms out of its cave, and attacks."
            SithFight(char, 'Sithspawn Rancor', 1, 1750)

def AncientArchives(char):
    print "You cautiously stride into the ancient Temple."
    print "You sneak through the halls till you enter the ancient archive. A holocron glows in the center."
    print "The Holocron is the control panel, and you grimace."
    print "In order to disable the defenses, you must be able to commune with the Holocron through the Force."
    print "So the stronger you are in the force, the more traps you'll be able to disable."
    traps = ['Poison Spikes', 'Rancor Pit', 'Ray Shields', 'Carbonite Chamber',
             'Electrified Hallway', 'Gas Mines', 'Floating Mines', 'Guardian Droid', 'Security Doors', 'Turrets']
    for thing in traps:
        print "Name of trap: {}."
    if char['lightside'] > 750 or char ['darkside'] > 750:
        print "You may disable 9 of the 10 traps in the Temple of the Blade."
        for trapnumber in range(9):
            disable = raw_input("Enter the name of the trap you wish to disable: ")
            if disable in traps:
                traps.remove(disable)
            else:
                disable = raw_input("Enter the name of the trap you wish to disable: ")
    elif char['lightside'] > 600 or char ['darkside'] > 600:
        print "You may disable 6 of the 10 traps in the Temple of the Blade."
        for trapnumber in range(6):
            disable = raw_input("Enter the name of the trap you wish to disable: ")
            if disable in traps:
                traps.remove(disable)
            else:
                disable = raw_input("Enter the name of the trap you wish to disable: ")
    elif char['lightside'] > 400 or char ['darkside'] > 400:
        print "You may disable 3 of the 10 traps in the Temple of the Blade."
        for trapnumber in range(3):
            disable = raw_input("Enter the name of the trap you wish to disable: ")
            if disable in traps:
                traps.remove(disable)
            else:
                disable = raw_input("Enter the name of the trap you wish to disable: ")
    elif char['lightside'] > 150 or char ['darkside'] > 150:
        print "You may disable 1 of the 10 traps in the Temple of the Blade."
        for trapnumber in range(1):
            disable = raw_input("Enter the name of the trap you wish to disable: ")
            if disable in traps:
                traps.remove(disable)
            else:
                disable = raw_input("Enter the name of the trap you wish to disable: ")
    return traps
    print "You disable as many traps as you can, and continue on."

def FindingTheBlade(traps, char):
    print "You stumble through the tomb."
    print "When you reach the final halllway, you grimace, knowing most of the traps are here."
    for item in traps:
        print "You fell victim to {}!".format(item)
        HealChoice(char)
        char['health'] = char['health'] - 10
        if char['health'] <= 0:
            print "Sorry, but you were killed by the traps."
            print "GAME OVER"
            quit()
    print "You finally stumble into the central chamber."
    print "You brush a sider out of your hair, and straighten your robes, attempting to look dignified."
    print "You step forward into the chamber, and quick suddenly, wish you hadn't."
    raw_input("Enter any key to continue: ")
    print "What was once the fiercest predator on Tatooine stands before you, fixing mechanical red eyes on you."
    print "A Sithspawn Krayt."
    print "You briefly consider demanding a raise plus even more hazard pay from Imperius."
    raw_input("Enter any key to start the fight.")
    SithFight(char, "Sithspawn Krayt", 1, 8000)
    print "Having got past the defenses, you step into the central chamber."
    print "You see a golden lightsaber hilt standing on the pedestal."
    print "You step forward, and activate the red-violet blade."
    print "You have found the Ancient Blade of Ragnos!"
    print "You now continue on to the next planet."

def Planet3A(char):
    LostTemple(char)
    ValleyOfTheDead(char)
    traps = AncientArchives(char)
    FindingTheBlade(char, traps)

##################################################################
def MandolorianClans(char):
    print "After jumping throug political loopholes and finally gaining access to the ruins, you head out."
    print "The ruins are surrounded by craters that have yet to be eroded by time."
    print "The planet here is scarred and deformed by war."
    print "A Mandolorian Clan, or aliit, has set up camp around the ruins."
    print "..."
    print "Of course, they have a bone to pick with Sith."
    print "Yeah, you're a little screwed, or so people say."
    print "You plan to provethem wrong."
    print "It's just another challenge, right?"
    print "...."
    print "You decide not to quit your day job to become a motivational speaker."
    print "You stare from your perch on a cliffside out at the ruins."
    raw_input("Enter any key to enter the camp: ")
    print "You sneak down what was once a small alley."
    print "Two guards are at the end of the alley ruins."
    if char['classname'] == 'Assassin':
        print "You slip past the guards, cloaking yourself in the Force."
        print "For good measure, you go ahead and pickpocket them."
        Credits(char, math.floor(random.random() * 1750))
    else:
        print "You bear down on them, sabers flashing."
        SithFight(char, "Mando'ad", 2, 350)
    print "You continue through, making your way to the city's ancient defense systems."
    print "A horde of Mando'ade have made this their home."
    print "..."
    print "Osik."
    raw_input("Enter any key to begin the fight: ")
    SithFight(char, "Mando'ad", 17, 550)
    print "You grimace."
    print "17 to 1 is bad odds on a brilliant day."
    print "Anyways. You were looking for that shab'la computer."
    print "You march into the ruins, trying in vain to brush blood off your clothes."
    print "..."
    print "You use the Force to blast through the collapsed walls."
    print "A Sith stands in front of the ancienct computer, downloading the data onto his Datapad."
    print "The white-skinned Chagrian turns to glare at you through golden eyes."
    print 'Of course, you decide to do something stupid.'
    print '''"I didn't know you Chagrians came in vanilla."'''
    raw_input("Enter ay key to deal with the fall-out: ")
    print "I am Lord Kyros, and you will treat me with respect, worm."
    print '''"Worm, really? Is that the best you can come up with, mir'osik?" You blurt out before you can stop yourself.'''
    print "You decide to blame it on the Dark side enrgies surrounding the ruins."
    print "Lord Kyros draws a golden doublebladed 'saber, and attack!"
    SithFight(char, 'Lord Kyros', 1, 1790)
    print "You stoop to grab the fallen datapad, marking the position of the ruins you'll need to go next."
    print "You head out, cheerfully looting the tomb of its relics on the way out, including some Jedi Holocrons."
    LDNpoints(char, 70, 20, 10)
    Credits(char, 5000)
    raw_input("Enter any key to continue: ")
    
def Ruins(char):
    print "You arrive at an abandoned space station."
    print "Ugh. Space suits always chafe."
    for steps in range(25):
        hahasucker = math.floor(random.random() * 100)
        if hahasucker > 90:
            print "Corroded wiring sparks, and shocks you, both literally and emotionally."
            char['health'] = char['health'] - 5
        elif hahasucker > 60 and hahasucker < 90:
            print "Floating mines, somehow still working, hang in the compartment before you."
            print "You may charge through absorbing damage, race through and try to outrun the blasts, or sneak through and avoid detection."
            act = raw_input("(1)Absorb the damage, (2) Outrun the blasts, (3)Sneak through: ")
            if act == '1':
                if char['classname'] == 'Juggernaut':
                    print "As a Juggernaut, unstoppable and firece, you make your way through in a blaze of epic glory."
                    print "You get nary a scratch."
                elif char['classname'] == 'Marauder':
                    print "Marauders aren't suited to taking damage, but you manage to avoid the worst of it with your inherent speed and reflexes."
                    char['health'] = char['health'] - 10
                else:
                    print "In no way are Assassins meant to try to tank."
                    char['health'] = char['health'] - 20
            elif act == '2':
                if char['classname'] == 'Marauder':
                    print "As a Marauder you are easily able to outrun the blasts."
                elif char['classname'] == 'Assassin':
                    print "You're not built for speed like a Marauder, but using the predatory quickness of an Assassin, you avoid the worst of it."
                    char['health'] = char['health'] - 10
                else:
                    print "It seems you have yet to come to terms with the fact that Juggernauts simply aren't meant for speed."
                    char['health'] = char['health'] - 20
            else:
                if char['classname'] == 'Assassin':
                    print "Of course, as an elite Assassin, you have no equal at sneaking."
                    print "You dance through the minefield with ease borne of practice, and then scamper on."
                elif char['classname'] == 'Marauder':
                    print "You don't normally do subtle, so you accidentally set off one of the mines."
                    print "You make your way through the rest, mostly unharmed, which have to admit was more likely due to luck than any sort of skill."
                    char['health'] = char['health'] - 10
                else:
                    print "Juggernauts don't do sneaky."
                    print "..."
                    print "At all."
                    char['health'] = char['health'] - 20
        elif hahasucker > 40 and hahasucker < 60:
            print "You get stuck trying to wiggle through the ducts."
            print "after some manuvering, you manage to get through, but not without some scrapes."
            char['health'] = char['health'] - 5
        elif hahasucker > 25 and hahasucker < 40:
            print "You found a stash of holocrons!"
            LDNpoints(char, 30, 30, 30)
        elif hahasucker > 15 and hahasucker < 25:
            print "You stumble into a storage room, and take the time to rest and heal."
            char['health'] = char['maxhealth']
        elif hahasucker > 5 and hahasucker < 15:
            print "You found a small stash of credits!"
            char['credit'] = char['credit'] + math.floor(random.random() * 250)
        else:
            print "A flock of mynocks shriek at you, flapping around your head as you franntically try to beat them away."
            print "At least the the only damage is to your pride, but you have a feeling that your pride has been in short supply lately anyway."
        raw_input("Enter any key to continue: ")
    print "You finally find the last trajectory of Adega's ship."
    print "You sit down, really wishing you hadn't played hooky so much dring your math classes."
    print "After a few hours of mental torment, you finally have a destination."
    raw_input("Enter any key to set out: ")
    
def Holocron(char):
    print "You head to the crash site, grimacing."
    print "What an ignomious way to die for a rather brilliant Sith lord."
    print "You guess it's better than tripping on a rock and accidentally impaling yourlef, like old Darth Riika."
    print "You make your way through the planet's wilds towards the crash site."
    print "Darth Acina sent troops to find the holocron."
    print "You may bribe them to leave if you have enough credits, promise to help Acina, or kill them to ensure Acina gets the message."
    action = raw_input("(1)Bribe, (2)Ally, or (3)Kill: ")
    if action == '1':
        if char['credit'] < 2500:
            print "You don't have enough credits to bribe them."
            print "Insulted that you would attempt to sway their loyalties with such a paltry sum, the troops attack you."
            SithFight(char, "Acina Solder", 15, 1000)
        else:
            print "You manage to bribe them away, grimacing at your lighter money pouch."
    elif action =='2':
        LDNpoints(char, 0, 150, 0)
        print "Treachery is the way of the Sith, and you are no different."
        print "Acina promises power, and asks you to act as her own agent from within Imperius's operations."
    else:
        print "You attack the troops!"
        LDNpoints(char, 30, 0, 40)
        SithFight(char, "Acina Solder", 15, 1000)
    print "After searching the wreckage, you unearth the Holocron."
    print "It's a mix of a Jedi and Sith holocron, a blue pyramid, swirling Light and Dark in the Force."
    print "You activate it cautiosly."
    print "Adega appears, and offers you knowledge: good or evil."
    force = raw_input("Enter 1 to gain the light side knowledge, 2 for dark, and 3 for neutral: ")
    if force == '1':
        print "You choose the light side knowledge."
        LDNpoints(char, 900, 0, 0)
        print "There is no ignorance, there is knowledge."
    elif force == '2':
        print "You choose the Dark Side knowledge."
        LDNpoints(char, 0, 900, 0)
        print "Remember, knowledge is power, and power is victory."
    else:
        print "You choose the Neutral Side."
        LDNpoints(char, 0, 0, 1200)
        print "The Force is neither good no evil; the user makes it so."
    print "You sigh, stretching your weary muscles."
    print "Time to head to Lola Sayu -- No rest for the wicked."
    raw_input("Enter any key to leave Raxus Prime: ")

def Planet3B(char):
    MandolorianClans(char)
    Ruins(char)
    Holocron(char)
 
def GettingEntrance(char):
    if char['classname'] == 'Marauder':
        print "You sweep past the guards, striding towards the heart of the facility."
        print "They hurry, yelling at you, but failing to keep up with the quick strides of a Marauder."
        print "The doors to the command center sweep open, and you stalk in."
        print "You eye the unprepared staff imperiously."
        print '''"How do you propose to keep your guests here if your pathetic worm-ridden guards cannot keep me out?" You're quite proud of yourself;
the staff is suitably cowed, and you did not have to do much.

"My lord," Commander Leng begins, "We did not expect you to arrive here so quickly. We have had a recent influx of traitors from all over the Empire.
We have devoted more resources to holding prisoners than to creating a suitable welcome."

You nod, looking suitably cold and emotionless. You deal with the expected formalities, gaining access."

You enter the room given to you for your stay, staring out the window accross the barren landscape, readying yourself for the next phase of your mission.'''
    elif char['classname'] == 'Juggernaut':
        print "You pretty much walk through the guards, forcing them around you."
        print "Your broad shoulders are an asset here, as you easily bully your way through the prison to the Command Center."
        print "The indomitable presensce of a Juggernaut is enough to quiet the officers without a spoken word by you."
        print "You let your eyes glow the yellow-gold of a Sith, and fear coils through the Command Center."
        print '''"If you want to show me to my rooms, now would be the time," you announce. Your mission begins tomorrow.'''
        
    else:
        print "You materialize in the command center, cheerfully scaring the lviing daylights of the unlucky officer you decided to reappear next to."
        print '"Your security is lacking," you announce, a smirk playing accross your features.'
        print "The officers scowl at each other, before remembering they are, in fact int eh presence of a Sith."
        print "You're shown to your quarters, where you meditate, prepping for your next mission."
def ImperialSecrets(char):
    prisoners = ["Connrad Vern'ner", "Kayli Ishta", "Ravo Sorkin", "Garrus Zorah", "Tiberius Spock", "Jayms Kirrk", "Alle'son Errnhart", "Audrii Luuwis",
                 "Ky'nesi Wintare", "Vertucci", "Isaa Swann", "Ton'ni Staark", "Captain Zeve Rog'gers", "Ashara Zavros", "Ely'saa Shuur",
                 "Xander Velocin"]
    print "Imperius has asked you to free Ashara Zavros."
    print "You make your way to the Command Center, going through the list of prisoners, and issuing their fate."
    for prisoner in prisoners:
        print "Prisoner: {}".format(prisoner)
        if prisoner == "Ashara Zavros":
            print "This is the Togruta Jedi you were told to free. You can feel her presence, a bright shining light in the darkness of the Citadel."
        else:
            print "Prisoner", prisoner
            jury = raw_input("Execute(1), Torture(2), or Release(3): ")
            if jury == '1':
                prisoners.remove(prisoner)
                print "You issue the order to execute", prisoner + '.'
                LDNpoints(char, 0, 20, 20)
            elif jury == '2':
                print "You issue the order to continue torture of", prisoner + '.'
                LDNpoints(char, 0, 40, 0)
            elif jury == '3':
                print "You order {} released.".format(prisoner)
                prisoners.remove(prisoner)
            else:
                print "By default, the prisoner will be executed for their crimes against the Empire."
    print "Having found Ashara, you head down to break her out."
    print "The Togruta is bruised, but her spirit is clearly intact."
    print "You stalk in as she tells the guard what he should do with a blaster, an akul, a Hutt, a B'omarr monk, and a speeder, and you're impressed by her rather explicit attention to detail."
    print "You slam your saber into the guard, wiping the shocked look off his face."
    for rooms in range(10):
        guards = math.floor(random.random() * 17)
        print "You find {} guards in the room.".format(guards)
        for p in prisoners:
            if random.random() > .35:
                print "{} defeats one of the guards!".format(p)
                guards = guards - 1
            else:
                print "{} is killed by one of the guards.".format(p)
                prisoners.remove(p)
        print "There's {} guards left.".format(guards)
        SithFight(char, "Citadel Guard", guards, 1000)
    print "After making your way through the fortress, you and Ashara flee in the {}.".format(char['shipname'])
    print "As you head to Dromund Kaas, Ashara grimaces."
    print "You feel it too."
    print "The Force is boiling. A strom is coming, and you're flying into the heartt of it."
    print '"It is only going to get worse," the Togruta murmurs, her expression guarded.'
    print '"I can handle it," you reply confidently.'
    print "That doeesn't chane the fact that you're prepared for the hardest fight of your life."
                    
def Planet4(char):
    GettingEntrance(char)
    ImperialSecrets(char)

def ConfrontingImperius(char):
    print '"Why?!?!" Your voice thunders through the Citadel. "I nearly got killed for these relics, and made an enemy of the Empire as well!"'
    print '''Imperius raises a gloved hand, and you snap your jaw shut. The Twi'lek is still a formidable woman, even with the power
you gained finding the Blade and holocron. "You met Darth Acina." Her voice rumbles with anger, her statement slicing through the air."

You nod, feeling the Force twisting through the office at Imperius's agitation. Then, she sighs. "I suppose you have a right to know. You are
my most trusted servant."

She takes a deep breath, standing up and moving towards the holomap on her wall of the Empire. "The Empire needs to change. No longer can we ignore the downtrodden,
the weak, and the small. It's not the way of the Sith, I know, and more the stance of a Light Sider than a Dark Sider, but that does not change the truth.
The Empire was founded in blood and in blood it shall die, unless we take control, and set it on a gentler, kinder path." There's passion in her eyes. Clearly,
this has been a project of hers for quite a while.

You gasp "You mean to overthrow the Emporer himself."

The Twi'lek nods. "Acina and I are working together to destroy him and the rest of the Dark Council, but I'm no fool-- She will betray me. She is a traditionalist,
holding old values, while I seek to move the Empire out of the Dark Ages the Sith Order has kept it in."

"But you seek to betray her as well."

"Kill, or be killed. But make sure your killing is due to a cause greater than yourself. That is the advice my mother gave me before I was
ripped from her arms to join the Sith Order. It has served me well."

"What happened to her?" You can't help but ask, from a morbid sense of curiosity.

"She died from disease in the slave camps before I was able to buy her freedom."

You nod, platitudes clearly unwelcome. "Her death gave you strength."

The Sith nods, lost in thought. You wait a while more, and then turn to leave. This meeting is clearly over.'''

def UndeadArmy(char):
    print "Outside of the citadel, away from Imperius' calm glacier-like Dark presence, the Force is a raging maelstrom."
    print "Out of the corner of your eye, you think you see a blue shimmer, but when you turn there's nothing."
    print "Shrugging you continue towards your apartment."
    print "You think you hear a whisper in the breeze, and turn around before you step into you're appointment."
    print '"{}....The time has come... Free us... {}..." A red fog hangs in the air, then fades away.'.format(char['name'], char['name'])
    print "You lock the doors behind you, activating security systems you enver have before."
    raw_input("Enter any key to continue: ")
    print "You wake up to see a ghost hovering above you, hate in it's frightful visage."
    print "You swear a blue streak, pushing out the Force in an effort to blast it back."
    print "It barely moves, floating towards you with hands outstretched."
    print "You race out of your home, grabbing backpacks full of supplies as you race out the door."
    print "To your horror, more ghosts float around Kaas City. You can hear the screams of its citizens filling the morning air."
    print "You race towards the Citadel. Surely, there's something there that can help."
    for steps in range(40):
        luck = random.random() * 100
        if luck > 70:
            print "A ghost appears in front of you, snarling."
            print "You swear a blue streak, and race away."
        elif luck < 70 and luck > 40:
            print "You're not getting away from this one."
            if char['lightside'] / 10 > 75 or char['darkside'] / 10 > 75:
                print "You blast the ghost away, and keep running."
            else:
                print "It claws at you through the Force, and you take 10 damage."
                char['health'] = char['health'] - 10
        elif luck < 40:
            print "You keep going without running into any more spectres."
        raw_input("Enter any key to continue: ")
    print "You step into the Citadel, and one of Imperius uards waves you over, clearly waiting for you."
    print '''"Imperius and Acina are fighting! Here, take this, it'll help with the ghosts." The Chiss hands you a pyramid, and the Force seems to contract around you
as you grab it. You nod your thanks and take off towards the plaza, the center of the disturbance.'''
    for steps in range(40):
        luck = random.random() * 100
        if luck > 70:
            print "A ghost appears in front of you, snarling."
            print "You swear a blue streak, and race away."
        elif luck < 70 and luck > 40:
            print "You're not getting away from this one."
            if char['lightside'] / 10 > 75 or char['darkside'] / 10 > 75:
                print "You blast the ghost away, and keep running."
            else:
                print "It claws at you through the Force, and you take 10 damage."
                char['health'] = char['health'] - 10
                SithFight(char, "Ghost", 1, 1500)
        elif luck < 40 and luck > 20:
            print "You keep going without running into any more spectres."
        else:
            print "You sneak up on a ghost, attacking it from behind."
            SithFight(char, "Unwary Ghost", 1, 1200)
        raw_input("Enter any key to continue: ")
    print "You near the entrance of the plaza, and stop to take a breath."
    char['health'] = char['maxhealth']
    
def FinalBattle(char):
    print "You sprint into Kaas Square. The town is abandoned, lightning raging around as the Force screams around the former bastion of Sith glory."
    print "The Sith Sanctum is shrouded in darkness, the Force Storms generated by the two Darths blocking out the sun completely."
    print "In the Square, you see two figures staring at each other across the plaza."
    print "A Twi'lek and a brunette cyborg, assassin and marauder, radical and traditionalist, Light and Dark."
    print "This fight determines the path of the Empire."
    print "The two are equally matched, the two most powerful Dark Lords of the century, maybe even the millenium."
    print "As you race towards them, you see the bodies of Ravage and Marr, twisted by Force and lightsaber attacks."
    raw_input("Enter any key to continue to the final battle: ")
    print "You have the choice to side with either Dark Lord:"
    print "Imperius (1) or Acina (2):"
    loyal = raw_input("Enter the number of the Dark Lord you wish to side with: ")
    if loyal == '1':
        print "You hurl a blast of Dark energy at Darth Acina, catching he off balance."
        print "However, the impact barely fazes her."
        print "She sneers at you, and the fight begins."
        print "For this fight, using the Light side will return health to you, while using the dark side will drain life to increase your attacks."
        print "Their alignment will be marked next to the name of the attack."
        AcinaHealth = 10000
        while AcinaHealth >= 0:
            print "It's your turn to attack!"
            print "You may use a Telekinetic(1), Blade(2), or Stealth(3), or Lightning Attack(4)!"
            attackchoice = raw_input("Choose the type of attack you wish to use: ")
            if attackchoice == '1':
                print "You may use a Force Wave(LS)(1) or a Force Choke(DS)(2)."
                spec = raw_input("Enter the number of the power you wish to use: ")
                if spec == '1':
                    print "You unleash a massive Force Wave at Acina. It knocks her off her feet."
                    if random.random() > .70:
                        print "Darth Imperius slashes at Acina, using your attacks to bolster her own."
                        AcinaHealth = AcinaHealth - 150
                        char['health'] = char['health'] + 15
                    else:
                        print "She snarls, using the Force to leap back up, although she's moving more gingerly than before..."
                        AcinaHealth = AcinaHealth - 100
                    char['health'] = char['health'] + 15
                elif spec == '2':
                    print "You choke Acina, lifting th brunette up off her feet, seizing her throat and cutting her off from oxygen."
                    char['health'] = char['health'] -15
                    print "You drain your own life to power your attack."
                    AcinaHealth = AcinaHealth - 300
                    if char['classname'] == 'Juggernaut':
                        AcinaHealth = AcinaHealth - 100
            elif attackchoice == '2':
                print "You may use Blade Storm(NS)(1), Valiant Charge(LS)(2), or Crazed Flurry(DS)(3)."
                spec = raw_input("Enter the number of the attack you wish to use: ")
                if spec == '1':
                    print "You storm through Acina's defenses, parrying attacks, and slicing at the Sith."
                    print "She falls back, and you slash at her side, striking the enraged Lord."
                    AcinaHealth = AcinaHealth - 300
                    if char['classname'] == 'Juggernaut':
                        print "As a Juggernaut, your attack is even more destructive."
                        AcinaHealth = AcinaHealth - 50
                elif spec == '2':
                    print "You leap forwards, using the Light Side of the Force to bolster your strike."
                    AcinaHealth = AcinaHealth - 250
                    if char['classname'] == 'Marauder':
                        print "Utilizing your skills as a Marauder, you sweep your blade forwards to strike the Dark Lord."
                        AcinaHealth = AcinaHealth - 70
                elif spec == '3':
                    print "In a maddened Dark frenzy, you strike at Acina."
                    print "She falls back under the strength of her blows."
                    char['health'] = char['health'] - 15
                    print "You drain your own life to power your attack."
                    AcinaHealth = AcinaHealth - 400
            elif attackchoice == '3':
                print "You may use Assassinate(DS)(1), Hand of Justice(LS)(2), or Mind Crush(DS)(3)."
                spec = raw_input("Enter the number of the power you wish to use: ")
                if char['classname'] == 'Assassin':
                    AcinaHealth = AcinaHealth - 100
                if spec == '1':
                    print "You slip into the Force, turning inot a living shadow, and sneak behind Acina."
                    print "You strike, catching her off guard, and dealing massive damage, but at great cost to yourself."
                    char['health'] = char['health'] - 50
                    AcinaHealth = AcinaHealth - 750
                elif spec == '2':
                    print "You warp reality around you, slipping behind the Dark Lord."
                    print "You turn the Light Side into a weapon, meant to strike down the festering Darkness you face."
                    AcinaHealth = AcinaHealth - 300
                    char['health'] = char['health'] + 30
                elif spec == '3':
                    print "You reach out with the Force, smashing through her mental defenses, safe from any backlash in a hidden perch"
                    print "Unfortunately, you're straining yourself to do this."
                    AcinaHealth = AcinaHealth - 350
                    char['health'] = char['health'] - 20
            elif attackchoice == '4':
                print "You may use Force Storm(DS)(1), Shock(NS)(2), or Disabling Strike(LS)(3)."
                spec = raw_input("Enter the number of the power you wish to use: ")
                if char['classname'] == 'Marauder':
                    AcinaHealth = AcinaHealth - 75
                if spec == '1':
                    print "You reach deep into the Dark Side, fueling a massive Force Storm."
                    print "While it knocks back Acina, dealing massive damage, you must drain your own strength to fuel the maelstrom."
                    char['health'] = char['health'] - 50
                    AcinaHealth = AcinaHealth - 1000
                elif spec == '2':
                    print "You send a burst of electricity towards Acina."
                    print "It knocks her back, and she hisses in a frenzied rage."
                    AcinaHealth = AcinaHealth - 250
                    if char['classname'] == 'Assassin':
                        AcinaHealth = AcinaHealth - 150
                elif spec == '3':
                    if char['classname'] == 'Juggernaut':
                        AcinaHealth = AcinaHealth - 50
                    print "You send a surge of ions through the atmosphere, knocking Acina down and stunning her, allowing Imperius room to manuver and strike."
                    ImperiusDam = math.floor(random.random() * 175) + 175
                    AcinaHealth = AcinaHealth - (100 + ImperiusDam)
                    print "Imperius strikes her for {} health.".format(ImperiusDam)
            print "You now have {} health.".format(char['health'])
            print "Imperius attacks!"
            Imp = math.floor(random.random() * 200) + 200
            print "She srikes for {} damage.".format(Imp)
            AcinaHealth = AcinaHealth - Imp
            print "Darth Acina now has {} health.".format(AcinaHealth)
            HealChoice(char)
            print "Acina strikes out."
            Acina = math.floor(random.random() * 200) + 100
            print "You lose {} health.".format(Acina)
            char['health'] = char['health'] - Acina
            if char['health'] <= 0:
                print "You've been struck down by Acina."
                print "GAME OVER"
                quit()
            HealChoice(char)
        print "The Light Side shivers in joy and relief as Acina breathes her last."
        print "Imperius grins, slapping your shoulder good naturedly."
        print "The Empire will enter a Golden Age with Empress Imperius at its helm."
        print "Her loyal friend, you help rule on her council of advisors."
        print "Once more the Sith rule the galaxy... And there is peace."
    if loyal == '2':
        print "You sling your blade at Imperius."
        print "The Twi'lek snarls in shock, her lekku twisting in rage."
        print "But then she unleashes a blast of energy, throwing you back onto the ground, and slamming Acina back several meters."
        print '"Treachery, {}?" The purple blades in her hands flicker with electricity, and you prepare for the hardest fight of your life.'.format(char['name'])
        print "During this fight, using Dark Abilities will drain health from Imperius to heal you, on top of normal damage."
        print "You may use a Telekinetic(1), Blade(2), or Stealth(3), or Lightning Attack(4)!"
        ImperiusHealth = 15000
        while ImperiusHealth <= 0:
            attackchoice = raw_input("Choose the type of attack you wish to use: ")
            if attackchoice == '1':
                print "You may use a Force Slam(DS)(1) or a Force Choke(DS)(2)."
                spec = raw_input("Enter the number of the power you wish to use: ")
                if spec == '1':
                    print "You slam Imperius to the ground, wounding her greatly."
                    print "At the same time, you drain life from the Twi'lek."
                    ImperiusHealth = ImperiusHealth - 500
                    char['health'] = char['health'] + 50
                elif spec == '2':
                    print "You grip Imperius's neck with the Force, choking the life out of her, and fueling your strength in the Dark Side."
                    ImperiusHealth = ImperiusHealth - 100
                    char['health'] = char['health'] + 60
            elif attackchoice == '2':
                print "You may use Blade Storm(NS)(1) or Crazed Flurry(DS)(2)."
                spec = raw_input("Enter the number of the attack you wish to use: ")
                if spec == '1':
                    print "You lash out with your blade, striking everywhere you see an opening."
                    ImperiusHealth = ImperiusHealth - 250
                elif spec == '2':
                    print "You let the Dark Side fuel a crazed flurry of slashes."
                    ImperiusHealth = ImperiusHealth - 300
                    char['health'] = char['health'] + 20
            elif attackchoice == '3':
                print "You may use Assassinate(DS), Sudden Strike(NS), or Mind Crush(DS)."
                spec = raw_input("Enter the number of the power you wish to use: ")
                if char['classname'] == 'Assassin':
                    AcinaHealth = AcinaHealth - 100
                if spec == '1':
                    print "You slip into the Force, turning inot a living shadow, and sneak behind Imperius."
                    print "You strike, catching her off guard, and dealing massive damage."
                    char['health'] = char['health'] + 50
                    ImperiusHealth = ImperiusHealth - 750
                elif spec == '2':
                    print "You warp reality around you, slipping behind the Dark Lord."
                    print "You turn the force into a weapon, meant to strike down the Twi'lek you face."
                    ImperiusHealth = ImperiusHealth - 300
                elif spec == '3':
                    print "You reach out with the Force, smashing through her mental defenses, safe from any backlash in a hidden perch"
                    print "You gain a sense of euphoria as the Dark Side surges around you."
                    ImperiusHealth = ImperiusHealth - 350
                    char['health'] = char['health'] + 20
            elif attackchoice == '4':
                print "You may use Force Storm(DS), Shock(NS), or Elecrocute(DS)."
                spec = raw_input("Enter the number of the power you wish to use: ")
                if char['classname'] == 'Marauder':
                    ImperiusHealth = ImperiusHealth - 75
                if spec == '1':
                    print "You reach deep into the Dark Side, fueling a massive Force Storm."
                    print "While it knocks back Imperius, dealing massive damage, you gain strength from the maelstrom."
                    char['health'] = char['health'] + 50
                    ImperiusHealth = ImperiusHealth - 1000
                elif spec == '2':
                    print "You send a burst of electricity towards Imperius."
                    print "It knocks her back, and she hisses in a frenzied rage."
                    ImperiusHealth = ImperiusHealth - 250
                    if char['classname'] == 'Assassin':
                        ImperiusHealth = ImperiusHealth - 150
                elif spec == '3':
                    if char['classname'] == 'Juggernaut':
                        ImperiusHealth = ImperiusHealth - 50
                    print "You electrocute the tw'lek, knocking Imperius down and stunning her, allowing Acina room to manuver and strike."
                    ImperiusDam = math.floor(random.random() * 175) + 175
                    ImperiusHealth = ImperiusHealth - (100 + ImperiusDam)
                    print "Acina strikes her for {} health.".format(ImperiusDam)
                print "You now have {} health.".format(char['health'])
            print "Acina attacks!"
            Imp = math.floor(random.random() * 200) + 200
            print "She srikes for {} damage.".format(Imp)
            ImperiusHealth = ImperiusHealth - Imp
            print "Darth Imperius now has {} health.".format(AcinaHealth)
            HealChoice(char)
            print "Imperius strikes out."
            Acina = math.floor(random.random() * 200) + 100
            print "You lose {} health.".format(Acina)
            char['health'] = char['health'] - Acina
            if char['health'] <= 0:
                print "You've been struck down by Imperius."
                print "GAME OVER"
                quit()
        print "You stare down at the Twi'lek's mutilated body."
        print "She seemed much larger in life."
        print "You feel the Dark Side of the Force strengthen and it almost feels... pleased."
        print "The Empire is now under the Rule of Empress Acina and Dark Lord {}".format(char['name'])
        print "The Dark always wins."
    
    
def Planet5(char):
    ConfrontingImperius(char)
    UndeadArmy(char)
    FinalBattle(char)
                    
def main():
    FirstPlanet()
    print "Moving on, you level up!"
    char['maxhealth'] = char['maxhealth'] + 50
    char['health'] = char['maxhealth']
    char['medpacs'] = char['medpacs'] + 20
    LDNpoints(char, 40, 40, 40)
    char['damage'] = char['damage'] + 50
    char['credit'] = char['credit'] + 1500
    raw_input("Enter any key to continue: ")
    SecondPlanet(char)
    print "Moving on, you level up!"
    char['maxhealth'] = char['maxhealth'] + 50
    char['health'] = char['maxhealth']
    char['medpacs'] = char['medpacs'] + 20
    LDNpoints(char, 40, 40, 40)
    char['damage'] = char['damage'] + 50
    char['credit'] = char['credit'] + 1500
    raw_input("Enter any key to continue: ")
    Planet3A(char)
    print "Moving on, you level up!"
    char['maxhealth'] = char['maxhealth'] + 50
    char['health'] = char['maxhealth']
    char['medpacs'] = char['medpacs'] + 20
    LDNpoints(char, 40, 40, 40)
    char['damage'] = char['damage'] + 50
    char['credit'] = char['credit'] + 1500
    raw_input("Enter any key to continue: ")
    Planet3B(char)
    print "Moving on, you level up!"
    char['maxhealth'] = char['maxhealth'] + 50
    char['health'] = char['maxhealth']
    char['medpacs'] = char['medpacs'] + 20
    LDNpoints(char, 40, 40, 40)
    char['damage'] = char['damage'] + 50
    char['credit'] = char['credit'] + 1500
    raw_input("Enter any key to continue: ")
    Planet4(char)
    print "Moving on, you level up!"
    char['maxhealth'] = char['maxhealth'] + 50
    char['health'] = char['maxhealth']
    char['medpacs'] = char['medpacs'] + 20
    LDNpoints(char, 40, 40, 40)
    char['damage'] = char['damage'] + 50
    char['credit'] = char['credit'] + 1500
    raw_input("Enter any key to continue: ")
    Planet5(char)
    print "GAME OVER."

main()
