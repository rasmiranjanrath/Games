import curses
from curses import KEY_LEFT, KEY_RIGHT

curses.initscr()
win=curses.newwin(20, 60, 0, 0)
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(1)

key = KEY_RIGHT                                                    # Initializing values
score = 0
while True:
	win.border(0)
