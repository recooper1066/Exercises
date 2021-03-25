largest_so_far = -1
print('Before', largest_so_far)

for thing in [3, 41, 12, 9, 74, 15]:
   if thing > largest_so_far:
      largest_so_far = thing
   print (largest_so_far, thing)

print('After', largest_so_far)
