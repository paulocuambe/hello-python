my_list = ["apple", "banana", "cherry", "mango"]

print(my_list[-2])  # Second last item of the list

my_list.append("lemon")

if "lemon" in my_list:
    print("Yes, that fruit is in the list.")
else:
    print("That fruit is not in the list.")

my_list.insert(2, "orange")
print(my_list)

new_list = my_list[1:]
print(new_list)

new_list.sort()
print(new_list)
print(sorted(my_list))

nums = [1, 3, 6, 7, 9]
sqr_list = [x * x for x in nums]
nums.extend([10, 12, 13])
print(nums)
print(sqr_list)

sqr_list.pop()
del nums[1:2]
print(nums)
print(sqr_list)
