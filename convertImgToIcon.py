from PIL import Image

# Put the image file in the same folder
filename = r'wnh.png'
img = Image.open(filename)
icon_sizes = [(16,16), (32, 32), (48, 48), (64,64)]
img.save('game.ico', sizes=icon_sizes)
