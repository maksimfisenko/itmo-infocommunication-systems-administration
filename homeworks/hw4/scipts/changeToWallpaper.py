import ctypes
import sys
import os


def change_wallpaper(image_path):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)


def main() -> None:
    if len(sys.argv) != 2:
        print("Error! Try: python changeToWallpaper.py <path_to_image>")
        return
    image_path = os.path.dirname(__file__) + '\\' + sys.argv[1]
    change_wallpaper(image_path)


if __name__ == "__main__":
    main()
