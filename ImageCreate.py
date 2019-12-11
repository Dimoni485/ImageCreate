import scipy as sp
import PIL
import PIL.Image as Image
import PIL.ImageDraw as ImageDraw
import PIL.ImageFont as ImageFont
from scipy import ndimage
import os
import postgresql
import time
import datetime

font_fname = 'tahoma.ttf'
font_size =12
font = ImageFont.FreeTypeFont(font_fname, font_size)

font2 = ImageFont.FreeTypeFont(font_fname, 13)
font3 = ImageFont.FreeTypeFont(font_fname, 10)




h, w = 128, 112
bg_colour = (0, 0, 0)
x = 0
z=0
db = postgresql.open('pq://user:password@hostname/otd')
pinstate = db.prepare("SELECT pintab.pin_state, par.sh_name, pintab.d_pin, pintab.state_udtm  FROM up_logistic_cur AS pintab, param AS par  WHERE pintab.pin_state = true AND par.adr = pintab.ob LIMIT 5")
if len(pinstate()) > 0:
    
    print(pinstate()[0][0])
    bg_image = sp.dot(sp.ones((h,w,3), dtype='uint8'), sp.diag(sp.asarray((bg_colour), dtype='uint8')))
    image0 = Image.fromarray(bg_image)
    draw = ImageDraw.Draw(image0)
    draw.text((2, 0), "Машина", font=font, fill='rgb(255, 255, 255)')
    draw.text((46, 0), "Напр", font=font, fill='rgb(255, 255, 255)')
    draw.text((75, 0), "Прост", font=font, fill='rgb(255, 255, 255)')
    draw.line((112,15,0,15), fill='rgb(255, 255, 255)')
    while x < len(pinstate()):
        nowtime = time.time()
        
        prosttime = (int(nowtime) - int(pinstate()[x][3]))
        prosttime = str(prosttime).split(".")

        print(prosttime[0])
        secondspr = prosttime[0]
        stringtime = time.strftime('%H:%M', time.gmtime(int(secondspr)))
        print(stringtime)
        #stringtime = datetime.timedelta(seconds=secondspr)
        draw.text((2, 16+z), pinstate()[x][1], font=font, fill='rgb(255, 255, 255)')
        if pinstate()[x][2]==2:
            status = "X"
        else:
            status = ""
        draw.text((55, 17+z), status, font=font2, fill='rgb(255, 255, 255)')
        draw.text((76, 17+z), stringtime, font=font, fill='rgb(255, 255, 255)')
        #draw.text((2, 36+z), "Кюстерс", font=font3, fill='rgb(255, 255, 255)')
        z=z+19
        x=x+1
    #draw.text((55, 36), "Х", font=font2, fill='rgb(255, 255, 255)')
    #draw.text((76, 36), "00:00", font=font, fill='rgb(255, 255, 255)')
    #draw.text((2, 55), "Кюстерс", font=font3, fill='rgb(255, 255, 255)')
    #draw.text((55, 55), "Х", font=font2, fill='rgb(255, 255, 255)')
    #draw.text((76, 55), "00:00", font=font, fill='rgb(255, 255, 255)')
    #draw.text((2, 75), "Кюстерс", font=font3, fill='rgb(255, 255, 255)')
    #draw.text((55, 75), "Х", font=font2, fill='rgb(255, 255, 255)')
    #draw.text((76, 75), "00:00", font=font, fill='rgb(255, 255, 255)')
    #draw.text((2, 95), "Кюстерс", font=font3, fill='rgb(255, 255, 255)')
    #draw.text((55, 95), "Х", font=font2, fill='rgb(255, 255, 255)')
    #draw.text((76, 95), "00:00", font=font, fill='rgb(255, 255, 255)')
    draw.line((112,34,0,34), fill='rgb(255, 255, 255)')
    draw.line((112,53,0,53), fill='rgb(255, 255, 255)')
    draw.line((112,72,0,72), fill='rgb(255, 255, 255)')
    draw.line((112,91,0,91), fill='rgb(255, 255, 255)')
    draw.line((112,110,0,110), fill='rgb(255, 255, 255)')
    draw.line((45,110,45,0), fill='rgb(255, 255, 255)')
    draw.line((73,110,73,0), fill='rgb(255, 255, 255)')
    draw.text((5, 112), "Ожидает", font=font2, fill='rgb(255, 255, 255)')
    draw.text((62, 112), str(len(pinstate())), font=font2, fill='rgb(255, 255, 255)')
    draw.text((75, 112), "мест", font=font2, fill='rgb(255, 255, 255)')
    imgrota = image0.rotate(270, expand=1)
    imgrota.save("tmp.bmp", "BMP")
else:
    bg_image = sp.dot(sp.ones((h,w,3), dtype='uint8'), sp.diag(sp.asarray((bg_colour), dtype='uint8')))
    image0 = Image.fromarray(bg_image)
    draw = ImageDraw.Draw(image0)
    draw.text((2, 0), "Машина", font=font, fill='rgb(255, 255, 255)')
    draw.text((46, 0), "Напр", font=font, fill='rgb(255, 255, 255)')
    draw.text((75, 0), "Прост", font=font, fill='rgb(255, 255, 255)')
    draw.line((112,15,0,15), fill='rgb(255, 255, 255)')
    draw.line((112,34,0,34), fill='rgb(255, 255, 255)')
    draw.line((112,53,0,53), fill='rgb(255, 255, 255)')
    draw.line((112,72,0,72), fill='rgb(255, 255, 255)')
    draw.line((112,91,0,91), fill='rgb(255, 255, 255)')
    draw.line((112,110,0,110), fill='rgb(255, 255, 255)')
    draw.line((45,110,45,0), fill='rgb(255, 255, 255)')
    draw.line((73,110,73,0), fill='rgb(255, 255, 255)')
    draw.text((5, 112), "Ожидает", font=font2, fill='rgb(255, 255, 255)')
    draw.text((63, 112), str(len(pinstate())), font=font2, fill='rgb(255, 255, 255)')
    draw.text((75, 112), "мест", font=font2, fill='rgb(255, 255, 255)')
    imgrota = image0.rotate(270, expand=1)
    imgrota.save("tmp.bmp", "BMP")

os.system('java -jar JavaProject1.jar')
