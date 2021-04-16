def products(nums):
    prefix_list = []
    for num in nums:
        if prefix_list:
            prefix_list.append(prefix_list[-1] * num)
        else:
            prefix_list.append(num)
    
    suffix_list = []
    for num in reversed(nums):
        if suffix_list:
            suffix_list.append(suffix_list[-1] * num)
        else:
            suffix_list.append(num)
    suffix_list = list(reversed(suffix_list))

    result = []
    for i in range(len(nums)):
        if i == 0:
            result.append(suffix_list[i+1])
        elif i == len(nums) - 1:
            result.append(prefix_list[i - 1])
        else:
            result.append(prefix_list[i - 1] * suffix_list[i + 1])

    return result

def productDiv(nums):
    lsum = 1
    for num in nums:
        lsum *= num
    
    result = []
    for num in nums:
        result.append(lsum // num)
    
    return result

print(products(list([1, 2, 3, 4, 5])))
print(productDiv(list([1, 2, 3, 4, 5])))