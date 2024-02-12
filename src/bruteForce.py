from pointCounter import countPoint

def brute_force(matrix, buffer, optimal_buffer, sequences, ukuran_buffer):
    # Algoritma bruteForce
    coordinate = buffer[1][-1]
    if (len(buffer[0]) % 2 == 0) :
        for i in range(len(matrix[0])):
            if (not (coordinate[0], i) in buffer[1]):
                buffer[0].append(matrix[coordinate[0]][i])
                buffer[1].append((coordinate[0], i))
                point = countPoint(buffer[0], sequences)
                if(point > optimal_buffer[2] or (point == optimal_buffer[2] and len(buffer[0]) < len(optimal_buffer[0]))):
                    optimal_buffer = (buffer[0].copy(), buffer[1].copy(), point)
                if (len(buffer[0]) < ukuran_buffer):
                    optimal_buffer = brute_force(matrix, buffer, optimal_buffer, sequences, ukuran_buffer)
                
                buffer[0].pop()
                buffer[1].pop()
    else:
        for i in range(len(matrix)):
            if (not (i, coordinate[1]) in buffer[1]):
                buffer[0].append(matrix[i][coordinate[1]])
                buffer[1].append((i, coordinate[1]))
                point = countPoint(buffer[0], sequences)
                if(point > optimal_buffer[2] or (point == optimal_buffer[2] and len(buffer[0]) < len(optimal_buffer[0]))):
                    optimal_buffer = (buffer[0].copy(), buffer[1].copy(), point)
                if (len(buffer[0]) < ukuran_buffer):
                    optimal_buffer = brute_force(matrix, buffer, optimal_buffer, sequences, ukuran_buffer)
                
                buffer[0].pop()
                buffer[1].pop()

    return optimal_buffer