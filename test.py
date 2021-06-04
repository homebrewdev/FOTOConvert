import sys
import os


# функция конвертации фоток в формат prefix_filename.jpg
# как массово дать одинаковый префикс для картинок (файлов)
# ls | xargs -I {} mv {} Prefix_{}
# в нашем случае:
# ls | xargs -I {} mv {} 60b4f190c9c53115c3d74223_{}
def add_prefix_jpg(prefix):
    init_convert = os.system("ls FOTO | xargs -I {} mv FOTO/{} FOTO/%s_{}" % prefix)
    if init_convert == 0:
        print("... Конвертация прошла успешно! Загляни в папку FOTO")
    else:
        print("... Ошибка конвертации.")


# find -type f -iname "*.jpg" -exec jpegoptim --strip-all --all-progressive {} \;
def squizzz_jpg():
    os.system("cd FOTO | find -type f -iname '*.jpg' -exec jpegoptim --strip-all --all-progressive {} \;")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        id = sys.argv[1]
        print("1 этап \n ... Сжимаю jpg ...")
        squizzz_jpg()
        print("2 этап. \n ...Начало конвертации фотографий с префиксом {}_".format(id))
        add_prefix_jpg(id)
    else:
        print("параметр - id prefix не указан. Вызовите утилиту convert.py с параметром id")
        print("например:")
        print("python3 convert.py 60b862670906971218f8223f")
