from pathlib import Path

DATA_DIR_NAME : str = "data"
COMMON_DIR_NAME : str = "common"

class TextParser :

    def __init__(self, filename : str):
        
        root = Path.cwd()

        self.filepath = Path.joinpath(root, COMMON_DIR_NAME, DATA_DIR_NAME, filename)

    
    def load_file_as_list (self) -> list:

        def try_parse (int_str : str):

            try:

                str_as_int = int(int_str)

                return str_as_int

            except ValueError:

                return int_str

        file_to_return = []

        print(f"Opening file as a list in {self.filepath}")

        if self.filepath.exists:

            with self.filepath.open("r") as f:

                file_to_return = [try_parse(l.rstrip()) for l in f]

        else :

            print(f"No file to load with name {self.filepath.name}")

        return file_to_return


        