# Python Lab 4.2: Use of Dictionaries

> The purpose of this practice is to help you apply the concepts discussed up to **now**: 
>
> - add keys and values to dictionaries
> - increment values based on keys

In `lab4_2.py` in the text editor at top-right, write a program which will:

Write a program to read through the `2021-07-08_clean-hashtags.tsv` and figure out the tag containing keywords around the coronavirus such as 'virus','coronavirus', 'vaccine', 'covid' with the most mentions. 

- The program looks for lines containing the #tag that includes the word 'virus' or 'coronavirus' or 'vaccine' or 'covid' and takes the second word of those lines as total mentions.

- The program creates a Python dictionary that maps each tag we are interested at with the number of its mentions. 

- After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the tag with the most mentions.

{% next %}


Your output should look like the following:
```
#covid19 34468

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

### A different way to search in the line
In the solution above we used multiple conditions to check if a line contains either of these words:

```
if 'virus' not in line and 'vaccine' not in line and 'coronavirus' not in line and 'covid' not in line:
         continue
```

Another way to perform this tast is to declare a list with all the words you are interested at ...
and in the loop check if any of the words is not found in the line, using the any keyword...

```
tags_to_search = ['virus', 'vaccine', 'corona', 'covid']
for line in fhand:
    if not any(tag in line for tag in tags_to_search):
        continue

 ```   

{% spoiler "Use a maximum type of loop " %}
```
max_tag = None
max_mentions = 0
for tag in virustags:
    if virustags[tag] > max_mentions:
        max_tag = tag
        max_mentions = virustags[tag]

print(max_tag, max_mentions)

```
{% endspoiler %}

## Execute your program 

Remember in order to execute your code you type in the terminal:
```
python lab4_2.py
```

Check that your code produces correct results. 

For the sample datafile the output should be:

#covid19 34468

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