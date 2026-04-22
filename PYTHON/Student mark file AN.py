valid_marks=0
pass_marks=0
fail_marks=0
try:
    with open("marks.txt", "r") as file:
        for line in file:
            values=line.split()
            for val in values:
                try:
                    mark=int(val)
                    if mark<0 or mark>100:
                        raise ValueError("Mark out of range")
                    valid_marks+=1

                    if mark>=40:
                        pass_marks+=1
                    else:
                        fail_marks+=1

                except ValueError:
                    print(f"Invalid data skipped: {val}")

except FileNotFoundError:
    print("File not found!")
else:
    print("\nSummary:")
    print("Valid Marks:",valid_marks)
    print("Pass Marks:",pass_marks)
    print("Fail Marks:",fail_marks)
finally:
    print("\nFile processing completed.")
