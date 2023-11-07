"""
SumAndProduct.py - This program computes sums and products.
Input:  Interactive.
Output:  Computed sum and product.
"""


# Write sums() function here.
def sums(num):
    sum = 0
    for i in range (num + 1):
        sum = sum + i
    print(sum)

# Write products() function here.
def products(num):
    products = 1
    for i in range(1, num + 1):
        products = products * i
    print(products)

numberString = input("Enter a positive integer or 0 to quit: ")
number = int(numberString)

while number != 0:
    # Call sums() function here.
    sums(number)
    # Call products() function here.
    products(number)
    numberString = input("Enter a positive integer or 0 to quit: ")
    number = int(numberString)
