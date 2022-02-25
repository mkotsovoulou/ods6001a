import check50  # import the check50 module


@check50.check()  # tag the function below as check50 check
def exists():  # the name of the check
    """Is your file saved as problem1.py"""  # this is what you will see when running check50
    check50.exists("problem2.py")  # the actual check


@check50.check(exists)  # only run this check if the exists check has passed
def test1():
    """Does the program calculate correct pay for hours less than 40?"""
    check50.run("python3 problem2.py").stdin("35").stdin("2.75").stdout("96.25\n").exit(0)


@check50.check(exists)  # only run this check if the exists check has passed
def test2():
    """Does the program calculate correct pay for hours more than 40?"""
    check50.run("python3 problem2.py").stdin(
        "45").stdin("10.50").stdout("498.75\n").exit(0)
