from pynput.keyboard import Key, Controller as KeyboardController, Listener
import pyautogui
import time
import threading
import random
import os

# Create a keyboard controller object
keyboard = KeyboardController()

# Use a lock to control access to actions more precisely
action_lock = threading.Lock()

# Global variable to keep track of whether the script is waiting or not
waiting = False

def on_press(key):
    if key == Key.delete:  # Check if the pressed key is Delete
        print("✅ Script stopped")
        os._exit(1)  # Stop the script immediately

def right_click_loop():
    while True:
        if not waiting:  # Check if the script is waiting before performing cursor movement and right-click
            # Random cursor movement
            x_move = random.randint(-50, 50)
            y_move = random.randint(-50, 50)
            pyautogui.move(x_move, y_move, duration=0.1)

            with action_lock:
                print("👉 Perform right click")
                pyautogui.mouseDown(button='right')
                pyautogui.mouseUp(button='right')


def search_bar_element_action():
    max_attempts = 5
    attempts = 0
    while attempts < max_attempts:
        try:
            time.sleep(1)  # Add a small delay
            search_bar_element_location = pyautogui.locateCenterOnScreen('elements/search_bar.png', confidence=0.7) 
            if search_bar_element_location is not None:
                print("✅ Search bar element found!")
                # Move the cursor to the center of the search_bar_element element
                pyautogui.moveTo(search_bar_element_location)
                # Move the cursor down 200 pixels
                pyautogui.moveRel(0, 200)
                # Perform a right-click
                pyautogui.mouseDown(button='right')
                pyautogui.mouseUp(button='right')
                print("👉 Buy items")
                time.sleep(1)
                pyautogui.mouseDown(button='right')
                pyautogui.mouseUp(button='right')
                time.sleep(1)
                pyautogui.mouseDown(button='right')
                pyautogui.mouseUp(button='right')
                time.sleep(1)
                pyautogui.moveRel(500, -100)
                break
            else:
                print(f"❌ Search bar element not found (attempt {attempts+1}/{max_attempts})")
        except pyautogui.ImageNotFoundException:
            print(f"❌ Search bar element not found (attempt {attempts+1}/{max_attempts})")
        except Exception as e:
            print(f"⛔ An exception occurred while trying to find the search_bar_element (attempt {attempts+1}/{max_attempts}): {e}")
        attempts += 1
        time.sleep(1)




def check_for_death_recap_element():
    global waiting
    death_recap_element_location = None

    try:
        death_recap_element_location = pyautogui.locateOnScreen('elements/dead.png', confidence=0.7)
        if death_recap_element_location is not None:
            print("✅ Death recap element found!")
            time.sleep(1)
            keyboard.press('p')
            keyboard.release('p')
            print("👉 Press P")
            waiting = True
            print("⏳ Waiting set to True: Preparing to interact with the search bar element after death recap detected.")

            search_bar_element_action()

            time.sleep(20)
            keyboard.press('p')
            keyboard.release('p')
            print("👉 Press P")
            waiting = False
            print("✅ Waiting set to False: Completed interaction with search bar element after death recap.")
            while True:
                check_for_death_recap_element()
                time.sleep(1)
        else:
            time.sleep(1)
            print('🔍 Look for death_recap_element')
    except pyautogui.ImageNotFoundException:
        print("⛔ PyAutoGUI couldn't find the death recap.")
        time.sleep(5)
    except Exception as e:
        print(f"⛔ An exception occurred while trying to find the button image: {e}")
        time.sleep(1)

def check_for_death_recap_element_loop():
    while True:
        check_for_death_recap_element()
        time.sleep(1)


def check_for_afk_button():
    try:
        afk_button_location = pyautogui.locateOnScreen('elements/afk.png', confidence=0.7)
        if afk_button_location is not None:
            print("✅ AFK button found!")
            pyautogui.click(afk_button_location)
            print("👉 Press OK")
    except pyautogui.ImageNotFoundException:
        print("⛔ PyAutoGUI couldn't find the AFK statement.")
    except Exception as e:
        print(f"⛔ An exception occurred while trying to find the button image: {e}")

def check_for_afk_button_loop():
    while True:
        check_for_afk_button()
        time.sleep(45)

def center_cursor_on_image():
    try:
        image_location = pyautogui.locateCenterOnScreen('elements/pseudo.png', confidence=0.8)
        if image_location is not None:
            print("✅ Pseudo found!")
            pyautogui.moveTo(image_location)
            print("✅ Cursor centered on the image")
            pyautogui.moveRel(200, 0)
        else:
            print("❌ Image not found")
    except pyautogui.ImageNotFoundException:
        print("⛔ PyAutoGUI couldn't find the pseudo.")
    except Exception as e:
        print(f"⛔ An exception occurred while trying to find the image: {e}")

