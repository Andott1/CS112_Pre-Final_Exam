def intro_header():  # Title and info about program
    print("\n-- CS112: COMPUTER PROGRAMMING 1 - PRE-FINAL EXAM --")
    print("Created by: Kurt Andre L. Olaer\n")
    print("About: This program displays all prime numbers within a range\n")
    print("Note: Type \"0\" to terminate program\n")


def check_primes(num):  # Check if the number is a prime number
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def display_primes(start, end):  # Collect and print the prime numbers
    primes_list = []
    for num in range(start, end + 1):
        if check_primes(num):
            primes_list.append(num)

    print("\nPrime numbers between " + str(start) + " and " + str(end) + " are:\n" + str(primes_list) + "\n")


def main():  # Main program flow
    intro_header()
    while True:
        try:
            while True:  # Ask for start integer
                start_number = int(input("Enter a number [start]: "))
                if start_number == 0:
                    print("\n- Program Terminated -")
                    exit()

                if start_number < 0:
                    print("Enter a non-negative number.\n")
                else:
                    break

            while True:  # Ask for end integer
                end_number = int(input("Enter a number [end]: "))
                if end_number == 0:
                    print("\n- Program Terminated -")
                    exit()

                if end_number <= start_number:
                    print("Enter a number greater than " + str(start_number) + ".\n")
                else:
                    break

            display_primes(start_number, end_number)

            while True:  # Ask user to input again
                response = input("Do you want to input again? (yes/no): ").lower()

                if response in ["yes", "no"]:
                    break
                elif response == "0":
                    print("\n- Program Terminated -")
                    exit()
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.\n")

            if response != "yes":
                print("\n- Program Terminated -")
                exit()
            else:
                print("")

        except ValueError:
            print("Invalid input. Please enter a valid integer.\n")


if __name__ == "__main__":  # Call main() if the script is the main program
    main()
