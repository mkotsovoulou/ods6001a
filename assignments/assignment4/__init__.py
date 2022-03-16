import check50  # import the check50 module

@check50.check()  # tag the function below as check50 check
def exists():  # the name of the check
    """Is your file saved as assignment4.py"""  # this is what you will see when running check50
    check50.exists("assignment4.py")  # the actual check



@check50.check(exists)  # only run this check if the exists check has passed
def test2(exists):
    """Does the main program call the function with arguments and return correct result ? """
    check50.run(
        "python assignment4.py").stdin("12").stdin("45").stdout("270.0\n").exit(0)

