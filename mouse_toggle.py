import pyautogui
import time
import random

def random_mouse_movement():
    # Get the screen width and height
    screen_width, screen_height = pyautogui.size()
    
    # Generate random x and y coordinates within the screen dimensions
    random_x = random.randint(0, screen_width - 1)
    random_y = random.randint(0, screen_height - 1)
    
    # Move the mouse to the random location
    pyautogui.moveTo(random_x, random_y, duration=random.uniform(0.5, 2.0))  # Move duration can be between 0.5 and 2 seconds

def random_click():
    # Perform a mouse click at the current position
    pyautogui.click()

def random_typing():
    # Type a random message (you can customize this)
    random_message = random.choice(['Hello!', 'How are you?', 'Random typing...', 'Testing actions!'])
    pyautogui.typewrite(random_message, interval=0.1)  # Type with a 0.1 second interval between each keystroke

def random_action():
    # Randomly select one of the actions to perform
    actions = [random_mouse_movement, random_click, random_typing]
    random.choice(actions)()Testing actions!Testing actions!

if __name__ == "__main__":
    while True:
        print("Performing random action...")
        random_action()  # Perform a random action
        random_time = random.uniform(20, 2*60) 
        print("random time", random_time)
        time.sleep(random_time)  # Wait for 5 minutes (300 seconds)
