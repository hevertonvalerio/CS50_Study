name = input("whta's your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Daco":
        print("Slytherin")
    case _:
        print("Who?")