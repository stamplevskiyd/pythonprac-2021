import pyfiglet
import locale
import os.path
import gettext

locale.setlocale(locale.LC_ALL, locale.getlocale())
translation = gettext.translation(
    'solver', os.path.join(os.path.dirname(__file__), 'solver'))
_ = translation.gettext


def solve(a, b):
    return -b / a if a else None


if __name__ == '__main__':
    figlet = pyfiglet.Figlet('graceful')
    a, b = input().split()
    res = solve(int(a), int(b))
    if res is not None:
        output = _("Root: {}").format(res)
    else:
        output = _("NO ROOTS")

    print(figlet.renderText(output))
