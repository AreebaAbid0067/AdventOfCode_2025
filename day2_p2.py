# PART 2 – Find invalid IDs made of a repeated pattern (repeated 2+ times)

def is_repeated_pattern(num_str):
    """Return True if num_str is some substring repeated 2+ times"""
    n = len(num_str)
    # Try every possible pattern length that divides the full length
    for pat_len in range(1, n // 2 + 1):
        if n % pat_len == 0:
            pattern = num_str[:pat_len]
            if pattern * (n // pat_len) == num_str:
                return True
    return False


def sum_invalid_ids(input_line):
    total = 0
    # Split by commas into ranges
    ranges = input_line.strip().split(",")

    for r in ranges:
        start, end = map(int, r.split("-"))
        for num in range(start, end + 1):
            s = str(num)
            if is_repeated_pattern(s):
                total += num

    return total


# --- INPUT PROVIDED BY YOU ---
puzzle_input = (
"3737332285-3737422568,5858547751-5858626020,166911-236630,15329757-15423690,"
"753995-801224,1-20,2180484-2259220,24-47,73630108-73867501,4052222-4199117,"
"9226851880-9226945212,7337-24735,555454-591466,7777695646-7777817695,1070-2489,"
"81504542-81618752,2584-6199,8857860-8922218,979959461-980003045,49-128,109907-161935,"
"53514821-53703445,362278-509285,151-286,625491-681593,7715704912-7715863357,29210-60779,"
"3287787-3395869,501-921,979760-1021259"
)

print("Calculating... please wait (large ranges).")
answer = sum_invalid_ids(puzzle_input)
print("Answer for Part 2 =", answer)
