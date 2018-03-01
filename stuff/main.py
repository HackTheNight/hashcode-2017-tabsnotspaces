
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

class Ride():

    def __init__(self, filepath):
        instructions = []
        with open(filepath, 'r') as f:
            next(f)
            for line in f:
                data = line.split()
                instructions.append(data)
                #print(data)
        self.rides = instructions



example_sim = Simulation('./a_example.in')
example_ride = Ride('./a_example.in')
print(example_ride.rides)


