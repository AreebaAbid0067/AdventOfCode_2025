def solve(rotations):
    pos = 50
    part1 = 0
    part2 = 0

    for rot in rotations:
        direction = rot[0]
        dist = int(rot[1:])

        step = 1 if direction == 'R' else -1

      
        for _ in range(dist):
            pos = (pos + step) % 100
            if pos == 0:
                part2 += 1

    
        if pos == 0:
            part1 += 1

    return part1, part2


with open("puzzle_input.txt") as f:
    rotations = f.read().strip().split()

p1, p2 = solve(rotations)

print("Part 1 password =", p1)
print("Part 2 password =", p2)
