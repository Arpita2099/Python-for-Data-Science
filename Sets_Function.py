# Function of sets
# len/sum/min/max
s={1,2,3,4,5}
s1={2,4,6,8,10}
print(sum(s))
print(len(s))
print(min(s))
print(max(s))
print(sorted(s))
print(sorted(s,reverse=True))

# intersection/unino/
# union/update
s={1,2,3,4,5}
s1={2,4,6,8,10}
# s1|s2
print(s1.union(s))
# Update
s.update(s1)
print(s1)

# intersection/intersection_update
s1={1,2,3,4,5}
s2={6,7,8,9,10}
s1.intersection(s2)
s1.intersection_update(s2)
print(s1)
print(s2)

# difference/difference_update
s1={1,2,3,4,5}
s2={6,7,8,9,10}
s1.difference(s2)
s1.difference_update(s2)
print(s1)
print(s2)

# symmetric_difference/ symmetric_difference_update
s1={1,2,3,4,5}
s2={6,7,8,9,10}
s1.symmetric_difference(s2)
s1.symmetric_difference_update(s2)
print(s1)
print(s2)

# isdisjoint
s1={1,2,3,4,5}
s2={2,4,6,8,10}
print(s1.isdisjoint(s2))

# issubset
s={1,2,3,4,5}
s1={3,4,5}
print(s1.issubset(s2))

# issuperset
s={1,2,3,4,5}
s1={3,4,5}
print(s1.issuperset(s2))

# copy
s1={1,2,3}
s2=s1.copy()
print(s2)

# frozenset: Frozen set is just an immutable version of a Python set object.
fs= frozenset([1,3,5])
print(fs)

# Set Comprehension
print({i for i in range(1,11) if i>5})
