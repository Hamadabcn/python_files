def hello(to="world"):
    print ("Hello,", to)
    
hello()

# Ask user for his name remove whitespace and capitalize user's name
name = input("What is your name ").strip().title()

# Split username into first and last name
first, last = name.split(" ")

# Say hello to user
print(f"Hello, Dear. {first}")