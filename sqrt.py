def sqrt(x, guess=1.0, tolerance=0.001):
    """
    Calculate the square root of a number using a recursive approach.

    Description:
    This function uses the Newton-Raphson method to iteratively
    approximate the square root of a given number.

    Args:
    x (float): The number to calculate the square root of.
    guess (float, optional): Initial guess for the square root. Defaults to 1.0.
    tolerance (float, optional): Acceptable error margin. Defaults to 0.001.

    Returns:
    float: The approximated square root of x.

    Operations:
    1. Check if the current guess is within the acceptable tolerance.
    2. If not, calculate a new guess using the Newton-Raphson formula.
    3. Recursively call the function with the new guess until tolerance is met.
    """
    if abs(guess * guess - x) < tolerance:
        return guess
    
    new_guess = (guess + x / guess) / 2
    return sqrt(x, new_guess, tolerance)



if __name__ == "__main__":
    # Example usage:
    result = sqrt(16)
    print(result)  # Output will be close to 4



