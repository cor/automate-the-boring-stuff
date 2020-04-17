def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1


def positive_int_input():
    number = None
    while number is None:
        try:
            number = int(input())
        except ValueError:
            print("ERROR: Please enter a positive number.")
            continue
        if number < 0:
            print("ERROR: Please enter a POSITIVE number.")
            continue
    return number


print("Enter a positive number to apply the Collatz sequence on:")
n = positive_int_input()

while n != 1:
    n = collatz(n)
    print(n)
