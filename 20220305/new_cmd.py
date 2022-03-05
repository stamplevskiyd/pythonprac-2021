import readline
import shlex
import cmd

class repl(cmd.Cmd):
    prompt = "> "

    def do_perform(self, arg):
        """
Variants:
         perform show arg
         perform sing arg
         """
        args = shlex.split(arg)
        if args[0] == 'sing':
            print('-'.join(args[1:]))
        elif args[0] == 'show':
            print(' '.join(args[1:]).upper())
        else:
            print(f"Do not know how to {args[0]}")

    def complete_perform(self, prefix, allcomand, beg, end):
        return [s for s in ("sing", "show") if s.startswith(prefix)]

    def do_exit(self, arg):
        return True

repl().cmdloop()
