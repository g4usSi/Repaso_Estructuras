import heapq
from collections import Counter, namedtuple

class Node(namedtuple("Node", ["char", "freq", "left", "right"])):
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    freq = Counter(text)
    heap = [Node(char, freq[char], None, None) for char in freq]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        parent = Node(None, left.freq + right.freq, left, right)
        heapq.heappush(heap, parent)
    
    return heap[0]

def generate_codes(node, prefix="", codebook={}):
    if node.char is not None:
        codebook[node.char] = prefix
    else:
        generate_codes(node.left, prefix + "0", codebook)
        generate_codes(node.right, prefix + "1", codebook)
    return codebook

def compress(text, codebook):
    return "".join(codebook[char] for char in text)

def main():
    print("--- Compresion Huffman ---")
    mensaje = input("Ingrese el mensaje: ")

    if not mensaje:
        print("Mensaje vacio. No hay nada para comprimir.")
        return

    tree = build_huffman_tree(mensaje)
    codebook = generate_codes(tree)

    mensaje_comprimido = compress(mensaje, codebook)

    original_bits = len(mensaje) * 8
    comprimido_bits = len(mensaje_comprimido)

    print("\n--- Resultados ---")
    print("Tamaño original:", original_bits, "bits")
    print("Tamaño comprimido:", comprimido_bits, "bits")
    print("Reduccion:", round((1 - (comprimido_bits / original_bits)) * 100, 2), "%")

    print("\nMensaje Comprimido (bits):")
    print(mensaje_comprimido)

    print("\nCodigos Huffman utilizados:")
    for char, code in codebook.items():
        print(f"'{char}': {code}")

if __name__ == "__main__":
    main()