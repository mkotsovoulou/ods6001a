# Python Lab 6.2: OOP
> The purpose of this practice is to help you apply the concepts discussed up to **now**: 
>
> - implement object classes and develop program to use them
> - test, debug and predict program behaviour

In `lab6_2.py` in the text editor at top-right, The exercise template contains a pre-defined BankAccount class, which can be used to model a BankAccount. Your task is to create the following methods in the BankAccount Class

1.  A method to deposit an amount to a BankAccount
2.  A method to withdraw an amount from a BankAccount
3.  An __str__ method which will return a string representation of the account


## Specifications

1. The Deposit method should accept an amount and increment the account balance by that amount
2. The Withdraw method should accept an amount and decrement the account balance by that amount. If the balance is not enough the withdrawal is considered as successful and the method should return true, else it should return false.
3. the __str__ method should return a formatted output like the following: 
```
BankAccount Owner:  Mary, Balance: 124.00
```

{% spoiler "HINT 1: The Deposit Method " %}

```
def deposit(self, amount):
        self.balance = self.balance + amount
        
```
{% endspoiler %}



{% spoiler "HINT 2: The WithDraw Method " %}

```
 def withdraw(self, amount: float):
        if amount <= self.balance:
            self.balance -= amount
            return True

        return False
        
```
{% endspoiler %}

### To Do

1. Instantiate 1 Bank Account variable which belongs to John and has an initial balance of 1000
2. Deposit 100 to this Bank Account
3. Print the result of a withdrawal of 250
4. Print the Bank Account details
5. Print thre result of a withdrawl of 5000
6. Print the Bank Account details


{% next %}

## Execute and Test your program 

Remember in order to execute your code you type in the terminal:
```
python lab6_2.py
```

Check that your code produces correct results. 

```

```

{% next %}


### Check Your Code

Execute the below to evaluate the correctness of your code using `check50`, but be sure to test it yourself also.


```
check50 mkotsovoulou/ods6001a/main/labs/lab6_2
```

Execute the below to evaluate the style of your code using `style50`.

```
style50 lab6_2.py
```

{% next %}

## Submit your code

Execute the command below, logging in with your `GitHub username` and `Personal Access Token` when prompted. For security, you'll see asterisks (`*`) instead of the actual characters in your token. 

If you do not have generated a Personal Access ToKen follow the instructions: 
https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token

```
submit50 mkotsovoulou/ods6001a/main/labs/lab6_2
```

You can re-submit your solution as many times as you want.
When you are happy with your solution, download the code and upload it to Canvas.

![Image of download](download.png)


# Done!
:tada: