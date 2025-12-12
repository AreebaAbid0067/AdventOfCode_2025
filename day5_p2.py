ranges = []

with open("input_d5.txt") as f:
    for line in f:
        line = line.strip()
        if not line:
            break
        a, b = map(int, line.split("-"))
        ranges.append((a, b))

# Sort ranges
ranges.sort()

merged = []
cur_start, cur_end = ranges[0]

for start, end in ranges[1:]:
    if start <= cur_end + 1:
        cur_end = max(cur_end, end)
    else:
        merged.append((cur_start, cur_end))
        cur_start, cur_end = start, end

merged.append((cur_start, cur_end))

# Count total fresh IDs
total = sum(end - start + 1 for start, end in merged)

print(total)
