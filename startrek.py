
#NOTE USED SOME OF THE ADVICE / TIPS GIVEN ON THE SITE.
import random
import time
import math
#CREATING THE BOARD FIRST/ ASSIGNING VARIABLES
#GRID
GRX = 10
GRY = GRX

#command abbreviation
north = 'n'
east = 'e'
west = 'w'
south = 's'

#energy
n=250
d=50

#selecting Kling, kling attack percent
ks = random.randint(1,4)
ka = random.randint(1,101)
#ship chance of hitting klington and ship hit.
sc = 75

#ingame contents
EMPTYAREA = '.'
ENTERPRISE = 'E'
KLING = 'K'
STAR = '*'
STARBASE = '#'

#win
win = False

#lose
lose = False
#GENERATING MAP
map = []

for y in range(GRY):
    map.append([EMPTYAREA]*GRX)


#placing Starbase

for i in range(1):
    while i<2:
        y= random.randint(1,9)
        x = random.randint(1,9)
        if map[y][x] == EMPTYAREA:
            break
    map[y][x] = STARBASE
basex = x
basey = y
#placing 3 KLING (SEPARATE KLINGS TO GET COORDS)
#kling1

for i in range(1):
    while i<2:
        y= random.randint(1,9)
        x = random.randint(1,9)
        if map[y][x] == EMPTYAREA:
            break
    map[y][x] = KLING
k1x = x
k1y = y
k1hp=1
#kling2
for i in range(1):
    while i<2:
        y= random.randint(1,9)
        x = random.randint(1,9)
        if map[y][x] == EMPTYAREA:
            break
    map[y][x] = KLING
k2x = x
k2y = y
k2hp =1
#kling3
for i in range(1):
    while i<2:
        y= random.randint(1,9)
        x = random.randint(1,9)
        if map[y][x] == EMPTYAREA:
            break
    map[y][x] = KLING

k3x = x
k3y = y
k3hp =1



#placing 10 Stars
#CHANGE
for i in range(10):
    while i<11:
        y= random.randint(1,9)
        x = random.randint(1,9)
        if map[y][x] == EMPTYAREA:
            break
    map[y][x] = STAR



#ENTERPRISE

for i in range(1):
    while i<2:
        y= random.randint(1,9)
        x = random.randint(1,9)
        if map[y][x] == EMPTYAREA:
            break
    map[y][x] = ENTERPRISE


shipx = x
shipy = y




print("type 'help' for commands")
print()
print()
print()

#COMMAND LINES

play = True


while True:
    if play == True:

        print('*NAVIGATION')

#kling ATTACKS
        if k1hp == 1:
            ka = random.randint(1,101)
            if ka <= 42:
#kling1
                if shipx in range(k1x-2, k1x+3):
                    if shipy in range(k1y-2, k1y+3):
                        print('Klingon at','(',k1x,',',k1y,')', "attacked")
                        if shipx in range(k1x+1, k1x+3):
#abovekling
                            if shipy in range (k1y-2,k1y):
                                n = n - (d/(math.sqrt(((shipy-k1y)**2)  + ((shipx - k1x)**2))))
#belowkling
                            elif shipy in range(k1y+1,k1y+3):
                                n = n - (d/(math.sqrt(((shipy-k1y)**2)  + ((shipx - k1x)**2))))

#equal to kling
                            elif shipy == k1y:
                                n = n- (d/(math.sqrt(((shipy-k1y)**2) + ((shipx - k1x)**2))))
#left of kling
                        elif shipx in range(k1x-2, k1x):
                            if shipy in range (k1y-2,k1y):
                                n = n - (d/(math.sqrt(((shipy-k1y)**2)  + ((shipx - k1x)**2))))
                            elif shipy in range(k1y+1,k1y+3):
                                n = n - (d/(math.sqrt(((shipy-k1y)**2)  + ((shipx - k1x)**2))))
                            elif shipy == k1y:
                                n = n- (d/(math.sqrt(((shipy-k1y)**2)  + ((shipx - k1x)**2))))
#same TOP OF BELOW OF KLING
                        elif shipx == k1x:
                            if shipy in range (k1y-2,k1y):
                                n = n - (d/(math.sqrt(((shipy-k1y)**2)  + ((shipx - k1x)**2))))
                            elif shipy in range(k1y+1,k1y+3):
                                n = n - (d/(math.sqrt(((shipy-k1y)**2)  + ((shipx - k1x)**2))))
            elif ka >42:
                if shipx in range(k1x-2, k1x+3):
                    if shipy in range(k1y-2, k1y+3):
                        print("Klingon at" ,'(',k1x,',',k1y,')', " missed")


