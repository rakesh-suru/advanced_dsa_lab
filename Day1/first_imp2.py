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

    for k in range(len(temp):
        arr[left + k] = temp[k]


# Input file handling
ip_name = input("\nEnter input file name (.txt): ")

if not ip_name.endswith(".txt"):
    print("Error: Input file must have a .txt extension.")
    exit()

nums = []

try:
    with open(ip_name, "r") as f:
        for line_number, line in enumerate(f, start=1):
            line = line.strip()

            if line:
                try:
                    nums.append(int(line))
                except ValueError:
                    print(f"Error: Invalid value '{line}' at line {line_number}.")
                    exit()

except FileNotFoundError:
    print("Error: File does not exist.")
    exit()


if len(nums) == 0:
    print("Error: Input file is empty.")
    exit()


# Sorting
mergesort(nums, 0, len(nums) - 1)


# Output file handling
op_name = input("\nEnter output file name (.txt): ")

if not op_name.endswith(".txt"):
    print("Error: Output file must have a .txt extension.")
    exit()

with open(op_name, "w") as f2:
    for num in nums:
        f2.write(str(num) + "\n")

print(f"\nSorting completed successfully.")
print(f"Output written to {op_name}")
