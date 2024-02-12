def countPoint(buffer, sequences):
    # Menghitung jumlah point dari suatu array of token (buffer) berdasarkan sequences input.
    point = 0
    for sequence in sequences:
        for i in range(len(buffer)):
            j = i
            match = True
            for token in sequence[0]:
                if (j >= len(buffer)):
                    match = False
                    break
                if (token != buffer[j]):
                    match = False
                    break
                j += 1
            if (match):
                point += sequence[1]
                break
    return point