#kling2
        if k2hp ==1:
            ka = random.randint(1,101)
            if ka <=42:

                if shipx in range(k2x-2, k2x+3):
                    if shipy in range(k2y-2, k2y+3):
                        print('Klingon at','(',k2x,',',k2y,')', "attacked")
                        if shipx in range(k2x+1, k2x+3):
#abovekling
                            if shipy in range (k2y-2,k2y):
                                n = n - (d/(math.sqrt(((shipy-k2y)**2)  + ((shipx - k2x)**2))))
#belowkling
                            elif shipy in range(k2y+1,k2y+3):
                                n = n - (d/(math.sqrt(((shipy-k2y)**2)  + ((shipx - k2x)**2))))

#equal to kling
                            elif shipy == k2y:
                                n = n- (d/((1+shipx)-(1+k2x)))
#left of kling
                        elif shipx in range(k2x-2, k2x):
                            if shipy in range (k2y-2,k2y):
                                n = n - (d/(math.sqrt(((shipy-k2y)**2)  + ((shipx - k2x)**2))))
                            elif shipy in range(k2y+1,k2y+3):
                                n = n - (d/(math.sqrt(((shipy-k2y)**2)  + ((shipx - k2x)**2))))
                            elif shipy == k2y:
                                n = n- (d/(math.sqrt(((shipy-k2y)**2)  + ((shipx - k2x)**2))))
#same TOP OF BELOW OF KLING
                        elif shipx == k2x:
                            if shipy in range (k2y-2,k2y):
                                n = n - (d/(math.sqrt(((shipy-k2y)**2)  + ((shipx - k2x)**2))))
                            elif shipy in range(k2y+1,k2y+3):
                                n = n - (d/(math.sqrt(((shipy-k2y)**2)  + ((shipx - k2x)**2))))


            elif ka >42:
                if shipx in range(k2x-2, k2x+3):
                    if shipy in range(k2y-2, k2y+3):
                        print("Klingon at" ,'(',k2x,',',k2y,')', " missed")
#kling3
        if k3hp == 1:
            ka = random.randint(1,101)
            if ka <= 42:
#kling3
                if shipx in range(k3x-2, k3x+3):
                    if shipy in range(k3y-2, k3y+3):
                        print('Klingon at','(',k3x,',',k3y,')', "attacked")
                        if shipx in range(k3x+1, k3x+3):
#abovekling
                            if shipy in range (k3y-2,k3y):
                                n = n - (d/(math.sqrt(((shipy-k3y)**2)  + ((shipx - k3x)**2))))
#belowkling
                            elif shipy in range(k3y+1,k3y+3):
                                n = n - (d/(math.sqrt(((shipy-k3y)**2)  + ((shipx - k3x)**2))))

#equal to kling
                            elif shipy == k3y:
                                n = n- (d/(math.sqrt(((shipy-k3y)**2)  + ((shipx - k3x)**2))))
#left of kling
                        elif shipx in range(k3x-2, k3x):
                            if shipy in range (k3y-2,k3y):
                                n = n - (d/(math.sqrt(((shipy-k3y)**2)  + ((shipx - k3x)**2))))
                            elif shipy in range(k3y+1,k3y+3):
                                n = n - (d/(math.sqrt(((shipy-k3y)**2)  + ((shipx - k3x)**2))))
                            elif shipy == k3y:
                                n = n- (d/(math.sqrt(((shipy-k3y)**2)  + ((shipx - k3x)**2))))
#same TOP OF BELOW OF KLING
                        elif shipx == k3x:
                            if shipy in range (k3y-2,k3y):
                                n = n - (d/(math.sqrt(((shipy-k3y)**2)  + ((shipx - k3x)**2))))
                            elif shipy in range(k3y+1,k3y+3):
                                n = n - (d/(math.sqrt(((shipy-k3y)**2)  + ((shipx - k3x)**2))))

            elif ka >42:
                if shipx in range(k3x-2, k3x+3):
                    if shipy in range(k3y-2, k3y+3):
                        print("Klingon at" ,'(',k3x,',',k3y,')', " missed")





        print('current coordinate',"(", shipx+1, ",", 10-shipy, ")")
#generating map
        for row in map:
            for col in row:
                print(col,end='   ')
            print()

        print("input command", "             ",  " current energy:", n )
        cmd = input()
        print()
        print()
        print()
        print()
        print()



