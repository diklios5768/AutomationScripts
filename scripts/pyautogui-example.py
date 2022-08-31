import time
import pyautogui
import pyperclip

students = [('211003044', '孙浩钧', '19990203'),
            ('211003045', '姚因', '19990303')]
with open('students.txt', 'r') as f:
    text = f.read()
    students = [student.split(',') for student in text.split('\n')]
students = students[:10]
print(students)
# # 获取当前屏幕分辨率
# screenWidth, screenHeight = pyautogui.size()

# # 获取当前鼠标位置
# currentMouseX, currentMouseY = pyautogui.position()
copy_success=False
clipboard_text=''
for student_number, name, birthday in students:
    start = time.time()
    # 移动到+按钮
    #pyautogui.moveTo(x=389, y=201,duration=1, tween=pyautogui.linear)
    pyautogui.moveTo(x=1630, y=504, duration=0.5, tween=pyautogui.linear)

    # time.sleep(2)
    # 按下+号
    #pyautogui.click(x=390, y=205,button='left',tween=pyautogui.linear)
    pyautogui.click()
    # pyautogui.click()

    # 移动到id框
    pyautogui.moveTo(x=700, y=215, duration=0.5, tween=pyautogui.linear)

    # 点击id框
    pyautogui.click()

    # 输入学号
    # pyautogui.typewrite(message='211003044',interval=0.1)
    while clipboard_text!=student_number:
        pyperclip.copy(student_number)
        pyautogui.hotkey('ctrl', 'v')
        pyperclip.copy('')
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'c')
        clipboard_text=pyperclip.paste()

    # 移动到姓名框
    pyautogui.moveTo(x=700, y=250, duration=0.5, tween=pyautogui.linear)

    # 点击姓名框
    pyautogui.click()

    # 输入姓名
    # pyautogui.typewrite(message='sunhaojun',interval=0.1)
    # pyperclip.copy(name)
    # pyautogui.hotkey('ctrl', 'v')
    while clipboard_text!=name:
        pyperclip.copy(name)
        pyautogui.hotkey('ctrl', 'v')
        pyperclip.copy('')
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'c')
        clipboard_text=pyperclip.paste()

    # 移动到出生日期框
    pyautogui.moveTo(x=700, y=325, duration=0.5, tween=pyautogui.linear)

    # 点击出生日期框
    pyautogui.click()

    # 输入出生日期
    # pyautogui.typewrite(message='19990203',interval=0.1)
    # pyperclip.copy(birthday)
    # pyautogui.hotkey('ctrl', 'v')
    while clipboard_text!=birthday:
        pyperclip.copy(birthday)
        pyautogui.hotkey('ctrl', 'v')
        pyperclip.copy('')
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'c')
        clipboard_text=pyperclip.paste()

    # 移动到save按钮
    pyautogui.moveTo(x=1770, y=505, duration=0.5, tween=pyautogui.linear)

    # 按下save按钮
    pyautogui.click()

    # 等待一秒钟让界面反应
    time.sleep(0.5)
    print(time.time()-start)
