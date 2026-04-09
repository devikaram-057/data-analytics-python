user_bio="""Hi, I am Anjali.
I love Python programming.
Improving my programming skills is my goal."""
print("->",user_bio)
print("->Total number of characters:",len(user_bio))
lines=user_bio.split('\n')
count=len(lines)
print("->Total number of lines:",count)
print("->Looping:")
for character in user_bio:print(character)
print("Loop ended")
if "python" in user_bio:print("->Substring \'python\' found")
if "java" not in user_bio:print("->Substring \'java\' not found") 
print("->Replaced:",user_bio.replace("Anjali","Student"))
print("->",lines)
print("->",user_bio+"\nA line concatenated")
print("->This is a message with new line:\nNew line..!")
print("->A line with \'Single quotes\'")