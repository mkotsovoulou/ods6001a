import check50  # import the check50 module

@check50.check()  # tag the function below as check50 check
def exists():  # the name of the check
    """Is your file saved as assignment6.py"""  # this is what you will see when running check50
    check50.exists("assignment6.py")  # the actual check

@check50.check(exists)
def main_test():
    """Does the program display the output correctly ?"""
    from re import match
    expected = "21 9 8\n"
    actual = check50.run("python3 assignment6.py").stdout()
    """21 9 8 is the correct output"""
    if "21" in actual and "9" not in actual:
        help = r"Almost! You found all students but not the common one!"
        if not match(expected, actual):
            raise check50.Mismatch("21 9 8\n", actual, help=help)

    if "21" in actual and "8" not in actual:
        help = r"Almost! You found all students but not the different ones!"
        if not match(expected, actual):
            raise check50.Mismatch("21 9 8\n", actual, help=help)

    if not match(expected, actual):
        help = r"Result not wait expected..."
        raise check50.Mismatch("21 9 8\n", actual, help=help)

