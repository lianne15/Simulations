import random

# Initialize six counters to store the frequencies for each face of the dice
face1_count = 0
face2_count = 0
face3_count = 0
face4_count = 0
face5_count = 0
face6_count = 0

# Roll the dice 1000 times and update the counters for each face
for i in range(1000):
    # Generate a random number between 0 and 1
    random_number = random.random()
    # Assign the face of the dice based on the range of the random number
    if random_number < 1/6:
        face1_count += 1
    elif random_number < 2/6:
        face2_count += 1
    elif random_number < 3/6:
        face3_count += 1
    elif random_number < 4/6:
        face4_count += 1
    elif random_number < 5/6:
        face5_count += 1
    else:
        face6_count += 1

# Compute the percentages for each face
face1_percentage = face1_count / 10
face2_percentage = face2_count / 10
face3_percentage = face3_count / 10
face4_percentage = face4_count / 10
face5_percentage = face5_count / 10
face6_percentage = face6_count / 10

# Print the table of frequencies and percentages
print("| Face | Count | Percentage |")
print("|------|-------|------------|")
print(f"| 1    | {face1_count}     | {face1_percentage:.1f}%      |")
print(f"| 2    | {face2_count}     | {face2_percentage:.1f}%      |")
print(f"| 3    | {face3_count}     | {face3_percentage:.1f}%      |")
print(f"| 4    | {face4_count}     | {face4_percentage:.1f}%      |")
print(f"| 5    | {face5_count}     | {face5_percentage:.1f}%      |")
print(f"| 6    | {face6_count}     | {face6_percentage:.1f}%      |")
