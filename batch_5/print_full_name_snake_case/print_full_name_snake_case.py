#input full name
full_name = input("Input: ")
#convert to snake casing
full_name = full_name.lower()
full_name = full_name.split()
full_name = "_".join(full_name)
#print full name
print(f"Output: {full_name}")
