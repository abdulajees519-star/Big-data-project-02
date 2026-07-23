from collections import defaultdict

def partition(mapped_data):

    partitions = defaultdict(list)

    for key, value in mapped_data:

        partition_no = hash(key) % 2

        partitions[partition_no].append((key, value))

    return partitions
