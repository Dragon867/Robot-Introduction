# Define the Robot class using Object-Oriented Programming
class Robot:
    def __init__(self, name, model, year):
        # Initialize the robot with name, model, and year of creation
        self.name = name
        self.model = model
        self.year = year

    def introduce(self):
        # Method to introduce the robot
        print(f"Hello! I am {self.name}, a {self.model} model.")
        print(f"I was created in the year {self.year}.")

    def perform_task(self, task):
        # Method to perform a task
        print(f"{self.name} is now performing the task: {task}")

# Create a Robot object
my_robot = Robot(name="RoboX", model="RX-1000", year=2024)

# Introduce the robot
my_robot.introduce()

# Perform some tasks
my_robot.perform_task("cleaning the room")
my_robot.perform_task("assisting in the kitchen")
