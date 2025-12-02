# Function to check if a number is of the form X repeated twice
def is_repeated_twice(n):
    s = str(n)
    if len(s) % 2 != 0:       # must be even length
        return False
    
    half = len(s) // 2
    return s[:half] == s[half:]   # first half equals second half


# Puzzle input
data = "3737332285-3737422568,5858547751-5858626020,166911-236630,15329757-15423690,753995-801224,1-20,2180484-2259220,24-47,73630108-73867501,4052222-4199117,9226851880-9226945212,7337-24735,555454-591466,7777695646-7777817695,1070-2489,81504542-81618752,2584-6199,8857860-8922218,979959461-980003045,49-128,109907-161935,53514821-53703445,362278-509285,151-286,625491-681593,7715704912-7715863357,29210-60779,3287787-3395869,501-921,979760-1021259"

# Parse ranges
ranges = []
for part in data.split(","):
    a, b = part.split("-")
    ranges.append((int(a), int(b)))

invalid_ids = []
total = 0

# Process all ranges
for start, end in ranges:
    for num in range(start, end + 1):
        if is_repeated_twice(num):
            invalid_ids.append(num)
            total += num

# Output
print("Total invalid ID sum:", total)
# If you want to see them:
# print(invalid_ids)
