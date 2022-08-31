# -*- encoding: utf-8 -*-
"""
@File Name      :   barcode_recognition.py    
@Create Time    :   2022/4/6 19:59
@Description    :   
@Version        :   
@License        :   MIT
@Author         :   diklios
@Contact Email  :   diklios5768@gmail.com
@Github         :   https://github.com/diklios5768
@Blog           :   
@Motto          :   All our science, measured against reality, is primitive and childlike - and yet it is the most precious thing we have.
"""
__auth__ = 'diklios'

import os

import cv2
import easyocr
import numpy as np
import pyzbar.pyzbar as pyzbar


def delete_useless_images(dir_path: str):
    for file_path in os.listdir(dir_path):
        if os.path.getsize(os.path.join(dir_path, file_path)) < 102400:
            os.remove(os.path.join(dir_path, file_path))


def handle_barcode(gray):
    texts = pyzbar.decode(gray)
    if not texts:
        angle = barcode_angle(gray)
        if angle < -45:
            angle = -90 - angle
        texts = handle_bar(gray, angle)
    if not texts:
        gray = np.uint8(np.clip((1.1 * gray + 10), 0, 255))
        angle = barcode_angle(gray)
        if angle < -45:
            angle = -90 - angle
        texts = handle_bar(gray, angle)
    return texts


def handle_bar(image, angle):
    gray = image
    bar = rotate_bound(gray, 0 - angle)
    roi = cv2.cvtColor(bar, cv2.COLOR_BGR2RGB)
    texts = pyzbar.decode(roi)
    return texts


def barcode_angle(image):
    gray = image
    ret, binary = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY_INV)
    kernel = np.ones((8, 8), np.uint8)
    dilation = cv2.dilate(binary, kernel, iterations=1)
    erosion = cv2.erode(dilation, kernel, iterations=1)
    erosion = cv2.erode(erosion, kernel, iterations=1)
    erosion = cv2.erode(erosion, kernel, iterations=1)

    contours, hierarchy = cv2.findContours(
        erosion, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    if len(contours) == 0:
        rect = [0, 0, 0]
    else:
        rect = cv2.minAreaRect(contours[0])
    return rect[2]


def rotate_bound(image, angle):
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)

    M = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])
    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))

    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY

    return cv2.warpAffine(image, M, (nW, nH))


def recognize_barcode(file_paths, top, bottom, left, right, ):
    for file_path in file_paths:
        image = cv2.imread(file_path)
        image_barcode_region = image[top:bottom, left:right]
        # cv2.imshow('image', image_barcode_region)
        # cv2.waitKey()
        image_gray = cv2.cvtColor(image_barcode_region, cv2.COLOR_BGR2GRAY)
        texts_recognized = handle_barcode(image_gray)
        if not texts_recognized:
            print("未识别成功")
        else:
            print("识别成功")
            # print(texts_recognized)
            for text in texts_recognized:
                barcode = text.data.decode("utf-8")
                print(barcode)


def handle_replace(text):
    replaces = {
        '8': 'B',
        '7': 'Y',
        '0': 'O',
        '1': 'I',
        '2': 'Z',

    }
    for key, value in replaces.items():
        text = text.replace(key, value)
    return text


def recognize_barcode_string(file_paths, top_percent: float = 0, bottom_percent: float = 0, left_percent: float = 0,
                             right_percent: float = 0):
    # 创建reader对象
    reader = easyocr.Reader([
        # 'ch_sim',
        'en'
    ], gpu=False)
    for file_path in file_paths:
        # 读取图像
        if os.path.isfile(file_path) and os.path.exists(file_path):
            image = cv2.imread(file_path)
            if not image:
                continue
            top = None
            bottom = None
            left = None
            right = None
            # 获取图像的高和宽
            height, width = image.shape[:2]
            # 计算图像的顶部和底部
            if top_percent:
                top = int(height * top_percent)
            if bottom_percent:
                bottom = int(height * bottom_percent)
            # 计算图像的左边和右边
            if left_percent:
                left = int(width * left_percent)
            if right_percent:
                right = int(width * right_percent)
            image_barcode_region = image[top:bottom, left:right]
            # cv2.imshow('image', image_barcode_region)
            # cv2.waitKey()
            # 识别图像
            result = reader.readtext(image_barcode_region)
            for text in result:
                if len(text[1]) == 9:
                    barcode = text[1]
                    # barcode_characters = handle_replace(barcode[2:4])
                    # barcode = barcode[:2] + barcode_characters + barcode[4:]
                    barcode = barcode[:2] + 'BY' + barcode[4:]
                    os.rename(file_path, os.path.join(os.path.dirname(file_path), barcode + '.jpg'))


if __name__ == '__main__':
    dir_path = './images'
    delete_useless_images(dir_path)
    file_paths = [os.path.join(dir_path, file_path) for file_path in os.listdir(dir_path)]
    recognize_barcode_string(file_paths, 0.05, 0.15, 0.7, 1.0)