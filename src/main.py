import time
from random import randint
from configReader import readConfig
from pointCounter import countPoint
from bruteForce import brute_force

def main():
    # INPUT
    print('Selamat datang!')
    print('Pilih metode Input!')
    print('1. File ".txt"')
    print('2. Otomatis\n')
    pilihan = input('Pilihan : ')
    print()
    while (pilihan != '1' and pilihan != '2'):
        print("Masukkan tidak tepat! Coba lagi.")
        pilihan = input("pilihan : ")
    
    if (pilihan == '1'): # Baca file txt
        print('Pastikan file berada di folder "test"!')
        path = '../test/' + input('Nama file ".txt" : ')
        config = readConfig(path)
        ukuran_buffer = config['buffer_size']
        matrix_width = config['matrix_width']
        matrix_height = config['matrix_height']
        jumlah_sekuens = config['number_of_sequences']
        sequences = config['sequences']
        matrix = config['matrix']


    else: # Otomatis
        jumlah_token_unik = input('Jumlah Token Unik : ')
        while not jumlah_token_unik.isdigit():
            print("Input tidak valid!")
            jumlah_token_unik = input('Jumlah Token Unik: ')
        jumlah_token_unik = int(jumlah_token_unik)

        token_unik = input('Token : ').split()
        # Cek Token Validity
        token_valid = True
        for token in token_unik:
            if len(token) != 2 or not token.isalnum():
                token_valid = False
                break
        token_set = set(token_unik)
        while not token_valid or len(token_unik) != jumlah_token_unik or len(token_unik) != len(token_set):
            print('Token tidak valid, tidak unik, atau tidak sesuai jumlah!')
            token_unik = input('Token : ').split()
            token_valid = True
            for token in token_unik:
                if len(token) != 2 or not token.isalnum():
                    token_valid = False
                    break
            token_set = set(token_unik)

        ukuran_buffer = input('Ukuran Buffer : ')
        while not ukuran_buffer.isdigit():
            print("Input tidak valid!")
            ukuran_buffer = input('Ukuran Buffer : ')
        ukuran_buffer = int(ukuran_buffer)

        matrix_size = input('Matrix Size : ').split()
        while len(matrix_size) != 2 or not (matrix_size[0].isdigit() and matrix_size[1].isdigit()):
            print('Input tidak valid!')
            matrix_size = input('Matrix Size : ').split()
        matrix_width = int(matrix_size[0])
        matrix_height = int(matrix_size[1])

        jumlah_sekuens = input('Jumlah Sekuens : ')
        while not jumlah_sekuens.isdigit():
            print("Input tidak valid!")
            jumlah_sekuens = input('Jumlah Sekuens : ')
        jumlah_sekuens = int(jumlah_sekuens)

        ukuran_maksimal_sekuens = input('Ukuran Maksimal Sekuens : ')
        while not ukuran_maksimal_sekuens.isdigit():
            print("Input tidak valid!")
            ukuran_maksimal_sekuens = input('Ukuran Maksimal Sekuens : ')
        ukuran_maksimal_sekuens = int(ukuran_maksimal_sekuens)

        print()

        # Create Random Matrix
        matrix = []
        for i in range(matrix_height):
            line = []
            for j in range(matrix_width):
                line.append(token_unik[randint(0, jumlah_token_unik-1)])
            matrix.append(line)

        # Create Random Sequence
        sequences = []
        for i in range(jumlah_sekuens):
            valid = False
            while not valid:
                sekuens = []
                for j in range(randint(1, ukuran_maksimal_sekuens)):
                    sekuens.append(token_unik[randint(0, jumlah_token_unik-1)])
                valid = True # Cek apakah sequence yang digenerate unik
                for sequence in sequences:
                    if (sequence[0] == sekuens):
                        valid = False
                        break
            sequences.append((sekuens, randint(-50, 50)))

    print()   
    
    # Print Matrix
    print("MATRIX")
    for baris in matrix:
        for token in baris:
            print(token, end=' ')
        print()
    print()
    
    # Print Sequence
    print("SEQUENCES")
    for sequence in sequences:
        print("Sequence : ", end='')
        for token in sequence[0]:
            print(token, end=' ')
        print()
        print("Reward : ", sequence[1])
        print()
    print()


    # PROCESS
    start_time = time.time()
    buffer = ([],[]) # (list of tokens, list of coordinates)
    optimal_buffer = ([], [], 0)

    for i in range(matrix_width):
        buffer[0].append(matrix[0][i])
        buffer[1].append((0, i))
        point = countPoint(buffer[0], sequences)
        if point > optimal_buffer[2]:
            optimal_buffer = (buffer[0].copy(), buffer[1].copy(), point)
        optimal_buffer = brute_force(matrix, buffer, optimal_buffer, sequences, ukuran_buffer)
        buffer[0].pop()
        buffer[1].pop()
    
    # output
    output = ""
    output += str(optimal_buffer[2]) + "\n"
    for token in optimal_buffer[0]:
        output += token + " "
    output += "\n"
    for coordinate in optimal_buffer[1]:
        output += str(coordinate[1]+1)+ ',' + str(coordinate[0]+1) + "\n"
    output += "\n"

    run_time = round((time.time() - start_time) * 1000)
    output += str(run_time) + " ms"

    print(output)

    pilihan = input("Apakah ingin menyimpan solusi? (y/n) ")
    print()
    while pilihan != 'y' and pilihan != 'n':
        print('Pilihan tidak valid! Ulangi masukan!')
        pilihan = input("Apakah ingin menyimpan solusi? (y/n) ")
        print()
    
    if pilihan == 'y':
        nama_output = input("Nama file output : ")
        f = open("../test/" + nama_output, "w")
        f.write(output)
        f.close()
        print('Output berhasil disimpan di "../test/{}".'.format(nama_output))

if __name__ == "__main__":
    main()