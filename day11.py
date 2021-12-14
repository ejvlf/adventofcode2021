from common.text_manipulations import TextParser


def neighbours(r : int, c : int, max_r : int, max_c : int):
    for dr, dc in [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]:
        if 0 <= r + dr < max_r and 0 <= c + dc < max_c:
            yield r + dr, c + dc


def count_flashes(has_been_flashed : bool):
    return sum(1 for line in has_been_flashed for has_been in line if has_been)


def simulate_octopussy(octs : list, max_r : int, max_c : int):
    has_been_flashed = [[False for _ in range(max_r)] for __ in range(max_c)]

    for r in range(max_r):
        for c in range(max_c):
            octs[r][c] += 1
    flashes = -1
    while flashes != count_flashes(has_been_flashed):
        flashes = count_flashes(has_been_flashed)
        for r in range(max_r):
            for c in range(max_c):
                if octs[r][c] == 10 and not has_been_flashed[r][c]:
                    for rr, cc in neighbours(r, c, max_r, max_c):
                        octs[rr][cc] = min(octs[rr][cc] + 1, 10)
                    has_been_flashed[r][c] = True
    for r in range(max_r):
        for c in range(max_c):
            octs[r][c] %= 10

    return octs, flashes


def count_flashes_over_time_steps(octs : list, number_of_time_steps : int, max_r : int, max_c : int) -> int:
    total = 0
    for _ in range(number_of_time_steps):
        octs, count = simulate_octopussy(octs, max_r, max_c)
        total += count
    return total


def find_first_synchronization_time(octs : list, max_r : int, max_c : int) -> int:
    all_equal = all(octs[0][0] == octopus for line in octs for octopus in line)
    time = 0
    while not all_equal:
        octs, _ = simulate_octopussy(octs, max_r, max_c)
        all_equal = all(octs[0][0] == octopus for line in octs for octopus in line)
        time += 1
    return time


def run():

    source = TextParser("day11.txt", parse_to_ints=False).load_file_as_list()
    octopussy = [[int(c) for c in line.strip()] for line in source]
    max_r = len(octopussy)
    max_c = len(octopussy[0])

    # Part 1
    part_1_score = count_flashes_over_time_steps([[o for o in os] for os in octopussy], 100, max_r, max_c)
    print(f"Part 1 score: {part_1_score}")

    # PArt 2
    part_2_score = find_first_synchronization_time([[o for o in os] for os in octopussy], max_r, max_c)
    print(f"Part 2 score: {part_2_score}")


if __name__ == "__main__":

    run()