import re

INPUT_FILENAMES = ["test.in.txt","Message from Space-small.in.txt", "Message from Space-large.in.txt"]
TEST_CASE_START = 1
GAME_TOKEN = "a63c6131-2ffc-48b2-b454-d3a264a31b57"

def parse_multiple_possibilities(test_case : str, l: int): 

    regex = re.compile(r'\((.*?)\)')

    inside_parentheses = [(m.start(0), m.end(0), m.end(0) - m.start(0)) for m in regex.finditer(test_case)]
    matches = regex.findall(test_case)
    values_to_return = {}

    if len(matches) == l:

        values_to_return = {k:(matches[k - 1], 0, False) for k in range(1, l+1)}

    else :

        current_index = 0
        values_to_return = {k:() for k in range(1, l+1)}

        for key in values_to_return.keys():

            if test_case[current_index] == "(":
                
                wildcard = tuple(filter(lambda x : x[0] == current_index, inside_parentheses))

                values_to_return[key] = (test_case[wildcard[0][0]+1:wildcard[0][1]-1], 0, False)

                current_index += wildcard[0][2]

            elif test_case[current_index] != ")":
                
                values_to_return[key] = (test_case[current_index], 0, True)
                
                current_index += 1

    return values_to_return

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

def split_token(token : str) -> dict:

    token_to_return = {}

    token_to_return["number_of_D_lines"] = token.split(" ")[1]
    token_to_return["length_of_D_lines"] = token.split(" ")[0]
    token_to_return["test_cases"] = token.split(" ")[2] 

def test_number_of_ocurrences (token : str, language_dictionary : list) -> int:

    result = filter(lambda x: x == token, language_dictionary)

    return len(list(result))

def word_test (current_test_case, language_dictionary, l: int):
    
    occurrence = 0
    
    while True: 

        str_to_test = []
        test_list = []

        for k,v in current_test_case.items():

            str_to_test.append(v[0][v[1]])
            test_list.append(v[2])

        if all(test_list) == True:

            break

        occurrence += test_number_of_ocurrences("".join(str_to_test), language_dictionary)

        counter = 1

        while counter <= l:

            if current_test_case[counter][1] >= len(current_test_case[counter][0]) - 1:

                current_test_case[counter] = (current_test_case[counter][0], 0, True)

            elif current_test_case[counter][1] < len(current_test_case[counter][0]) - 1:

                current_test_case[counter] = (current_test_case[counter][0], current_test_case[counter][1] + 1, current_test_case[counter][2])

                break
                
            counter += 1

    return occurrence

def run():

    for file in INPUT_FILENAMES:

        raw_data = open_and_parse_input(file)
        d = int(raw_data[0].split(" ")[1])
        l = int(raw_data[0].split(" ")[0])
        n = int(raw_data[0].split(" ")[2]) 


        language_dictionary = [raw_data[i] for i in range(1,d + 1)]
        test_cases = [raw_data[i] for i in range(d + 1, len(raw_data))]
        case_output = []

        for idx, case in enumerate(test_cases):

            case_counter = 0
        
            if case.find("(") == -1:

                case_counter += test_number_of_ocurrences(case, language_dictionary)
            
            elif case.find("(") > -1:

                word_is_ready = False            
                v1 = parse_multiple_possibilities(case, l)

                while word_is_ready == False:

                    occ = word_test(v1, language_dictionary, l)

                    case_counter += occ

                    word_is_ready = True


            case_output.append(f"Case #{idx +1}: {case_counter}")
            print(idx + 1)

        write_output_file(file, case_output)



if __name__ == "__main__":

    run()