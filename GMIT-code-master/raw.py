# question 1
print("Welcome To Code-Master-Hotel")
gst=12
s=" "
detail=[]
name =input("Sir! your name :")
detail.append(name)
ph =input("your phone number :")
detail.append(ph)

items_name=["Gobi","Pizza","Burger","PaniPuri","Biryani","Panner Masala","Egg Curry","Roti","Soda"]
items_prize=[30,60,90,20,90,40,40,20,15]
print()
print('{:-^33}'.format('order list'))
for i in range(0,len(items_name)):
    print(f"id.{i}{s*5}{items_name[i]}  {s*(15-len(items_name[i]))}{items_prize[i]}rs")

print()
order_list=[]
qunatity_list=[]

print(" Order  Now Sir/Madam")
continue_order=True
while(continue_order):
    order=int(input("enter your order id :"))
    qunatity=int(input("Quantity sir :"))
    order_list.append(order)
    qunatity_list.append(qunatity)
    co=input("Would you like to order more [y/n] :")
    if co=='n':
        continue_order=False
    else:
        print()
        print("Order Menu")
        for i in range(0,len(items_name)):
            print(f"id. {i}{s*5}{items_name[i]}  {s*(15-len(items_name[i]))}: {items_prize[i]}rs")
        print()

print()
print()


sum_amnt=0
print("--------------------------------------------------------------------")
print(f"                Welcome to our hotel ")
print("--------------------------------------------------------------------")

print(f"Name :{name}                                       Ph No:{ph}")
print("-----------------------order list----------------------------------")
print(f"Perticular{s*10}Quantity{s*12}Prize{s*15}Amount")
for i in range(0,len(order_list)):
    print(f"{items_name[order_list[i]]}{s*(20-len(items_name[order_list[i]]))}{qunatity_list[i]}{s*(20-len(str(qunatity_list[i])))}{items_prize[order_list[i]]}{s*(20-len(str(items_prize[order_list[i]])))}{qunatity_list[i] * items_prize[order_list[i]]}")
    sum_amnt=sum_amnt+qunatity_list[i] * items_prize[order_list[i]]


print("--------------------------------------------------------------------")
print(f"Total amount :{sum_amnt}")
print()
print(f"Total  GST({gst})% :{(sum_amnt * (gst/100))}")
print("--------------------------------------------------------------------")
print(f"Total Amnt including GST :{(sum_amnt * (gst/100))+sum_amnt}")
print("--------------------------------------------------------------------")
