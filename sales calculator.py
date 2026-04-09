unit_price=570
qty_sold=4
sales_tgt=3000
newqty_sales=3
qty_sold+=newqty_sales
tot_sales=unit_price*qty_sold
tgt_met=tot_sales>=sales_tgt
res=(tot_sales>=sales_tgt>0)
print("Sales Details:")
print("Price:",unit_price)
print("Total Quantity:",qty_sold)
print("Sales target:",sales_tgt)
print("Total Sales:",tot_sales)
print("Target Met:",res)



