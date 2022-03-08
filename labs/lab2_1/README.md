# Python Lab 2.1: Conditionals 
In `lab2_1.py` in the text editor at top-right, write a few python commands to:

1. Ask the user to type their score in a test and store it in a variable
2. Test if the score entered by the user falls within the valid range from 0 to 100. If not display `Invalid score`.
3. If the user enters character/s instead of a number display `Wrong input`.
4. Using the following table to find and display the letter grade of the user score.

![Image of ranges](ranges.png)


{% spoiler "Hint 1 : Validate range " %}

if score < 0 or score > 100:
    print('Invalid score')

{% endspoiler %}


{% spoiler "Hint 2 : Invalid Input " %}

use a try/except block after reading the score and converting to a floating point number

try:
    score = float(score)
except:
    print(Wrong input)
    quit()

{% endspoiler %}

{% spoiler "Hint 3 : Finding the letter grade " %}

if score < 60: 
    print('F')
elif score < 70:
    print('D')
elif score < 80:
    print('C')
elif score < 90:
    print('B')
else:
    print('A')

{% endspoiler %}

{% next %}

## Execute your program 

Remember in order to execute your code you type in the terminal:
```
python lab2_1.py
```

Use the following test data to make sure your program produces correct resutls.

### TEST 1:

Enter your score: 35

F

### TEST 2:

Enter your score: 102

Invalid score

### TEST 3:

Enter your score: 60

D

{% next %}

### Check Your Code

Execute the below to evaluate the correctness of your code using `check50`, but be sure to test it yourself using:


- [x] a number out of the valid range
- [x] a character or word as input
- [x] a number below 60
- [x] a number in every possible range :tada:


```
check50 mkotsovoulou/ods6001a/main/labs/lab2_1
```

Execute the below to evaluate the style of your code using `style50`.

```
style50 lab2_1.py
```

{% next %}

## Submit your code

Execute the command below, logging in with your `GitHub username` and `Personal Access Token` when prompted. For security, you'll see asterisks (`*`) instead of the actual characters in your token. 

If you do not have generated a Personal Access ToKen follow the instructions: 
https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token

```
submit50 mkotsovoulou/ods6001a/main/labs/lab2_1
```

# Done!
:tada: