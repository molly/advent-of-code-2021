def part_one(data):
    increased_count = 0
    for i in range(1, len(data)):
        if data[i] > data[i - 1]:
            increased_count += 1

    print("Part one:", increased_count)


def part_two(data):
    increased_count = 0
    prev_window_sum = data[0] + data[1] + data[2]
    for i in range(3, len(data)):
        curr_window_sum = data[i - 2] + data[i - 1] + data[i]
        if curr_window_sum > prev_window_sum:
            increased_count += 1
        prev_window_sum = curr_window_sum
    print("Part two:", increased_count)


if __name__ == "__main__":
    with open("data/day1.txt", "r") as data_file:
        d = [int(l.strip()) for l in data_file.readlines()]

    part_one(d)
    part_two(d)


