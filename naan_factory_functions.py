# Define functions here

# Functions aren't called here as this will violate the separation of concerns
# and they will be run elsewhere

def make_dough(arg1, arg2):
    if arg1 == 'wheat' and arg2 == 'flour':
        return 'dough'
    else:
        return "Err 1"

def bake_dough(arg1):
    if arg1 == 'dough':
        return 'naan'
    else:
        return "Err2"

def run_factory(arg1, arg2):
    dough = make_dough()

    if dough == 'dough':
        return (bake_dough(dough))
    else:
        return dough