def fnv1_hash(texto):
    FNV_PRIME = 16777619
    OFFSET_BASIS = 2166136261

    hash_value = OFFSET_BASIS

    for char in texto:
        hash_value = hash_value * FNV_PRIME
        hash_value = hash_value ^ ord(char)
        hash_value = hash_value & 0xffffffff
    return hash_value

def main():
    print("--- Hashing FNV-1 ---")
    mensaje = input("Ingrese un mensaje de texto: ")

    resultado = fnv1_hash(mensaje)

    print("\nHash FNV-1 (32 bits) generado:")
    print(hex(resultado))

main()
