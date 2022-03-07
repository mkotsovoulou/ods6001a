import check50  # import the check50 module


@check50.check()  # tag the function below as check50 check
def exists():  # the name of the check
    """Is your file saved as lab2.py?"""  # this is what you will see when running check50
    check50.exists("lab2_1.py")  # the actual check


@check50.check(exists)  # only run this check if the exists check has passed
def test1():
    """Does the program print D for a score of 60? """
    check50.run("python3 lab2_1.py").stdin("60").stdout("D\n").exit(0)
