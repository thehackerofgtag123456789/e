import socket
import pyautogui
import time
import subprocess
import threading

class YouTubeBotMac:
    def __init__(self):
        # The channel you want to visit
        self.url = "https://www.youtube.com/@TTSD3XXY"
        
        # JS to click the Subscribe button on the page
        self.js_commands = [
            'var subBtn = document.querySelector("ytd-subscribe-button-renderer button"); if(subBtn) subBtn.click();',
            'var bellBtn = document.querySelector("ytd-subscription-notification-toggle-button-renderer button"); if(bellBtn) bellBtn.click();'
        ]

        # macOS Launch commands and DevTools shortcuts
        # Chrome: Cmd+Option+J | Safari: Cmd+Option+C
        self.browsers = {
            'Google Chrome': {'cmd': f'open -a "Google Chrome" {self.url}', 'key': 'j'},
            'Safari': {'cmd': f'open -a "Safari" {self.url}', 'key': 'c'}
        }

        self.wait_time = 5  # Seconds to wait for the page to load
        self.running = True

    def is_connected(self):
        try:
            socket.create_connection(("8.8.8.8", 53), timeout=3)
            return True
        except OSError:
            return False

    def run_bot(self):
        print(f"Bot started for {self.url} on macOS.")
        
        while self.running:
            if self.is_connected():
                for name, info in self.browsers.items():
                    print(f"Launching {name}...")
                    
                    # Launching with macOS 'open' command
                    subprocess.Popen(info['cmd'], shell=True)

                    # WAIT for the page to load
                    time.sleep(self.wait_time)

                    # macOS shortcut: Command + Option + Key
                    pyautogui.hotkey('command', 'option', info['key'])
                    time.sleep(2)

                    # Typing the code into the console
                    for cmd in self.js_commands:
                        pyautogui.write(cmd, interval=0.01)
                        pyautogui.press('enter')
                        time.sleep(1)

                    print(f"Task done in {name}.")
                    
                self.running = False # Stops after one run through the browsers
            else:
                print("No internet. Retrying in 5 seconds...")
                time.sleep(5)

if __name__ == "__main__":
    bot = YouTubeBotMac()
    bot.run_bot()
