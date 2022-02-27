INPUT_FILENAMES = ["test3.in.txt","Fastest Crossing-small.in.txt", "Fastest Crossing-large.in.txt"]
KEY_TO_FIND = "welcome to everis"
GAME_TOKEN = "6cd97082-383a-49bb-b5d6-397d6afef0e1"

def open_and_parse_input(filename : str) -> list[str]:

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

def calculate_x_or_y (signal_data : str) -> bool:

    data = signal_data.split(" ")
    x_signal = int(data[0])
    y_signal = int(data[1])
    t = int(data[2])
    return True
    

def run():

    for file in INPUT_FILENAMES:

        raw_data = open_and_parse_input(file)

        c = int(raw_data[0])
        current_row = 1
        current_test_case = 1

        while current_test_case <= c:

            line = raw_data[current_row].split(" ")
            n = int(line[0])
            m = int(line[1])

            starting_coord = (0,m)
            ending_coord = (n,0)

            current_row += n

            calculate_x_or_y(line)





if __name__ == "__main__":

    run()