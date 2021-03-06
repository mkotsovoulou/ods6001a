import check50  # import the check50 module

@check50.check()  # tag the function below as check50 check
def exists():  # the name of the check
    """Is your file saved as lab7_1.py?"""  # this is what you will see when running check50
    check50.exists("lab7_1.py")  # the actual check

# only run this check if the exists check has passed
@check50.check(exists)
def main_test(exists):
    """Does the program read the file and count tags ?"""
    output = check50.run("python3 lab7_1.py").stdout()
    if output == "\n":
        raise check50.Failure("Your code did not produce the expected results")
