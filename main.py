from mapper import mapper
from partitioner import partition
from reducer import reducer

# Read input file
with open("input.txt", "r") as file:
    lines = file.readlines()

# Split into two parts
middle = len(lines) // 2

part1 = lines[:middle]
part2 = lines[middle:]

# Mapping
mapped_data = mapper(part1) + mapper(part2)

# Partitioning
partitions = partition(mapped_data)

print("----- Partition Output -----")

for partition_no, values in partitions.items():
    print(f"\nPartition {partition_no}")

    for value in values:
        print(value)

# Reducing
print("\n----- Final Output -----")

for partition_no, values in partitions.items():

    result = reducer(values)

    for key in sorted(result):
        print(key, result[key])
