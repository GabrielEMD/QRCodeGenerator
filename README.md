# Generador de códigos QR

## "Español"
Este script de Python genera un código QR con propiedades específicas.

## Requisitos

- Python 3.x
- Biblioteca [qrcode](https://pypi.org/project/qrcode/)
- Biblioteca [PIL (Pillow)](https://pypi.org/project/pillow/)

Puedes instalar las bibliotecas necesarias utilizando el siguiente comando:

```bash
pip install qrcode Pillow
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

| Personalización                                  | Descripción                                                              | Ejemplo de Uso                              |
|--------------------------------------------------|--------------------------------------------------------------------------|---------------------------------------------|
| `-c` o `--content`                               | Ajusta el contenido del QR.                                              | `main -c "Texto de ejemplo"`                |
| `-n` o `--name`                                  | Ajusta el nombre del QR.                                                 | `main -n "NombreQR"`                        |
| `-t` o `--transparent`                           | Ajusta si el QR tendrá transparencia.                                    | `main -t`                                   |
| `--color`                                        | Ajusta el color del código QR.                                           | `main --color "white"`                      |
| `--size` y `--amount`                            | Ajusta el tamaño y la densidad del código QR en el script.               | `main --size 200 --amount 3`                |
| `--image` y `--image-width`                      | Ajusta la imagen y su tamaño en el centro del código QR en el script.    | `main --image "logo.png" --image-width 50`  |


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

# QR Code Generator
## "English"

This Python script generates a QR code with specific properties.

## Requirements

- Python 3.x
- [qrcode](https://pypi.org/project/qrcode/) library
- [PIL (Pillow)](https://pypi.org/project/pillow/) library

You can install the necessary libraries using the following command:

```bash
pip install qrcode Pillow
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

| Customization                                    | Description                                                               | Example Usage                              |
|--------------------------------------------------|---------------------------------------------------------------------------|--------------------------------------------|
| `-c` or `--content`                              | Adjusts the content of the QR.                                            | `main -c "Example text"`                   |
| `-n` or `--name`                                 | Adjusts the name of the QR.                                               | `main -n "QRName"`                         |
| `-t` or `--transparent`                          | Adjusts whether the QR will have transparency.                            | `main -t`                                  |
| `--color`                                        | Adjusts the color of the QR code.                                         | `main --color "white"`                     |
| `--size` and `--amount`                          | Adjusts the size and density of the QR code in the script.                | `main --size 200 --amount 3`               |
| `--image` and `--image-width`                    | Adjusts the image and its size in the center of the QR code in the script.| `main --image "logo.png" --image-width 50` |


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
