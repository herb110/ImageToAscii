from PIL import Image
import argparse

ascii_char = list("$@B%B&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'.") 

def get_char(r, g, b, alpha = 256):
    if alpha == 0:
        return " "
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0+1)/length
    return ascii_char[ int(gray/unit) ]

def Parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('file')     #输入文件
    parser.add_argument('-o', type = str, default = 'output.txt')   #输出文件
    parser.add_argument('--width', type = int,default = 80)     #输出字符画宽
    parser.add_argument('--height',type = int, default = 80)    #输出字符画高
    args = parser.parse_args()

    dict = {
    'IMG':args.file,
    'WIDTH':args.width,
    'HEIGHT':args.height,
    'OUTPUT':args.o
    }

    return dict
    
def ImageToAscii():
    dict = Parser()
    
    IMG = str(dict['IMG'])
    WIDTH = int(dict['WIDTH'])
    HEIGHT = int(dict['HEIGHT'])
    OUTPUT = str(dict['OUTPUT'])
    
    im = Image.open(IMG)
    im = im.resize((WIDTH,HEIGHT),Image.NEAREST)
    
    txt =""
    for h in range(HEIGHT):
        for w in range(WIDTH):
            txt += get_char( *im.getpixel((w,h)))
        txt += '\n'
    print(txt)
    
    if OUTPUT:
        with open(OUTPUT,'w') as f:
            f.write(txt)
        
if __name__ == '__main__':
    ImageToAscii()