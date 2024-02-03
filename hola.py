def main():
    name = input("What is your name? ")
    print(hola(name))
    
def hola(to="world"):
    return f"Hola, {to}"

if __name__ == "__main__":
    main()