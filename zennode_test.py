# Our products are apple, banana, orange.

apple = 20

banana = 40

orange = 50

# Asking the user if they want the product to be wrapped in the gift or not. Uses recursive function because we need the exact answer (yes / no).

def giftwrap():

    gift_wrap = input("Do you want this product wrapped as a gift (yes/no)")

    yes_choices = ['yes', 'y']

    no_choices = ['no', 'n']

    if gift_wrap.lower() in yes_choices:
        
        return 1
    
    elif gift_wrap.lower() in no_choices:
        
        return 0
    
    else:

        # if the user type something else rather than yes/no it will ask the question again until we get yes/no

        print("You have entered the wrong answer. please read carefully.")

        wrap = giftwrap()

        return wrap



wrap_apple = 0

wrap_banana = 0

wrap_orange = 0

# Taking the quantity of each product that user wants.

apple_amount = int(input("How much apple do you want ?"))

if apple_amount > 0:

    wrap_apple = giftwrap()

banana_amount = int(input("How much banana do you want ?"))

if banana_amount > 0:

    wrap_banana = giftwrap()

orange_amount = int(input("How much orange do you want ?"))

if orange_amount > 0:

    wrap_orange = giftwrap()


# To show orderd product and their prices.

if apple_amount > 0:

    print("You have orderd",apple_amount,"apple for :$", apple*apple_amount)

    
if banana_amount > 0:

    print("You have orderd",banana_amount,"banana for :$", banana*banana_amount)

    
if orange_amount > 0:

    print("You have orderd",orange_amount,"orange for : $", orange*orange_amount)



total_amount = apple_amount + banana_amount + orange_amount

# total price of ordered products

subtotal = apple*apple_amount+banana*banana_amount+orange*orange_amount

print("subtotal for this purchase is : $",subtotal)


flat_10_discount = 0

bulk_5_discount = 0

bulk_10_discount = 0

tiered_50_discount = 0

discount_1 = 0

discount_2 = 0

discount_3 = 0

discount_4 = 0


# Calculating every discount to find out how much discount customer can get from every discount

# flat_10_discount

if subtotal > 200:

    discount_1 = 10

    flat_10_discount = subtotal - discount_1


# bulk_5_discount

if apple_amount >10 or orange_amount > 10 or banana_amount > 10:

    if apple_amount > 10:
        
        discount_2 = (apple_amount*apple*5)/100
        
    elif banana_amount > 10:

        discount_2 = (banana_amount*banana*5)/100
        
    elif orange_amount > 10:

        discount_2 = (orange_amount*orange*5)/100

bulk_5_discount = subtotal - discount_2


#bulk_10_discount

if apple_amount + banana_amount + orange_amount > 20:

    discount_3 = (subtotal * 10) / 100

    bulk_10_discount = subtotal - discount_3


#tiered_50_discount

if (apple_amount + banana_amount + orange_amount > 30) and ( apple_amount > 15 or banana_amount > 15 or orange > 15 ):

    if apple_amount > 15 :

        discount_4 = ( (apple_amount - 15 ) * apple * 50 ) / 100


    elif banana_amount > 15 :

        discount_4 = ( ( banana_amount - 15 ) * banana * 50 ) / 100


    elif orange_amount > 15 :

        discount_4 = ( ( orange_amount - 15 ) * orange * 50 ) / 100


    tiered_50_discount = subtotal - discount_4
    

# Sorting the discount and selecting the most sutable discount for this customer

final_discount = [ discount_1 , discount_2 , discount_3 , discount_4 ]

final_discount.sort()

discount_flag=0

if final_discount[3] == discount_1:

    discount_flag=1

    print("flat_10_discount is applied. The discount amount is : $", discount_1)

elif final_discount[3] == discount_2:

    discount_flag=2

    print("bulk_5_discount is applied. The discount amount is : $", discount_2)

elif final_discount[3] == discount_3:

    discount_flag=3

    print("bulk_10_discount is applied. The discount amount is : $", discount_3)

elif final_discount[3] == discount_4:

    discount_flag=4

    print("tiered_50_discount is applied. The discount amount is : $", discount_4)


# Applying that selected discount value to the total price

if discount_flag == 1:

    total = flat_10_discount 

elif discount_flag == 2:

    total = bulk_5_discount 

elif discount_flag == 3:

    total = bulk_10_discount 

elif discount_flag == 4:

    total = tiered_50_discount 

else: 
    total = subtotal


total_gift_wrap_fee = 0

# Adding the gift wrap fee to the total price

if wrap_apple == 1:

    total=total + apple_amount

    total_gift_wrap_fee = total_gift_wrap_fee + apple_amount

    print("Gift wrap fee for apple : $", apple_amount)

if wrap_banana == 1:

    total=total + banana_amount

    total_gift_wrap_fee = total_gift_wrap_fee + banana_amount

    print("Gift wrap fee for banana : $", banana_amount)

if wrap_orange == 1:

    total=total + orange_amount

    total_gift_wrap_fee = total_gift_wrap_fee + orange_amount

    print("Gift wrap fee for orange : $", orange_amount)


if wrap_orange == 1 or wrap_banana == 1 or wrap_apple == 1:

    print("total gift wrap fee is : $", total_gift_wrap_fee)


# Adding the shipping amount to the total price. 

if total_amount % 10 == 0:

    package_quantity = int( ( total_amount / 10 ))

    print("The shipping fee for your purchase : $", package_quantity * 5)
    
else:

    package_quantity = int( ( total_amount / 10 ) +1)

    print("The shipping fee for your purchase : $", package_quantity * 5)

shipping_fee = package_quantity * 5

total = total + shipping_fee

print("Your total amount for this order is : $", total)
