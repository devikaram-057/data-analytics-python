st_name="Aradhya"
exam_sc=99
att_per=89
bns_marks=20
final_sc=exam_sc+bns_marks
sc_check=final_sc>=75
att_check=att_per>=80
iseligible=(sc_check) and (att_check)
print("Student Deatils: ")
print("Student Name:",st_name)
print("Final score:",final_sc)
print("Attendence percentage:",att_per,"%")
print("Eligibility status:",iseligible)