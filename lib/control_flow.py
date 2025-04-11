# lib/control_flow.py

def admin_login(username, password):
    """
    Checks if the provided username and password match the admin credentials.

    Args:
        username (str): The username to check.
        password (str): The password to check.

    Returns:
        str: "Access granted" if the credentials are correct, "Access denied" otherwise.
    """
    if (username == "admin" or username == "ADMIN") and password == "12345":
        return "Access granted"
    else:
        return "Access denied"

def hows_the_weather(temperature):
    """
    Describes the weather based on the given temperature.

    Args:
        temperature (int): The temperature in degrees.

    Returns:
        str: A description of the weather.
    """
    if temperature < 40:
        return "It's brisk out there!"
    elif 40 <= temperature <= 65:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"

def fizzbuzz(number):
    """
    Applies the FizzBuzz logic to a given number.

    Args:
        number (int): The number to evaluate.

    Returns:
        str or int: "Fizz" for multiples of 3, "Buzz" for multiples of 5,
                     "FizzBuzz" for multiples of both, otherwise the number itself.
    """
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return number

def calculator(operation, num1, num2):
    """
    Performs a basic arithmetic operation on two numbers.

    Args:
        operation (str): The operation to perform (+, -, *, /).
        num1 (int or float): The first number.
        num2 (int or float): The second number.

    Returns:
        int or float or None: The result of the operation if valid, otherwise None.
                             Also prints an "Invalid operation!" message.
    """
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        print("Invalid operation!")
        return None