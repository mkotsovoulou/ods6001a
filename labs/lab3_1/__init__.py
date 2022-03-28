from re import match
import check50  # import the check50 module

@check50.check()  # tag the function below as check50 check
def exists():  # the name of the check
    """Is your file saved as lab3_1.py?"""  # this is what you will see when running check50
    check50.exists("lab3_1.py")  # the actual check


@check50.check(exists)  # only run this check if the exists check has passed
def function_test(exists):
    """Does the function return correct results? """
    expected = "2.0\n"
    result = check50.run(
        "python -c \"from lab3_1 import avg_digits; print(avg_digits(\'123\'))\"").stdout()

    if result != expected:
        help = "Have a look at the code in the function... "
        raise check50.Mismatch(expected, result, help=help)


# only run this check if the exists check has passed
@check50.check(exists)
def main_test(exists):
    """Does the program display the average correctly ?"""
    from re import match
    # check50.run("python3 lab3_1.py").stdout("6.33\n").exit(0)
    expected = "6.33\n"
    actual = check50.run("python3 lab3_1.py").stdin("PYnative29@#8496").stdout()

    if actual == '6.333333333333333':
        help = r"Almost! Did you forget to format the output using two decimals?"
    if not match(expected, actual):
        raise check50.Mismatch("6.33\n", actual, help=help)