def perform_action(action, delay):
    with action_lock:  # Acquire the lock for this action
        if not waiting:
            if action in ['ctrl_a', 'ctrl_z', 'ctrl_e', 'ctrl_r', 'c', 'v']:
                if action.startswith('ctrl_'):
                    # Handle key combinations like Ctrl+A
                    key = action.split('_')[1]
                    print(f"⬆️ Press Ctrl+{key.upper()}")
                    keyboard.press(Key.ctrl)
                    keyboard.press(key)
                    keyboard.release(key)
                    keyboard.release(Key.ctrl)
                else:
                    print(f"👉 Press {action.upper()}")
                    keyboard.press(action)
                    keyboard.release(action)
            elif action == 't_click':
                print("👍 Perform thumbs up")
                keyboard.press('t')
                keyboard.release('t')
                time.sleep(0.5)
                pyautogui.mouseDown(button='left')
                time.sleep(0.1)
                pyautogui.mouseUp(button='left')
            elif action == 'perform_combo':
                perform_chat_combo()
            else:
                print(f"👉 Press {action.upper()}")
                keyboard.press(action)
                keyboard.release(action)
            time.sleep(delay)

messages = [
    "ez",
    "gg",
    "weeeeeeee",
    "gj",
    "comon bro"
]

def perform_chat_combo():
    selected_message = random.choice(messages)
    print(f"😂 Write '{selected_message}' in the chat")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.5)

    for char in selected_message:
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.1)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def perform_actions_sequentially():
    while True:
        actions = [
        ('t_click', 3),
        ('ctrl_e', 2),
        ('a', 2),
        ('ctrl_a', 2),
        ('ctrl_z', 2),
        ('e', 2),
        ('ctrl_r', 2),
        ('w', 2),
        ('t_click', 3),
        ('center_cursor', 3),
        ('ctrl_e', 2),
        ('a', 2),
        ('ctrl_a', 2),
        ('r', 2),
        ('perform_combo', 2.5),
        ('ctrl_z', 2),
        ('e', 2),
        ('v', 2),
        ('v', 2),
        ('ctrl_r', 2),
        ('w', 2),
        ('t_click', 3),
        ('center_cursor', 3),
        ('ctrl_e', 2),
        ('a', 2),
        ('ctrl_a', 2),
        ('r', 2),
        ('perform_combo', 2.5),
        ('ctrl_z', 2),
        ('e', 2),
        ('c', 2),
        ('ctrl_r', 2),
        ('center_cursor', 3),
        ('w', 2),
        ('t_click', 3),
        ('ctrl_e', 2),
        ('a', 2),
        ('ctrl_a', 2),
        ('r', 2),
        ('perform_combo', 2.5),
        ('ctrl_z', 2),
        ('e', 2),
        ('ctrl_r', 2),
        ('center_cursor', 3),
        ('w', 2),
        ('v', 2),
        ('v', 2),
        ('t_click', 3),
        ('ctrl_e', 2),
        ('center_cursor', 3),
        ('a', 2),
        ('ctrl_a', 2),
        ('ctrl_z', 2),
        ('e', 2),
        ('c', 2),
        ('ctrl_r', 2),
        ('center_cursor', 3),
        ('w', 2),
        ('t_click', 3),
        ('ctrl_e', 2),
        ('a', 2),
        ('ctrl_a', 2),
        ('perform_combo', 2.5),
        ('ctrl_z', 2),
        ('center_cursor', 3),
        ('e', 2),
        ('v', 2),
        ('v', 2),
        ('ctrl_r', 2),
        ('w', 2),
        ('t_click', 3),
        ('ctrl_e', 2),
        ('center_cursor', 3),
        ('a', 2),
        ('ctrl_a', 2),
        ('r', 2),
        ('ctrl_z', 2),
        ('e', 2),
        ('c', 2),
        ('ctrl_r', 2),
        ('center_cursor', 3),
        ('w', 2),
        ('t_click', 3),
        ('ctrl_e', 2),
        ('a', 2),
        ('ctrl_a', 2),
        ('r', 2),
        ('perform_combo', 2.5),
        ('center_cursor', 3),
        ('ctrl_z', 2),
        ('e', 2),
        ('ctrl_r', 2),
        ('w', 2),
        ('center_cursor', 3),
        ('v', 2),
        ('v', 2),
        ('t_click', 3),
        ('ctrl_e', 2),
        ('a', 2),
        ('ctrl_a', 2),
        ('center_cursor', 3),
        ('r', 2),
        ('perform_combo', 2.5),
        ('ctrl_z', 2),
        ('e', 2),
        ('c', 2),
        ('ctrl_r', 2),
        ('w', 2),
        ('center_cursor', 3)
        ]

        for action, delay in actions:
            if action == 'center_cursor':
                center_cursor_on_image()
            else:
                perform_action(action, delay)

listener = Listener(on_press=on_press)
listener.start()

time.sleep(5)  # Wait a bit before starting

keyboard.press('p')
keyboard.release('p')
print("👉 Press P")

search_bar_element_action()

keyboard.press('p')
keyboard.release('p')
print("👉 Press P")

keyboard.press('y')

# Start the thread for right clicks
threading.Thread(target=right_click_loop, daemon=True).start()

# Start the thread for checking for the element
threading.Thread(target=check_for_death_recap_element_loop, daemon=True).start()

# Start the thread for checking for the AFK button
threading.Thread(target=check_for_afk_button_loop, daemon=True).start()

# Call the function to perform the main actions in an infinite loop
perform_actions_sequentially()
