import ipsedixit
import sys

if __name__ == '__main__':
    if len(sys.argv) == 2:  # только число параграфов
        generator = ipsedixit.Generator()
        paragraphs = generator.paragraphs(int(sys.argv[1]))
        print('\n\n'.join(paragraphs))
    elif len(sys.argv) == 3:
        if sys.argv[2] in ('caesar', 'tacitus'):
            text = sys.argv[2]  # ipsedixit знает, где их искать
        else:
            try:
                with open(sys.argv[2], 'rt') as word_base:
                    text = word_base.read()
            except FileNotFoundError as E:
                print("Error! This file does not exist")
                sys.exit()
        generator = ipsedixit.Generator(text)
        paragraphs = generator.paragraphs(int(sys.argv[1]))
        print('\n\n'.join(paragraphs))
    else:
        print("Wrong input. Required 1 or 2 arguments")
