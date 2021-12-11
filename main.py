# https://stackoverflow.com/questions/54862795/encode-multiple-jpg-files-in-a-folder-as-base-64-in-python
# Файлы в python, ввод-вывод
# https://pythonru.com/osnovy/fajly-v-python-vvod-vyvod
import os
import base64

words = []
directory = 'img'

# Запись в файл
resultImages = ""
f = open('images.txt','w')  # открытие в режиме записи
# f.write("import Vue from 'vue' \n const state = { \n  images: { \n")  # запись Hello World в файл


for filename in os.listdir(directory):
    if filename.endswith(".png"): 
        with open(os.path.join(directory, filename), "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
            # decode the bytes object to produce a string
            resultImages += "'" + filename + "':{" + "\n" + "src: 'data:image/png;base64," + encoded_string.decode("utf-8") + "'," + "\n" + " }," + "\n"
            # words.extend(extract_ocr_Words(encoded_string))
    else:
        continue
print('Words from all files')
print(resultImages)

f.write(resultImages) 