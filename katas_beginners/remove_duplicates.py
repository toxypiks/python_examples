def remove_duplicates(nums):
    for i in range(0,len(nums)):
        for j in range(1,len(nums)):
            if nums[i] == nums[j]:
                nums.pop(j)
                nums.append(-1)
    unique_nums = 0
    print(nums)
    for number in nums:
        if number != -1:
            unique_nums = unique_nums + 1
    return unique_nums

def main():
    nums = [1,1,1,3,3,3,4,4,4,5,5,5]
    no_duplicates = remove_duplicates(nums)
    print(no_duplicates)

if __name__ == "__main__":
    main()
