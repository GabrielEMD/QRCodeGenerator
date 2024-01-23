
from os.path import dirname, abspath, exists
from os import makedirs
from qrcode import QRCode
from qrcode.constants import ERROR_CORRECT_L
from PIL import Image

class QRCodeGenerator:
    """
    QRCodeGenerator is a class for generating QR codes with specified properties.

    Attributes:
        content (str): The content to convert into a QR code.
        name (str): The desired name for the output file.
        color (str): The color for the QR code.
        transparent (bool): Whether to use a transparent background.

    Methods:
        set_colors(): Sets the colors for the QR code.
        generate_qrcode(size: int, version: int) -> None: Generates the QR code based on the provided or default values.
        make_transparent_background(img: Image) -> Image: Makes the QR code background transparent.
        add_image_to_qr(qr_image: Image) -> Image: Superposes an image into the center of the generated QR code.
        validate_options(image: str = None, image_width: int | None = None) -> None: Validates and sets additional options.
        more_options(qr_image: Image) -> Image: Provides additional options such as adding an image.

    Create:
        Gabriel Muñoz
        22/01/2024
    """

    def __init__(self, content:str, name:str, color:str, transparent:bool) -> None:
        """Initialize the QRCodeGenerator with user-provided or default values.

        Args:
            content (str): The content to convert to a QR code.
            name (str): The desired name for the output file.
            color (str): The color for the QR code.
            transparent (bool): Whether to have a transparent background.

        Create:
            Gabriel Muñoz
            22/01/2024
        """
        self.content = content
        self.name = name
        self.color = color.lower()
        self.transparent = transparent

        route = dirname(abspath(__file__))+"\\images\\"
        route = route.replace("lib\\models\\", "")
        self.route = route.replace("models\\", "")


    def set_colors(self) -> None:
        """Set colors for the QR code.

        Create:
            Gabriel Muñoz
            22/01/2024
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


    def generate_qrcode(self, size:int, version:int) -> None:
        """Generate the QR code based on the provided or default values.

        Args:
            size (int): The QR code size/width.
            version (int): The pixels amount for the QR code.

        Create:
            Gabriel Muñoz
            22/01/2024
        """
        self.size = size

        qr = QRCode(
            version=version,
            error_correction=ERROR_CORRECT_L,
            box_size=size,
            border=4,
        )

        qr.add_data(self.content)
        qr.make(fit=True)

        img = qr.make_image(fill_color=self.color, back_color=self.color2)

        img = img.convert("RGBA")

        if self.transparent:
            img = self.make_transparent_background(img)

        img = self.more_options(img)

        makedirs(self.route, exist_ok=True)

        img.save(f"{self.route}{self.name}.png", "PNG")

        print(f"The QR code has been saved as {self.name}.png")


    def make_transparent_background(self, img:Image) -> Image:
        """Make the QR code background transparent.

        Args:
            img (Image): The QR code image.

        Returns:
            Image: The QR code image with a transparent background.

        Create:
            Gabriel Muñoz
            22/01/2024
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


    def add_image_to_qr(self, qr_image:Image) -> Image:
        """Superpose an image into the center of the generated QR code.

        Args:
            qr_image (Image): The QR code image.

        Returns:
            Image: The QR code image with the added image.

        Create:
            Gabriel Muñoz
            23/01/2024
        """
        try:
            scale_factor = self.scale_factor

            # Open the image to be added
            overlay = Image.open(self.image)

            # Calculate the position to center the image on the QR code
            x_position = (qr_image.width - int(overlay.width * scale_factor)) // 2
            y_position = (qr_image.height - int(overlay.height * scale_factor)) // 2

            # Resize the overlay image
            overlay = overlay.resize((int(overlay.width * scale_factor), int(overlay.height * scale_factor)))

            # Paste the overlay onto the QR code
            qr_image.paste(overlay, (x_position, y_position), overlay)

            return qr_image
        except Exception as e:
            raise ValueError(f"An error occurred while adding the image to the QR code: {e}")


    def validate_options(self, image:str=None, image_width:int|None=None):
        """Validates and sets additional options.

        Args:
            image (str, optional): Path to the image file to be added.
            image_width (int, optional): Scaling factor for the added image.

        Create:
            Gabriel Muñoz
            23/01/2024
        """
        self.image = image
        self.scale_factor = image_width


    def more_options(self, qr_image: Image) -> Image:
        """Provides additional options such as adding an image.

        Args:
            qr_image (Image): The QR code image.

        Returns:
            Image: The QR code image with additional options applied.

        Create:
            Gabriel Muñoz
            23/01/2024
        """
        if (self.image):
            if (exists(self.image)):
                if (not self.scale_factor):
                    self.scale_factor = self.size / 50
                qr_image = self.add_image_to_qr(qr_image)
            else:
                raise ValueError("Could not find the image.")
        return qr_image
