import os
import hashlib
import ecdsa
import json
from Crypto.Cipher import AES

class XRPLWalletGenerator:
    def __init__(self):
        # Gera uma chave privada aleatória (256 bits)
        self.private_key = os.urandom(32)
        
        # Usa a chave privada para calcular a chave pública
        self.public_key = self.generate_public_key()

        # Deriva o endereço da carteira a partir da chave pública
        self.address = self.generate_address()

    def generate_public_key(self):
        # Cria uma chave privada usando a biblioteca ecdsa
        private_key = ecdsa.SigningKey.from_string(self.private_key, curve=ecdsa.SECP256k1)

        # Obtém a chave pública
        public_key = private_key.get_verifying_key().to_string()

        return public_key

    def generate_address(self):
        # Hash da chave pública usando SHA-256 e RIPEMD-160
        sha256_hash = hashlib.sha256(self.public_key).digest()
        ripe160_hash = hashlib.new('ripemd160', sha256_hash).digest()

        # Prefixa com um byte de versão (0x00 para Bitcoin, por exemplo)
        versioned_hash = b'\x00' + ripe160_hash

        # Calcula o checksum usando SHA-256 duas vezes
        checksum = hashlib.sha256(hashlib.sha256(versioned_hash).digest()).digest()

        # Concatena o endereço com o checksum
        address = versioned_hash + checksum[:4]

        # Codifica o endereço em base58 (opcional, mas comum em criptomoedas)
        base58_address = self.base58_encode(address)

        return base58_address

    def base58_encode(self, data):
        # Base58 encode - converte para uma representação legível por humanos
        alphabet = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
        base_count = len(alphabet)
        encode = ''
    
        # Converte os bytes para um número inteiro
        num = int.from_bytes(data, 'big')

        # Base58 encode
        while num > 0:
            num, rem = divmod(num, base_count)
            encode = alphabet[rem] + encode

        return encode

    def save_to_json(self, filename, password):
        """
        Salva as informações da carteira em um arquivo JSON criptografado.

        Args:
            filename (str): Caminho do arquivo JSON para salvar.
            password (str): Senha para criptografar a chave privada.
        """

        wallet_info = {
            "addresses": [],
            "private_keys": [],
            "public_keys": [],
        }

        # Adiciona os dados da carteira ao dicionário
        wallet_info["addresses"].append(self.address)
        
        # Criptografa a chave privada antes de salvá-la
        cipher = AES.new(password.encode(), AES.MODE_ECB)
        encrypted_private_key = cipher.encrypt(self.private_key)

        wallet_info["private_keys"].append(encrypted_private_key.hex())
        wallet_info["public_keys"].append(self.public_key.hex())

        # Salva o dicionário em um arquivo JSON
        with open(filename, "w") as f:
            json.dump(wallet_info, f, indent=4)

# Cria um objeto XRPLWalletGenerator
wallet_generator = XRPLWalletGenerator()

# Imprime o endereço da carteira
print(f"Endereço: {wallet_generator.address}")

# Salva as informações da carteira em um arquivo JSON
wallet_generator.save_to_json("wallet.json", "1234567890qwerty")
