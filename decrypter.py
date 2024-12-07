import os
from cryptography.fernet import Fernet

def decrypt_file(encrypted_file):
    # Lê a chave do arquivo
    with open('filekey.key', 'rb') as filekey:
        key = filekey.read()

    # Instancia o objeto Fernet
    fernet = Fernet(key)
    
    # Abre o arquivo encriptado
    with open(encrypted_file, 'rb') as file:
        encrypted = file.read()
        
    # Decripta o conteúdo
    decrypted = fernet.decrypt(encrypted)
    
    # Salva o arquivo decriptado
    original_file = encrypted_file.replace('.encrypted', '')
    with open(original_file, 'wb') as file:
        file.write(decrypted)
        
    # Remove o arquivo encriptado
    os.remove(encrypted_file)
    
    print(f'Arquivo {encrypted_file} decriptado!')

if __name__ == "__main__":
    filename = "arquivo_teste.txt.encrypted"
    decrypt_file(filename)