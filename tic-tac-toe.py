# tic-tac-toe
import random
print('Tic-tac-toe')

# output grid
def outputgrid():
    for i in range(9):
        if grid[i] == '-':
            print(i + 1, end=' ')
        elif (grid[i] == 'X')or(grid[i] == 'O'):
            print(grid[i], end=' ')
        if (i == 2)or(i == 5)or(i == 8):
            print()

# remember course
def remembercourse(z, c):
    if (grid[c] == '-'):
        grid[c] = z
        for i in range(24):
            if (ilg[i] == str(c)):
                global zlg
                zlg = zlg[:i]+z+zlg[i+1:24]
                if (z == 'X'):
                    kxl[i // 3] += 1
                elif (z == 'O'):
                    kol[i // 3] += 1
    else:
        print(' this cell is busy')
        c = int(input(' enter free cell number: ' ))
        c -= 1
        remembercourse(zp, c)

# search for a version of the move for the computer
def searchcourse():
    l = []
    if (zc == 'O'):
        # if can win
        if ((kol.count(2) != 0)and(kxl[kol.index(2)] == 0)):
            for i in range(3):
                if (zlg[kol.index(2) * 3 + i] == '-'):
                    c = int(ilg[kol.index(2) * 3 + i])
        # if the player can finish the next motion
        elif ((kxl.count(2) != 0)and(kol[kxl.index(2)] == 0)):
            for i in range(3):
                if (zlg[kxl.index(2) * 3 + i] == '-'):
                    c = int(ilg[kxl.index(2) * 3 + i])
        # if the central cell is free - to occupy it
        elif (grid[4] == '-'):
            c = 4
        # if the player has taken a corner - to take the opposite, if the opposite is occupied - to occupy any side cell
        elif (((grid[0] == 'X')and(grid[8] == '-'))or((grid[2] == 'X')and(grid[6] == '-'))or((grid[6] == 'X')and(grid[2] == '-'))or((grid[8] == 'X')and(grid[0] == '-'))):
            if ((grid[0] == 'X')and(grid[8] == '-')):
                c = 8
            elif ((grid[2] == 'X')and(grid[6] == '-')):
                c = 6
            elif ((grid[6] == 'X')and(grid[2] == '-')):
                c = 2
            elif ((grid[8] == 'X')and(grid[0] == '-')):
                c = 0
        # put in an angle between two occupied side cells - not prescribed
        # take any corner cell
        elif (grid[0] == '-')or(grid[2] == '-')or(grid[6] == '-')or(grid[8] == '-'):
            for i in (0, 2, 6, 8):
                if (grid[i] == '-'):
                    l.append(i)
            c = random.choice(l)
        # take any side cell
        elif (grid[1] == '-')or(grid[3] == '-')or(grid[5] == '-')or(grid[7] == '-'):
            for i in (1, 3, 5, 7):
                if (grid[i] == '-'):
                    l.append(i)
            c = random.choice(l)

    elif (zc == 'X'):
        # if can win
        if ((kxl.count(2) != 0)and(kol[kxl.index(2)] == 0)):
            for i in range(3):
                if (zlg[kxl.index(2) * 3 + i] == '-'):
                    c = int(ilg[kxl.index(2) * 3 + i])
        # if the player can finish the next motion
        elif ((kol.count(2) != 0)and(kxl[kol.index(2)] == 0)):
            for i in range(3):
                if (zlg[kol.index(2) * 3 + i] == '-'):
                    c = int(ilg[kol.index(2) * 3 + i])
        # if the central cell is free - to occupy it
        elif (grid[4] == '-'):
            c = 4
        # if the player has taken a corner - to take the opposite, if the opposite is occupied - to occupy any side cell
        elif (((grid[0] == 'O')and(grid[8] == '-'))or((grid[2] == 'O')and(grid[6] == '-'))or((grid[6] == 'O')and(grid[2] == '-'))or((grid[8] == 'O')and(grid[0] == '-'))):
            if ((grid[0] == 'O')and(grid[8] == '-')):
                c = 8
            elif ((grid[2] == 'O')and(grid[6] == '-')):
                c = 6
            elif ((grid[6] == 'O')and(grid[2] == '-')):
                c = 2
            elif ((grid[8] == 'O')and(grid[0] == '-')):
                c = 0
            else:
                for i in (1, 3, 5, 7):
                    if (grid[i] == '-'):
                        l.append(i)
                c = random.choice(l)
        # put in an angle between two occupied side cells - not prescribed
        # take any corner cell
        elif (grid[0] == '-')or(grid[2] == '-')or(grid[6] == '-')or(grid[8] == '-'):
            for i in (0, 2, 6, 8):
                if (grid[i] == '-'):
                    l.append(i)
            c = random.choice(l)
        # take any side cell
        elif (grid[1] == '-')or(grid[3] == '-')or(grid[5] == '-')or(grid[7] == '-'):
            for i in (1, 3, 5, 7):
                if (grid[i] == '-'):
                    l.append(i)
            c = random.choice(l)
    return c

s = 'y'
while (s == 'Y')or(s == 'y')or(s == 'YES')or(s == 'yes'):
    grid = ['-', '-', '-', '-', '-', '-', '-', '-', '-'] # grid 3х3
    ilg = '012345678036147258048246' # indices of the cells of lines, one of which must be filled (three digits - one line)
    zlg = '------------------------' # cell values by lines
    kxl = [0, 0, 0, 0, 0, 0, 0, 0  ] # the number of X in each line (i*3 - index of the first cell of the line grid ilg[i*3:i*3+3])
    kol = [0, 0, 0, 0, 0, 0, 0, 0  ] # the number of O in each line (i*3 - index of the first cell of the line grid ilg[i*3:i*3+3])

    # choice of sign
    s = input('choose yourself a sign (X/O): ')
    if (s == 'X')or(s == 'x')or(s == 'Х')or(s == 'х'):
        zp = 'X'
        zc = 'O'
    elif (s == 'O')or(s == 'o')or(s == 'О')or(s == 'о')or(s == '0'):
        zp = 'O'
        zc = 'X'

    # output empty grid
    print('\nempty grid:')
    outputgrid()
    print('the numbers you see are the numbers of the cells grid\n in order to make your move (put "%s") - you will need to enter the cell number' % zp)
    input()

    # process of the game
    while ((kxl.count(3) == 0)and(kol.count(3) == 0))and(grid.count('-') != 0):
        if (zp == 'X'):
            # player progress
            c = int(input('your move, enter the cell number: ' )) - 1
            remembercourse(zp, c)
            outputgrid()
            input()
            if ((kxl.count(3) == 1)or(grid.count('-') == 0)):
                break
            # computer progress
            c = searchcourse()
            remembercourse(zc, c)
            print('the computer made a move in %d cell' % (c + 1))
            outputgrid()
            print()
        elif (zp == 'O'):
            # computer progress
            c = searchcourse()
            remembercourse(zc, c)
            print('the computer made a move in %d cell' % (c + 1))
            outputgrid()
            print()
            if ((kxl.count(3) == 1)or(grid.count('-') == 0)):
                break
            # player progress
            c = int(input('your move, enter the cell number: ' )) - 1
            remembercourse(zp, c)
            outputgrid()
            input()

    if (kxl.count(3) == 1):
        print('X won!')
    elif (kol.count(3) == 1):
        print('O won!')
    elif (grid.count('-') == 0):
        print('draw!')
    print()
    s = input('restart? (y/n): ')