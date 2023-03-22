# decorators are part of the functional programming peradmine

def announce(f):
    def wrapper():
        print('about to run the function...')
        f()
        print('done running the function')
    return wrapper

@announce
def hello():
    print("Hello, World!")

hello()

# decorators are used in django
# where the decorators sometimes take functions and check that if the user is logged in or not
# and depending on that the decorator might run or not run the function