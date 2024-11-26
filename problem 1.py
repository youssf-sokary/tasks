
steps_input = input("Enter the number of steps taken each day, separated by spaces: ")

steps = list(map(int, steps_input.split()))


highest_steps = max(steps)


lowest_steps = min(steps)

average_steps = sum(steps) / len(steps)

sorted_steps = sorted(steps, reverse=True)


print("Highest steps:", highest_steps)
print("Lowest steps:", lowest_steps)
print("Average steps:", average_steps)
print("Steps in descending order:", sorted_steps)
