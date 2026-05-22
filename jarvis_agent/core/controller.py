import pyautogui
import time
import subprocess
import os

class JarvisController:
    def __init__(self):
        # Safety margin for GUI operations
        pyautogui.FAILSAFE = True
        pyautogui.PAUSE = 0.5
    
    def open_browser(self):
        # Launches default web browser on local OS environment
        print("Executing workspace terminal command: Open Browser")
        if os.name == 'nt': # For Windows systems
            subprocess.Popen(['start', 'chrome'], shell=True)
        else: # For Linux/macOS standard systems
            subprocess.Popen(['xdg-open', 'https://google.com'])
        time.sleep(2)
    
    def trigger_hotkey(self, key1, key2=None):
        # Handles low-level OS GUI key mappings
        if key2:
            pyautogui.hotkey(key1, key2)
        else:
            pyautogui.press(key1)
    
    def write_text(self, text_content):
        # Automates text field injection
        pyautogui.write(text_content, interval=0.05)
        pyautogui.press('enter')
    
    def capture_system_state(self):
        # Local system screenshot logs
        timestamp = int(time.time())
        screenshot_path = f"system_state_{timestamp}.png"
        screenshot = pyautogui.screenshot()
        screenshot.save(screenshot_path)
        print(f"System architecture state captured: {screenshot_path}")
