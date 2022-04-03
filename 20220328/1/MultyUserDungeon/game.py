"""Module for game commandline."""

import cmd
import shlex
from MultyUserDungeon import field


class Game_Cmd(cmd.Cmd):
    """Commandline module."""

    prompt = field.prompt

    def __init__(self):
        """Init game using field information."""
        cmd.Cmd.__init__(self)
        self.field = [[[] for x in range(field.field_width)]
                      for y in range(field.field_height)]
        self.player_x = 0
        self.player_y = 0

    def do_add(self, arg):
        """Add monster to given cell."""
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
        self.field[x][y].append(field.Cell(x, y, monster_name, hp))

    def do_show(self, arg):
        """Show monsters at player's position."""
        args = shlex.split(arg)
        if len(args) != 1 or args[0] != 'monsters':
            print("Correct format is 'show monsters'")
            return
        for i in range(field.field_height):
            for j in range(field.field_width):
                for monster in self.field[i][j]:
                    print(f"{monster.monster_name} at ({monster.x} {monster.y}) hp {monster.health}")

    def do_move(self, arg):
        """Move player by one cell."""
        args = shlex.split(arg)
        if len(args) != 1:
            print("Correct format is 'move <direction>'")
            return
        direction = args[0]
        if direction == 'up':
            if self.player_y - 1 < 0:
                print("cannot move")
                return
            self.player_y -= 1
        elif direction == 'down':
            if self.player_y + 1 >= field.field_height:
                print("cannot move")
                return
            self.player_y += 1
        elif direction == 'left':
            if self.player_x - 1 < 0:
                print("cannot move")
                return
            self.player_x -= 1
        elif direction == 'right':
            if self.player_y + 1 >= field.field_width:
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

    def do_attack(self, arg):
        """Attack monster in player's cell."""
        args = shlex.split(arg)
        if len(args) != 1:
            print("Correct format is 'attack <monster name>'")
            return
        monster = args[0]
        monster_id = -1
        for i in range(len(self.field[self.player_x][self.player_y])):  # там не список строк, простой index не поможет
            if self.field[self.player_x][self.player_y][i].monster_name == monster:
                monster_id = i
                break
        if monster_id < 0:
            print(f"no {monster} here")
            return
        self.field[self.player_x][self.player_y][monster_id].health -= 10
        if self.field[self.player_x][self.player_y][monster_id].health > 0:
            print(f"{monster} lost 10 hp, now has {self.field[self.player_x][self.player_y][monster_id].health} hp")
        else:
            print(f"{monster} dies")
            self.field[self.player_x][self.player_y].pop(monster_id)  # оно есть в списке в любом случае

    def complete_add(self, prefix, allcomand, beg, end):
        """Add method autocomplete."""
        args = shlex.split(allcomand)
        if len(args) == 1:  # только add, префикса быть не может
            return ['monster']
        if len(args) == 2:
            if prefix:
                return ['monster'] if 'monster'.startswith(prefix) else ''
            else:
                return ['name']
        elif len(args) == 3:
            if prefix:
                return ['name'] if 'name'.startswith(prefix) else ''
        elif len(args) == 4:
            if not prefix:
                return ['hp']
        elif len(args) == 5:
            if prefix:
                return ['hp'] if 'hp'.startswith(prefix) else ''
        elif len(args) == 6:
            if not prefix:
                return ['coords']
        elif len(args) == 7:
            if prefix:
                return ['coords'] if 'coords'.startswith(prefix) else ''

    def complete_show(self, prefix, allcomand, beg, end):
        """Show method autocomplete."""
        return ['monsters'] if 'monsters'.startswith(prefix) else ''

    def complete_move(self, prefix, allcomand, beg, end):
        """Move method autocomplete."""
        return [s for s in ['up', 'down', 'left', 'right'] if s.startswith(prefix)]

    def complete_attack(self, prefix, allcomand, beg, end):
        """Attack method autocomplete."""
        monsters = [monster.monster_name for monster in self.field[self.player_x][self.player_y]]
        return [monster if len(monster.split()) == 1 else repr(monster)
                for monster in monsters if monster.startswith(prefix)]

    def do_exit(self, args):
        """Exit processing."""
        print('Bye!')
        return True
