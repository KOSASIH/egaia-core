import numpy as np
from biotechnology.reforestation import ReforestationAlgorithm

# Example usage of the reforestation algorithm
def reforestation_example():
    # Define the area to be reforested
    area = np.array([
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 1, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ])

    # Create an instance of the reforestation algorithm
    algorithm = ReforestationAlgorithm(area)

    # Run the algorithm to generate a reforestation plan
    plan = algorithm.run()

    # Print the reforestation plan
    print("Reforestation Plan:")
    for row in plan:
        print(row)

if __name__ == "__main__":
    reforestation_example()
