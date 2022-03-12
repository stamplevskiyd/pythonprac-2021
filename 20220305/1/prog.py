import cmd
import readline
import shlex


class Cell:
    def __init__(self, X, Y, monster_n, monster_h):
        self.x = X
        self.y = Y
        self.monster_name = monster_n
        self.health = monster_h


# add monster name <имя монстра> hp <число очков здоровья> coords <X> <Y>
#  -1     0     1       2        3       4                  5      6   7

class Game(cmd.Cmd):
    field_width = 10
    field_height = 10
    prompt = '> '

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.field = [[[] for x in range(Game.field_width)]
                      for y in range(Game.field_height)]
        self.player_x = 0
        self.player_y = 0

    def do_add(self, arg):
        args = shlex.split(arg)
        if len(args) != 8 or args[:2] != ['monster', 'name']:
            print("Correct format is: 'add monster name <monster_name> hp <hp_count> coords <X> <Y>'")
            return
        monster_name = args[2]  # если имя монстра из нескольких слов, оно - в кавычках
        if args[3] != 'hp':
            print("Correct format is: 'add monster name <monster_name> hp <hp_count> coords <X> <Y>'")
            return
        hp = int(args[4])
        if args[5] != 'coords':
            print("Correct format is: 'add monster name <monster_name> hp <hp_count> coords <X> <Y>'")
            return
        x, y = int(args[6]), int(args[7])
        self.field[x][y].append(Cell(x, y, monster_name, hp))

    def do_show(self, arg):
        args = shlex.split(arg)
        if len(args) != 1 or args[0] != 'monsters':
            print("Correct format is 'show monsters'")
            return
        for i in range(Game.field_height):
            for j in range(Game.field_width):
                if self.field[i][j].monster:
                    print(f"{self.field[i][j].monster} at ({self.field[i][j].x} {self.field[i][j].y}) hp {self.field[i][j].health}")

    def do_move(self, arg):
        args = shlex.split(arg)
        if len(args) != 1:
            print("Correct format is 'move <direction>")
            return
        direction = args[0]
        if direction == 'up':
            if self.player_y - 1 < 0:
                print("cannot move")
                return
            self.player_y -= 1
        elif direction == 'down':
            if self.player_y + 1 >= Game.field_height:
                print("cannot move")
                return
            self.player_y += 1
        elif direction == 'left':
            if self.player_x - 1 < 0:
                print("cannot move")
                return
            self.player_x -= 1
        elif direction == 'right':
            if self.player_y + 1 >= Game.field_width:
                print("cannot move")
                return
            self.player_x += 1
        else:
            print("Unknown direction")
            return
        print(f"player at {self.player_x} {self.player_y}")
        if self.field[self.player_x][self.player_y]:
            for monster in self.field[self.player_x][self.player_y]:
                print(f"{monster.monster_name} {monster.health} hp")

    def do_exit(self, args):
        print('Bye!')
        return True


Game().cmdloop()
