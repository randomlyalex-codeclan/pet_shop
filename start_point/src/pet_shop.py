# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, cash_amount):
    pet_shop["admin"]["total_cash"] += cash_amount

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]  

def increase_pets_sold(pet_shop, pets_sold):
    pet_shop["admin"]["pets_sold"] += pets_sold

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, breed_type):
    pets = pet_shop["pets"]
    found_pets_by_breed = []
    for pet in pets:
        if pet["breed"] == breed_type:
            found_pets_by_breed.append(pet)
    return found_pets_by_breed

def find_pet_by_name(pet_shop, pet_name):
    pets = pet_shop["pets"]
    for pet in pets:
        if pet["name"] == pet_name:
            return pet

def remove_pet_by_name(pet_shop, pet_name):
    pets = pet_shop["pets"]
    for pet in pets:
        if pet["name"] == pet_name:
            pets.remove(pet)

def add_pet_to_stock(pet_shop, new_pet):
    pets = pet_shop["pets"]
    pets.append(new_pet)

def get_customer_cash(customers):
    return customers["cash"]

def remove_customer_cash(customer, cash):
        customer["cash"] -= cash

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, pet):
    customer["pets"].append(pet)