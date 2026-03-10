# Score Management System
#menu

def show_menu():
    print("\n====== Score Management System ======")
    print("1. Add score")
    print("2. show all")
    print("3. Modify score")
    print("4. Delete score")
    print("0. Exit system")
    print("===========================")

#add

def add_score():
    name = input("Please enter your name：")
    score = input("Please enter the score：")

    with open("scores.txt", "a", encoding="utf-8") as f:
        f.write(f"name={name},score={score}\n")

    print("Added successfully！")

#show all

def show_all():
    print("\nAll scores：")
    try:
        with open("scores.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
            if not lines:
                print("No scores available")
                return
            for line in lines:
                name, score = line.strip().split(",")
                print(f"name: {name},score:{score}\n")
    except:
        print("No scores available")

#modify

def modify_score():
    name = input("Please enter the name of the student to modify：")
    new_score = input("Please enter the new score：")

    lines = []
    found = False

    try:
        with open("scores.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()

        with open("scores.txt", "w", encoding="utf-8") as f:
            for line in lines:
                n, s = line.strip().split(",")
                if n == name:
                    f.write(f"{name},{new_score}\n")
                    found = True
                else:
                    f.write(line)

        if found:
            print("Modify successful！")
        else:
            print("Student not found")
    except:
        print("No score records available")

#delete

def delete_score():
    name = input("Please enter the name of the student to delete：")

    try:
        with open("scores.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()

        with open("scores.txt", "w", encoding="utf-8") as f:
            found = False
            for line in lines:
                n, s = line.strip().split(",")
                if n == name:
                    found = True
                    continue
                f.write(line)

        if found:
            print("Delete successful！")
        else:
            print("Student not found!")
    except:
        print("No score records found!")

#run
def main():
    while True:
        show_menu()
        choice = input("Please enter a number：")

        if choice == "1":
            add_score()
        elif choice == "2":
            show_all()
        elif choice == "3":
            modify_score()
        elif choice == "4":
            delete_score()
        elif choice == "0":
            print("Exiting system")
            break
        else:
            print("Input error,please try again")

if __name__ == "__main__":
    main()
