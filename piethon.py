while True:
    lines = []
    with open(f"file.txt") as fh:
        for line in fh:
            if line:
                lines.append(line)

