# pip install opencv-python
# pip install pytesseract

from os import listdir
from os.path import isfile, join
from cv2 import imread
import pytesseract


class PhoneNumbers:
    def fetch_phone_numbers(self, folder_path):
        """
        This method is used to fetch phone numbers from image or screenshots.
        Updates can be added. You can add regex to get only phone numbers
        :param folder_path: Folder includes images
        :return: <list> return phone numbers from ocr engine
        """
        phone_numbers: list = list()
        #  ocr path must be updated regarding your own ocr engine path
        pytesseract.pytesseract.tesseract_cmd = (
            r"C:/Program Files/tesseract-ocr/tesseract.exe"
        )
        files = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]
        for file in files:
            full_path = f"{folder_path}/{file}"
            try:
                number_img = imread(full_path)
                # convert image to text using tesseract
                text = pytesseract.image_to_string(number_img)
                phone_numbers.append(text)
            except Exception as error:
                phone_numbers.append("ERROR")
        return phone_numbers


phone_obj = PhoneNumbers()
phones = phone_obj.fetch_phone_numbers("your_folder_path_which_includes_images")
