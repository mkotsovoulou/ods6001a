import check50  # import the check50 module

@check50.check()  # tag the function below as check50 check
def exists():  # the name of the check
    """Is your file saved as assignment3.py"""  # this is what you will see when running check50
    check50.exists("assignment3.py")  # the actual check


@check50.check(exists)  # only run this check if the exists check has passed
def test1():
    """Does the program calculate the area of a triangle with base 12 and height 45 correctly ? """
    check50.run("python3 assignment3.py").stdout("270\n").exit(0)
