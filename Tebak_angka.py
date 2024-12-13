# Proyek : Game Tebak Angka
# " Fitur : Pemain menebak angka antara 1 dan 100 dengan 
# petunjuk "terlalu besar" atau "terlalu kecil". "

import random

def play_game():
    print("\nSelamat datang di Game Tebak Angka!")
    print("Saya telah memilih sebuah angka antara 1 dan 100.")
    print("Coba tebak angka tersebut!\n")

    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Masukkan tebakan Kamu: "))
            attempts += 1

            if guess < number_to_guess:
                print("Tebakan Kamu terlalu kecil. Coba lagi!\n")
            elif guess > number_to_guess:
                print("Tebakan Kamu terlalu besar. Coba lagi!\n")
            else:
                print(f"Selamat! Kamu berhasil menebak angka {number_to_guess} dalam {attempts} percobaan!\n")
                break
        except ValueError:
            print("Masukkan angka yang valid!\n")

    return attempts

def main():
    while True:
        play_game()
        play_again = input("Apakah Kamu ingin bermain lagi? (y/n): ").lower()
        if play_again != 'y':
            print("Terima kasih telah bermain!\n")
            break

if __name__ == "__main__":
    main()
