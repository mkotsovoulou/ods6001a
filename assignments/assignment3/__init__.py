import check50  # import the check50 module

@check50.check()  # tag the function below as check50 check
def exists():  # the name of the check
    """Is your file saved as assignment3.py"""  # this is what you will see when running check50
    check50.exists("assignment3.py")  # the actual check


@check50.check(exists)  # only run this check if the exists check has passed
def test1():
    """Does the program calculate the area of a triangle with base 12 and height 45 correctly ? """
    check50.run(
        "python -c \"from assignment3 import areaTriangle;print(areaTriangle(12, 45))\"").stdout("270.0\n").exit(0)


@check50.check(exists)  # only run this check if the exists check has passed
def test2():
    """Does the program call the function with arguments ? """
    check50.run(
        "python assignment3.py").stdin("12").stdin("44").stdout("270.0\n").exit(0)
