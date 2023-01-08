# initialize the count variable to 0
# initialize the sum variable to 0
# input full_name
# input the min_price and convert it to float
# create a list of prices example: price_list = [69.0, 71.0, 84.5, 91.0, 67.4, 81.2, 84.6, 58.8,
# 79.3, 101.2]
# for price in price_list
#    add current price to sum
#    if price > min_price
#        increment count by 1
# output "Hello",name,"the minimum price is ",min_price
# output "There are ",count,"prices greater than the minimum price"
# output "The total price is ",sum

count = 0
sum = 0

user_name = input("Please enter your FIRST and LAST Name here: ")
min_price = float(5.00)
price_list = [12, 15.3, 24, 28.5, 32, 34.8, 48.2, 55.5, 87, 3, 140]
for price in price_list:
    sum += price
    if price > min_price:
        count += 1

print('Hello ' + str(user_name) + ', the minimum price is ' + str(min_price))
print('There are ' + str(count) + ' prices greater than the minimum price')
print('The total price is ' + str(sum))
