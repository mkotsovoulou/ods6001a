import check50  # import the check50 module

@check50.check()  # tag the function below as check50 check
def exists():  # the name of the check
    """Is your file saved as assignment4.py"""  # this is what you will see when running check50
    check50.exists("assignment4.py")  # the actual check



@check50.check(exists)  # only run this check if the exists check has passed
def test_empty(exists):
    """sample1.txt should return empty """
    check50.run(
        "python assignment4.py").stdin("sample1.txt").stdout("empty\n").exit(0)


@check50.check(exists)  # only run this check if the exists check has passed
def test_character(exists):
    """sample2.txt should return character """
    check50.run(
        "python assignment4.py").stdin("sample2.txt").stdout("character\n").exit(0)

@check50.check(exists)  # only run this check if the exists check has passed
def test_words(exists):
    """sample3.txt should return words """
    check50.run(
        "python assignment4.py").stdin("sample3.txt").stdout("words\n").exit(0)


@check50.check(exists)  # only run this check if the exists check has passed
def test_sentence(exists):
    """sample4.txt should return sentence """
    check50.run(
        "python assignment4.py").stdin("sample4.txt").stdout("sentence\n").exit(0)


@check50.check(exists)  # only run this check if the exists check has passed
def test_paragraph(exists):
    """sample5.txt should return paragraph """
    check50.run(
        "python assignment4.py").stdin("sample5.txt").stdout("paragraph\n").exit(0)


@check50.check(exists)  # only run this check if the exists check has passed
def test_document(exists):
    """sample6.txt should return document """
    check50.run(
        "python assignment4.py").stdin("sample6.txt").stdout("document\n").exit(0)

