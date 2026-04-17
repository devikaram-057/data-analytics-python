num=int(input("Input number of student:"))
pass_count=0
valid_count=0
fail_count=0
for i in range(num):
    mark=int(input(f"->Enter marks for student {i+1}:"))
    if mark==-1:
        print("Process stopped by user.")
        break
    if mark<0 or mark>100:
        print("Invalid mark,skipped")
        continue
    valid_count+=1
    if mark>=80: 
        print("Excellent")
        pass_count+=1
    elif mark>=60: 
        print("Good")
        pass_count+=1
    elif mark>=40: 
        print("Pass")
        pass_count+=1
    else: 
        print("Failed")
        fail_count+=1
else:
 print("->Analysis completed succesfully using loop else")
 print("Total valid students:",valid_count)
 print("Passed students:",pass_count)
 print("Failed students:",fail_count)