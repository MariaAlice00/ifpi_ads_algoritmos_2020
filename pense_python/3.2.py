def do_twice(a, b):
    a(b)
    a(b)

def print_twice(b):
    print(b)
    print(b)

def do_four(a, b):
    do_twice(a, b)
    do_twice(a, b)

print('')
do_twice(print, 'spam')
print('')
do_four(print, 'spam')
print('')