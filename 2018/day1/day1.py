import time

start_time = time.time()

with open("input") as f:
    freq_input = f.readlines()

# === Part One ===

freq_input = [int(x.strip()) for x in freq_input]
print("Result frequency:", sum(freq_input))


# === Part Two ===

repeated_freq = {0: 1}

current_freq = 0
found = False

while True:
    for freq in freq_input:
        current_freq += freq
        if current_freq in repeated_freq:
            found = True
            break
        else:
            repeated_freq[current_freq] = 1
    if found:
        break

print("First repeating frequency:", current_freq)

print("Time elapsed: ", time.time() - start_time)