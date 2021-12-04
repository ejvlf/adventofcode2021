import sys
sys.path.append("/home/ejvlf/personal/adventofcode2021")
print(sys.path)

from common.text_manipulations import TextParser

class Submarine:

    """Coords are a tuple (front - reverse, up - down)"""
    def __init__(self, starting_coords : tuple):

        self.starting_coords = starting_coords

        self.current_displacement = starting_coords[0]
        self.current_depth = starting_coords[1]
        self.travel_history = [starting_coords]
        self.current_position = starting_coords
        self.current_aim = 0
        self.part2 = False

    def navigate (self, command_list = [], part=""):

        print(f"Starting navigation from {self.current_position}")

        # set navigation rules for part 2
        if part != "":

            self.part2 = True
            self.current_displacement = 0
            self.current_depth = 0
            self.travel_history = [(0,0)]
            self.current_position = (0,0)
 

        for command in command_list:

            parsed = self.__command_parser(command)

            # In case we can't parse it
            if parsed is None:
                print("Unable to parse instruction")
                continue

            self.__rudder(parsed)

            print(f"Traveled to {self.current_position}")

    def __rudder (self, coordinate_to_parse : tuple):

        self.current_depth = self.current_depth + coordinate_to_parse[1]
        self.current_displacement = self.current_displacement + coordinate_to_parse[0]
        self.current_position = (self.current_displacement, self.current_depth)
        self.travel_history.append(self.current_position)

    def __command_parser (self, command : str) -> tuple:

        instructions = command.split(" ")
        
        if instructions[0] == "forward":

            depth = 0
            displacement = int(instructions[1])

            if self.part2:

                depth = self.current_aim * displacement

            return (displacement, depth)

        elif instructions[0] == "up":

            if self.part2:

                self.current_aim -= int(instructions[1])

                return (0,0)

            return (0, int(instructions[1]))

        elif instructions[0] == "down":

            if self.part2:

                self.current_aim += int(instructions[1])

                return (0,0)            

            return (0, int(instructions[1]) * -1)

        return


def run():

    #source file loading
    source_list = TextParser("day2.txt").load_file_as_list()

    # create the submarine
    sub = Submarine((0,0))

    # travel
    sub.navigate(source_list)

    #Part 1
    print(sub.current_displacement * abs(sub.current_depth))

    #Part 2
    sub.navigate(source_list, "part2")
    print(sub.current_displacement * abs(sub.current_depth))





if __name__ == "__main__":

    run()