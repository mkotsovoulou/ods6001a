import check50  # import the check50 module

@check50.check()  # tag the function below as check50 check
def exists():  # the name of the check
    """Is your file saved as lab3_1.py?"""  # this is what you will see when running check50
    check50.exists("lab3_1.py")  # the actual check


@check50.check(exists)  # only run this check if the exists check has passed
def test2(exists):
    """Does the calculate the average correctly ?"""
    check50.run("python3 lab3_1.py").stdout("5\n").exit(0)

