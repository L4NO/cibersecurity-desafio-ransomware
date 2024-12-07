import os
from cryptography.fernet import Fernet

def encrypt_file(filename, key=None):
    # Gera ou usa a chave fornecida
    if key is None:
        key = Fernet.generate_key()
        # Salva a chave em um arquivo
        with open('filekey.key', 'wb') as filekey:
            filekey.write(key)
    
    # Instancia o objeto Fernet
    fernet = Fernet(key)
    
    # Abre e lê o arquivo original
    with open(filename, 'rb') as file:
        original = file.read()
        
    # Encripta o arquivo
    encrypted = fernet.encrypt(original)
    
    # Salva o arquivo encriptado
    encrypted_file = filename + '.encrypted'
    with open(encrypted_file, 'wb') as file:
        file.write(encrypted)
        
    # Remove o arquivo original
    os.remove(filename)
    
    print(f'Arquivo {filename} encriptado!')

if __name__ == "__main__":
    filename = "arquivo_teste.txt"
    encrypt_file(filename)