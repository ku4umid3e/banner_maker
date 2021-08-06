from PIL import Image, ImageDraw, ImageFont


im = Image.open(input('Укажите название файла:\n'))
msg = input('Укажите текст для картинки:\n')

# Обрезаем фото (x,y верхний левый угол, x,y нижний правый угол) 
im_crop = im.crop((0,150,1920,510))

# Размер получившегося изображения
W, H = 1920, 360

# Шрифт и его размер
font = ImageFont.truetype('Carlito-Bold.ttf', size=48)

# вычесляем размер сообщения
w,h = font.getsize(msg)

# Переносим текст на изображение
draw_text = ImageDraw.Draw(im_crop)

# Параметры текста (( Указываем положение текста), передаём сам текст, передаём шрифт и его размер, передаём цвет шрифта)
draw_text.text(
        ((W-w)/2,(H-h)/2),
        msg,
        font=font,
        fill=('#ffffff'),
        )

# Показываем и сохраняем изображение
im_crop.show()
im_crop.save(input('Как сохранить?\n'))
