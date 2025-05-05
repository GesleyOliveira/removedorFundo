from rembg import remove
from PIL import Image

input_path = './imagens/Foto.jpg'
output_path = 'ElonMusk.png'

inp = Image.open(input_path)
output = remove(inp)
output.save(output_path)