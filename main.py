
from argparse import ArgumentParser
from models.QRCodeGenerator import QRCodeGenerator

def run():
    """Parse command line arguments, validate inputs, and generate a QR code.

    Command Line Arguments:
        -c, --content: Content for the QR code.
        -n, --name: Desired name for the output file.
        -t, --transparent: Use transparent background.
        --color: Color for the QR code (choices: 'white' or 'black', default: 'white').
        --size: QR size (default: 10).
        --amount: QR pixels amount (default: 1).
        --image: QImage into the QR code.
        --image-width: Width for image into the QR code.

    Create:
        Gabriel Muñoz
        22/01/2024
    """
    parser = ArgumentParser(description='Generate QR code with specified properties.')

    # Add command line arguments
    parser.add_argument('-c', '--content', type=str, help='Content for the QR code')
    parser.add_argument('-n', '--name', type=str, help='Desired name for the output file')
    parser.add_argument('-t', '--transparent', action='store_true', help='Use transparent background')
    parser.add_argument('--color', type=str, choices=['white', 'black'], default='white', help='Color for the QR code')
    parser.add_argument('--size', type=int, default=10, help='Qr size (Default: 10)')
    parser.add_argument('--amount', type=int, default=1, help='Qr pixels amount (Default:1)')
    parser.add_argument('--image', type=str, help='Image into the QR code')
    parser.add_argument('--image-width', type=float, help='Width for image into the QR code')

    # Parse the arguments
    args = parser.parse_args()

    # Assign values or ask for input
    content = args.content or input("Enter the content to convert to a QR code: ")
    name = args.name or input("Enter the desired name for the output file: ")
    transparent = args.transparent
    color = args.color
    size = args.size
    amount = args.amount
    image = args.image or None
    image_width = args.image_width or None

    # Validate inputs
    if not content:
        raise ValueError("Content cannot be empty.")
    if not name:
        raise ValueError("Name cannot be empty.")
    if size <= 0:
        raise ValueError("Size must be a positive number.")
    if amount <= 0:
        raise ValueError("Amount must be a positive number.")

    try:
        qr_code = QRCodeGenerator(content, name, color, transparent)
        qr_code.set_colors()
        qr_code.validate_options(image, image_width)
        qr_code.generate_qrcode(size, amount)
    except ValueError as ve:
        print(f"An error occurred while validating the inputs: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred while generating the QR code: {e}")

if __name__ == "__main__":
    run()
