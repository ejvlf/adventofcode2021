from common.text_manipulations import TextParser

class Probe:

    def __init__(self):

        self.__drag_impact = 1
        self.__gravity_impact = 1
        self.current_position_x = 0
        self.current_position_y = 0
        self.step_limit = 50
        self.successful_initial_speeds = []
        self.heights = {}

    def set_ideal_area(self, description : str):
        
        c = description[description.find("target area:") + len("target area:"):].split(",")
        prize_area = [tuple(i[3:].split("..")) for i in c]
        for i,p in enumerate(prize_area):

            prize_area[i] = (int(p[0]), int(p[1]))

        self.__prize_area = prize_area

    def __test_victory_condition(self) -> bool:

        if (self.current_position_x >= self.__prize_area[0][0] and self.current_position_x <= self.__prize_area[0][1]) \
            and (self.current_position_y >= self.__prize_area[1][0] and self.current_position_y <= self.__prize_area[1][1]):

            print("Success!")

            return True

        return False

    def fire_probe(self, initial_velocity : tuple) -> bool:
        
        victory = False
        step = 0
        self.__initial_velocity = initial_velocity

        self.current_velocity_x = initial_velocity[0]
        self.current_velocity_y = initial_velocity[1]
        heights = []

        while step <= self.step_limit:

            step += 1

            print(f"Starting step {step}")
            
            heights.append(self.current_position_y)
            self.current_position_x = self.current_position_x + self.current_velocity_x
            self.current_position_y = self.current_position_y + self.current_velocity_y

            print(f"Current position {(self.current_position_x, self.current_position_y)}")

            self.current_velocity_x = self.current_velocity_x - self.__drag_impact if self.current_velocity_x - self.__drag_impact >= 0 else 0
            self.current_velocity_y = self.current_velocity_y - self.__gravity_impact            

            if self.__test_victory_condition():
                self.successful_initial_speeds.append(self.__initial_velocity)
                victory = True
                self.heights[self.__initial_velocity] = heights

                break
                
        
        return victory, step
    def calculate_part1_score (self):

        pass



def run():

    source = TextParser("day17_test.txt").load_file_as_raw_string()

    # Part 1
    p = Probe()
    p.set_ideal_area(source)

    keep_testing = True
    start_speed = (0,0)

    while keep_testing:
        success, step = p.fire_probe(start_speed)

        if success == True and len(p.successful_initial_speeds) > 0:
            
            start_speed = (start_speed[0], start_speed[1]+1)

        elif success == False and len(p.successful_initial_speeds) == 0:

            y_speed_to_add = start_speed[1] + 1
            x_speed_to_add = 1 if y_speed_to_add % 2 == 0 else 0
            

            start_speed = (start_speed[0] + x_speed_to_add, y_speed_to_add)
        else :

            keep_testing = False

def parse_data(data):
    #target area: x=241..273, y=-97..-63
    coords = { "x": [], "y": []}
    data = data.split()
    for line in (line for line in data if "=" in line):
        for coord in (coord for coord in line.strip(",")[2:].split('..')):
            coords[line[0]].append(int(coord))
    
    return coords

def launch_probe(velocity,target):
    p_x,p_y = [0,0]
    v_x,v_y = velocity
    t_x = sorted(target["x"])
    t_y = sorted(target["y"])
    max_y = p_y
    while (p_x < max(t_x)+1 and not (v_x == 0 and p_x < min(t_x))) and not (p_x > min(t_x) and p_y < min(t_y)):
        p_x += v_x
        p_y += v_y
        if v_x > 0:
            v_x -= 1
        elif v_x < 0:
            v_x += 1
        v_y -= 1
        if p_y > max_y:
            max_y = p_y
        if (p_x in range(min(t_x),max(t_x)+1)) and (p_y in range(min(t_y),max(t_y)+1)):
            
            return True,velocity,max_y
    
    return False,velocity,max_y

def main():
    target = parse_data(TextParser("day17.txt").load_file_as_raw_string())
    max_y = 0
    optimal = []
    count = 0
    for x in range(1,max(target["x"])*2):
        for y in range(min(target["y"]),max(target["x"])):
            r,velocity,this_max_y = launch_probe([x,y],target)
            if r == True:
                count += 1
                if this_max_y > max_y:
                    max_y = this_max_y
                    optimal = velocity
    
    print(optimal)
    print(max_y)
    print(count)
    

if __name__ == "__main__":

    main()