#help COMMANDS

    if cmd ==("help"):
        print("MOVEMENT COMMANDS ")
        print("the movement commands are 'north','east','south','west'")
        print("shortcuts the movement commands are 'n','e','s','w'")
        print(" ")
        print("DESTRUCT COMMAND ")
        print("to self destruct, type 'destruct'")
        print(" ")
        print("QUIT COMMAND ")
        print("the exit the game, type 'quit'")
        print(" ")
        print(" ")
        print("FIRE COMMAND")
        print("type 'fire' to shoot at Klingons, the chance of hitting is calculated by your distance")
        print(" ")
        print("DOCK COMMAND")
        print("type 'dock' to refill ship energy")
        print(" ")
        print(" ")
        print("Ready to start playing? ")
        print("type 'play' to display board and begin playing")
        print(" ")
        print(" ")

        play = False
        cmd = input()
    elif cmd == ("destruct"):
        print("self destructing in 5...")
        time.sleep(1)
        print("self destructing in 4...")
        time.sleep(1)
        print("self destructing in 3...")
        time.sleep(1)
        print("self destructing in 2...")
        time.sleep(1)
        print("self destructing in 1...")
        time.sleep(1)
        print("bye")
        exit()
    elif cmd == ("quit"):
        exit()
    elif cmd == ("play"):
        print("welcome back!")
        play = True


#from here on will be movement commands




#South (SORT OF COMPLETE)

    elif cmd == ("s"):
        if shipy in range(0,9):
            print("your last command was south")
            shipy = shipy+1
            if map[shipy][shipx] == EMPTYAREA:
                map[shipy][shipx] = ENTERPRISE
                shipy = shipy-1
                map[shipy][shipx] = EMPTYAREA
                shipy = shipy+1
            else:
                shipy = shipy-1
                print("there is something in the way!")
        elif shipy == 9:
            print('you cannot move south anymore')


    elif cmd == ("south"):
        if shipy in range(0,9):
            print("your last command was south")
            shipy = shipy+1
            if map[shipy][shipx] == EMPTYAREA:
                map[shipy][shipx] = ENTERPRISE
                shipy = shipy-1
                map[shipy][shipx] = EMPTYAREA
                shipy = shipy+1
            else:
                shipy = shipy-1
                print("there is something in the way!")
        elif shipy == 9:
            print('you cannot move south anymore')

#north ( SORT OF COMPLETE)
    elif cmd == ("n"):
        if shipy in range(1,10):
            print("your last command was north")
            shipy = shipy-1
            if map[shipy][shipx] == EMPTYAREA:
                map[shipy][shipx] = ENTERPRISE
                shipy = shipy+1
                map[shipy][shipx] = EMPTYAREA
                shipy = shipy-1
            else:
                shipy = shipy+1
                print("there is ssomething in the way!")
        elif shipy ==0:
            print('you cannot move north anymore')


    elif cmd == ("north"):
        if shipy in range(1,10):
            print("your last command was north")
            shipy = shipy-1
            if map[shipy][shipx] == EMPTYAREA:
                map[shipy][shipx] = ENTERPRISE
                shipy = shipy+1
                map[shipy][shipx] = EMPTYAREA
                shipy = shipy-1
            else:
                shipy = shipy+1
                print("there is something in the way!")
        elif shipy ==0:
            print('you cannot move north anymore')

#EAST
    elif cmd == ("e"):
        if shipx in range(0,9):
            print("your last command was east")
            shipx = shipx+1
            if map[shipy][shipx] == EMPTYAREA:
                map[shipy][shipx] = ENTERPRISE
                shipx = shipx-1
                map[shipy][shipx] = EMPTYAREA
                shipx = shipx+1
            else:
                shipx = shipx-1
                print("there is something in the way!")
        elif shipx == 9:
            print('you cannot move east anymore')



    elif cmd == ("east"):
        if shipx in range(0,9):
            print("your last command was east")
            shipx = shipx+1
            if map[shipy][shipx] == EMPTYAREA:
                map[shipy][shipx] = ENTERPRISE
                shipx = shipx-1
                map[shipy][shipx] = EMPTYAREA
                shipx = shipx+1
            else:
                shipx = shipx-1
                print("there is something in the way!")
        elif shipx == 9:
            print('you cannot move east anymore ')



#WEST
    elif cmd == ("w"):
        if shipx in range(1,10):
            print("your last command was west")
            shipx = shipx-1
            if map[shipy][shipx] == EMPTYAREA:
                map[shipy][shipx] = ENTERPRISE
                shipx = shipx+1
                map[shipy][shipx] = EMPTYAREA
                shipx = shipx-1
            else:
                shipx = shipx+1
                print("there is something in the way!")
        elif shipx == 0:
            print('you cannot move west anymore')



    elif cmd == ("west"):
        if shipx in range(1,10):
            print("your last command was west")
            shipx = shipx-1
            if map[shipy][shipx] == EMPTYAREA:
                map[shipy][shipx] = ENTERPRISE
                shipx = shipx+1
                map[shipy][shipx] = EMPTYAREA
                shipx = shipx-1
            else:
                shipx = shipx+1
                print("there is something in the way!")
        elif shipx == 0:
            print('you cannot move west anymore')


