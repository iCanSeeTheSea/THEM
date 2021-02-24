# APOCALYPSE: World Go Boom  - THEM vA0.1

# Copyright (C) 2021


def apocalypse_world_go_boom(): 
    import time
    from random import randint
    # introduction
    print(''); time.sleep(1)
    print(''); time.sleep(1)
    print('it was a dark and stormy night...'); print(''); time.sleep(2)
    print('...the waves crashed against the rocks...'); print(''); time.sleep(2)
    print('...we had no notice...'); print(''); time.sleep(2)
    print('...apart from the signs we all chose to ignore...'); print(''); time.sleep(2)
    print('...the storms...'); print(''); time.sleep(2)
    print('...the fires...'); print(''); time.sleep(2)
    print('...'); print(''); time.sleep(2)
    print('...'); print(''); time.sleep(2)
    print('...the virus...'); print(''); time.sleep(2)
    print('...'); print(''); time.sleep(2)
    print('...noone knew what was happening...'); print(''); time.sleep(2)
    print('...untill it was too late...'); print(''); time.sleep(2)

    for i in range(5):
        print('...'); time.sleep(0.5); print('')
    print('WELCOME TO:'); time.sleep(0.5)
    print('''
                               ________________
                          ____/ (  (    )   )  \___
                         /( (  (  )   _    ))  )   )\\
                       ((     (   )(    )  )   (   )  )
                     ((/  ( _(   )   (   _) ) (  () )  )
                    ( (  ( (_)   ((    (   )  .((_ ) .  )_
                   ( (  )    (      (  )    )   ) . ) (   )
                  (  (   (  (   ) (  _  ( _) ).  ) . ) ) ( )
                  ( (  (   ) (  )   (  ))     ) _)(   )  )  )
                 ( (  ( \ ) (    (_  ( ) ( )  )   ) )  )) ( )
                  (  (   (  (   (_ ( ) ( _    )  ) (  )  )   )
                 ( (  ( (  (  )     (_  )  ) )  _)   ) _( ( )
                  ((  (   )(    (     _    )   _) _(_ (  (_ )
                   (_((__(_(__(( ( ( |  ) ) ) )_))__))_)___)
                   ((__)        \\\\||lll|l||///          \_))
                                /(/ (  )  ) )\   
                               ( ( ( | | ) ) )\   
                               /(| / ( )) ) ) )) 
                               ( ((((_(|)_)))))     
                                 ||\(|(|)|/||     
                                 |(||(||)||||        
                                //|/l|||)|\\\\ \     
                         / / //  /|//||||\\\\  \ \  \ _
--------------------------APOCALYPSE: WORLD GO BOOM--------------------------
    '''); print(''); time.sleep(2)
        
    character_health = 0
    chracter_speed = 0
    character_hunger = 0
    character_attack = 0

    print('''
 ------------------------------------------
 --- CHARACTER TYPES:                   ---   
 ---                                    ---
 --- (health, speed, hunger, attack)    ---
 ---                                    ---
 --- Hunter(h): 10, 20, 15, 15          ---
 --- Archer(a): 15, 15, 10, 20          ---
 --- Soldier(s): 20, 10, 10, 20         ---
 ---                                    ---
 ------------------------------------------
    
    '''); print(''); time.sleep(3)
    turn = ''

    while True: 
        character_select = input('please choose a character: '); print(''); time.sleep(1)
        print('you have chosen...'); print(''); time.sleep(1)

        # hunter character
        if character_select == 'h':
            print('hunter!'); print(''); time.sleep(1)
            # sets attributes
            character_health = 10
            character_speed = 20
            character_hunger = 15
            character_attack = 15
            max_health = 10
            max_speed = 20
            max_hunger = 15
            max_attack = 15
            weapon = 'shotgun'
            turn = 'h'
            break
        
        # archer character
        elif character_select == 'a':
            print('archer!'); print(''); time.sleep(1)
            # sets attributes
            character_health = 15
            character_speed = 15
            character_hunger = 10
            character_attack = 20
            max_health = 15
            max_speed = 15
            max_hunger = 10
            max_attack = 20
            weapon = 'bow'
            turn = 'a'
            break
        
        # soldier character
        elif character_select == 's':
            print('soldier!'); print(''); time.sleep(1)
            # sets attributes
            character_health = 20
            character_speed = 10
            character_hunger = 10
            character_attack = 20
            max_health = 20
            max_speed = 10
            max_hunger = 10
            max_attack = 20
            weapon = 'rilfe'
            turn = 's'
            break
    
        else:
            print('... that\'s not a valid character. please @me in the games channel if you have an idea for one.'); print(''); time.sleep(3)


    

    inventory = []
    inventory.append(weapon)

    # starting stats
    print(f'health: {character_health}, speed: {character_speed}, hunger: {character_hunger}, attack: {character_attack}, inventory: {inventory}'); print(''); time.sleep(1)

    # setting scene to their abreviations 
    places = {'h': 'hunting cabin      ', 'a': 'tree house         ', 's': 'barracks           ','w': 'woods              ', 'ci': 'city               ', 'sr': 'shooting range     ', 'mh': 'mess hall          ', 'av': 'abandoned village  ', 'rp': 'radioactive plains ',
    'hd': 'halls of death     ', 'wh': 'witch\'s hut        ', 'ca': 'castle             ', 'd': 'desert             ', 'dt': 'temple             ', 'dtw': 'temple              ', 'd2': 'desert             ', 'F': 'FINISH!            ', 'ae': 'secret ending      '}
    place = places[turn]
    turn_count = 1

    # introduction sequence
    print(f'you wake up in your {place}, well rested and fed.'); print(''); time.sleep(1)
    print('you can\'t quite remember what heppend last night, or how you got home'); print(''); time.sleep(1)
    print('anyways, it\'s time for a new adventure!'); print(''); time.sleep(1)

    
    # main game loop
    while character_health > 0: 
        # keeps track of the turn
        place = places[turn]

        print(f'''
-----------------------------------------  
--- you are at the {place}---
---                                   ---
--- options:                          ---
--- forage: f                         ---
--- eat: e                            ---
--- rest: r                           ---
--- continue: c                       ---
---                                   ---
-----------------------------------------      
        '''); print(''); time.sleep(2)

        # start of turn stats
        print(f'start of turn {turn_count}. health: {character_health}, speed: {character_speed}, hunger: {character_hunger}, attack: {character_attack}, inventory: {inventory}'); print(''); time.sleep(2)
        action = input('what would you like to do? '); print(''); time.sleep(1)

        # lets player find food
        if action == 'f':
            forage = randint(1,4)
            if forage == 1:
                # food added to inventory if found
                print('you found food!'); print(''); time.sleep(1)
                inventory.append('food')
            else:
                print('you didnt find anything'); print(''); time.sleep(1)

        # lets player gain hunger
        elif action == 'e':
            # 1 to 3 hunger is added (if possible), and one 'food' is used
            if 'food' in inventory and character_hunger < max_hunger:
                eat = randint(1, 3)
                character_hunger += eat
                if character_hunger > max_hunger:
                    character_hunger = max_hunger
                inventory.remove('food')
                print(f'you gained {eat} hunger'); print(''); time.sleep(1)
            elif 'food' not in inventory:
                print('you have no food'); print(''); time.sleep(1)
            elif character_hunger == max_hunger:
                print('you are not hungry'); print(''); time.sleep(1)

        # lets player gain speed
        elif action == 'r':
            # 1 to 4 speed is added (if possible)
            if character_speed < max_speed:
                rest = randint(1, 4)
                character_speed += rest
                if character_speed > max_speed:
                    character_speed = max_speed
                print(f'you gained {rest} speed'); print(''); time.sleep(1)
            elif character_speed == max_speed:
                print('you are not tired'); print(''); time.sleep(1)

        # lets player continue story
        elif action == 'c':

            if turn == 'h':
                # hunter starts in the hunting cabin
                turn = input(' you can to go the woods(w), or the city(ci)'); print(''); time.sleep(1)

            elif turn == 'a':
                # archer starts in the tree house
                turn = input('you can go to the city(ci) or the shooting range(sr)'); print(''); time.sleep(1)

            elif turn == 's':
                # soldier starts in the barracks
                turn = input('you can go to the shooting range(sr) or the mess hall(mh)'); print(''); time.sleep(1)

            # woods
            elif turn == 'w':
                print('you are hunkered down in a shrub, looking out for any animal to cross your path'); print(''); time.sleep(1)
                print(f'you see movement from behind one of the trees and swing your {weapon} round to look'); print(''); time.sleep(1)
                print('but...'); print(''); time.sleep(1)
                print('...thats not a deer...'); print(''); time.sleep(1)
                print('its a car. but, there are no cars anymore...'); print(''); time.sleep(1)
                # 1 to 5 food chance from deer
                hunt = randint(1, 5)
                for i in range(hunt):
                    inventory.append('food')
                print('a deer runs across your path'); print(''); time.sleep(1)
                print(f'you shoot it, and manage to salvage {hunt} food before the wolves arrive to finish off the carcas'); print(''); time.sleep(1)
                # choose next destination
                turn = input('now with some food, you can either go to the city(ci) or the abandoned village(av) '); print(''); time.sleep(1)

            # city
            elif turn == 'ci':
                # city
                print('you arrive in the city, weaving your way past the rubble and shacks'); print(''); time.sleep(1)
                print('you notice more poeple around than usual, but you dismiss it'); print(''); time.sleep(1)
                # choose next destination
                turn = input('you can either go to the shooting range(sr), the abandoned village(av), the woods(w) or the radioactive plains(rp)'); print(''); time.sleep(1)

            # shooting range
            elif turn == 'sr':
                print(f'you arrive at the shooting range {weapon} in hand'); print(''); time.sleep(1)
                target = randint(2,7)
                print('you sidle up to the first platform, taking each shot in quick sucession'); print(''); time.sleep(1)
                print(f'you get {target} bullseyes!'); print(''); time.sleep(1)
                print('you notice that the targets have far more holes in than last week'); print(''); time.sleep(1)
                # choose next destination
                turn = input('you can either go to the mess hall(mh), the city(ci), the radioactive plains(rp) or the halls of death(hd)'); print(''); time.sleep(1)

            # mess hall
            elif turn == 'mh':
                print('you arrive at the mess hall, and jump for joy! the line is very small!'); print(''); time.sleep(1)
                # chance of 1 to 3 food
                meal = randint(1,3)
                print(f'you get to the counter quickly and receive {meal} food'); print(''); time.sleep(1)
                for i in range(meal):
                    inventory.append('food')
                # choose next destination
                turn = input('you can either go to the shooting range(sr) or the halls of death(hd)'); print(''); time.sleep(1)

            # abandoned village
            elif turn == 'av':
                # 1 in 3 chance of being attacked
                attack = randint(1,3)
                if attack == 1:
                    nomads = randint(3,6)
                    print(f'you arrive in the abandoned village, and are ambushed by {nomads} nomads!'); print(''); time.sleep(1)
                    # numerb of shots determined by speed
                    shots = randint(1, character_speed)
                    for i in range(nomads, shots):
                        shoot = input('type . to shoot! '); print(''); time.sleep(0.3)
                    # number of nomads killed determined by number of shots and attack damage
                    if shots > nomads and character_attack > 6:
                        print('you managed to shoot them all!'); print(''); time.sleep(1)
                    else:
                        # random damage done by nomads if you don't kill them
                        lose = randint(1, nomads)
                        character_health -= lose
                        print(f'oh no! you lost {lose} health before defeating them!'); print(''); time.sleep(1)
                        if character_health <= 0:
                            print('---  GAME OVER  ---'); print(''); time.sleep(1)
                            break
                else:
                    print('you arrive in the abandoned village, and spot a group of nomads on the other side'); print(''); time.sleep(1)
                    # if you don't get attacked, chance for 1 to 2 food
                    house = randint(1,2)
                    for i in range(house):
                        inventory.append('food')
                    print(f'you go into some of the houses and find {house} food!'); print(''); time.sleep(1)
                # choose next destination
                turn = input(' you can either go to the radioactive plains(rp), the witches hut(wh) or the desert(d)'); print(''); time.sleep(1)

            # radioactive plains
            elif turn == 'rp':
                # character must have more than 8 health to withstand the radiation 
                if character_health < 8:
                    print('you arrive on the radioacctive plains, but you\'re too weak to withstand the radiation!'); print(''); time.sleep(1)
                    character_health = 0
                    print('---  GAME OVER  ---'); print(''); time.sleep(1)
                # player attacked by 5 to 9 mutants
                mutants = randint(5,9)
                print(f'you arrive on the radioactive plains, and are attacked by {mutants} mutants!'); print(''); time.sleep(1)
                # numebr of shots determined by speed
                shots = randint(2, character_speed)
                for i in range(mutants, shots):
                    shoot = input('type . to shoot! '); print(''); time.sleep(0.3)
                # number of mutants killed determined by number of shots and attaack damage
                if shots > mutants and character_attack > 5:
                    print('you managed to shoot them all!'); print(''); time.sleep(1)
                else:
                    # random fdamage done by mutants if you don't kill them all
                    lose = randint(1, mutants)
                    character_health -= lose
                    print(f'oh no! you lost {lose} health before defeating them!'); print(''); time.sleep(1)
                    if character_health <= 0:
                        print('---  GAME OVER  ---'); print(''); time.sleep(1)
                        break
                # choose next destination
                turn = input('you can either go to the witches hut(wh) or the castle(ca)'); print(''); time.sleep(1)

            # halls of death
            elif turn == 'hd':
                print('you arrive in the halls of death and.. oh no...'); print(''); time.sleep(1)
                print('there are zombies everywhere!'); print(''); time.sleep(1)
                # 3 rounds of zombies to fight
                for i in range(1, 4):
                    print(f'---  ROUND {i} ---'); print(''); time.sleep(1)
                    # 4 to 12 zombies per round
                    zombies = randint(4, 12)
                    print(f'there are {zombies} zombies apporaching!'); print(''); time.sleep(1)
                    # number of shots determined by speed
                    shots = randint(4, character_speed)
                    # numebr of zombies killed determined by number of shots and attack damage
                    if (shots > zombies and character_attack > 8) or (shots > zombies*2 and character_attack > 4):
                        print('you killed them all!'); print(''); time.sleep(1)
                    else:
                        # random damage done by zombies (each round) if you kill them all
                        lose = randint(1, zombies)
                        character_health -= lose
                        print(f'oh no! you lost {lose} health before defeating them'); print(''); time.sleep(1)
                        if character_health <= 0:
                            print('---  GAME OVER  ---'); print(''); time.sleep(1)
                print('well done! you sucessfully defeated all the zombies!'); print(''); time.sleep(1)
                print('a flash on the wall draws your attention...'); print(''); time.sleep(1)
                print('you see some writing in what looks to be made of gold'); print(''); time.sleep(1)
                print('you can only make out a few of the characters:'); print(''); time.sleep(1)
                # clue for maze
                print(''' 
                
:00001:11001::01001:10011::10010:01100:10010:10010:

                '''); print(''); time.sleep(1)
                # choose next destination
                turn = input(' you can either go to the radioactive plains(rp) or the castle(ca)'); print(''); time.sleep(1)

            # witch's hut
            elif turn == 'wh':
                # 1 in 4 chance of witch arriving
                witch = randint(1,4)
                print('you arrive at the witch\'s hut, and see that the witch is not there'); print(''); time.sleep(1)
                ingo = input('do you go in? y/n '); print(''); time.sleep(1)
                # choice to go inside
                if ingo == 'y':
                    print('you go into the witches hut, and notice a dark red liquid in the cauldron'); print(''); time.sleep(1)
                    # chance for potion be be healing or poisonous
                    safe = randint(1,2)
                    drink = input('do you drink it? y/n '); print(''); time.sleep(1)
                    if drink == 'y':
                        if safe == 1:
                            # healing potion increases max health by 5, and heals character fully
                            temp = character_health
                            max_health += 5
                            character_health = max_health
                            print(f'it was a healing potion! you gained {character_health - temp} health!'); print(''); time.sleep(1)
                        elif safe == 2:
                            # poisonous potion decreases max health and character health by 5
                            max_health -= 5
                            character_health -= 5
                            print(f'oh no! it was a poisonous potion! you lost 5 health'); print(''); time.sleep(1)
                    if witch == 1:
                        print('oh no! the witch is outside!'); print(''); time.sleep(1)
                        if character_speed < 10:
                            # if character is too slow when witch comes, they get captured
                            print('you couldn\'t get out the window fast enough! the witch caught you!'); print(''); time.sleep(1)
                            print('she puts a bag over your head and starts to drag you away...'); print(''); time.sleep(1)
                            print('the last thing you notice before you pass out is the sound of construction, and a sweltering heat'); print(''); time.sleep(1)
                            turn = 'dtw'
                        else:
                            # if character is fast enough they escape
                            print('you make it out a window before the witch comes in. phew'); print(''); time.sleep(1)
                            # choose next destination
                            turn = input('you can either go to the desert(d) or the castle(ca)')
                # character can only travel to the desert temple if the witch comes
                    else:
                        print('you leave the witch hut and head towards the castle'); print(''); time.sleep(1)
                        turn = 'ca'
                else:
                    print('you decide to stear this one clear, and head on towards the castle'); print(''); time.sleep(1)
                    turn = 'ca'

            # castle
            elif turn == 'ca':
                print('you arrive at the castle, and are greeted by the guards'); print(''); time.sleep(1)
                # 1 in 7 chance of being turned away by guards
                guards = randint(1,7)
                print('they ask to see identification, you give it to them'); print(''); time.sleep(1)
                if guards == 1:
                    print('oh no! your identity card was damaged on your way here!, the guards don\'t allow you to enter'); print(''); time.sleep(1)
                    print('you turn and leave')
                    if character_speed < 4:
                        # if character is too slow they get stabbed by guards
                        character_health -= 7
                        print('you are so slow that the guards impale you for not leaving!'); print(''); time.sleep(1)
                        print('as you lay there, injured, by the side of the moat, you notice a flash in the distance'); print(''); time.sleep(1)
                        print('wait! thats coming from the d...'); print(''); time.sleep(2)
                    else: 
                        print('you manage to get out of there without being impaled. phew'); print(''); time.sleep(1)
                        print('you sit by the moat, studying your now invalid identity card'); print(''); time.sleep(1)
                        print('you notice a flash in the distance, but pay no mind to it...'); print(''); time.sleep(2)
                else:
                    print('you enter the castle, and approach the throne room.'); print(''); time.sleep(1)
                    print('you see a flash through one of the windows as you approach the hearing'); print(''); time.sleep(2)
                # after the castle, the game ends
                turn = 'F'

            # desert
            elif turn == 'd':
                print('you strip a layer in the sweltering heat of the desert sun'); print(''); time.sleep(1)
                print('the sun is causing heat waves to ripple across the horizon'); print(''); time.sleep(1)
                print('you see something in the distance'); print(''); time.sleep(1)
                print('its a pack of hyenas!'); print(''); time.sleep(1)
                choice = input('do you hide behind a cactus(c) or run away(r)? '); print(''); time.sleep(1)
                if choice == 'c':
                    # if character hides, they are eaten
                    print('you hide behind the cactus, but the hyenas aren\'t fazed'); print(''); time.sleep(1)
                    print('you shoot defiantly at them, but there are just too many...'); print(''); time.sleep(1)
                    print('noone hears your screams as you are quickly devoured'); print(''); time.sleep(1)
                    character_health = 0
                    print('---  GAME OVER  ---'); print(''); time.sleep(1)
                    break
                elif choice == 'r':
                    if character_speed > 10:
                        # if character is fast enough, they outrun the hyenas
                        print('you manage to out run the hyenas, and find yourself in the middle of a canyon'); print(''); time.sleep(1)
                        print('you keep going, down the only path you can'); print(''); time.sleep(1)
                        print('the canyon opens up and you see what looks like a temple'); print(''); time.sleep(1)
                        # character is tired
                        character_speed -= 5
                        # desert leads to the desert temple
                        turn = 'dt'           
                    else:
                        # if character is too slow they get eaten
                        print('you run as fast as you can, but the hyenas slowly catch up'); print(''); time.sleep(1)
                        print('they reach you just before the entrance to a canyon'); print(''); time.sleep(1)
                        print('you shoot defiantly at them, but there are too many...'); print(''); time.sleep(1)
                        print('noone hears your screams as you are quickly devoured...'); print(''); time.sleep(2)
                        print('...or so you think...'); print(''); time.sleep(2)
                        character_health = 0
                        print('---  GAME OVER  ---'); print(''); time.sleep(1)
                        break
            
            # temple (from desert)
            elif turn == 'dt':
                print('you stumble into the temple, hot and tired from the desert'); print(''); time.sleep(1)
                print('you marvel at the architecture, but your awe is cut short...'); print(''); time.sleep(1)
                print('...you realise something...'); print(''); time.sleep(1)
                print('...'); print(''); time.sleep(1)
                print('...this is the temple of the necromancer...'); print(''); time.sleep(2)
                print('...the one that brought the zombies...'); print(''); time.sleep(2)
                print('...the one that made the mutants...'); print(''); time.sleep(2)
                print('...the one that created the virus...'); print(''); time.sleep(2)
                print('...the one that started the fires...'); print(''); time.sleep(2)
                print('...the one that caused the storms...'); print(''); time.sleep(2)
                print('...then you see it...'); print(''); time.sleep(1)
                print('BANG'); print(''); time.sleep(1)
                print('darkness descends...'); print(''); time.sleep(1)
                turn = 'dtw'

            # temple (once captured)
            elif turn == 'dtw':
                for i in range(3):
                    print('you wake up in a dark room'); print(''); time.sleep(1)
                    print('you\'re blinded by a birght purple light'); print(''); time.sleep(1)
                    print('the necromancer is there, with the witch'); print(''); time.sleep(1)
                    print('they\'re performing some sort of ritual'); print(''); time.sleep(1)
                    print('you try and sneak out the door to the side of the room'); print(''); time.sleep(1)
                    print('you make it!'); print(''); time.sleep(1)
                    print('hmm, you find yourself in some sort of maze...'); print(''); time.sleep(1)
                    seq = ['r','l','r','r','l','r']
                    # player must take the correct sequence of turns to escape the maze
                    player_seq = []
                    for i in range(6):
                        choice = input('do you go right(r) or left?(l) ')
                        player_seq.append(choice)
                    if player_seq == seq:
                        break
                    else:
                        # player is recaptured if they fail
                        print('you stumble into a room'); print(''); time.sleep(1)
                        print('its the necromancer and the witch, they see you'); print(''); time.sleep(1)
                        print('BANG'); print(''); time.sleep(1)
                if player_seq == seq:
                    print('you\'ve made it out of the maze!'); print(''); time.sleep(1)
                    print('the desert air buffets you, as you turn your face up to the sun'); print(''); time.sleep(1)
                    print('you stumble out into the desert, tired and hungry'); print(''); time.sleep(1)
                    character_hunger -= 5
                    character_speed -= 5
                    turn = 'd2'
                else:
                    # if character doesn't make it out, the game ends
                    character_hunger = 1
                    print('you\'re so tired, so hungry'); print(''); time.sleep(1)
                    print('you just need a little lie down...'); print(''); time.sleep(2)
                    print('you see a bright flash through your eyelids...'); print(''); time.sleep(2)
                    turn = 'F'
            
            elif turn == 'd2':
                print('hours pass...'); print(''); time.sleep(2)
                print('...you\'re tired and hungry'); print(''); time.sleep(2)
                character_hunger -= 4
                character_speed -= 2
                print('you find a small cave to rest in, ad lie down'); print(''); time.sleep(4); print('')
                print('you wake up, feeling rested, and continue through the desert'); print(''); time.sleep(1)
                print('as you travel, you start seeing things...'); print(''); time.sleep(1)
                print('water... trees...'); print(''); time.sleep(1)
                print('mirages... they\'re just mirages'); print(''); time.sleep(1)
                print('wait... that doesn\'t look like the others...'); print(''); time.sleep(2)
                print('is that...'); print(''); time.sleep(2)
                print('...but why...'); print(''); time.sleep(4)
                print('as you get closer, it becomes more clear'); print(''); time.sleep(2)
                print('it\'s a rocket...'); print(''); time.sleep(4)
                turn = 'ae'

            # finish
            elif turn == 'F':
                # game end sequence
                print('the explosion rips through the land, destroying everything in its path. '); print(''); time.sleep(2)
                print('if only you could have done something to stop it...'); print(''); time.sleep(2)
                print('''
                               ________________
                          ____/ (  (    )   )  \___
                         /( (  (  )   _    ))  )   )\\
                       ((     (   )(    )  )   (   )  )
                     ((/  ( _(   )   (   _) ) (  () )  )
                    ( (  ( (_)   ((    (   )  .((_ ) .  )_
                   ( (  )    (      (  )    )   ) . ) (   )
                  (  (   (  (   ) (  _  ( _) ).  ) . ) ) ( )
                  ( (  (   ) (  )   (  ))     ) _)(   )  )  )
                 ( (  ( \ ) (    (_  ( ) ( )  )   ) )  )) ( )
                  (  (   (  (   (_ ( ) ( _    )  ) (  )  )   )
                 ( (  ( (  (  )     (_  )  ) )  _)   ) _( ( )
                  ((  (   )(    (     _    )   _) _(_ (  (_ )
                   (_((__(_(__(( ( ( |  ) ) ) )_))__))_)___)
                   ((__)        \\\\||lll|l||///          \_))
                                /(/ (  )  ) )\   
                               ( ( ( | | ) ) )\   
                               /(| / ( )) ) ) )) 
                               ( ((((_(|)_)))))     
                                 ||\(|(|)|/||     
                                 |(||(||)||||        
                                //|/l|||)|\\\\ \     
                         / / //  /|//||||\\\\  \ \  \ _
-------------------------------------------------------------------------------
    '''); print(''); time.sleep(2)
                break
            
            # secret ending (shhhh)
            elif turn == 'ae':
                print('um, well done ig'); print(''); time.sleep(2)
                break

        def stats_to_0(character_health, character_hunger, character_speed, character_attack):
            # unsures character's stats don't go below 0
            if character_health < 0:
                character_health = 0
            if character_hunger < 0:
                character_hunger = 0
            if character_speed < 0:
                character_speed = 0
            if character_attack < 0:
                character_attack = 0
        stats_to_0(character_health, character_hunger, character_speed, character_attack)
        
        # end of turn stats
        print(f'end of turn {turn_count}. health: {character_health}, speed: {character_speed}, hunger: {character_hunger}, attack: {character_attack}, inventory: {inventory}'); print(''); time.sleep(2)
        
        # lose 1 hunger every 3 turns
        if turn_count%3 == 0:
            character_hunger -= 1

        # character can increase stats, but loose hunger if hunger is high enough
        if character_hunger > 8:
            if character_health < max_health:
                character_hunger -= 1
                character_health += 1
            if character_speed < max_speed:
                character_hunger -= 1
                character_speed += 1
            if character_attack < max_attack:
                character_hunger -= 1
                character_attack += 1

        # when character runs out of hunger, they loose other stats
        elif character_hunger <= 0:
            print('sooooooo hungry'); print(''); time.sleep(1)
            character_health -= 1
            character_speed -= 3
            character_attack = 0

        # when character is running out of hunger, they loose other stats
        elif character_hunger < 2:
            character_speed -= 2
            character_attack -= 2

        # when character starts to run out of hunger, they loose other stats     
        elif character_hunger < 5:
            character_speed -= 1
            character_attack -= 1
        
        stats_to_0(character_health, character_hunger, character_speed, character_attack)

        # game ends if character speed runs out
        if character_speed <= 0:
            print('so tired...'); print(''); time.sleep(1)
            print('just gonna lie down here...'); print(''); time.sleep(2)
            print('---  GAME OVER  ---'); print(''); time.sleep(2)

        # game ends if character health runs out
        if character_health <= 0:
            print('---  GAME OVER  ---'); print(''); time.sleep(2)
            break
        
        # end of turn
        turn_count += 1 

    # end message
    print('---    THANK YOU FOR PLAYING:    ---'); print(''); time.sleep(2)
    print('---  APOCALYPSE: WORLD GO BOOM!  ---'); print(''); time.sleep(2)


apocalypse_world_go_boom()
