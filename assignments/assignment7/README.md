# Programming Problem 6: Web Services and APIs

> The purpose of this assignment is to test your understanding and application of the concepts discussed up to **week 7**:
>
> - Call a web service
> - Retrieve a JSON Object
> - Load JSON into a Dictionary
> - Parse Data 

## Specifications
A company has created a webservice to expose its products, their prices and the number of items they have in stock. The API documentation of the webservice, can be found at: https://dummyjson.com/docs/products

Create a program to download the json products and categories data sets from the following web services:
- https://dummyjson.com/products
- https://dummyjson.com/products/categories 

Use the data retrieved to:

1. Find the most expensive product in each category and the product name.

2. The total number of items the company has in stock for the specific category.

3. Produce a formatted output, like the following, in a text file called 'stats.txt':
```
CATEGORY           MOST EXPENSIVE PRODUCT           PRICE   CAT STOCK
----------------   -------------------------------  -----   --------- 
smartphones        Samsung Universe 9                1249         319
laptops            MacBook Pro                       1749         386
fragrances         Non-Alcoholic Concentrated P       120         397
skincare           Freckle Treatment Cream- 15g        70         470
groceries          Gulab Powder 50 Gram                70         465
home-decoration    Handcraft Chinese style             60         263
```
Display only those categories where a product exists!

4. Display the price of the most expensive product of all in the terminal.


{% spoiler "Hint 1 : Nested Loops" %}
Loop through the categories and in this Loop,

    - Loop through the products

        - if the product category is equal to the current category from the outer loop
            - add the stock to a categoryStock dictionary

            - check the product price to see if it larger to the previous "larger" price

                - if yes, assign this product's price to a largest variable...and the name to another variable

    - Add the final values to another dictionary with key the category and as a value a list of the required information (product name, price and total category stock)

    
{% endspoiler %}

{% next %}


## Execute and Test your program 

*Remember*: in order to execute your code you type in the terminal:

```
python assignment7.py

```


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
When you are happy with your solution, download the code and the stats.txt and upload it to Canvas.

![Image of download](download.png)

# Done!
:tada: