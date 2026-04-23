import csv
import os
from datetime import datetime
import sys

history = []


def save_to_history(operation, result):
    history.append(
        {
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "operation": operation,
            "result": result,
        }
    )


def export_to_csv(filename="history.csv"):
    if not history:
        return False
    try:
        file_exists = os.path.exists(filename)

        with open(filename, "a", newline="") as csvfile:
            list = ["time", "operation", "result"]
            writer = csv.DictWriter(csvfile, fieldnames=list)
            if not file_exists:
                writer.writeheader()
            writer.writerows(history)
        return True
    except Exception as e:
        print(f"Error exporting to CSV: {e}")
        return False


def main():
    print("\n1.Add 2.Subtract 3.Multiply 4.Divide 5.operation(BODMAS) 6.Exit")
    choice = input("\nEnter your choice (1-5):")

    if choice in ["1", "2", "3", "4"]:
        x = int(input("Enter first number:"))
        y = int(input("Enter second number:"))

        if choice == "1":
            result = x + y
            print(f"Result: {int(result) if result == int(result) else float(result)}")
            save_to_history(f"{x} + {y}", result)
        elif choice == "2":
            result = x - y
            print(f"Result: {int(result) if result == int(result) else float(result)}")
            save_to_history(f"{x} - {y}", result)
        elif choice == "3":
            result = x * y
            print(f"Result: {int(result) if result == int(result) else float(result)}")
            save_to_history(f"{x} * {y}", result)
        elif choice == "4":
            if y == 0:
                print("Error: Cannot divide by zero")
            else:
                result = x / y
                print(
                    f"Result: {int(result) if result == int(result) else float(result)}"
                )
                save_to_history(f"{x} / {y}", result)

    elif choice == "5":
        operation = input("Enter an operation (e.g. 10 + 5 * 2):")
        try:
            result = eval(operation)
            print(f"Result: {int(result) if result == int(result) else float(result)}")
            save_to_history(operation, result)
        except:
            print("Invalid operation. Please try again")

    elif choice == "6":
        print("Exiting")
        sys.exit()
    else:
        print("Invalid choice. Please select 1-5")

    export_to_csv()
    main()


if __name__ == "__main__":
    main()
