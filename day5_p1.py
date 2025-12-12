# Read input from file (paste your input into input.txt)
with open("input_d5.txt") as f:
    lines = [line.strip() for line in f.readlines()]

# Split ranges and values
split_index = lines.index("")
range_lines = lines[:split_index]
value_lines = lines[split_index + 1:]

# Parse ranges
ranges = []
for r in range_lines:
    start, end = map(int, r.split("-"))
    ranges.append((start, end))

# Sort ranges
ranges.sort()

# Merge overlapping ranges
merged = []
for start, end in ranges:
    if not merged or start > merged[-1][1] + 1:
        merged.append([start, end])
    else:
        merged[-1][1] = max(merged[-1][1], end)

# Parse available IDs
values = list(map(int, value_lines))

# Count fresh IDs
count = 0
for v in values:
    for start, end in merged:
        if start <= v <= end:
            count += 1
            break

print(count)
