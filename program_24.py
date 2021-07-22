# 24). With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to make a list whose elements are intersection of the above given lists.

list1 = [1, 3, 6, 78, 35, 55]
list2 = [12, 24, 35, 24, 88, 120, 155]
list3 = []


if len(list1) > len(list2) or len(list1) == len(list2):
    for num in list1:
        if num in list2:
            list3.append(num)

elif len(list2) > len(list1) or len(list1) == len(list2):
    for num in list2:
        if num in list1:
            list3.append(num)
print(list3)
