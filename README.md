This application utilizes the pynput library to track keystrokes and store them to a log file. First, ensure that you have the pynput library installed. You may install it via pip.To achieve this, run the following command in your VS Code terminal:

pip install pynput

After installing the library, you can execute the code. It will begin recording your keystrokes and saving them to a file called 'keylog.txt' in the same directory as the Python script.

A function named on_press that is triggered whenever a key is pressed. The function does the following:
Try Block: Attempts to get the character representation of the key using key.char. If successful, it writes the character along with a timestamp to the file keylog.txt.
Except Block: If an AttributeError occurs (which happens when the key pressed is a special key like Shift, Enter, or Ctrl), it writes the name of the special key in a bracketed format (e.g., [Key.shift]) along with the timestamp to the file.

 A function named on_release that is triggered whenever a key is released. The function checks if the key released is the ESC key. If it is, the function returns False, which stops the listener and ends the keylogging session. This provides a way to gracefully exit the program.

 It handles both regular and special keys, and it continues running until the ESC key is pressed, at which point it stops the keylogger and closes the log file. The use of the time module allows for accurate tracking of when each key was pressed, and the file handling is optimized to keep the log file open during the entire session.






