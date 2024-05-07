from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
from Crypto.Random import get_random_bytes

def encrypt_message(message, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(message.encode(), AES.block_size))
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    ct = base64.b64encode(ct_bytes).decode('utf-8')
    return iv, ct

def decrypt_message(iv, ct, key):
    iv_decoded = base64.b64decode(iv)
    ct_decoded = base64.b64decode(ct)
    cipher = AES.new(key, AES.MODE_CBC, iv_decoded)
    pt = unpad(cipher.decrypt(ct_decoded), AES.block_size)
    return pt.decode('utf-8')

def main():
    print("=========================================-=")
    print('|==ENCRYPT & DECRYPT WITH AES ALGORITHM===|')
    print("===========================================")
    
    key = get_random_bytes(16)  # Generate a random key
    
    while True:
        print("\nMenu:")
        print("1. Enkripsi")
        print("2. Dekripsi")
        print("3. Keluar")
        option = input("Pilih Option: ")
        
        if option == '1':
            message = input("Masukkan pesan yang akan dienkripsi: ")
            iv, ciphertext = encrypt_message(message, key)
            print("\nPesan Terenkripsi:")
            print("Key :", iv)
            print("Ciphertext:", ciphertext)
        elif option == '2':
            iv = input("Masukkan Key : ")
            ciphertext = input("Masukkan Ciphertext: ")
            decrypted_message = decrypt_message(iv, ciphertext, key)
            print("\nPesan Terdekripsi:")
            print("Message:", decrypted_message)
        elif option == '3':
            print("Terima kasih telah menggunakan program ini.")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")

if __name__ == "__main__":
    main()
