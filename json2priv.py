import base58
from solders.keypair import Keypair

secret_key_list = [] # UInt8[64]

key_pair = Keypair.from_bytes(bytes(secret_key_list))

private_key_base58 = base58.b58encode(key_pair.to_bytes()).decode("ascii")

print(f"Address: {key_pair.pubkey()}")
print(f"private key: {private_key_base58}")