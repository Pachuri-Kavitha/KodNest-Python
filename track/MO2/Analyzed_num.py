# Read how many numbers will be entered
size = int(input())
# Initialize the counters and total
pos_count = 0
neg_count = 0
zero_count = 0
total = 0

# Read and analyze each number
for i in range(size):
    num = int(input())
    if num > 0:
        pos_count += 1
    elif num < 0:
        neg_count += 1
    else:
        zero_count += 1
    total += num

# Display the final analysis
print(f"Positive Count: {pos_count}")
print(f"Negative Count: {neg_count}")
print(f"Zero Count: {zero_count}")
print(f"Total: {total}")
