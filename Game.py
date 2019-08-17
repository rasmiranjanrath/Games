import curses
from curses import KEY_LEFT, KEY_RIGHT
import random



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
collision=0
v_position=1

object_position=0


vehicle=[[17,4],[18,5],[18,3],[16,5],[16,3]]
vehicle1=[[17,15],[18,16],[18,14],[16,16],[16,14]]
obj=[[15,5],[14,5],[15,4],[14,4]]
obj_right=[[15,15],[14,16],[15,15],[14,16]]

vehicle_x=[vehicle[0][0],vehicle[1][0],vehicle[2][0],vehicle[3][0]]
vehicle_y=[vehicle[0][1],vehicle[1][1],vehicle[2][1],vehicle[3][1]]
vehicle1_y=[vehicle1[0][1],vehicle1[1][1],vehicle1[2][1],vehicle1[3][1]]

obj_x=[obj[0][0],obj[1][0],obj[2][0],obj[3][0]]
obj_y=[obj[0][1],obj[1][1],obj[2][1],obj[3][1]]

win.addch(vehicle[0][0], vehicle[0][1], '*')
win.addch(vehicle[1][0], vehicle[1][1], '*')
win.addch(vehicle[2][0], vehicle[2][1], '*')
win.addch(vehicle[3][0], vehicle[3][1], '*')
win.addch(vehicle[4][0], vehicle[4][1], '*')






while key != 27:                                                   # While Esc key is not pressed
    win.border(0)
    win.addstr(0, 2, 'Collision : ' + str(collision) + ' ')        # Printing 'Score' and
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


    win.addch(obj[0][0], obj[0][1], ' ')
    win.addch(obj[1][0], obj[1][1], ' ')
    win.addch(obj[2][0], obj[2][1], ' ')
    win.addch(obj[3][0], obj[3][1], ' ')
    

    #calculate colision for left position
    if obj[0][0] == vehicle [0][0] and v_position !=2:
    	collision+=1

    #TODO calculate position for right position


    obj[0][0]+=2
    obj[1][0]+=2
    obj[2][0]+=2
    obj[3][0]+=2


    if obj[2][0]>18 or obj[3][0] >18:
        object_position=random.randint(0,2)
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
        win.addch(vehicle1[0][0], vehicle1[0][1], '*')
        win.addch(vehicle1[1][0], vehicle1[1][1], '*')
        win.addch(vehicle1[2][0], vehicle1[2][1], '*')
        win.addch(vehicle1[3][0], vehicle1[3][1], '*')
        win.addch(vehicle1[4][0], vehicle1[4][1], '*')
        v_position=2

    if key == KEY_LEFT:
    	win.addch(vehicle1[0][0], vehicle1[0][1], ' ')
        win.addch(vehicle1[1][0], vehicle1[1][1], ' ')
        win.addch(vehicle1[2][0], vehicle1[2][1], ' ')
        win.addch(vehicle1[3][0], vehicle1[3][1], ' ')
        win.addch(vehicle1[4][0], vehicle1[4][1], ' ')
        win.addch(vehicle[0][0], vehicle[0][1], '*')
        win.addch(vehicle[1][0], vehicle[1][1], '*')
        win.addch(vehicle[2][0], vehicle[2][1], '*')
        win.addch(vehicle[3][0], vehicle[3][1], '*')
        win.addch(vehicle[4][0], vehicle[4][1], '*')
        v_position=1

    if True:    
        if object_position==1:
            old_obj_left = obj
            if animation == 0:
                win.addch(old_obj_left[0][0], old_obj_left[0][1], '#')
                win.addch(old_obj_left[1][0], old_obj_left[1][1], '#')
                win.addch(old_obj_left[2][0], old_obj_left[2][1], '#')
                win.addch(old_obj_left[3][0], old_obj_left[3][1], '#')
                animation = 1
            else:
                win.addch(old_obj_left[0][0], old_obj_left[0][1], '@')
                win.addch(old_obj_left[1][0], old_obj_left[1][1], '&')
                win.addch(old_obj_left[2][0], old_obj_left[2][1], '@')
                win.addch(old_obj_left[3][0], old_obj_left[3][1], '&')
                animation = 0
            del old_obj_left
        if object_position==2:
            obj_right=[[obj[0][0],15],[obj[1][0],16],[obj[2][0],15],[obj[3][0],16]]
            if animation == 0:
                win.addch(obj_right[0][0], obj_right[0][1], '#')
                win.addch(obj_right[1][0], obj_right[1][1], '#')
                win.addch(obj_right[2][0], obj_right[2][1], '#')
                win.addch(obj_right[3][0], obj_right[3][1], '#')
                animation = 1
            else:
                win.addch(obj_right[0][0], obj_right[0][1], '@')
                win.addch(obj_right[1][0], obj_right[1][1], '&')
                win.addch(obj_right[2][0], obj_right[2][1], '@')
                win.addch(obj_right[3][0], obj_right[3][1], '&')
                animation = 0
            del obj_right
            
curses.endwin()

