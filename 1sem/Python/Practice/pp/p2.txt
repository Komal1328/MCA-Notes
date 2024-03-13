phone_book = {}

# Adding entries to phone book
phone_book["Sam"] = 9832113224
phone_book["Ram"] = 7832113224
phone_book["Joy"] = 9854103224
phone_book["Abhi"] = 7439925256
print("Phone Book: ",phone_book)
print()

# Deleting an entry from phone book
del phone_book["Ram"]
print("Phone Book after deletion: ",phone_book)
print()

# Searching an entry in phone book
if "Joy" in phone_book:
    print("XYZ's number is", phone_book["Joy"])
else:
    print("Joy is not in the phone book.")
print()

# Sorting the elements of the phone book based on names in ascending order
sorted_phone_book = dict(sorted(phone_book.items(), key=lambda x: x[1]))

# Printing the sorted phone book
print("Sorted phone book:",sorted_phone_book)
