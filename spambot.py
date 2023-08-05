import pywhatkit, win32clipboard
# import pyautogui, webbrowser, pyperclip
# from time import sleep

with open('numbers.txt') as f:
    lines = f.read().replace(" ", "").strip().split(',')

phoneNumbers = ["+54" + str(number) for number in lines]

final = list(set(phoneNumbers))

msg = 'hola esto es una prueba :^]'

for number in final:
    pywhatkit.sendwhatmsg_instantly(number, msg, 10, True, 3)
