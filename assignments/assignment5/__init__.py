import check50  # import the check50 module

@check50.check()  # tag the function below as check50 check
def exists():  # the name of the check
    """Is your file saved as assignment5.py"""  # this is what you will see when running check50
    check50.exists("assignment5.py")  # the actual check


@check50.check(exists)  # only run this check if the exists check has passed
def test_document(exists):
    """sample7.txt should return File Not Found """
    check50.run(
        "python assignment5.py").stdout("^[Ff]ile [Nn]ot [Ff]ound\.?\n").exit(0)

