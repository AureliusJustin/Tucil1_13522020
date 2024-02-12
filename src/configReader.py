import os

def readConfig(path):
    # Membaca file .txt menjadi config program.
    if(os.path.isfile(path)):
        try:
            with open(path) as file:
                lines = []
                for line in file:
                    lines.append(line.rstrip())
        except IOError as e:
            print("File tidak berhasil dibuka!")
            exit()
    else:
        print(path, "Tidak ditemukan! Cek nama file")
        exit()

    # input 
    matrix_width = int(lines[1].split()[0])
    matrix_height = int(lines[1].split()[1])
    matrix = []
    for i in range(2, 2+matrix_height):
        matrix.append(lines[i].split())
    
    # input sequence
    number_of_sequences = int(lines[2+matrix_height])
    sequences = []
    for i in range(3+matrix_height, 3 + matrix_height + 2*number_of_sequences, 2):
        sequences.append(((lines[i].split()), int(lines[i+1])))
    
    config = {
        'buffer_size' : int(lines[0]),
        'matrix_width' : matrix_width,
        'matrix_height' : matrix_height,
        'number_of_sequences' : number_of_sequences,
        'sequences' : sequences,
        'matrix' : matrix
    } 
    return config
