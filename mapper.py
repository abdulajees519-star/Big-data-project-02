def mapper(lines):
    output = []

    for line in lines:
        languages = line.strip().split()

        for language in languages:
            output.append((language, 1))

    return output
