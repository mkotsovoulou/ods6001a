import check50  # import the check50 module

@check50.check()  # tag the function below as check50 check
def exists():  # the name of the check
    """Is your file saved as assignment7.py?"""  # this is what you will see when running check50
    check50.exists("assignment7.py")  # the actual check

@check50.check(exists)  # tag the function below as check50 check
def stats():  # the name of the check
    """Does you code produce the stats.txt file ?"""  
    check50.exists("stats.txt")  

@check50.check(stats)
def main_test():
    """Does the program find the most expensive price ?"""
    check50.run("python3 assignment7.py").stdout("1749\n").exit(0)

