from pathlib import Path

DATA_DIR_NAME : str = "data"
COMMON_DIR_NAME : str = "common"

class TextParser :

    def __init__(self, filename : str, parse_to_ints = True):
        
        root = Path.cwd()

        self.parse_to_ints = parse_to_ints

        self.filepath = Path.joinpath(root, COMMON_DIR_NAME, DATA_DIR_NAME, filename)

    def __try_parse (self, int_str : str):

            try:

                str_as_int = int(int_str)

                return str_as_int

            except ValueError:

                return int_str  
    
    def load_file_as_list (self) -> list:

        file_to_return = []

        print(f"Opening file as a list in {self.filepath}")

        if self.filepath.exists:

            with self.filepath.open("r") as f:

                if self.parse_to_ints:

                    file_to_return = [self.__try_parse(l.rstrip()) for l in f]

                else:

                    file_to_return = [l.rstrip() for l in f]


        else :

            print(f"No file to load with name {self.filepath.name}")

        return file_to_return
          

    def load_file_as_ints (self, splitchar: str = ",") -> list:

        file_to_return = []

        print(f"Opening file as a list of ints {self.filepath}")

        if self.filepath.exists:

            with self.filepath.open("r") as f:

                if self.parse_to_ints:

                    file_to_return = list(map( lambda x : self.__try_parse(x), f.read().split(splitchar)))

                else:

                    file_to_return = f.read().split(splitchar)


        else :

            print(f"No file to load with name {self.filepath.name}")

        return file_to_return



        