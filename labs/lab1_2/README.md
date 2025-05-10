# Python Lab 1.2: Using Build-in Functions

To start this lab practice edit:
```
lab1_2.py
```

Create a program to:
1. ask the user to type their name and store it in a variable
2. display the length of the name
3. convert the name in upper case letters, without printing it.
4. display the lowest character in alphabetical order in the name

<details>
<summary>
Hint 1:
</summary>

```
- the built-in function to count the characters in a string is: `len()`
- the built-in function to find the smallest/lowest character in alphabetical order is `min()`
```

</details>

Keep in mind that the sample solution is not the only solution. There are different ways to reach to the same result...

And here is the Solution...

<details>
<summary>
Sample Solution:
</summary>

```
name = input("What is your name?")
print(len(name))
name = name.upper()
print(min(name))
```

</details>

### Execute your program

Remember in order to execute your code, you type in the terminal:

```
python lab1_2.py
```

Make sure that the output is correct. For `John` it should display `4`, and the lowest letter is `H` (in uppercase)


### Check Your Code

Run your code using the `test_lab2_1.py` to evaluate the correctness of your code using my predefined `unit tests`, but be sure to test it yourself before that...


## Submit your code

When you are happy with your solution, download the code and upload it to Blackboard.


# Done!
:tada: