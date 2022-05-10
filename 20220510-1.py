#HW21 Exponent function
#allow to take a certain number and raise it to a specific power
#Usual
print(2**3) #2^3
print("\n")

#Via creating exponent function
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(3, 2))
print(raise_to_power(3, 4))
print(raise_to_power(2, 3))