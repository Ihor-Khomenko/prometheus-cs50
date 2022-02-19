houses = {"Harry": "Griffindor", "Draco": "Slytherin"}
print("Harry's house is: ")
print(houses["Harry"])

hero = input("Input name: ")

if hero == "Harry":
    print(f"{hero} house is: " + houses["Harry"])

# Add Hermione
houses["Hermione"] = "Griffinfor"
print("Hermione's house is: ")
print(houses["Hermione"])