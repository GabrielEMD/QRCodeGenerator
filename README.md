# Generador de códigos QR

"Español"
Este script de Python genera un código QR con propiedades específicas.

## Requisitos

- Python 3.x
- Biblioteca qrcode

Puedes instalar las bibliotecas necesarias utilizando el siguiente comando:

```bash
pip install qrcode
```
Uso

Clona el repositorio o descarga el script.

```bash
git clone https://github.com/GabrielEMD/QRCodeGenerator.git
cd QRCodeGenerator
```

Ejecuta el script
```bash
python main.py
```

Ingresa la URL o mensaje cuando se te solicite
Ingresa el nombre del archivo a crear (sin extensión)

Personalización
Ajusta el contenido del QR con el parámetro "-c" o "--content"
Ajusta el nombre del QR con el parámetro "-n" o "--name"
Ajusta si el QR tendrá transparencia con el parámetro "-t" o "--transparent"
Ajusta el parámetro "--color" para elegir el color del código QR.
Ajusta los parámetros "--size" y "--amount" en el script para controlar el tamaño y la densidad del código QR.

Notas
Asegúrate de tener Python instalado y las bibliotecas requeridas antes de ejecutar el script.

Ejecutable
Para la creación de un ejecutable, se utilizará cx_Freeze

Ejecuta el script
```bash
pip install cx_Freeze
python setup.py install
```

Se generará una carpeta build con el ejecutable.

"English"

# QR Code Generator

This Python script generates a QR code with specific properties.

## Requirements

- Python 3.x
- qrcode library

You can install the necessary libraries using the following command:

```bash
pip install qrcode
```
Usage

Clone the repository or download the script.
```bash
git clone https://github.com/GabrielEMD/QRCodeGenerator.git
cd QRCodeGenerator
```

Run the script.
```bash
python main.py
```

Enter the URL or message when prompted.
Enter the desired file name to create (without extension).

Customization
Adjust the QR content with the "-c" or "--content" parameter.
Adjust the QR name with the "-n" or "--name" parameter.
Specify if the QR should have transparency with the "-t" or "--transparent" parameter.
Adjust the "--color" parameter to choose the color of the QR code.
Adjust the "--size" and "--amount" parameters in the script to control the size and density of the QR code.

Notes
Make sure to have Python installed and the required libraries before running the script.

Executable
To create an executable, cx_Freeze will be used.

Run the script.
```bash
pip install cx_Freeze
python setup.py install
```

A "build" folder with the executable will be generated.
