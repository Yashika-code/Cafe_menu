# define the menu of cafe
menu={
    "Pizza" : 40,
    "Pasta" : 50,
    "Burger" : 60,
    "Cold-drink" : 40,
    "Coffee" : 80
}
print("\nWelcome to our python restaurant !!")
print("Pizza : Rs 40 \nPasta : Rs 50\nBurger : Rs 60\nCold-drink : Rs 40\nCoffee : Rs 80\n")

order_total=0

item_1=input("enter the name of item you want to order : ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item {item_1} has been added in your order")
else:
    print(f"ordered  item {item_1} has been not available yet !!")
another_order=input("do you want to order another item ? (Yes/No) : ")
while another_order != "No":
    if another_order == "Yes":
        item_2=input("enter the name of another  item : ")
        if item_2 in menu :
            order_total += menu[item_2]
            print(f"your item {item_2} has been added in your ordered !!")
        else:
            print(f"ordered item {item_2} has not been available yet !!")
    another_order=input("do you want to order another item ? (Yes/No) : ")

print(f"The total amount of items to pay is {order_total}")