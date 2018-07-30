from switch_reverser import list_check


def main():
    global run
    run = True
    values = []
    while run:
        print("Enter exit to stop")
        value = input("Please insert items : ")
        if value.lower() == "exit":
            run = False
            return
        else:
            try:
                values.append(int(value))
            except ValueError:
                values.append(str(value))
            print(list_check(values))


if __name__ == "__main__":
    main()
