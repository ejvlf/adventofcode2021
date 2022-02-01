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

def test_char_exists(char : str, pos : int, word_dictionary) -> bool:

    for v in word_dictionary:

        if v[pos - 1] == char:

            return True

    return False

def count_occurrence (case : str, word_dictionary : list, l : int) -> int:

    counter = 1
    current_index = counter - 1
    occurrence = 0
    eval_result = []
    
    while counter <= l:        

        if case[current_index] == "(":
            
            token_result = []
            closing_parentheses_index = case.find(")", current_index)

            for char in case[current_index+1:closing_parentheses_index]:

                token_result.append(1 if test_char_exists(char, counter, word_dictionary) else 0)
            
            current_index = closing_parentheses_index + 1
            eval_result.append(sum(token_result))

        else :

            eval_result.append(1 if test_char_exists(case[current_index], counter, word_dictionary) else 0)
            current_index += 1


        counter += 1

        if min(eval_result) == 0:

            occurrence = 0

        elif min(eval_result) == 1:

            occurrence = 1

        else:

            occurrence = max(eval_result)
            

    return occurrence


def run():

    for file in INPUT_FILENAMES:

        raw_data = open_and_parse_input(file)
        d = int(raw_data[0].split(" ")[1])
        l = int(raw_data[0].split(" ")[0])
        n = int(raw_data[0].split(" ")[2]) 

            
        word_dictionary =  [tuple(raw_data[i]) for i in range(1,d + 1)]
        test_cases = [raw_data[i] for i in range(d + 1, len(raw_data))]
        case_output = []

        for idx, case in enumerate(test_cases):

            number_of_occurrence = count_occurrence(case, word_dictionary, l)

            case_output.append(f"Case #{idx +1}: {number_of_occurrence}")
            print(idx + 1)

        write_output_file(file, case_output)



if __name__ == "__main__":

    run()