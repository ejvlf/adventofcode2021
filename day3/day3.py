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
        
if __name__ == "__main__":

    run()