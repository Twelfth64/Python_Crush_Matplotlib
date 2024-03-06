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
            x_step = self.get_step()
            y_step = self.get_step()

            # Rejection of unnecessary steps
            if x_step == 0 and y_step == 0:
                continue

            # Update the current position.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

    def get_step(self):
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
        step = direction * distance

        return step
