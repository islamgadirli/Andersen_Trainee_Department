def task_line_one():
    number = int(input("Enter a number: "))
    if number > 7:
        print("Hello")
    else:
        print("Number is not greater than 7")


def task_line_two():
    name = input("Enter a name: ")
    if name == "John":
        print("Hello, John")
    else:
        print("There is no such name")


def task_line_three():
    length = int(input("Enter array length: "))

    array = []
    print("Enter", length, "numbers:")

    for _ in range(length):
        array.append(int(input()))

    print("Numbers divisible by 3:")
    for num in array:
        if num % 3 == 0:
            print(num, end=" ")

    print() 


def main():
    print("Line 1")
    task_line_one()

    print("\nLine 2")
    task_line_two()

    print("\nLine 3")
    task_line_three()


if __name__ == "__main__":
    main()
