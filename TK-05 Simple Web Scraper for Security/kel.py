import keyboard
def on_key_event(Keyboard_event):
    if Keyboard_event.event_type==keyboard.KEY_DOWN:
        print(Keyboard_event.name)
keyboard.hook(on_key_event)
keyboard.wait('esc')     