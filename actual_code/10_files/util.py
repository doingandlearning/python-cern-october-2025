def get_batch_size(file, start=0, batch_size=2):
    """
    Get a batch of lines from a file.
    :param file: File handle to open
    :param start: Which batch size to start with
    :param batch_size: How big a batch to read
    :return: A list of lines
    """
    file.seek(0)
    for _ in range(start * batch_size):
        if not file.readline():
            return []  # handles getting to the end of file

    output = []
    for _ in range(batch_size):
        line = file.readline()
        if line is not None:
            output.append(line)

    return output