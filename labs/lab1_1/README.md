# Python Lab 1.1: Variables and Types

Recall that Python supports multiple "data types" among them strings, floats and integers. It is important to note that the data type of a variable matters!

To start this lab practice edit:
```
lab1_1.py
```

At first glance, the program looks like it

1. prompts the user for two inputs, `x` and `y`,
2. adds `x` and `y`, storing the sum in `z`, and
3. prints `z`.

But let's look more closely.

Execute your program by typing: `python lab1_1.py` in the terminal window at bottom-right, followed by Enter.
- When prompted for `x`, input `1`, followed by Enter.
- When prompted for `y`, again input `1`, followed by Enter.

How curious!
- Python thinks that 1+1=11


### Not what you expected!
Contrary to what this program thinks, 1 plus 1 does not equal 11! The sum should, of course, equal 2.

Modify `lab1_1.py` in the text editor at top-right in such a way that the program correctly outputs the sum of `x` and `y`.

<details>
<summary>
Hint 1:
</summary>

```
Try to convert your x and y inputs into a numeric data type.
```

</details>

If you need extra help ...

<details>
<summary>
Hint 2:
</summary>

  Consider using the float function, so your program can add floating point numbers as well as integers!

</details>

If you want extra help... here is the solution:

<details>
<summary>
SOLUTION:
</summary>

 ```
  z = float(x) + float(y)
 ```
</details>

### Execute your program

Provide the value 1 for x, and 1 for y

Remember in order to execute your code you type in the terminal:

```
python lab1_1.py
```
Make sure that the output is 2.0!


### Check Your Code

Run your code using the `test_lab1_1.py` to evaluate the correctness of your code using my predefined `unitests`, but be sure to test it yourself before that...



## Submit your code
Download the py code and upload it to Blackboard.

![Image of download](download.png)

# Done!
:tada:
