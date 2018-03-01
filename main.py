
INPUT_A ='./stuff/a_example.in'
INPUT_B ='./stuff/b_should_be_easy.in'
INPUT_C ='./stuff/c_no_hurry.in'
INPUT_D ='./stuff/d_metropolis.in'
INPUT_E ='./stuff/e_high_bonus.in'

class Simulation():

    def __init__(self, filepath):
        with open(filepath, 'r') as f:
            first_line = f.readline()
        data = first_line.split()
        self.num_rows = data[0]
        self.num_cols = data[1]
        self.fleet_size = data[2]
        self.num_rides = data[3]
        self.ride_bonus = data[4]
        self.steps = data[5]

class RideData():

    def __init__(self, filepath):
        instructions = []
        with open(filepath, 'r') as f:
            next(f)
            for line in f:
                data = line.split()
                data  = [int(i) for i in data]
                instructions.append(data)
                #print(data)
        self.rides = instructions

class Riders():

    def __init__(self, value_list):
        self.start_coords = value_list[0:2]
        self.end_coords = value_list[2:4]
        self.start_time = value_list[4]
        self.finish_time = value_list[5]

    def is_possible(self):
        window = self.finish_time - self.start_time
        return window >= self.calculate_distance()

    def calculate_distance(self):
        distance = (abs(self.start_coords[0] - self.end_coords[0]), abs(self.start_coords[1] - self.end_coords[1]))
        steps = abs(distance[0] + distance[1])
        return steps

    def calculate_earliest_completion(self):
        return self.start_time + self.calculate_distance()

    def calculate_latest_start_time(self):
        return self.finish_time - self.calculate_distance()

class Drivers():

    def __init__(self):
        self.coords = (0, 0)
        self.internal_steps = 0

    def get_position(self):
        return self.coords

    def get_steps(self):
        return self.internal_steps

    def add_step(self):
        self.internal_steps += 1

    def calculate_dist_from_ride(self, rider):
        distance = (abs(self.coords[0] - rider.start_coords[0]), abs(self.coords[1] - rider.start_coords[1]))
        steps = abs(distance[0] + distance[1])
        return steps

    def can_make_in_time(self, rider):
        distance = self.calculate_dist_from_ride(rider) + self.internal_steps
        latest_start = rider.calculate_latest_start_time
        return (latest_start - distance) >= 0

    def can_make_start_time(self, rider):
        distance = self.calculate_dist_from_ride(rider) + self.internal_steps
        start = rider.start_time
        return (start - distance) >= 0


sim_a = Simulation(INPUT_A)
sim_b = Simulation(INPUT_B)
sim_c = Simulation(INPUT_C)
sim_d = Simulation(INPUT_D)
sim_e = Simulation(INPUT_E)

rides_a = map(Riders,RideData(INPUT_A).rides)
rides_b = map(Riders,RideData(INPUT_B).rides)
rides_c = map(Riders,RideData(INPUT_C).rides)
rides_d = map(Riders,RideData(INPUT_D).rides)
rides_e = map(Riders,RideData(INPUT_E).rides)

# make sure no rides are impossible.
filter(lambda x: x.is_possible(), rides_a)
filter(lambda x: x.is_possible(), rides_b)
filter(lambda x: x.is_possible(), rides_c)
filter(lambda x: x.is_possible(), rides_d)
filter(lambda x: x.is_possible(), rides_e)





















