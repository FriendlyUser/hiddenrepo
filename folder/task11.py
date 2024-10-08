import re
import collections

# Constants for Day 9 Part 2
SENSOR_BOOST_INPUT = 2

class IntcodeComputer:
    instruction_pattern = re.compile(r"(\d)(\d)(\d)(\d{2})")

    opcode_map = {
        1: "add",
        2: "multiply",
        3: "input",
        4: "output",
        5: "jump-if-true",
        6: "jump-if-false",
        7: "less than",
        8: "equals",
        9: "relative-base-offset",
        99: "exit",
    }

    def __init__(self, input, return_first_output=False):
        self.memory = [int(x) for x in input.split(",")]
        self.memory.extend([0 for _ in range(10_000 - len(self.memory))])
        self.pointer = 0
        self.relative_base = 0
        self.return_first_output = return_first_output

    def get_param_value(self, mode_param, param):
        if mode_param == "0":
            return self.memory[param]
        elif mode_param == "1":
            return param
        elif mode_param == "2":
            return self.memory[param + self.relative_base]

    def get_param_address(self, mode_param, param):
        if mode_param == "0":
            return param
        elif mode_param == "2":
            return param + self.relative_base

    def run(self, *input_values):
        input_values_index = 0
        while True:
            instruction = str(self.memory[self.pointer]).rjust(5, "0")
            m = self.instruction_pattern.match(instruction)
            opcode = m.group(4)
            mode_param1 = m.group(3)
            mode_param2 = m.group(2)
            mode_param3 = m.group(1)
            function = self.opcode_map.get(int(opcode))

            if function == "exit":
                break

            # Param definition
            param1 = self.memory[self.pointer + 1]
            self.pointer += 2
            param1_value = self.get_param_value(mode_param1, param1)
            param1_address = self.get_param_address(mode_param1, param1)

            if function not in ("input", "output", "relative-base-offset"):
                param2 = self.memory[self.pointer]
                self.pointer += 1
                param2_value = self.get_param_value(mode_param2, param2)

                if function not in ("jump-if-true", "jump-if-false"):
                    param3 = self.memory[self.pointer]
                    self.pointer += 1
                    param3_address = self.get_param_address(mode_param3, param3)

            # Function processing
            if function == "add":
                self.memory[param3_address] = param1_value + param2_value

            elif function == "multiply":
                self.memory[param3_address] = param1_value * param2_value

            elif function == "less than":
                self.memory[param3_address] = 1 if param1_value < param2_value else 0

            elif function == "equals":
                self.memory[param3_address] = 1 if param1_value == param2_value else 0

            elif function == "jump-if-true":
                if param1_value != 0:
                    self.pointer = param2_value

            elif function == "jump-if-false":
                if param1_value == 0:
                    self.pointer = param2_value

            elif function == "input":
                self.memory[param1_address] = input_values[input_values_index]
                input_values_index += 1

            elif function == "output":
                if self.return_first_output:
                    return param1_value
                print(param1_value)


