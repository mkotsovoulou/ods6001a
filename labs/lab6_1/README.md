# Python Lab 6.1: Reading CSV Files
> The purpose of this practice is to help you apply the concepts discussed up to **now**: 
>
> - implement object classes and develop program to use them
> - test, debug and predict program behaviour

In `lab6_1.py` in the text editor at top-right, The exercise template contains a pre-defined ShoppingList class, which can be used to model a shopping list. Your task is to add a method to the class definition. You do not need to change any methods already defined.

Assuming we have a ShoppingList object referenced in a variable named shopping_list, the object can be handled with the following methods:

Please write a function named total_units(my_list: ShoppingList), which takes a ShoppingList type object as its argument. The function should calculate the total number of units listed, and return the value.

You can use the following code to test your function:
```
if __name__ == "__main__":
    my_list = ShoppingList()
    my_list.add_item("bananas", 10)
    my_list.add_item("apples", 5)
    my_list.add_item("pineapple", 1)

    print(total_units(my_list))
```

{% next %}




## Execute your program 

Remember in order to execute your code you type in the terminal:
```
python lab6_1.py
```

Check that your code produces correct results. 



{% next %}

### Check Your Code

Execute the below to evaluate the correctness of your code using `check50`, but be sure to test it yourself also.


```
check50 mkotsovoulou/ods6001a/main/labs/lab6_1
```

Execute the below to evaluate the style of your code using `style50`.

```
style50 lab6_1.py
```

{% next %}

## Submit your code

Execute the command below, logging in with your `GitHub username` and `Personal Access Token` when prompted. For security, you'll see asterisks (`*`) instead of the actual characters in your token. 

If you do not have generated a Personal Access ToKen follow the instructions: 
https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token

```
submit50 mkotsovoulou/ods6001a/main/labs/lab6_1
```

You can re-submit your solution as many times as you want.
When you are happy with your solution, download the code and upload it to Canvas.

![Image of download](download.png)


# Done!
:tada: