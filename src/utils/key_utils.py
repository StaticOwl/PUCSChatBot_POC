import keyboard
import queue
import threading

key_to_press = "esc"

def wait_for_key(e, key_queue):
    if e.name == key_to_press:
        key_queue.put(True)

key_queue = queue.Queue()
keyboard.on_press(lambda e: wait_for_key(e, key_queue))

def stop_key_listener():
    if not key_queue.empty():
        print(f"{key_to_press} pressed. Stopping setup...")
        return True
    return False