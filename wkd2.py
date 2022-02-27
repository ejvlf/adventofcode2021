INPUT_FILENAMES = ["test2.in.txt","Welcome to NTTData-small.in.txt", "Welcome to NTTData-large.in.txt"]
KEY_TO_FIND = "welcome to everis"
GAME_TOKEN = "7aa7948f-19ce-449e-8a28-ccaecedf7531"

def open_and_parse_input(filename : str) -> list:

    trimmed_data = []

    with open(filename) as f:

        input_data = f.readlines()

        trimmed_data = map(lambda x: x.rstrip(), input_data)

    return list(trimmed_data)

def write_output_file(filename : str, results : list):

    output_filename = filename.replace("in", "out")

    with open(output_filename, "w") as f:

        f.write(GAME_TOKEN)
        f.write("\n")
        list_with_n = map(lambda x : x+"\n", results)
        f.writelines(list_with_n)

def count_frequency(case):
    M = len(KEY_TO_FIND)
    N = len(case)
    res = 0
    idx_valid = []
    mapping = False

    counts = {}
    for i in range(0, M):

        str_to_look = KEY_TO_FIND[0:i+1]

        counts[str_to_look] = case.count(str_to_look)

        




    return res

def run():

    for file in INPUT_FILENAMES:

        raw_data = open_and_parse_input(file)
        n = int(raw_data[0])
        test_cases = [i for i in raw_data[1:]]

        case_output = []

        for idx, case in enumerate(test_cases):

            test = count_frequency(case)

            case_output.append(f"Case #{idx +1}: {test}")
            print(idx + 1)

        write_output_file(file, case_output)



if __name__ == "__main__":

    run()