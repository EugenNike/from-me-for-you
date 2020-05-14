from PIL import ImageDraw, Image


class DoorImageDraw(ImageDraw.ImageDraw):
    def door(self, xy, fill):
        width = xy[-1]
        drw.rectangle((xy[0], xy[1], xy[0] + width, xy[1] + width * 2), fill=fill[0])
        for i in range(2):
            drw.rectangle((xy[0] + width // 8, xy[1] + width // 8 + width * i, xy[0] + (width - width // 8), xy[1] + width * (i + 1) - width // 8),fill=fill[1])
            drw.line((xy[0] + width // 8, xy[1] + width // 8 + width * i, xy[0] + (width - width // 8),
                      xy[1] + width * (i + 1) - width // 8), fill=fill[-1], width=3)
            drw.line((xy[0] + width // 8, xy[1] + width * (i + 1) - width // 8, xy[0] + (width - width // 8),
                      xy[1] + width // 8 + width * i), fill=fill[-1], width=3)
        drw.line((xy[0], xy[1] + width, xy[0] + width, xy[1] + width), fill=fill[-1], width=3)


img = Image.new('RGB', (1000, 1000), '#000000')
drw = DoorImageDraw(img)
drw.door((275, 50, 450), ('#ffffff', '#999999', '#666666'))
img.save('result.png')
