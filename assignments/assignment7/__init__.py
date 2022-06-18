import check50  # import the check50 module

@check50.check()  # tag the function below as check50 check
def exists():  # the name of the check
    """Is your file saved as assignment7.py?"""  # this is what you will see when running check50
    check50.exists("assignment7.py")  # the actual check

@check50.check()
def main_test(exists):
    """Does the program apply the 3% interest and calculate the sum correctly ?"""
    check50.run("python3 assignment7.py").stdout("2369.0\n").exit(0)

