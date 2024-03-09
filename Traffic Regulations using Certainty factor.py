class CertaintyFactor:
    def __init__(self, belief, disbelief, uncertainty):
        self.belief = belief
        self.disbelief = disbelief
        self.uncertainty = uncertainty

    def calculate_cf(self):
        if self.uncertainty == 0:
            return self.belief - self.disbelief
        else:
            return (self.belief - self.disbelief) * (1 - abs(self.uncertainty))

# Input from the user
traffic_density = float(input("Enter the traffic density (normalized between 0 and 1): "))
road_condition = float(input("Enter the road condition (normalized between 0 and 1): "))
belief = float(input("Enter the degree of belief (0 to 1): "))
disbelief = float(input("Enter the degree of disbelief (0 to 1): "))
uncertainty = float(input("Enter the degree of uncertainty (0 to 1): "))

# Check if the input values are within the valid range
if 0 <= traffic_density <= 1 and 0 <= road_condition <= 1 and 0 <= belief <= 1 and 0 <= disbelief <= 1 and 0 <= uncertainty <= 1:
    cf = CertaintyFactor(belief, disbelief, uncertainty)
    certainty_factor = cf.calculate_cf()

    # Define the fuzzy_membership function
    def fuzzy_membership(value, low, high):
        if value <= low:
            return 0.0
        elif value >= high:
            return 1.0
        else:
            return (value - low) / (high - low)

    # Define fuzzy linguistic variables and rules for traffic management
    heavy_traffic = min(fuzzy_membership(traffic_density, 0.7, 1), fuzzy_membership(road_condition, 0.3, 0.6))
    moderate_traffic = min(fuzzy_membership(traffic_density, 0.4, 0.7), fuzzy_membership(road_condition, 0.2, 0.4))
    light_traffic = min(fuzzy_membership(traffic_density, 0, 0.4), fuzzy_membership(road_condition, 0, 0.2))

    # Aggregation of fuzzy rules (e.g., using "max" operator)
    aggregated_traffic = max(heavy_traffic, moderate_traffic, light_traffic)

    # Defuzzification using the certainty factor
    defuzzified_traffic = certainty_factor * aggregated_traffic

    print("Certainty Factor:", certainty_factor)
    print("Fuzzy Output (Traffic Level - Before Defuzzification):", defuzzified_traffic)

else:
    print("Invalid input values. Please enter values within the valid range.")