def day07(input_data):
    def part1():
        values = []
        for amp_a_setting in range(5):
            for amp_b_setting in range(5):
                for amp_c_setting in range(5):
                    for amp_d_setting in range(5):
                        for amp_e_setting in range(5):
                            if len({amp_a_setting, amp_b_setting, amp_c_setting, amp_d_setting, amp_e_setting}) != 5:
                                continue

                            amp_a_output = IntcodeComputer(input_data, True).run(amp_a_setting, 0)
                            amp_b_output = IntcodeComputer(input_data, True).run(amp_b_setting, amp_a_output)
                            amp_c_output = IntcodeComputer(input_data, True).run(amp_c_setting, amp_b_output)
                            amp_d_output = IntcodeComputer(input_data, True).run(amp_d_setting, amp_c_output)
                            amp_e_output = IntcodeComputer(input_data, True).run(amp_e_setting, amp_d_output)

                            values.append(amp_e_output)

        return max(values)

    def part2():
        values = []
        for amp_a_setting in range(5, 10):
            for amp_b_setting in range(5, 10):
                for amp_c_setting in range(5, 10):
                    for amp_d_setting in range(5, 10):
                        for amp_e_setting in range(5, 10):
                            if len({amp_a_setting, amp_b_setting, amp_c_setting, amp_d_setting, amp_e_setting}) != 5:
                                continue

                            amp_a_computer = IntcodeComputer(input_data, True)
                            amp_b_computer = IntcodeComputer(input_data, True)
                            amp_c_computer = IntcodeComputer(input_data, True)
                            amp_d_computer = IntcodeComputer(input_data, True)
                            amp_e_computer = IntcodeComputer(input_data, True)

                            amp_a_output = amp_a_computer.run(amp_a_setting, 0)
                            amp_b_output = amp_b_computer.run(amp_b_setting, amp_a_output)
                            amp_c_output = amp_c_computer.run(amp_c_setting, amp_b_output)
                            amp_d_output = amp_d_computer.run(amp_d_setting, amp_c_output)
                            amp_e_output = amp_e_computer.run(amp_e_setting, amp_d_output)

                            last_value = 0

                            while True:
                                amp_a_output = amp_a_computer.run(amp_e_output)
                                amp_b_output = amp_b_computer.run(amp_a_output)
                                amp_c_output = amp_c_computer.run(amp_b_output)
                                amp_d_output = amp_d_computer.run(amp_c_output)
                                amp_e_output = amp_e_computer.run(amp_d_output)

                                if amp_e_output is None:
                                    break

                                last_value = amp_e_output

                            values.append(last_value)

        return max(values)

    result1 = part1()
    result2 = part2()
    return result1, result2


def day09(input_data):
    def part1():
        IntcodeComputer(input_data).run(1)

    def part2():

        IntcodeComputer(input_data).run(SENSOR_BOOST_INPUT)

    part1()
    part2()


def day02(input_data):
    def run(noun, verb):
        memory = [int(x) for x in input_data.split(",")]
        memory[1] = noun
        memory[2] = verb

        pointer = 0
        instruction = 0
        while instruction != 99:
            instruction = memory[pointer]
            param1 = memory[pointer + 1]
            param2 = memory[pointer + 2]
            param3 = memory[pointer + 3]
            pointer += 4

            if instruction == 1:
                memory[param3] = memory[param1] + memory[param2]
            elif instruction == 2:
                memory[param3] = memory[param1] * memory[param2]

        return memory[0]

    def part1():
        return run(12, 2)

    def part2():
        for noun in range(100):
            for verb in range(100):
                if run(noun, verb) == 19690720:
                    return 100 * noun + verb

    return part1(), part2()


def day04():
    def is_valid_part1(password):
        return password == "".join(sorted(password)) and len(set(password)) < 6

    def is_valid_part2(password):
        return password == "".join(sorted(password)) and 2 in collections.Counter(password).values()

    part1 = 0
    part2 = 0

    for i in range(172851, 675870):
        if is_valid_part1(str(i)):
            part1 += 1
        if is_valid_part2(str(i)):
            part2 += 1

    return part1, part2


def day08(input_data):
    input_list = list(input_data)
    layers = []

    while input_list:
        layer = []
        for _ in range(6):
            row = []
            for __ in range(25):
                row.append(input_list.pop(0))
            layer.append(row)
        layers.append(layer)

    def part1():
        min_0 = None
        min_layer = None

        for layer in layers:
            layer_count = 0
            for row in layer:
                layer_count += row.count("0")
            if min_0 is None or layer_count < min_0:
                min_0 = layer_count
                min_layer = layer

        digits_1 = 0
        digits_2 = 0
        for row in min_layer:
            digits_1 += row.count("1")
            digits_2 += row.count("2")

        return digits_1 * digits_2

    def part2():
        image = []

        for y in range(6):
            image_row = []
            for x in range(25):
                for layer in layers:
                    if layer[y][x] != "2":
                        image_row.append(layer[y][x])
                        break
            image.append(image_row)

        image_result = "\n".join("".join(row).replace("1", "#").replace("0", ".") for row in image)
        return image_result

    return part1(), part2()


