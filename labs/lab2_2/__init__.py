import check50  # import the check50 module


@check50.check()  # tag the function below as check50 check
def exists():  # the name of the check
    """Is your file saved as lab2_2.py?"""  # this is what you will see when running check50
    check50.exists("lab2_2.py")  # the actual check


@check50.check(exists)  # only run this check if the exists check has passed
def test1():
    """Does the program print 25 for 5 inputs (5,5,5,5,5) """
    check50.run("python3 lab2_2.py").stdin("5").stdin("5").stdin("5").stdin("5").stdin("5").stdout("25\n").exit(0)
