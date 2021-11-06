# Factors of a Number
# Python 3.5.1
# Written by alfredmuffin


def get_num():
    while True:
        try:
            user_num = int(input("\nEnter a number: "))
        except ValueError:
            print("That's not a number.\n")
            continue
        else:
            break
    return user_num


def factor(num):
    # return a list of factors of integer input
    if num == 0:
        return [0]

    else:
        factor_list = []
        for item in range(1, abs(num) // 2 + 1):
            # upper limit is 1 greater than abs(num) to account for negative integers
            if num % item == 0:
                factor_list.append(item)
        factor_list.append(abs(num))

        if num < 0:
            # for negative intger input, the final factor list must include the negation of every number in the original list
            new_factor_list = list(factor_list)
            for item in factor_list:
                new_factor_list.insert(0, item * -1)

            return new_factor_list

        return factor_list


def print_factors(num):
    if num == 0:
        print("0 has infinitely many factors\n")
        return

    else:
        # create empty string to print elements of list, separated by commas, and excluding the list brackets
        factor_string = ""
        factors = factor(num)
        for number in factors:
            factor_string += str(number)
            # len(factors) - 1 to exclude comma after final element in list
            if factors.index(number) < len(factors) - 1:
                factor_string += ", "
        print("\nThese are the factors of {0}:".format(num))
        print(factor_string, "\n")

    # if num is prime, there will only be two elements in its factor list
    if len(factors) == 2:
        print("{0} is a prime number!\n".format(num))


print_factors(get_num())
factors_fixed.py
def get_number_from_user():
    while True:
        try:
            user_number = int(input("\nEnter a number: "))
            break
        except ValueError:
            print("That's not a number.\n")
    return user_number


def find_factors(number):
    if number == 0:
        return [0]
    # can search only in first half of dividers
    # because there's no factors after it for sure
    factors = [divider for divider in range(1, abs(number) // 2 + 1)
               if not number % divider]
    factors.append(abs(number))
    if number < 0:
        factors += [-item for item in factors]
    return factors


def print_factors(number):
    if number == 0:
        print("0 has infinitely many factors\n")
        return
    factors = find_factors(number)
    str_factors = [str(factor) for factor in factors]
    factors_formatted = ', '.join(str_factors)
    print(f"\nThese are the factors of {number}:")
    print(factors_formatted, "\n")
    if len(factors) == 2:
        print(f"{number} is a prime number!\n")


if __name__ == '__main__':
    user_input = get_number_from_user()
    print_factors(user_input)