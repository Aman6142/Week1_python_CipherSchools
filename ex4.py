name,char=input("enter comma sepertaed name and character: ").split(",")
print(f"length of name is {len(name)}")
print(f"character count:{name.count(char)}") #case sensitive
#Ankit - ankit
#A - a
print(f"character count:{name.lower().count(char.lower())}")
