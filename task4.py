import random

# Get user input for number of sides and rolls
sides = int(input("Enter the number of sides on the dice: "))
rolls = int(input("Enter the number of times to roll the dice: "))

# Function to simulate dice rolls
def roll_dice(sides, rolls):
    results = []
    for _ in range(rolls):
        result = random.randint(1, sides)
        results.append(result)
    return results

# Roll the dice and show the results
results = roll_dice(sides, rolls)
print(f"\nResults of {rolls} rolls with a {sides}-sided dice: {results}")
