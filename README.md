# RSAKeyAnalyzer

## Introduction

`RSAKeyAnalyzer` is a tool designed to decode RSA private keys from their PEM format, analyze their ASN.1 structure, and convert them into a hexadecimal representation. This project is useful for cryptographic tasks, educational purposes, and anyone interested in understanding the structure of RSA keys.

## Features

- Decode RSA private keys from PEM format.
- Analyze and display the ASN.1 structure of the keys.
- Convert the decoded keys into a hexadecimal representation.

## Requirements

- Python 3.x
- `pyasn1` library for ASN.1 parsing (optional for advanced analysis)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/valorisa/RSAKeyAnalyzer.git
   cd RSAKeyAnalyzer
   ```

2. Install the required Python packages:
   ```bash
   pip install pyasn1
   ```

## Usage

1. Place your RSA private key file (e.g., `example.pem`) in the project directory.
2. Run the decoding script:
   ```bash
   python decode.py > hexa_example
   ```
3. The hexadecimal representation of the key will be saved in `hexa_example`.

## File Structure

- `decode.py`: The main script to decode PEM files and convert them to hexadecimal.
- `example.pem`: An example RSA private key file in PEM format.
- `hexa_example`: The output file containing the hexadecimal representation of the key.
- `original-private-key.pem`: Another example PEM file for testing.
- `screen.pem`: A partial key file for demonstration purposes.

## ASN.1 Structure

RSA private keys in PEM format are encoded using ASN.1, which is a standard notation for describing data structures. The ASN.1 structure of an RSA private key typically includes:

- Version
- Modulus (n)
- Public Exponent (e)
- Private Exponent (d)
- Prime1 (p)
- Prime2 (q)
- Exponent1 (d mod (p-1))
- Exponent2 (d mod (q-1))
- Coefficient (qInv)

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact

For any questions or suggestions, feel free to contact us at [your-email@example.com](mailto:your-email@example.com).
```

### Directory Structure

```plaintext
RSAKeyAnalyzer/
├── decode.py
├── example.pem
├── hexa_example
├── original-private-key.pem
├── screen.pem
├── README.md
└── LICENSE
```

### Additional Notes

- **LICENSE**: Include a license file, such as the MIT License, to specify the terms under which the project can be used and distributed.
- **Contributing Guidelines**: Consider adding a `CONTRIBUTING.md` file to guide contributors on how to contribute to the project.
- **Issue Tracking**: Use GitHub Issues to track bugs, enhancements, and feature requests.

This setup should provide a solid foundation for your project on GitHub. If you need further customization or additional features, feel free to ask!

