fb_msg=" Hello Team, the service was Excellent! "
print(fb_msg)
stripped=fb_msg.strip()
print("Uppercase:",fb_msg.upper())
print("Lowercase:",fb_msg.lower())
strpd_len=len(stripped)
if "service" in fb_msg:pass
if "bad" not in fb_msg:pass
print("First character:",stripped[0])
print("Last character:",stripped[-1])
print("Sliced:",stripped[14:23])
print(f"Cleaned Message:{stripped}")
print(f"Length of the string is {strpd_len}")
print(f"\'Service\' is found in\'{fb_msg}\'")
print(f"\'Bad\' is not found in{fb_msg}")