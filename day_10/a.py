def get_adapters():
    adapters = [0]
    with open('input.txt', 'r') as file:
        for line in file.readlines():
            line = line.strip("\n")
            adapters.append(int(line))
    adapters.sort()
    adapters.append(adapters[-1] + 3)
    return adapters


def classify_adapters(adapters):
    values = [0, 0, 0]
    for n in range(1, len(adapters)):
        values[adapters[n-1] - adapters[n]] += 1
    return values


adapters = get_adapters()
classification = classify_adapters(adapters)
print(classification)
print(classification[0] * classification[2])

