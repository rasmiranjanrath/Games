import curses
from curses import KEY_LEFT, KEY_RIGHT



curses.initscr()
win = curses.newwin(20, 20, 0, 10)
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(1)

key = KEY_RIGHT                                                    # Initializing values
score = 0
animation=0





vehicle=[[17,4],[18,5],[18,3],[16,5],[16,3]]
obj=[[15,5],[14,5],[15,4],[14,4]]




win.addch(vehicle[0][0], vehicle[0][1], '*')
win.addch(vehicle[1][0], vehicle[1][1], '*')
win.addch(vehicle[2][0], vehicle[2][1], '*')
win.addch(vehicle[3][0], vehicle[3][1], '*')
win.addch(vehicle[4][0], vehicle[4][1], '*')

while key != 27:                                                   # While Esc key is not pressed
    win.border(0)
    win.addstr(0, 2, 'Score : ' + str(score) + ' ')                # Printing 'Score' and
    prevKey = key                                                  # Previous key pressed
    event = win.getch()
    key = key if event == -1 else event

    win.timeout(1000)
    score+=1

    if key == ord(' '):                                            # If SPACE BAR is pressed, wait for another
        key = -1                                                   # one (Pause/Resume)
        while key != ord(' '):
            key = win.getch()
        key = prevKey
        continue
    obj_old = obj[:]

    if animation == 0:
        win.addch(obj[0][0], obj[0][1], '#')
        win.addch(obj[1][0], obj[1][1], '#')
        win.addch(obj[2][0], obj[2][1], '#')
        win.addch(obj[3][0], obj[3][1], '#')
        animation = 1
    else:
        win.addch(obj[0][0], obj[0][1], '&')
        win.addch(obj[1][0], obj[1][1], '@')
        win.addch(obj[2][0], obj[2][1], '@')
        win.addch(obj[3][0], obj[3][1], '&')
        animation = 0

    obj[0][0]+=2
    obj[1][0]+=2
    obj[2][0]+=2
    obj[3][0]+=2




    if obj[2][0]>18 or obj[3][0] >18:
        obj[0][0] = 1
        obj[1][0] = 2
        obj[2][0] = 1
        obj[3][0] = 2



    if key == KEY_RIGHT:
    	win.addch(vehicle[0][0], vehicle[0][1], ' ')
        win.addch(vehicle[1][0], vehicle[1][1], ' ')
        win.addch(vehicle[2][0], vehicle[2][1], ' ')
        win.addch(vehicle[3][0], vehicle[3][1], ' ')
        win.addch(vehicle[4][0], vehicle[4][1], ' ')
    	vehicle=[[17,15],[18,16],[18,14],[16,16],[16,14]]
        win.addch(vehicle[0][0], vehicle[0][1], '*')
        win.addch(vehicle[1][0], vehicle[1][1], '*')
        win.addch(vehicle[2][0], vehicle[2][1], '*')
        win.addch(vehicle[3][0], vehicle[3][1], '*')
        win.addch(vehicle[4][0], vehicle[4][1], '*')

    if key == KEY_LEFT:
    	win.addch(vehicle[0][0], vehicle[0][1], ' ')
        win.addch(vehicle[1][0], vehicle[1][1], ' ')
        win.addch(vehicle[2][0], vehicle[2][1], ' ')
        win.addch(vehicle[3][0], vehicle[3][1], ' ')
        win.addch(vehicle[4][0], vehicle[4][1], ' ')
    	vehicle=[[17,4],[18,5],[18,3],[16,5],[16,3]]
        win.addch(vehicle[0][0], vehicle[0][1], '*')
        win.addch(vehicle[1][0], vehicle[1][1], '*')
        win.addch(vehicle[2][0], vehicle[2][1], '*')
        win.addch(vehicle[3][0], vehicle[3][1], '*')
        win.addch(vehicle[4][0], vehicle[4][1], '*')



curses.endwin()

