def classify_sales(sales_amt):
    if sales_amt>=100000:return " High Performance"
    elif sales_amt>=50000:return " Average Performance"
    else: return "Low Performance"
calc_bonus=lambda sales_amt:sales_amt*0.05
def tot_sales_recursive(sales_list):
    if len(sales_list) == 0:
        return 0
    return sales_list[0] + tot_sales_recursive(sales_list[1:])
months=int(input("Enter number of months:"))
sales_data = []

for i in range(months):
    sales_amt=int(input(f"->Enter sales amount of month {i+1}:"))
    if sales_amt==-0:
        print("->Skipped")
        continue
    if sales_amt<0:
        print("->Negetive value entered.Stopping input")
        break
    sales_data.append(sales_amt)
print("->Month-wise report")
for i, sale in enumerate(sales_data, start=1):
    category = classify_sales(sales_amt)
    bonus = calc_bonus(sales_amt)
    print(f"Month {i}:")
    print(f"  Sales: {sales_amt}")
    print(f"  Category: {category}")
    print(f"  Bonus: {bonus}")
    print()
total = tot_sales_recursive(sales_data)
print("Total Sales:", total)