def day06(input_data):
    orbit_map = {}
    for line in input_data.splitlines():
        orbited = line[:line.index(")")]
        orbiting = line[line.index(")") + 1:]
        orbit_map[orbiting] = orbited

    def count_orbits(planet):
        if planet == "COM":
            return 0
        return 1 + count_orbits(orbit_map[planet])

    def get_orbited(planet, orbited):
        orbited.append(planet)
        if planet != "COM":
            get_orbited(orbit_map[planet], orbited)

    def part1():
        total = 0
        for planet in orbit_map.keys():
            total += count_orbits(planet)
        return total

    def part2():
        you_orbiting = []
        san_orbiting = []
        get_orbited(orbit_map["YOU"], you_orbiting)
        get_orbited(orbit_map["SAN"], san_orbiting)

        for planet in you_orbiting:
            if planet in san_orbiting:
                common_planet = planet
                break

        return you_orbiting.index(common_planet) + san_orbiting.index(common_planet)

    return part1(), part2()


def day01(input_data):
    def calculate_fuel(mass):
        return int(mass / 3) - 2

    def part1():
        total = 0
        for module_mass in input_data.splitlines():
            total += calculate_fuel(int(module_mass))
        return total

    def part2():
        total = 0
        for module_mass in input_data.splitlines():
            fuel = int(module_mass)
            while fuel >= 9:
                fuel = calculate_fuel(fuel)
                total += fuel
        return total

    return part1(), part2()


def day05(input_data):
    def part1():
        return IntcodeComputer(input_data).run(1)

    def part2():
        return IntcodeComputer(input_data).run(5)

    return part1(), part2()


def day03(input_data):
    def get_coords(wire_path):
        coords = {}
        step_count = 0
        x = 0
        y = 0

        for step in wire_path.split(","):
            direction = step[:1]
            distance = step[1:]

            for _ in range(int(distance)):
                step_count += 1
                if direction == "R":
                    x += 1
                elif direction == "L":
                    x -= 1
                elif direction == "U":
                    y += 1
                elif direction == "D":
                    y -= 1

                coords[(x, y)] = step_count

        return coords

    wire1_coords = get_coords(input_data.splitlines()[0])
    wire2_coords = get_coords(input_data.splitlines()[1])
    intersections = set(wire1_coords) & set(wire2_coords)

    min_distance = min([abs(x) + abs(y) for (x, y) in intersections])
    min_steps = min([wire1_coords[(x, y)] + wire2_coords[(x, y)] for (x, y) in intersections])

    return min_distance, min_steps


def main():
    with open("input/day01.txt") as file:
        input_day01 = file.read()

    with open("input/day02.txt") as file:
        input_day02 = file.read()

    with open("input/day03.txt") as file:
        input_day03 = file.read()

    with open("input/day04.txt") as file:
        input_day04 = file.read()

    with open("input/day05.txt") as file:
        input_day05 = file.read()

    with open("input/day06.txt") as file:
        input_day06 = file.read()

    with open("input/day07.txt") as file:
        input_day07 = file.read()

    with open("input/day08.txt") as file:
        input_day08 = file.read()

    with open("input/day09.txt") as file:
        input_day09 = file.read()

    # Testing the core functionality of the script with print statements
    print("Results for Day 01:", day01(input_day01))
    print("Results for Day 02:", day02(input_day02))
    print("Results for Day 03:", day03(input_day03))
    print("Results for Day 04:", day04())
    print("Results for Day 05:", day05(input_day05))
    print("Results for Day 06:", day06(input_day06))
    print("Results for Day 07:", day07(input_day07))
    print("Results for Day 08:", day08(input_day08))
    day09(input_day09)


if __name__ == "__main__":
    main()
