import curses


def adder(a, b):
    return a + b


def shower(n):
    screen = curses.initscr()
    curses.noecho()
    curses.cbreak()
    screen.box()
    screen.addstr(10, 20, str(n))
    screen.getch()
    curses.endwin()


if __name__ == '__main__':
    import sys
    res = adder(sys.argv[1], sys.argv[2])
    shower(res)
