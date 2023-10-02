import time
import random
import webbrowser
import pyautogui

# List of search queries
queries = [
    "populartiy of faecbook"
    "prime minster of canad"
    "nashnal animal of astralia"
    "biggest city in inda"
    "officail langage of germay"
    "currncy of jamaika"
    "curent monrch of swden"
    "famous explorer from portugall"
    "nashional sport of brazill"
    "tallest bilding in the wrld"
    "presdent of south africa"
    "independnce day of frnace"
    "capitol of thailnd"
    "largst river in canad"
    "currnt king of norwya"
    "nashnal emblm of spain"
    "offical religon of iran"
    "famouz painting by Italin artist"
    "highest moutain in afrika"
    "founding fther of the Unted States"
    "Nobell laurate from Inda"
    "nashional dish of mexio"
]

# Open the web browser and navigate to Bing
# then make a url variable
url = "https://www.bing.com/#!"
  
# getting path
edge_path = r"/opt/microsoft/msedge/microsoft-edge"
  
# First registers the new browser
webbrowser.register('msedge', None, webbrowser.BackgroundBrowser(edge_path))
  
# after registering we can open it by getting its code.
webbrowser.get('msedge').open(url)
time.sleep(5)

pyautogui.hotkey("ctrl","shift","I")
time.sleep(4)

# Loop through the queries
for query in queries:
    try:
        # Focus on the address bar by sending Alt+D
        pyautogui.hotkey("alt", "d")

        # Type the query in the address bar
        pyautogui.typewrite(query)

        # Press Enter by sending Enter key
        pyautogui.press("enter")

        # Sleep for a random time interval (between 4 to 8 seconds)
        sleep_time = random.uniform(6, 10)
        time.sleep(sleep_time)
    except Exception as e:
        print(f"Error processing query: {query}")
        print(f"Error message: {str(e)}")

# End of script
