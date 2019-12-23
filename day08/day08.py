

with open('day08_input.txt') as f:
    sif = f.read()


pixels = [int(pixel) for pixel in sif]

width = 25
height = 6
depth = int(len(pixels) / (width * height))

layers = []

for strata in range(depth):
    layers.append(pixels[strata * width * height : (strata + 1) * width * height])
my_min = 1000
my_layer = []

for layer in layers:
    if layer.count(0) < my_min:
        my_min = layer.count(0)
        my_layer = layer

print(my_layer.count(1) * my_layer.count(2))

def get_pixel(p, layer_index):
    pixel = layers[layer_index][p]
    if pixel == 2:
        pixel = get_pixel(p, layer_index + 1)
    return pixel

my_image = []
layer_index = 0
for p, pixel in enumerate(layers[layer_index]):
    my_pixel = get_pixel(p, layer_index)

    my_image.append(my_pixel)

for i in range(height):
    print(my_image[i * width: i * width + width])


