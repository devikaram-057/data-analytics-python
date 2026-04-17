import csv
try:
    with open("sales.csv","r") as file:
        reader=csv.reader(file)
        header=next(reader)
        data=[]
        for row in reader:
            month,amt=row
            try:
                amt=float(amt)
                if amt<0:
                    raise ValueError("Negative value found for:",month)
                if amt>=80000:
                    cat="High"
                elif amt>=50000:
                    cat="Medium"
                else:
                    cat="Low"
                data.append([month,amt,cat])
            except ValueError:
                print("Skiipping Invalid data:",row)
    with open("sales_summary.csv","w",newline="") as file:
        writer=csv.writer(file)
        writer.writerow(["month","amount","category"])
        writer.writerows(data)
    print("Summary file created.")
except FileNotFoundError:
    print("sales.csv file not found")
              
                