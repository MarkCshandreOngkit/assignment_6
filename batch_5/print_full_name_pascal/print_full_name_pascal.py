#input full name
full_name = input("Input: ")
#convert to pascal casing
full_name = full_name.title()
full_name = full_name.split()
full_name = "".join(full_name)
#print full name
print(f"Output: {full_name}")

