""" I am going to use the keyboard module to listen for the key presses and then
use that to stop any ongoing loop. This will help on logging the errors safely and properly,
otherwise KeyboardInterrupt usually gives off a lot of garbage errors."""

import subprocess
import sys

subprocess.check_call([sys.executable, "-m", "pip", "install", "keyboard"], stdout=subprocess.DEVNULL,
                      stderr=subprocess.DEVNULL)
import keyboard
import queue

key_to_press = "esc"


def wait_for_key(e, keypress_queue):
    """
    This method is used to put the key in the queue if it is pressed.
    :param e: key pressed.
    :param keypress_queue: queue to put the key in.
    :return: queue with the bool if matches.
    """
    if e.name == key_to_press:
        keypress_queue.put(True)


key_queue = queue.Queue()
keyboard.on_press(lambda e: wait_for_key(e, key_queue))


def stop_key_listener():
    """
    This method is used to stop the key listener.
    :return: True if key is pressed, False otherwise.
    """
    if not key_queue.empty():
        print(f"{key_to_press} pressed. Stopping setup...")
        return True
    return False
