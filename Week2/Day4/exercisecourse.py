# # Exercise
# #  1. create a function that takes a number as an argument, and check if this number is even or odd
# # 2. create a function that takes a list of numbers as an argument, and check if each number is even or odd

# def evenorodd (a):
#     if a % 2 == 0:
#         print(f"{a} is 'even'")
#     else:
#         print(f"{a} is 'odd'")


# evenorodd(5)



# nums = [1, 2, 3, 4]
# print(nums[0])


# def evenoroddlist (nums):

#  for number in nums:
#     if number % 2 == 0 :
#         print(f"{number} is 'even'")
#     else:
#         print(f"{number} is 'odd'")


# evenoroddlist(nums)




def pricecar():
    age = int(input('what is your age ?'))
    if age < 40:
        pricecar =  200
    else:
        pricecar = 300
    return pricecar, age 


def priceflight():
    destination = (input('what is your destination  ?'))
    if destination ==  'Paris'.lower():
        pricedestination =  400
    else:
        pricedestination = 600
    return pricedestination, destination

def informationaboutprice():
    dat_car = pricecar()
    data_fligh = priceflight()
    totalcost = dat_car[0] + data_fligh[0]
    return totalcost, dat_car, data_fligh

print(f'You have {informationaboutprice()[1][1]} {informationaboutprice()[1][1]}')





