product_name="boost"
price="70"
qty="2"
disc_per=30
price=float(price)
qty=int(qty)
total_amt=price*qty
disc_amt=(disc_per/100)*total_amt
final_amt=total_amt-disc_amt
tax=service_charge=0
print("Bill Details:")
print("Product Name:",product_name)
print("Product Price:",price)
print("Quantity:",qty)
print("Total Amount:",total_amt)
print("Discount:",disc_per,"%")
print("Discount Amount:",disc_amt)
print("Final Price:",final_amt)