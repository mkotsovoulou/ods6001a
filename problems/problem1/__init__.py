import check50  # import the check50 module


@check50.check()  # tag the function below as check50 check
def exists():  # the name of the check
    """Is your file saved as problem1.py"""  # this is what you will see when running check50
    check50.exists("problem1.py")  # the actual check


@check50.check(exists)  # only run this check if the exists check has passed
def prints2():
    """Does the program print 4 when your input is John """
    check50.run("python3 problem1.py").stdin("35").stdin("2.75").stdout("96.25\n").exit(0)
