from solders.keypair import Keypair

private_key_in_bs58 = "" # Private key in base58 exported from wallet

key_pair = Keypair.from_base58_string(private_key_in_bs58)

print(f"Address: {key_pair.pubkey()}")
print(f"id.json: {key_pair.to_json()}")