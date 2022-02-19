# Create an empty set
s = set()

# Add elements to set
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(5)
s.add(3)
print("Show elements from the set. Dublicates are not shown")
print(s)
print(f"The set has {len(s)} elements.")

s.remove(2)
print("Remove 2 from the set")
print(s)

# len - shows quantity
print(f"The set has {len(s)} elements.")