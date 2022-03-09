import check50  # import the check50 module


@check50.check()  # tag the function below as check50 check
def exists():  # the name of the check
    """Is your file saved as lab2_2.py?"""  # this is what you will see when running check50
    check50.exists("lab2_2.py")  # the actual check


@check50.check(exists)  # only run this check if the exists check has passed
def test1():
    """Does the program print 25 for 5 inputs (5,5,5,5,5) """
    check50.run("python3 lab2_2.py").stdin("5").stdin("5").stdin("5").stdin("5").stdin("5").stdout("25.0\n").exit(0)


def test2():
    """Does the program print 25 for 5 inputs (5,5,5,5,5) """
    check50.run("python3 lab2_2.py").stdin("2").stdin("1").stdin(
        "-1").stdout("0.0\n").exit(0)

@check50.check(exists)  # only run this check if the exists check has passed
def test2():
    """Does the program print 'Wrong input' for a? """
    check50.run("python3 lab2_2.py").stdin("a").stdout("Wrong input\n").exit(0)


@check50.check(exists)  # only run this check if the exists check has passed
def test3():
    """Does the program print 'Wrong input' for 2 inputs (1,a)? """
    check50.run("python3 lab2_2.py").stdin("2").stdin(
        "a").stdout("Wrong input\n").exit(0)
