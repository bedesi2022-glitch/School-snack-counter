snack1 = {"apple" , "banana" , "mango" , "apple" , "grape"}
snack2 = {"mango" , "kiwi" , "banana" , "kiwi"}
print("Snack1:" , snack1)
print("Snack2:" , snack2)
snack1.add("orange")
print("Snack1 after adding orange:" , snack1)
common_snacks = snack1.intersection(snack2)
print("Snacks in both baskets:" , common_snacks)
import array as arr
snack_counts = arr.array('i' ,[3,5,2,4])
print("Snacks counts array: " , snack_counts )
snack_counts.insert(0,1)
snack_counts.append(6)
print("Snack counts after adding items:" , snack_counts)
count_of_4 = snack_counts.count(4)
print("Number of items 4 appears:" , count_of_4)
snack_counts.reverse()
print("Reversed snacks counts array:" , snack_counts)
print("")
print("===SCHOOL SNACKS COUNTER===")
print("Snack1:" , snack1)
print("Snack2:" , snack2)
print("Shared snacks" , common_snacks)
print("Snack counts:", snack_counts)
print("=================================")



