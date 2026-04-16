mobile_buyers={120,132,143,122}
laptop_buyers={132,178,122}
print("->Customers who bought both mobile and laptop:",mobile_buyers.intersection(laptop_buyers))
print("->Customers who bought only mobile:",mobile_buyers.difference(laptop_buyers))
print("->Customers who bought only laptop:",laptop_buyers.difference(mobile_buyers))
print("->Total unique customers:",len(mobile_buyers.union(laptop_buyers)))
mobile_buyers.remove(120)
print("120 cancelled the order of mobile,hence removed..!-",mobile_buyers)
c_profile={
    120:{"name":"Ben","city":"Mumbai","tot_purchase":20000},
    132:{"name":"Mick","city":"Kolkata","tot_purchase":60000},
    143:{"name":"Olive","city":"Delhi","tot_purchase":70000},
    122:{"name":"Zeke","city":"Goa","tot_purchase":95000},
    178:{"name":"Cal","city":"LA","tot_purchase":45000}
}
print("->All customer IDs:")
for id in c_profile:print(id,end=" ")
print("\n->Customers with purchase above ₹50, 000:")
for id in c_profile:
    if c_profile[id]["tot_purchase"]>50000:
        print(c_profile[id]["name"],end=" ")
c_profile[124]={"name":"Saanvi","city":"Goa","tot_purchase":19000}
print("\n->A new customer was added")
del c_profile[143]
print("->A customer deleted")
print("->After adding and deleting details,the customer IDs are:")
for id in c_profile:print(id,end=" ")
new_info=c_profile.copy()
c_profile.clear()
print("\n->The copied dictionary:",new_info)
print("\n->The cleared dictionary:",c_profile)