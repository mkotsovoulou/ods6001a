from re import match
import check50  # import the check50 module

@check50.check()  # tag the function below as check50 check
def exists():  # the name of the check
    """Is your file saved as lab3_1.py?"""  # this is what you will see when running check50
    check50.exists("lab3_1.py")  # the actual check


@check50.check(exists)  # only run this check if the exists check has passed
def test2(exists):
    """Does the calculate the average correctly ?"""
    from re import match
    # check50.run("python3 lab3_1.py").stdout("6.33\n").exit(0)
    expected = "6.33\n"
    actual = check50.run("python3 lab3_1.py").stdout()
    help = None
    if actual == '6.333333333333333':
        help = r"Did you forget to format the output using two decimals?"
    if not match(expected, actual):
        help = None
    raise check50.Mismatch("6.33\n", actual, help=help)
