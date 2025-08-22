def print_result(a, b, operation_name, result):
    print(f"\n--- {operation_name} ---")
    print(f"Operand A: {a} (binary: {bin(a)})")
    print(f"Operand B: {b} (binary: {bin(b)})")
    print(f"Result   : {result} (binary: {bin(result)})\n")


def bitwise_and(a, b):
    return a & b

def bitwise_or(a, b):
    return a | b

def bitwise_xor(a, b):
    return a ^ b

def bitwise_not(a):
    return ~a

def bitwise_left_shift(a, shift):
    return a << shift

def bitwise_right_shift(a, shift):
    return a >> shift


def main():
    while True:
        print("Choose a bitwise operation:")
        print("1. AND (&)")
        print("2. OR (|)")
        print("3. XOR (^)")
        print("4. NOT (~)")
        print("5. Left Shift (<<)")
        print("6. Right Shift (>>)")
        print("0. Exit")

        choice = input("Enter your choice (0-6): ")

        if choice == "0":
            print("Exiting the program.")
            break

        if choice in ["1", "2", "3"]:
            a = int(input("Enter first integer (A): "))
            b = int(input("Enter second integer (B): "))

            if choice == "1":
                result = bitwise_and(a, b)
                print_result(a, b, "AND", result)

            elif choice == "2":
                result = bitwise_or(a, b)
                print_result(a, b, "OR", result)

            elif choice == "3":
                result = bitwise_xor(a, b)
                print_result(a, b, "XOR", result)

        elif choice == "4":
            a = int(input("Enter integer (A): "))
            result = bitwise_not(a)
            print(f"\n--- NOT ---")
            print(f"Operand A: {a} (binary: {bin(a)})")
            print(f"Result   : {result} (binary: {bin(result & 0xffffffff)})\n")  # Mask for 32-bit display

        elif choice == "5":
            a = int(input("Enter integer (A): "))
            shift = int(input("Enter number of bits to shift left: "))
            result = bitwise_left_shift(a, shift)
            print(f"\n--- LEFT SHIFT ---")
            print(f"A        : {a} (binary: {bin(a)})")
            print(f"Shift by : {shift}")
            print(f"Result   : {result} (binary: {bin(result)})\n")

        elif choice == "6":
            a = int(input("Enter integer (A): "))
            shift = int(input("Enter number of bits to shift right: "))
            result = bitwise_right_shift(a, shift)
            print(f"\n--- RIGHT SHIFT ---")
            print(f"A        : {a} (binary: {bin(a)})")
            print(f"Shift by : {shift}")
            print(f"Result   : {result} (binary: {bin(result)})\n")

        else:
            print("Invalid choice. Please select a valid option (0-6).\n")


if __name__ == "__main__":
    main()
