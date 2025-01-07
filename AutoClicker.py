import pyautogui
import time
import keyboard

delay = float(input("Enter the delay between clicks (in seconds): "))
print("Press 's' to start clicking and 'q' to stop.")

# Define the autoclicker function to accept a delay argument
def autoclicker(delay):
    while True:
        if keyboard.is_pressed('q'):  # Press 'q' to quit
            print("Autoclicker stopped.")
            break
        pyautogui.click()
        time.sleep(delay)  # Use the user-defined delay

if __name__ == "__main__":
    while True:
        if keyboard.is_pressed('s'):  # Press 's' to start
            try:
                print(f"Autoclicker started with a {delay}-second delay.")
                autoclicker(delay)
            except ValueError:
                print("Invalid input! Please enter a number.")
