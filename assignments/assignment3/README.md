# Programming Problem 3: Functions 

> The purpose of this assignment is to test your understanding and application of the concepts discussed in **Week 2**:
>
> - define functions that accept parameters and return values
> - call functions with arguments
> - perform user input validation and exception handling

## Specifications

Change the code in `assignment3.py` so that **areaTriangle** takes parameters for the **base** and **height** of a triangle and computes its area. 
The formula provided is correct (base*height)/2

Then, enhance your code to:
- Ask the user to provide input from base and height.
- Validate user input to be positive integer numbers.
- Display 'Wrong input' if not valid and quit.
- Call the function to calculate the area and print the result. 


## Some Technical Details: A Basic Python main()

In some Python scripts, you may see a function definition and a conditional statement that looks like the example below:
```
def main():
    print("Hello World!")

if __name__ == "__main__":
    main()
```
In this code, there is a function called main() that prints the phrase Hello World! when the Python interpreter executes it. There is also a conditional (or if) statement that checks the value of __name__ and compares it to the string "__main__". When the if statement evaluates to True, the Python interpreter executes main().

In this program write your code to accept user input in def main():


{% next %}

## Execute and Test your program 

*Remember*: in order to execute your code you type in the terminal:

```
python assignment3.py
```

Test your function with base = 12 and height = 45 the function should return 270.


{% next %}

## Check Your Code

Execute the below to evaluate the correctness of your code using `check50`, but be sure to test it yourself before that...
Login with your `GitHub username` and `Personal Access Token` when prompted. For security, you'll see asterisks (`*`) instead of the actual characters in your token. 

If you do not have generated a Personal Access ToKen follow the instructions: 
https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token

```
check50 mkotsovoulou/ods6001a/main/assignments/assignment3
```

Execute the below to evaluate the style of your code using `style50`.

```
style50 assignment3.py
```

{% next %}

## Submit your code

Execute the command below, logging in with your `GitHub username` and `Personal Access Token` when prompted. For security, you'll see asterisks (`*`) instead of the actual characters in your token. 

```
submit50 mkotsovoulou/ods6001a/main/assignments/assignment3
```

You can re-submit your solution as many times as you want.
When you are happy with your solution, download the code and upload it to Canvas.

![Image of download](download.png)

# Done!
:tada: