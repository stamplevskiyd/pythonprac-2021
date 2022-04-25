DOIT_CONFIG = {'default_tasks': ['diagram']}

def task_diagram():
    """Convert dot diagramm to png"""

    return {
        'actions': ['dot  -Tpng diagram.dot -o diagram.png'],
        'file_dep': ['diagram.dot'],
        'targets': ["diagram.png"],
    }


def task_icon():
    """Create an icon"""
    iname = "proj/icon.png"
    return {
        'actions': [f'convert diagram.png -crop 200x200+100+100 -resize 64x64 {iname}'],
        'file_dep': ['diagram.png'],
        'targets': [f'{iname}'],
    }


def task_cleanup():
    """Remove all"""

    return {
        'actions': ['rm -f *.png'],
    }

def task_show():
    return {
        'actions': ["eom icon.png"],
    }
