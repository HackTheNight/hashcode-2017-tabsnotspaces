
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
        self.riders = filter(lambda x: x.is_possible(), map(Riders, RideData(filepath).rides))
        self.drivers = [Drivers() for i in range(int(self.fleet_size))]

    def __repr__(self):
        return "###############\nSimulation:" + "\n" \
               + "rows " + self.num_rows + " x cols " + self.num_cols + "\n" \
               + "Fleet Size: " + self.fleet_size + " Number of Riders: " + self.num_rides + "\n" \
               + "Bonus Points " + self.ride_bonus + " Max time " + self.steps + "\n" \
               + "Divers Location:" + "\n" \
               + str(self.drivers) + "\n" \
               + "Riders Location:" + "\n" \
               + str(self.riders) + "\n"

    def print_drivers_locations(self):
        print(self.drivers)

    def print_riders_location(self):
        print(self.riders)

    def max_theoretical_score(self):
        total_journey_points = reduce((lambda a, b: a + b), map(lambda r: r.calculate_distance(), self.riders))
        total_bonus_points = len(self.riders) * int(self.ride_bonus)
        return "Max Dis = " + str(total_journey_points + total_bonus_points)

    def run_simulation(self):
        print self
        for step in self.steps:
            for driver in self.drivers:
                if driver.available:
                    driver.select_ride(self.riders)
                driver.move()


class RideData:

    def __init__(self, filepath):
        instructions = []
        with open(filepath, 'r') as f:
            next(f)
            for line in f:
                data = line.split()
                data = [int(i) for i in data]
                instructions.append(data)
        self.rides = instructions


class Riders:

    def __init__(self, value_list):
        self.start_coords = value_list[0:2]
        self.end_coords = value_list[2:4]
        self.start_time = value_list[4]
        self.finish_time = value_list[5]
        self.state = 'waiting'

    def __repr__(self):
        return " State: " + str(self.state) \
               + " start_coords={0} end_coords={1}".format(self.start_coords, self.end_coords)

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


class Drivers:

    def __init__(self):
        self.available = True
        self.coords = (0, 0)
        self.internal_steps = 0
        self.destination_cood = None

    def __repr__(self):
        return "coords=" + "{0}".format(self.coords ) + " steps=" + str(self.internal_steps)

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

    def select_ride(self, riders):
        print filter(lambda r: r.state == 'waiting', riders).sort(key=lambda r: self.calculate_dist_from_ride(r), reverse=False)[0]


    def move(self):
        if self.destination_cood:
            # move coloum/row
            drows = (self.coords[0] - self.destination_cood[0])
            dcol = (self.coords[1] - self.destination_cood[1])
            if not(drows == 0):
                self.coords[0]
            elif not(dcol == 0):
                self.coords[1]
            else:
                pass
                # can drop / can pick
        self.add_step()


all_sims = [Simulation(INPUT_A), Simulation(INPUT_B), Simulation(INPUT_C), Simulation(INPUT_D), Simulation(INPUT_E)]


# for sim in all_sims:
#     print(sim.max_theoretical_score())
#
# all_sims[0].run_simulation()
# print sim.drivers

