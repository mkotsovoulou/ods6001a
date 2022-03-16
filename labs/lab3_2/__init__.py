import check50  # import the check50 module

@check50.check()  # tag the function below as check50 check
def exists():  # the name of the check
    """Is your file saved as lab3_2.py?"""  # this is what you will see when running check50
    check50.exists("lab3_2.py")  # the actual check

# only run this check if the exists check has passed
@check50.check(exists)
def main_test(exists):
    """Does the program calcuate the sum xmax from the file ?"""
    check50.run("python3 lab3_2.py").stdout("13487\n").exit(0)



