import pyautogui
from time import sleep

time = 0
while time != 10:
    time += 1
    print("DcSpammer waiting... " + str(time))


def spam(msg, maxMsg):
    count = 0
    while count != maxMsg:
        count += 1
        print("Send message: " + str(count))
        pyautogui.write(msg)
        pyautogui.press("enter")
        if count == 5 or count == 5 * 2 or count == 5 * 3:
            sleep(8)


spam("Rotta", 20)
