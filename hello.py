def main():
    Hello()
    name = input('What is your name?').strip().title()
    Hello(name)

def Hello(x="World"):
    print('Hello', x)

main()