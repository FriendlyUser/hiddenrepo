
def fact_rec(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact_rec(n - 1)


class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0.0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__account_balance}")
        else:
            print("Invalid deposit amount. Amount must be greater than 0.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__account_balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def display_balance(self):
        print(f"Account Balance for {self.__account_holder_name}: ${self.__account_balance}")


def is_leap_year(year):
    if (year % 400 == 0) and (year % 100 == 0):
        return True
    elif (year % 4 == 0) and (year % 100 != 0):
        return True
    else:
        return False


class Player:
    def play(self):
        print("The player is playing cricket.")


class Batsman(Player):
    def play(self):
        print("The batsman is batting.")


class Bowler(Player):
    def play(self):
        print("The bowler is bowling.")


def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda x: x.cgpa, reverse=True)
    return sorted_students


class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa


def binary_search_product(product_list, target_product):
    """Searches for all occurrences of a target product in an unsorted list of products using binary search.

    Args:
        product_list: An unsorted list of product names.
        target_product: The product to search for.

    Returns:
        A list of original indices where the target product is found, or an empty list if not found.
    """
    # Pair each product with its original index
    indexed_products = [(product, index) for index, product in enumerate(product_list)]
    
    # Sort the products based on product names while keeping the original indices
    indexed_products.sort(key=lambda x: x[0])

    indices = []
    left = 0
    right = len(indexed_products) - 1

    # Binary search on the sorted products
    while left <= right:
        mid = (left + right) // 2

        if indexed_products[mid][0] == target_product:
            # Add the original index to the result
            indices.append(indexed_products[mid][1])
            
            # Search for other occurrences to the left and right
            i = mid - 1
            while i >= 0 and indexed_products[i][0] == target_product:
                indices.append(indexed_products[i][1])
                i -= 1
            i = mid + 1
            while i < len(indexed_products) and indexed_products[i][0] == target_product:
                indices.append(indexed_products[i][1])
                i += 1
            break  # Exit the outer loop after finding all occurrences
        elif indexed_products[mid][0] < target_product:
            left = mid + 1
        else:
            right = mid - 1

    # Return the indices in ascending order
    return sorted(indices)



def main():
    # Test factorial functionality
    number = 5  # Example fixed input
    print("Factorial Testing:")
    res = fact_rec(number)
    print("The number of factorial of {} is {}.\n".format(number, res))

    # Test bank account functionality
    print("Bank Account Testing:")
    my_account = BankAccount("12345", "Dinesh", 1000.0)
    my_account.display_balance()
    my_account.deposit(500.0)
    my_account.withdraw(200.0)
    my_account.display_balance()
    print()

    # Test leap year functionality
    year = 2000
    print("Leap Year Testing:")
    if is_leap_year(year):
        print("{0} is a leap year\n".format(year))
    else:
        print("{0} is not a leap year\n".format(year))

    # Test player functionality
    print("Player (Cricket) Testing:")
    batsman = Batsman()
    bowler = Bowler()
    batsman.play()
    bowler.play()
    print()

    # Test student sorting functionality
    print("Student Sorting Testing:")
    students = [
        Student("Alice", "101", 3.8),
        Student("Bob", "102", 3.5),
        Student("Charlie", "103", 3.9),
        Student("David", "104", 3.7),
    ]
    sorted_students = sort_students(students)
    for student in sorted_students:
        print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
    print()

    # Test product search functionality
    print("Product Search Testing:")
    products = ["Apple", "Banana", "Orange", "Apple", "Grapes"]
    target_product = "Apple"
    result = binary_search_product(products, target_product)
    if result:
        print(f"The target product '{target_product}' was found at indices: {result}")
    else:
        print(f"The target product '{target_product}' was not found in the list.")


if __name__ == "__main__":
    main()

