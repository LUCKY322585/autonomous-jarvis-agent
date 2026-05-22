from core.speech import JarvisSpeech
from core.controller import JarvisController
import sys
import time

def run_autonomous_loop():
    # Primary pipeline execution loop for Jarvis system
    speech_system = JarvisSpeech()
    hardware_control = JarvisController()
    
    speech_system.speak("Autonomous Jarvis system core modules initialized successfully. Standing by for interface routing instructions.")
    
    while True:
        try:
            pulse_command = speech_system.listen()
            if not pulse_command:
                continue
            
            # Command routing matrix
            if "initialize browser" in pulse_command or "open google" in pulse_command:
                speech_system.speak("Executing local browser deployment protocols.")
                hardware_control.open_browser()
            elif "capture state" in pulse_command or "take screenshot" in pulse_command:
                speech_system.speak("Logging current desktop visualization frames.")
                hardware_control.capture_system_state()
            elif "terminal terminal" in pulse_command or "close window" in pulse_command:
                speech_system.speak("Terminating foreground active window pipeline.")
                # Alt + F4 mapping for Windows target platform
                hardware_control.trigger_hotkey('alt', 'f4')
            elif "shutdown routine" in pulse_command or "exit system" in pulse_command:
                speech_system.speak("De-energizing core agent runtime stacks. Goodbye.")
                sys.exit()
            else:
                print(f"Command '{pulse_command}' processed but no internal route matched.")
            time.sleep(1)
        except KeyboardInterrupt:
            print("\nManual override detected. Terminating Jarvis engine threads.")
            break
        except Exception as system_fault:
            print(f"Critical Runtime Exception: {system_fault}")
            time.sleep(2)

if __name__ == "__main__":
    run_autonomous_loop()
