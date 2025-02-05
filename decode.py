import base64
import binascii

def decode_pem_to_hex(pem_file_path):
    try:
        with open(pem_file_path, 'r') as f:
            lines = f.readlines()

        # Supprimer les lignes de début et de fin
        base64_data = []
        in_base64_section = False
        for line in lines:
            line = line.strip()
            if line.startswith('-----BEGIN') or line.startswith('-----END'):
                in_base64_section = not in_base64_section
                continue
            if in_base64_section:
                base64_data.append(line)

        base64_string = ''.join(base64_data)

        # Décoder la base64
        binary_data = base64.b64decode(base64_string)

        # Convertir en hexadécimal
        hex_data = binascii.hexlify(binary_data).decode('ascii')

        # Afficher les octets en hexadécimal
        for i in range(0, len(hex_data), 96):
            print(hex_data[i:i+96])

    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

# Exemple d'utilisation
decode_pem_to_hex('example.pem')
