
from argparse import ArgumentParser
from models.QRCodeGenerator import QRCodeGenerator

def run():
    parser = ArgumentParser(description='Generate QR code with specified properties.')

    # Add command line arguments
    parser.add_argument('-c', '--content', type=str, help='Content for the QR code')
    parser.add_argument('-n', '--name', type=str, help='Desired name for the output file')
    parser.add_argument('-t', '--transparent', action='store_true', help='Use transparent background')
    parser.add_argument('--color', type=str, choices=['white', 'black'], default='white', help='Color for the QR code')
    parser.add_argument('--size', type=int, default=10, help='Qr size (Default: 10)')
    parser.add_argument('--amount', type=int, default=1, help='Qr pixels amount (Default:1)')

    # Parse the arguments
    args = parser.parse_args()

    # Assign values or ask for input
    content = args.content or input("Enter the content to convert to a QR code: ")
    name = args.name or input("Enter the desired name for the output file: ")
    transparent = args.transparent
    color = args.color
    size = args.size
    amount = args.amount

    qr_code = QRCodeGenerator(content, name, color, transparent)
    qr_code.set_colors()
    qr_code.generate_qrcode(size, amount)

if __name__ == "__main__":
    run()