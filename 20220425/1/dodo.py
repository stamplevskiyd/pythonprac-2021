DOIT_CONFIG = {'default_tasks': ['translate', 'test', 'wheel', 'source_dist', 'cleanup']}


def task_translate():
    return {
        "actions": ["pybabel extract -o po/solver.pot --input-dirs=.",
                    "pybabel update -l ru -D solver -i po/solver.pot -d po",
                    "pybabel compile -l ru -D solver -d po"],
        "file_dep": ["solver.py"],
        'targets': ['po/solver.pot', 'po/ru/LC_MESSAGES/solver.mo'],
        "clean": True,
    }


def task_test():
    return {
        "actions": ["python3 -m unittest -v"],
    }


def task_wheel():
    return {
        "actions": ["python3 -m build -w"],
        "file_dep": ["solver.py", "po/ru/LC_MESSAGES/solver.mo"],
        "targets": ["dist/solver-0.0.1-py3-none-any.whl"]
    }


def task_cleanup():
    return {
        "actions": ["rm po/solver.pot",
                    "rm po/ru/LC_MESSAGES/solver.mo"]
    }


def task_source_dist():
    return {
        "actions": ["python3 -m build -s"],
        "file_dep": ["task.py", "po/ru/LC_MESSAGES/solver.mo"],
        "targets": ["dist/prog-0.0.1.tar.gz"]
    }