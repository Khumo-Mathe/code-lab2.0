#list aliasing

sneaker_list = ['nike', 'adidas', 'puma', 'reebok', 'new_balance']

another_list = sneaker_list
print(sneaker_list)

print(id(another_list))
print(id(sneaker_list))

sneaker_list += ['converse', 'vans']
print(sneaker_list)
print(another_list)  # This will also show the updated list since both variables point to the same object
print(id(another_list))  # id remains the same, showing that both variables point to the same list object
print(id(sneaker_list))  # id remains the same, showing that both variables point to the same list object