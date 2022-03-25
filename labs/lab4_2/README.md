# Python Lab 4.2: Use Dictionaries

> The purpose of this practice is to help you apply the concepts discussed up to **now**: 
>
> - add keys and values to dictionaries
> - increment values based on keys

In `lab4_2.py` in the text editor at top-right, write a program which will:

Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 

- The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
- The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
- After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

{% next %}




Your output should look like the following:
```
cwen@iupui.edu 5

```


{% spoiler "Solution" %}
```


```
{% endspoiler %}


## Execute your program 

Remember in order to execute your code you type in the terminal:
```
python lab4_2.py
```

Check that your code produces correct results. 

For the sample datafile the outout shoud be:
cwen@iupui.edu 5

{% next %}

### Check Your Code

Execute the below to evaluate the correctness of your code using `check50`, but be sure to test it yourself also.


```
check50 mkotsovoulou/ods6001a/main/labs/lab4_2
```

Execute the below to evaluate the style of your code using `style50`.

```
style50 lab4_2.py
```

{% next %}

## Submit your code

Execute the command below, logging in with your `GitHub username` and `Personal Access Token` when prompted. For security, you'll see asterisks (`*`) instead of the actual characters in your token. 

If you do not have generated a Personal Access ToKen follow the instructions: 
https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token

```
submit50 mkotsovoulou/ods6001a/main/labs/lab4_2
```

You can re-submit your solution as many times as you want.
When you are happy with your solution, download the code and upload it to Canvas.

![Image of download](download.png)


# Done!
:tada: