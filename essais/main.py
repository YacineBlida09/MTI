# File: python/main.py

print("Hello Fedora + VS Code + Python!")
print("Hello Fedora " + "VS Code" + " \n Python!")
for i in range(1, 10):
    print("siu", end="")


def siumeter(n):
    if n > 10:
        print("don't push your luck next time!")
    elif n < 1:
        print("clever much?")
    else:
        for i in range(0, n):
            print("siu")


usrin = int(input("\nyou only get one chance (for the beta program) give a number\n"))
siumeter(usrin)

