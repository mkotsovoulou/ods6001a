# Programming Problem 7: OOP

> The purpose of this assignment is to test your understanding and application of the concepts discussed up to **week 6**:
>
> - implement object classes and develop program to use them
> - test, debug and predict program behaviour

## Specifications
###### In assignment7.py, BankAccount class

1. Complete the add_interest method to increase the balance by applying the annual interest

###### In assignment7.py, Main Program**
2. Open account.txt to read

3. For each line in accounts.txt 
   - Split using the comma and strip the empty characters
   - Create a BankAccount object with the owner and balance in the line
   - and add it in the BankAccounts list

4. Modify the annual interest (class variable) to 3%

5. Call the add interest method on all Bank Accounts

6. Calculate the sum of all balances in the list and print it


{% next %}


## Execute and Test your program 

*Remember*: in order to execute your code you type in the terminal:

```
python assignment7.py

```
The sum of all balances after the interest is applied should be 2346.0

## Check Your Code

Execute the below to evaluate the correctness of your code using `check50`, but be sure to test it yourself before that...
Login with your `GitHub username` and `Personal Access Token` when prompted. For security, you'll see asterisks (`*`) instead of the actual characters in your token. 

If you do not have generated a Personal Access ToKen follow the instructions: 
https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token

```
check50 mkotsovoulou/ods6001a/main/assignments/assignment7
```

Execute the below to evaluate the style of your code using `style50`.

```
style50 assignment7.py
```

{% next %}

## Submit your code

Execute the command below, logging in with your `GitHub username` and `Personal Access Token` when prompted. For security, you'll see asterisks (`*`) instead of the actual characters in your token. 

```
submit50 mkotsovoulou/ods6001a/main/assignments/assignment7
```

You can re-submit your solution as many times as you want.
When you are happy with your solution, download the code and upload it to Canvas.

![Image of download](download.png)

# Done!
:tada: