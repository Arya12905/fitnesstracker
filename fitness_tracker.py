import datetime

def add_workout():
    workout = input("Enter workout type (e.g. Running, Pushups): ")
    duration = int(input("Enter duration in minutes: "))
    calories = duration * 5  # simple formula: 5 calories per min

    log = f"{datetime.datetime.now()} | {workout} | {duration} min | {calories} cal\n"
    with open("fitness_log.txt", "a") as file:
        file.write(log)
    
    print("✅ Workout logged!")

def view_log():
    try:
        with open("fitness_log.txt", "r") as file:
            print("\n📋 Your Fitness Log:")
            print(file.read())
    except FileNotFoundError:
        print("No workout log found yet.")

def menu():
    while True:
        print("\n=== FITNESS TRACKER MENU ===")
        print("1. Add Workout")
        print("2. View Log")
        print("3. Exit")
        choice = input("Choose option (1/2/3): ")

        if choice == "1":
            add_workout()
        elif choice == "2":
            view_log()
        elif choice == "3":
            print("👋 Goodbye! Stay fit 💪")
            break
        else:
            print("❌ Invalid input. Try again.")

if __name__ == "__main__":
    menu()

