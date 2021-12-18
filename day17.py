from common.text_manipulations import TextParser

class Probe:

    def __init__(self, initial_velocity : tuple):

        self.__start_x_velocity = initial_velocity[0]
        self.__start_y_velocity = initial_velocity[1]
        self,__drag_impact = 1
        self.__gravity_impact = 1

    def set_ideal_area(self, description : str):
        
        c = description[description.find("target area:"):].split(",")
        prize_area = [tuple(i[2:].split(":")) for i in c]

        return prize_area
        


def run():

    source = TextParser("day17.txt").load_file_as_raw_string()

    # Part 1
    print(f"Part 1 result: {sm.vsum}")

    #Part 2
    print(f"Part 2 result: {sm.result}")

if __name__ == "__main__":

    run()