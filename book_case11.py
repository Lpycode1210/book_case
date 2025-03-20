# from PIL import image
# im = image.open('picture.gif')#提取动图帧图片
# try:
#     im.save('picframe{:02d}.png'.format(im.tell()))
#     while True:
#         im.seek(im.tell()+1)
#         im.save('picframe{:02d}.png'.format(im.tell()))
# except:
#     print("end")


from PIL import Image
im = Image.open('astro.jpg').convert('RGB')
ascii_char = list(r'"$%_&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-/+@<>i!;:,\^`.')
def get_char(r, b, g, alpha=256):
    if alpha == 0:
        return ' '
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = 256 / len(ascii_char)
    return ascii_char[int(gray//unit)]
def main():
    im = Image.open('astro.jpg')
    WIDTH, HEIGHT = 100, 60
    im = im.resize((WIDTH, HEIGHT))
    txt = ""
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j, i)))
        txt += '\n'
    fo = open("pic_char.txt","w")
    fo.write(txt)
    fo.close()
main()
