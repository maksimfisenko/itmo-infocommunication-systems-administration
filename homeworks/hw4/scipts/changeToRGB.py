import ctypes
import sys
import os
from PIL import Image


def change_wallpaper(r: float, g: float, b: float) -> None:
    img = Image.new("RGB", (1920, 1080), (r, g, b))
    img_path = os.path.dirname(__file__) + '\\image_rgb.jpg'
    img.save(img_path)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, img_path, 3)


def main() -> None:
    if len(sys.argv) != 4:
        print("Error! Try: python changeToRGB.py <R> <G> <B>")
        return
    change_wallpaper(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))


if __name__ == "__main__":
    main()
