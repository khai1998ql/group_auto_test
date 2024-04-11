import time
import subprocess
from typing import Union, Tuple

import numpy
import pyautogui
import pytesseract
from pyautogui import Point
from PIL import Image, ImageGrab

class Helpers:

    def get_text_by_image(self, image: str) -> str:
        txt = pytesseract.image_to_string(Image.open(image), lang='eng')
        return txt

    def click_by_coords(self, coords: list) -> None:
        pyautogui.click(*coords)

    def right_click_by_coords(self, coords: list) -> None:
        pyautogui.moveTo(*coords)
        pyautogui.rightClick()

    def get_coords_by_img(self, img_path: str) -> Union[Tuple, None]:
        try:
            coords = pyautogui.locateOnScreen(img_path)
            return coords
        except pyautogui.ImageNotFoundException:
            return None

    def gert_center_coords(self, img_path) -> Point:
        coords = self.get_coords_by_img(img_path)
        if not coords:
            raise  pyautogui.ImageNotFoundException
        return pyautogui.center(coords)

    def screenshot(self, img_path: str) -> None:
        pyautogui.screenshot(img_path)