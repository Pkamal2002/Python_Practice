# Using f-strings, .format(), and the % operator, print the following sentence in three different ways:
# 'The price of 3 apples is Rs. 45.00' Use variables: item='apples', qty=3, price=45.0

item = 'apples';
qty = 3;
price = 45.00;

# Using f-strings
print(f'The Price of {qty} {item} is Rs. {price:.2f}');
# Using .format()
print('The Price of {} {} is Rs. {:.2f}'.format(qty, item, price)) 
# Using % operator
print( 'The Price of %d %s is Rs. %.2f' %(qty, item, price));