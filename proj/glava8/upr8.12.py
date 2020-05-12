def make_pizza(*toppings):
    print("Приготовленна с этими начинками ")
    for topping in toppings:
        print(topping)


make_pizza('mushrooms', 'green peppers')
make_pizza('mushrooms')
make_pizza('green peppers', 'extra cheese')
