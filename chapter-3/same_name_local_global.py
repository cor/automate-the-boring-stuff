def spam():
    global eggs
    eggs = 'spam' # global variable

def bacon():
    eggs = 'bacon' # local variable

def ham():
    print(eggs)

eggs = 42
spam()
bacon()
print(eggs)