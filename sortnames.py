names = []
for _ in range(10):
    names.append(input("What is your name? "))
for name in sorted(names):
    print(f"hello, {name}")