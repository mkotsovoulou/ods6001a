# Programming Problem 5: Data Structures

> The purpose of this assignment is to test your understanding and application of the concepts discussed up to **week 4**:
>
> - read data from files
> - parse and extract information
> - load data into dictionaries
> - perform calculations

## Specifications

Create a program which will read a text file containing Stock Market purchase information and then figure out whether the company has lost or earned money. 

The structure of the file is as follows: Symbol,Date,ClosingPrice,Volume

* The Volume is an integer. When the Volume contains a positive number it represents the number of stocks the company bought at Closing Price, and when is negative it represents the number of stocks the company sold, again at the closing price.

* You have to remove the dollar sign '$' from the price (which is a float). 

* Ignore the dates.

Some sample data from the file:

```
AAPL,2/28/2022,$165.12,30
FB,2/28/2022,$211.03,100
AAPL,3/7/2022,$159.30,-30
```

When the data are loaded and processed produce:
1. The total amount of profit/loss from all stocks rounded in the nearest integer (display it in the screen)
2. Write to a file called `results.txt` the contents of the dictionary. Display the Stock Symbol and the amount of profit or loss. You may need to think about the sign...


### Hint 1 : 
Use the appropriate data structure which can utilize the stock symbol as the key: i.e. AAPL, and the running amount amount of profit/loss as a value. Ignore the dates during your load.

If for example the company bought 30 stocks of AAPP in the price of 165.12, the amount invested should be 4,953.6 and when the company sold 30 stocks of AAPP at the price of 200.34, the amount received was 6,010.2. So the total investment has a produced profit of 1,056.6. 

### Hint 2 :
While reading data from the file, first load data in your data structure, either by adding a stock symbol which does not exist or updating the amount, to keep track of the total profit/loss.

You are free to create your own functions for code modularity. Use comments to describe your algorithm to process the data.


{% next %}


## Execute and Test your program 

*Remember*: in order to execute your code you type in the terminal:

```
python assignment5.py

```


A sample `results.txt` should contain the following info:
```
AAPL,-2544.1000000000026
FB,-515.1999999999971
SBUX,-5657.519999999997
TSLA,26133.749999999985
MSFT,-202.99999999999818
```


## Check Your Code

Execute the below to evaluate the correctness of your code using `check50`, but be sure to test it yourself before that...
Login with your `GitHub username` and `Personal Access Token` when prompted. For security, you'll see asterisks (`*`) instead of the actual characters in your token. 

If you do not have generated a Personal Access ToKen follow the instructions: 
https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token

```
check50 mkotsovoulou/ods6001a/main/assignments/assignment5
```

Execute the below to evaluate the style of your code using `style50`.

```
style50 assignment5.py
```

{% next %}

## Submit your code

Execute the command below, logging in with your `GitHub username` and `Personal Access Token` when prompted. For security, you'll see asterisks (`*`) instead of the actual characters in your token. 

```
submit50 mkotsovoulou/ods6001a/main/assignments/assignment5
```

You can re-submit your solution as many times as you want.
When you are happy with your solution, download the code and `results.txt` produced with the data from the dictionary and upload it to Canvas.

![Image of download](download.png)

# Done!
:tada: