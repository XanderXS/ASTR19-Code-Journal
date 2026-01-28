class FavoriteAnimal:
    def __init__(self, arm_length, leg_length, num_eyes, has_tail, is_furry):
        # Data members (physical characteristics)
        self.arm_length = arm_length      # float
        self.leg_length = leg_length      # float
        self.num_eyes = num_eyes          # int
        self.has_tail = has_tail          # bool
        self.is_furry = is_furry          # bool

    def describe(self):
        print("Animal Physical Characteristics:")
        print(f"Arm length: {self.arm_length}")
        print(f"Leg length: {self.leg_length}")
        print(f"Number of eyes: {self.num_eyes}")
        print(f"Has a tail? {'Yes' if self.has_tail else 'No'}")
        print(f"Is furry? {'Yes' if self.is_furry else 'No'}")



my_animal = FavoriteAnimal(0.5, 0.7, 2, True, True)

my_animal.describe()
