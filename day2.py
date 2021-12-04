def part_one(data):
    horiz = 0
    depth = 0
    for i in range(len(data)):
        [command, value] = data[i].split(" ")
        value = int(value)
        if command == "forward":
            horiz += value
        elif command == "down":
            depth += value
        else:
            depth -= value
    return horiz * depth


def part_two(data):
    aim = 0
    horiz = 0
    depth = 0
    for i in range(len(data)):
        [command, value] = data[i].split(" ")
        value = int(value)
        if command == "forward":
            horiz += value
            depth += aim * value
        elif command == "down":
            aim += value
        else:
            aim -= value
    return horiz * depth


if __name__ == "__main__":
    with open("data/day2.txt", "r") as data_file:
        d = [l.strip() for l in data_file.readlines()]

    print(part_one(d))
    print(part_two(d))