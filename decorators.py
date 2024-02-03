# wrappers function (also called decorators) are used to modify or extend the behavior of an existing function
def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function...")
    return wrapper
# @announce to add the announce decorator to this function
@announce
def hello():
    print("Hello, everyone!")

hello()