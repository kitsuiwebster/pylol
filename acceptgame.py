import pyautogui
import time

def click_accept_button():
    accept_button_location = None
    attempts = 0
    found_count = 0

    print('👉 The script has started.')
    print('👉 The script is now looking for the button image on the screen.')
    while found_count < 999:
        while accept_button_location is None:
            try:
                accept_button_location = pyautogui.locateOnScreen('elements/accept.png', confidence=0.7)
                if accept_button_location is not None:
                    print("✅ The button image has been found on the screen!")
                    time.sleep(1)
                    accept_button_center = pyautogui.center(accept_button_location)
                    print("👉 The script is now calculating the center of the button image.")
                    pyautogui.click(accept_button_center)
                    print("✅ The script has clicked the button image!")
                    found_count += 1
                    break
                else:
                    print(f"👉 Attempt {attempts}")
                    time.sleep(1)
                    attempts += 1
            except pyautogui.ImageNotFoundException:
                print(f"👉 Attempt {attempts}")
                time.sleep(1)
                attempts += 1
            except Exception as e:
                print(f"⛔ An exception occurred while trying to find the button image: {e}")
                time.sleep(1)
                attempts += 1
        if found_count < 3:
            print(f"✅ The button image has been found {found_count} time(s) so far.")
            print("👉 Retrying in 5 seconds in case someone did not accept the game.")
            print("🎮 Good game and do not forget to report the jungler !")
            time.sleep(5)
            accept_button_location = None

    print('🎮 Good Game! The script is now exiting...')
    time.sleep(5)
    exit()

click_accept_button()
