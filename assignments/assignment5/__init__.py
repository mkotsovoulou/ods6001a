import check50  # import the check50 module

@check50.check()  # tag the function below as check50 check
def exists():  # the name of the check
    """Is your file saved as assignment5.py"""  # this is what you will see when running check50
    check50.exists("assignment5.py")  # the actual check


@check50.check(exists)
def existsresults():  # the name of the check
    """Does your program produce a results.txt file?"""  # this is what you will see when running check50
    check50.exists("results.txt")  # the actual check

@check50.check(exists)
def main_test(exists):
    """Does the program display profit correctly ?"""
    from re import match
    expected = "17214\n"
    actual = check50.run("python3 assignment5.py").stdout()

    if actual == '17213.929999999993' or actual == '-17213.929999999993':
        help = r"Almost! Did you forget to round the output to the nearest integer?"
        if not match(expected, actual):
            raise check50.Mismatch("17214\n", actual, help=help)

    if actual == '-17214\n':
        help = r"Getting Close... Are you sure the sign is correct ?"
        if not match(expected, actual):
            raise check50.Mismatch("17214\n", actual, help=help)

    if not match(expected, actual):
        help=None
        raise check50.Mismatch("17214\n", actual, help=help)
