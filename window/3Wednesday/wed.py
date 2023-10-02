import time
import random
import webbrowser
import pyautogui

# List of search queries
queries = [
            "traveling on a student budjet",
    "exploring beutiful beeches in thailand",
    "passport requirments for europe travel",
    "must-see attraactions in rome, italy",
    "how to find budget-friendly hotls in paris, france",
    "adventure travel destnations in south africa",
    "family-friendly activitis in orlndo, florida",
    "culturally rich experinces in mexico",
    "what to pack for a beech vacation",
    "best time to visit new zealad",
    "exotic food in southeast asia",
    "travelng with pets internationly",
    "intresting musuems in lndon, england",
    "backpacking trips in the rockis",
    "vacation rental optins in thailand",
    "natural beuty of costa rca",
    "planing an eco-frendly trip",
    "amazing skiing destnations in switzerland",
    "romantic getaways in prague, czech republc",
    "unique shoping experinces in tokyo, japan",
    "solo travel saftey tips",
    "cultural festvals in moroco"
]

# Open the web browser and navigate to Bing
# then make a url variable
url = "https://www.bing.com/#!"
  
# getting path
edge_path = r"C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"
  
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
