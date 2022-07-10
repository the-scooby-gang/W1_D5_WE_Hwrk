# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(pet_shop):
    return pet_shop ["name"]


# The first bracket is your variable. we are passing the code 'name' to search inside the dictionary each name to see if it can find "camelot of pets" and therefore passed the test. If not found. "None"

# def get_total_cash(pet_shop) :
#     sum = (pet_shop['admin'])
#     return ['total_cash']
#Ask why this won't work if you've already directed to the correct dictionary

def get_total_cash(pet_shop):
     return(pet_shop['admin']['total_cash'])

     

#This is what I got without help
# def add_or_remove_cash(pet_cash,amount):
#     return (pet_cash['admin']['total_cash']) + (amount[10])

def add_or_remove_cash(pet_shop,amount):
    pet_shop['admin']['total_cash'] = pet_shop['admin']['total_cash'] + amount
    return (pet_shop['admin']['total_cash'])

#amount of arguments split by a , (that's how you know how many need to pass through) 

def get_pets_sold(pet_shop):
    return(pet_shop['admin']['pets_sold'])

def increase_pets_sold(pet_shop, number):
    pet_shop['admin']['pets_sold'] = pet_shop['admin']['pets_sold'] + number

def get_stock_count(pet_shop):
    stock = pet_shop['pets']
    return len(stock)

def get_pets_by_breed(pet_shop, breed):
    pet_number_by_breed = []
    pet_stock = pet_shop['pets']
    for pet in pet_stock:
        if pet['breed'] == breed:
            pet_number_by_breed.append(pet)
    return pet_number_by_breed

def find_pet_by_name(pet_shop, name):
    pets = pet_shop['pets']
    for pet in pets:
        if pet['name'] == name:
            return pet

#def remove_pet_by_name(pet_shop, name):
    # pet_to_delete = find_pet_by_name(pet_shop, name)
    # pet_list = pet_shop['pets']
    # pet_list.pop(pet_to_delete)

    #(I tried) 








    













