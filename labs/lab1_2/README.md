# Python Lab 1.2: Using Build-in Functions

In `lab1_2.py` in the text editor at top-right, write a few python commands to:
1. ask the user to type their name and store it in a variable
2. display the length of the name
3. convert the name in upper case letters
4. display the lowest character in alphabetical order in the name

{% spoiler "Hint 1" %}
- the built-in function to count the characters in a string is: `len()`
- the built-in function to find the smallest/lowest character in alphabetical order is `min()`
{% endspoiler %}


{% next %}
Keep in mind that this solution is not the only solution. There are different ways to reach to the same result...

And here is the Solution...

{% spoiler "Solution" %}

name = input("What is your name?")

print(len(name))

name = name.upper()

print(min(name))

{% endspoiler %}

### Execute your program 

Provide a value for name
for example: John

Remember in order to execute your code, you type in the terminal:

```
python3 lab1_2.py
```
Make sure that the output is correct. For John it should be 4, and the lowest letter is J

{% next %}

### Check Your Code

Execute the below to evaluate the correctness of your code using `check50`, but be sure to test it yourself before that...

```
check50 mkotsovoulou/ods6001a/main/labs/lab1_2
```

Execute the below to evaluate the style of your code using `style50`.

```
style50 lab1_2.py
```

{% next %}

## Submit your code

Execute the command below, logging in with your `GitHub username` and `Personal Access Token` when prompted. For security, you'll see asterisks (`*`) instead of the actual characters in your token. 

If you do not have generated a Personal Access ToKen follow the instructions: 
https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token

```
submit50 mkotsovoulou/ods6001a/main/labs/lab1_2
```

