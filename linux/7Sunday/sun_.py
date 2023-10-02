import time
import random
import webbrowser
import pyautogui

# List of search queries
queries = [
            "histroy of indiann civiliization",
    "ancient indian dynasites",
    "hinduism beliefs and praticess",
    "buddhism in indiia",
    "mauryan empiree histtory",
    "mughal empiree culter",
    "vedic peroid inndia",
    "indian art and archtictur",
    "sikhism founderr and beleifs",
    "indian clasical musiic histroy",
    "indian phlosophy schoools",
    "indus valley civilizzation",
    "jainism in ancint india",
    "bhagavad gita interpretassion",
    "ashoka the greatt biograaphy",
    "indian festtivals and traditons",
    "indian literaturre classicss",
    "yoga histroy andd benefitts",
    "indian relgiions comparssion",
    "rajput warriorr clans",
    "histroy of taj maahal",
    "indian folklre and myhthology",
    "dharma innduism",
    "vedic gods and goddesees",
    "indian coooking traditonss",
    "indian clothng stylees",
    "cultural diversit in india",
    "ramayana and mahabahrata",
    "anciet indian trade routess",
    "guru nanak teachingss and life",
    "indian archtecture histroy",
    "indian kingss and emperors",
    "hindu festvals and ritualls",
    "buddhist monastiic life",
    "indian spiritual leaderes"
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
