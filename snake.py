import curses
from random import randint

def create_food(snake, box):
    food = None
    while food is None:
        food = [randint(box[0]+1, box[1]-1), randint(box[2]+1, box[3]-1)]
        if food in snake:
            food = None
    return food

def main(stdscr):
    curses.curs_set(0)
    stdscr.timeout(100)

    sh, sw = stdscr.getmaxyx()
    w = curses.newwin(sh, sw, 0, 0)
    w.keypad(1)
    w.timeout(100)

    box = [3, sh-3, 3, sw-3]
    snake = [
        [sh//2, sw//2 + 1],
        [sh//2, sw//2],
        [sh//2, sw//2 - 1]
    ]

    direction = curses.KEY_RIGHT

    for y, x in snake:
        w.addch(y, x, "*")

    food = create_food(snake, box)
    w.addch(food[0], food[1], "#")

    while True:
        key = w.getch()

        if key not in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_UP, curses.KEY_DOWN]:
            break

        if (
            (direction == curses.KEY_RIGHT and key == curses.KEY_LEFT) or
            (direction == curses.KEY_LEFT and key == curses.KEY_RIGHT) or
            (direction == curses.KEY_UP and key == curses.KEY_DOWN) or
            (direction == curses.KEY_DOWN and key == curses.KEY_UP)
        ):
            key = direction

        new_head = [snake[0][0], snake[0][1]]

        if key == curses.KEY_DOWN:
            new_head[0] += 1
        elif key == curses.KEY_UP:
            new_head[0] -= 1
        elif key == curses.KEY_LEFT:
            new_head[1] -= 1
        elif key == curses.KEY_RIGHT:
            new_head[1] += 1

        snake.insert(0, new_head)

        if (
            new_head[0] in [box[0], box[1]] or
            new_head[1] in [box[2], box[3]] or
            new_head in snake[1:]
        ):
            break

        if new_head == food:
            food = create_food(snake, box)
            w.addch(food[0], food[1], "#")
        else:
            tail = snake.pop()
            w.addch(tail[0], tail[1], ' ')

        w.addch(snake[0][0], snake[0][1], "*")

    w.addstr(sh//2, sw//2 - 5, "Game Over", curses.A_BOLD)
    w.refresh()
    w.getch()

curses.wrapper(main)
