def card_finder(arr, firstbound, lastbound, element):
    if lastbound > firstbound:
        mid = (firstbound + lastbound) // 2
        if arr[mid] == element:
            return mid
        elif element < arr[mid]:
            print(firstbound, "  ", lastbound)
            return card_finder(arr, firstbound, mid - 1, element)
        else:
            print(firstbound, "  ", lastbound)
            return card_finder(arr, mid + 1, lastbound, element)
    else:
        return -1


print("Enter list/array to search in :")
lst1 = [int(i) for i in input().split()]
if len(lst1) == 0:
    print("Array invalid")
    exit()
lst1 = sorted(lst1)
element_to_find = int(input("Enter element to find :"))
index = card_finder(lst1, 0, len(lst1) - 1, element_to_find)
if index == -1:
    print("Not found")
else:
    print("Element Index = ", index)
