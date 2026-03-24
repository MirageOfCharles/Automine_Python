import time
from pynput.mouse import Controller as MouseController, Button
from pynput.keyboard import Listener, KeyCode, Controller as KeyboardController, Key

mouse = MouseController()
keyboard = KeyboardController()

# State variable to track if we are currently mining
is_mining = False
toggle_key = KeyCode(char='m')

def on_press(key):
    global is_mining
    
    # Check if the pressed key is our toggle key ('m')
    if key == toggle_key:
        is_mining = not is_mining
        
        if is_mining:
            print("⛏️ Auto-miner ON: Walking, sneaking, and mining...")
            keyboard.press(Key.shift)  # Hold sneak
            keyboard.press('w')        # Hold walk forward
            mouse.press(Button.left)   # Hold left click to mine
        else:
            print("🛑 Auto-miner OFF: Releasing keys...")
            keyboard.release(Key.shift)
            keyboard.release('w')
            mouse.release(Button.left)

print("Minecraft Auto-Miner Script is running!")
print(" -> Press 'm' in-game to toggle ON/OFF.")
print(" -> Press Ctrl+C in this console window to completely exit.")

# Start listening to keyboard events globally
with Listener(on_press=on_press) as listener:
    listener.join()