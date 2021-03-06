import check50  # import the check50 module

@check50.check()  # tag the function below as check50 check
def exists():  # the name of the check
    """Is your file saved as lab2_2.py?"""  # this is what you will see when running check50
    check50.exists("lab2_2.py")  # the actual check

# @check50.check(exists)  # only run this check if the exists check has passed
# def test1(exists):
#     expected="10.0\n"
#     """Does the function return correct results? Is the loop correct ? """
#     result = check50.run("python -c \"from lab2_2 import add;print(add(2))\"").stdin(
#         '5').stdin('5').stdout().exit(0)
#     if result != expected :
#         help = "Does your code repeat exactly X times? "
#         raise check50.Mismatch(expected, result, help=help)
    

@check50.check(exists)  # only run this check if the exists check has passed
def test2(exists):
    """Does the program print 0.0 for 2 inputs (1,-1) """
    check50.run("python3 lab2_2.py").stdin("2").stdout("Type a number to add:").stdin("1").stdout("Type a number to add:").stdin(
        "-1").stdout("0.0\n").exit(0)


@check50.check(exists)  # only run this check if the exists check has passed
def test3(exists):
    """Does the program print 25.0 for 5 inputs (5,5,5,5,5) """
    check50.run("python3 lab2_2.py").stdin("5").stdout("Type a number to add:").stdin("5").stdout("Type a number to add:").stdin(
        "5").stdout("Type a number to add:").stdin("5").stdout("Type a number to add:").stdin(
        "5").stdout("Type a number to add:").stdin("5").stdout("25.0\n").exit(0)

@check50.check(exists)  # only run this check if the exists check has passed
def test4(exists):
    """Does the program print 'Wrong input' for input a? """
    check50.run("python3 lab2_2.py").stdin(
        "a").stdout("^[Ww]rong [Ii]nput\.?\n").exit(0)

# only run this check if the exists check has passed
@check50.check(exists)
def test5(exists):
    """Does the program print 'Wrong input' for 2 inputs (1,a)? """
    check50.run("python3 lab2_2.py").stdin("2").stdin(
        "a").stdout("^[Ww]rong [Ii]nput\.?\n").exit(0)
