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


ip_name = input("\nEnter file name ending with '.txt' to read the input: ")

nums = []

try:
	with open(ip_name, "r") as f:
		for line in f:
			line = line.strip()
			if line:
				if line.lstrip('-').isdigit():
					nums.append(int(line))
				else:
					raise ValueError(f"Invalid input '{line}'. File contains non-numeric values.")

except FileNotFoundError:
	print("Error: Input file not found.")
	exit()

except ValueError as e:
	print("Error:", e)
	exit()


mergesort(nums, 0, len(nums) - 1)

op_name = input("\nEnter file name for storing your output ending with '.txt' : ")

with open(op_name, "w") as f2:
	for num in nums:
		f2.write(f"{num}\n")

print(f"\nOutput Written to {op_name} successfully")
