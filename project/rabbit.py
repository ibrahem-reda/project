def main():
    print("Welcome to place the rabbit ..\n")

    rabbit=[['🍀','🍀','🍀'],['🍀','🍀','🍀'],['🍀','🍀','🍀']]

    print(f"{rabbit[0]}\n{rabbit[1]}\n{rabbit[2]}")
    print("\nWhere should the raabbit go? 🐇")

    choose = get_choose()

    row    = int(choose[0])-1
    column = int(choose[1])-1
    
    rabbit[row][column] = '🐇'

    print("\n Success .....\n")
    print(f"{rabbit[0]}\n{rabbit[1]}\n{rabbit[2]}")
    input("\nExit ...")


def get_choose():
    while True:
        try:
            h = input("Please choose a row and a column: ")
            if len(h) == 2:
                row = int(h[0])
                col = int(h[1])
                if row in [1,2,3] and col in[1,2,3]:
                    return h
        except:
            pass

main()