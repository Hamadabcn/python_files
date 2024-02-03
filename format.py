import re
name = input("What's your name? ").strip()
# := walrus operator to asign a value from right to left and ask a boolean question about it
if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)
print(f"Hello, {name}")