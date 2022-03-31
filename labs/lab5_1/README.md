# Python Lab 5.1: Sets and Tuples

> The purpose of this practice is to help you apply the concepts discussed up to **now**: 
>
> -


In `lab5_1.py` in the text editor at top-right, write a program which will:



{% next %}


Your output should look like the following:
```


```


{% spoiler "Read the file and add the data in the dictionary " %}
```

fhand = open('2021-07-08_clean-hashtags.tsv', 'r')
virustags = {}

for line in fhand:
    if 'virus' not in line and 'vaccine' not in line and 'coronavirus' not in line and 'covid' not in line:
         continue
    tag = line.split()[0]
    tagmentions = line.split()[1]
    virustags[tag] = virustags.get(tag, 0) + int(tagmentions)

```
{% endspoiler %}


{% spoiler "Solution  " %}
```


```
{% endspoiler %}

## Execute your program 

Remember in order to execute your code you type in the terminal:
```
python lab5_1.py
```

Check that your code produces correct results. 





{% next %}

### Check Your Code

Execute the below to evaluate the correctness of your code using `check50`, but be sure to test it yourself also.


```
check50 mkotsovoulou/ods6001a/main/labs/lab5_1
```

Execute the below to evaluate the style of your code using `style50`.

```
style50 lab5_1.py
```

{% next %}

## Submit your code

Execute the command below, logging in with your `GitHub username` and `Personal Access Token` when prompted. For security, you'll see asterisks (`*`) instead of the actual characters in your token. 

If you do not have generated a Personal Access ToKen follow the instructions: 
https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token

```
submit50 mkotsovoulou/ods6001a/main/labs/lab5_1
```

You can re-submit your solution as many times as you want.
When you are happy with your solution, download the code and upload it to Canvas.

![Image of download](download.png)


# Done!
:tada: