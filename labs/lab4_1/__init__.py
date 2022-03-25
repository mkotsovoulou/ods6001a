import check50  # import the check50 module

@check50.check()  # tag the function below as check50 check
def exists():  # the name of the check
    """Is your file saved as lab4_1.py?"""  # this is what you will see when running check50
    check50.exists("lab4_1.py")  # the actual check

# only run this check if the exists check has passed
@check50.check(exists)
def main_test(exists):
    """Does the program read the file and count the unique words ?"""
    output = check50.run("python3 lab4_1.py").stdout()
    if output != ['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east', 'envious', 'fair', 'grief', 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'the', 'through', 'what', 'window', 'with', 'yonder']:
        raise check50.Failure("Correct output not detected")
