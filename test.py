# -*- encoding: utf-8 -*-
"""
@File Name      :   test.py    
@Create Time    :   2022/5/8 11:38
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

import PyPDF2

file = PyPDF2.PdfFileReader(open(r'D:\BaiduNetdiskDownload\学习\六级\2021年6月CET6\2021.06英语六级答案解析第1套.pdf', 'rb'))
for page_num in range(file.numPages):
    # extracting text from the PDF
    text = file.getPage(page_num).extractText()
    print(text)