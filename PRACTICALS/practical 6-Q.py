


A = input("Enter status of Room A (Clean/Dirty): ").lower()
B = input("Enter status of Room B (Clean/Dirty): ").lower()
location = input("Enter vacuum location (A/B): ").upper()

if location == "A":
    if A == "dirty":
        print("Room A is cleaned")
        A = "clean"
    if B == "dirty":
        print("Moving to Room B")
        print("Room B is cleaned")
        B = "clean"

elif location == "B":
    if B == "dirty":
        print("Room B is cleaned")
        B = "clean"
    if A == "dirty":
        print("Moving to Room A")
        print("Room A is cleaned")
        A = "clean"

print("Final status of Room A:", A)
print("Final status of Room B:", B)
