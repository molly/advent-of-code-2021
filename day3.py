def part_one(data):
    num_zeroes_in_pos = [0] * len(d[0])
    for entry in data:
        for pos in range(len(entry)):
            if entry[pos] == '0':
                num_zeroes_in_pos[pos] += 1

    total_entries = len(data)
    gamma = ''
    epsilon = ''
    for freq_zero in num_zeroes_in_pos:
        if freq_zero > total_entries / 2:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'
    return int(gamma, 2) * int(epsilon, 2)


def get_num_zeroes_in_position(data, position):
    num_zeroes = 0
    for entry in data:
        if entry[position] == '0':
            num_zeroes += 1
    return num_zeroes


def filter_by_bit_criteria(data, comparator):
    filtered_data = []
    current_bit = 0
    while True:
        total_entries = len(data)
        num_zeroes = get_num_zeroes_in_position(data, current_bit)
        bit_to_keep = comparator(num_zeroes, total_entries)
        for entry in data:
            if entry[current_bit] == bit_to_keep:
                filtered_data.append(entry)
        if len(filtered_data) == 1:
            return filtered_data[0]
        data = filtered_data
        filtered_data = []
        current_bit += 1


def part_two(data):
    oxygen_generator = filter_by_bit_criteria(
        data,
        lambda zs, num_entries: '1' if zs <= num_entries / 2 else '0'
    )
    co2_scrubber = filter_by_bit_criteria(
        data,
        lambda zs, num_entries: '0' if zs <= num_entries / 2 else '1'
    )

    return int(oxygen_generator, 2) * int(co2_scrubber, 2)


if __name__ == "__main__":
    with open("data/day3.txt", "r") as data_file:
        d = [l.strip() for l in data_file.readlines()]

    print(part_one(d))
    print(part_two(d))
