import check50
import check50.c

@check50.check()
def Cexists():
    """salesTax.cpp exists."""
    check50.exists("salesTax.cpp")

@check50.check(Cexists)
def Ccompiled():
   """C++ salesTax executable is generated"""
   check50.exists("salesTax")


@check50.check(Ccompiled)
def Cproduces_correct_output():
    """C++ code produces correct output for sample input"""
    check50.run(
        "./salesTax ").stdin("100").stdin(".30").stdin("0.24").stdout("100 0.3 0.24 130 31.2 161.2").exit(0)


@check50.check()
def Jexists():
    """salesTax.java exists."""
    check50.exists("salesTax.java")


@check50.check(Jexists)
def Jcompiled():
   """salesTax java executable is generated"""
   check50.exists("salesTax.class")


@check50.check(Jcompiled)
def Jproduces_correct_output():
    """Java code produces correct output for sample input"""
    check50.run(
        "java salesTax ").stdin("100").stdin(".30").stdin("0.24").stdout("100.0 0.3 0.24 130.0 31.2 161.2").exit(0)
