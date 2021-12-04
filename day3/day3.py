import sys
sys.path.append("/home/ejvlf/personal/adventofcode2021")
print(sys.path)

from common.text_manipulations import TextParser

def calculate_rates (column : list) -> str:

    count_of_0 = 0
    count_of_1 = 0
    gamma_bit = ""
    epsilon_bit = ""

    for bit in column:

        if bit == "0":
            count_of_0 += 1
        else:
            count_of_1 += 1

    if count_of_0 > count_of_1:

        gamma_bit = "0"
        epsilon_bit = "1"

    else:

        gamma_bit = "1"
        epsilon_bit = "0"

    return gamma_bit, epsilon_bit    
       
def o2_binary(i, work_list):
    zeros = 0
    ones = 0

    for x in work_list:
        if x[i] == '0':
            zeros += 1
        else: ones += 1
    if zeros > ones:
        return '0'
    else: return '1'

def co2_binary(i, work_list):
    zeros = 0
    ones = 0

    for x in work_list:
        if x[i] == '0':
            zeros += 1
        else: ones += 1
    if zeros > ones:
        return '1'
    else: return '0'

def engine(fun, source):
    lines_gen = source
    i = 0
    while i < 12:
        if len(lines_gen) == 1:
            break
        else: 
            bit_to_add = fun(i, lines_gen)
            lines_gen = list(filter(lambda x: x[i] == bit_to_add, lines_gen))
            i += 1
    return lines_gen[0]

def run():

    #source file loading
    source_list = TextParser("day3.txt", parse_to_ints=False).load_file_as_list()
    gamma_rate : str = ""
    epsilon_rate : str = ""
    counter : dict = {}

    # Part 1 

    # get the bytes per column
    for byte in source_list:

        for i in range(0, len(byte)):

            if i in counter:
                counter[i].append(byte[i])
            else :
                counter[i] = [byte[i]]

    
    # append the bytes to rates
    for col in counter:

        gamma_char, epsilon_char = calculate_rates(counter[col])

        gamma_rate = gamma_rate + gamma_char
        epsilon_rate = epsilon_rate + epsilon_char

    gamma_rate_dec = int(gamma_rate, 2)
    epsilon_rate_dec = int(epsilon_rate, 2)

    print(f"Part 1 solution is {gamma_rate_dec * epsilon_rate_dec}")

    # Part 2

    o2 = int(engine(o2_binary, source_list), 2)
    co2 = int(engine(co2_binary, source_list), 2)

    print(f"Part 2 solution is {o2 * co2}")
        
if __name__ == "__main__":

    run()