#fire command
    elif cmd == ("fire"):

        if n <=49:
            print("you do not have enough energy")
            print(n,"is not enough to fire")

        if n >= 50:

#kling1 attack
            if k1hp ==1:
                if k1x in range(shipx-2,shipx+3):
                    if k1y in range(shipy-2, shipy+3):
                        n=n-50
                        sc = 75
                        sc = int(sc/(math.sqrt(((shipy-k1y)**2)  + ((shipx - k1x)**2))))

                        sh = random.randint(1,101)
                        if sh in range (1,sc+1):
                            k1hp = 0
                            print('you have destroyed','(',1+k1x,',',10-k1y,')')
                        elif sh not in range(1,sc+1):
                            print('shot missed!','(',1+k1x,',',10-k1y,')')

                    elif k3y not in range (shipy-2, shipy+3):
                        continue

                elif k3x not in range(shipx-2,shipx+3):
                    continue

#kling2 attack
            if k2hp ==1:
                if k2x in range(shipx-2,shipx+3):
                    if k2y in range(shipy-2, shipy+3):
                        n=n-50
                        sc = 75
                        sc = int(sc/(math.sqrt(((shipy-k2y)**2)  + ((shipx - k2x)**2))))

                        sh = random.randint(1,101)
                        if sh in range (1,sc+1):
                            k2hp = 0
                            print('you have destroyed','(',1+k2x,',',10-k2y,')')
                        elif sh not in range(1,sc+1):
                            print('shot missed!','(',1+k2x,',',10-k2y,')')

                    elif k2y not in range (shipy-2, shipy+3):

                        continue
                elif k2x not in range(shipx-2,shipx+3):
                    continue
#kling3 attack
            if k3hp == 1:
                if k3x in range(shipx-2,shipx+3):
                    if k3y in range(shipy-2, shipy+3):
                        n=n-50
                        sc = 75
                        sc = int(sc/(math.sqrt(((shipy-k3y)**2)  + ((shipx - k3x)**2))))

                        sh = random.randint(1,101)
                        if sh in range (1,sc+1):
                            print('you have destroyed','(',1+k3x,',',10-k3y,')')
                            k3hp = 0
                        elif sh not in range(1,sc+1):
                            print('shot missed!','(',1+k3x,',',10-k3y,')')

                    elif k3y not in range (shipy-2, shipy+3):

                        continue
                elif k3x not in range(shipx-2,shipx+3):
                    continue
            else:
                continue



#Dock Command
    elif cmd == ("dock"):
        if shipx in range(basex-1, basex+2 ):
            if shipy in range(basey-1,basey+2):
                print('Energy replenished')
                n = 250
            elif shipy not in range(basey-1,basey+2):
                print('No starbase adjacent')
        elif shipx not in range (basex-1, basex+2 ):
            print('No starbase adjacent')




    else:
        print('invalid command')
    if k1hp == 0:

        map[k1y][k1x] = EMPTYAREA
        k1hp = 3
    if k2hp == 0:

        map[k2y][k2x] = EMPTYAREA
        k2hp = 3
    if k3hp == 0:

        map[k3y][k3x] = EMPTYAREA
        k3hp = 3

    if k1hp == 3:
        print('Kling1', '(',1+k1x,',',10-k1y,')', 'has been destroyed!')

    if k2hp == 3:
        print('Kling2', '(',1+k2x,',',10-k2y,')', 'has been destroyed!')

    if k3hp == 3:
        print('Kling3', '(',1+k3x,',',10-k3y,')', 'has been destroyed!')

#checking for win

    if k1hp+k2hp+k3hp == 9:
        win = True

    if win == True:
        print('congratulations! you have beaten the game!')
        print('game will now close in 5 seconds')
        print('5')
        time.sleep(1)
        print('4')
        time.sleep(1)
        print('3')
        time.sleep(1)
        print('2')
        time.sleep(1)
        print('1')
        quit()
    if n <= 0:
        lose = True
        map[shipy][shipx] = EMPTYAREA
    elif n < 50:
        print('energy levels low, please fill up!')
    if lose == True:
        print('GAME OVER! your ship has blown up')
        print('game will now close in 5 seconds')
        print('5')
        time.sleep(1)
        print('4')
        time.sleep(1)
        print('3')
        time.sleep(1)
        print('2')
        time.sleep(1)
        print('1')
        quit()
