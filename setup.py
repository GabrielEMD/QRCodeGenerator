from cx_Freeze import setup, Executable

setup(
    name="QRCodeGenerator",
    version="0.1",
    description="A QR Code Generator",
    executables=[Executable("main.py")]
)
