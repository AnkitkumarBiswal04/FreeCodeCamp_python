# raising a specific function to a specific power
print(2**3)

#using for loop creating a exponential function

def raise_to_power(base_num,pow_num):
    result=1
    for index in range(pow_num):
        result=result*base_num
    return result

print(raise_to_power(2,3))