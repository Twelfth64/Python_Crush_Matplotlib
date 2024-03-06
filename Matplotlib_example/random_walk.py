from random import choice


class RandomWalk:
    """Class to generate random walks."""

    def __init__(self, num_points=5000):
        """Initialize a random walk attributes."""
        self.num_points = num_points

        # All walks start from point (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Generate all point of walk."""

        # Generate steps untill specified lenght(num_points).
        while len(self.x_values) < self.num_points:

            # Specify the direction and lenght of the step.
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # Rejection of unnecessary steps
            if x_step == 0 and y_step == 0:
                continue

            # Update the current position.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)