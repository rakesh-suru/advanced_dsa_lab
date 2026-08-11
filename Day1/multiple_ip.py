def mergesort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        mergesort(arr, left, mid)
        mergesort(arr, mid + 1, right)

        merge(arr, left, mid, right)


def merge(arr, left, mid, right):
    i = left
    j = mid + 1
    temp = []

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1

    while i <= mid:
        temp.append(arr[i])
        i += 1

    while j <= right:
        temp.append(arr[j])
        j += 1

    for k in range(len(temp)):
        arr[left + k] = temp[k]


ip_name = input("\nEnter file name ending with '.txt' : ")

# Read all lines
with open(ip_name, "r") as f:
    lines = f.readlines()

# Remove only newline characters
lines = [line.strip() for line in lines]

test_cases = []
i = 0

while i < len(lines):

    # Skip empty lines
    if lines[i] == "":
        i += 1
        continue

    # First number is n
    n = int(lines[i])
    i += 1

    nums = []

    # Read n numbers
    for _ in range(n):
        if i < len(lines) and lines[i] != "":
            nums.append(int(lines[i]))
            i += 1

    test_cases.append(nums)

# Sort every test case
for nums in test_cases:
    mergesort(nums, 0, len(nums) - 1)


op_name = input("\nEnter file name for storing your output ending with '.txt' : ")

with open(op_name, "w") as f2:
    for nums in test_cases:
        for num in nums:
            f2.write(f"{num}\n")

        # Empty line between test cases
        f2.write("\n")

print(f"\nOutput Written to {op_name} successfully")