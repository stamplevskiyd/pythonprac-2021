DOIT_CONFIG = {'default_tasks': ['extract', 'update', 'compile', 'test']}

def task_extract():
    return {
        "actions": ["pybabel extract -o solver/po/solver.pot solver"],
        "targets": ["solver/po/solver.pot"]
    }

def task_update():
    return {
        "actions": ["pybabel update -D solver -i solver/po/solver.pot -d solver/po -l ru",
                    "pybabel update -D solver -i solver/po/solver.pot -d solver/po -l en"],
        "file_dep": ["solver/po/solver.pot"],
        "targets": ["solver/po/ru/LC_MESSAGES/solver.po"]
    }

def task_compile():
    return {
        "actions": ["pybabel compile -D solver -d solver/po -l ru",
                    "pybabel compile -D solver -d solver/po -l en"],
        "targets": ["solver/po/ru/LC_MESSAGES/solver.mo"]
    }

def task_test():
    return {
        "actions": ["python3 -m test"]
    }
