
from os.path import dirname, abspath
from os import makedirs
import qrcode

class QRCodeGenerator:
    def __init__(self, content:str, name:str, color:str, transparent:bool):
        """Initialize the QRCodeGenerator with user-provided or default values.

        Args:
            content (str): The content to convert to a QR code.
            name (str): The desired name for the output file.
            color (str): The color for the QR code.
            transparent (bool): Whether to have a transparent background.
        """
        self.content = content
        self.name = name
        self.color = color.lower()
        self.transparent = transparent

        route = dirname(abspath(__file__))+"\\images\\"
        route = route.replace("lib\\models\\", "")
        self.route = route.replace("models\\", "")

    def set_colors(self):
        """Set colors for the QR code.
        """
        if self.color == "white":
            self.color2 = "black"
            self.rgb_color = (0,0,0)
        elif self.color == "black":
            self.color2 = "white"
            self.rgb_color = (255,255,255)
        else:
            print("Invalid color. Please enter either 'white' or 'black'.")
            self.color = (input("Enter color for the QR code (white or black): ")).lower()
            self.set_colors()

    def generate_qrcode(self, size:int, version:int):
        """Generate the QR code based on the provided or default values.
        """
        qr = qrcode.QRCode(
            version=version,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=size,
            border=4,
        )

        qr.add_data(self.content)
        qr.make(fit=True)

        img = qr.make_image(fill_color=self.color, back_color=self.color2)

        img = img.convert("RGBA")

        if self.transparent:
            img = self.make_transparent_background(img)

        makedirs(self.route, exist_ok=True)

        img.save(f"{self.route}{self.name}.png", "PNG")
        print(f"The QR code has been saved as {self.name}.png")

    def make_transparent_background(self, img):
        """Make the QR code background transparent.

        Args:
            img (Image): The QR code image.

        Returns:
            Image: The QR code image with a transparent background.
        """
        data = img.getdata()
        new_data = []

        for item in data:
            if item[:3] == self.rgb_color:  # Change white background to transparent
                new_data.append((255, 255, 255, 0))
            else:
                new_data.append(item)

        img.putdata(new_data)
        return img
