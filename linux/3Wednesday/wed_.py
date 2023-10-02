import time
import random
import webbrowser
import pyautogui

# List of search queries
queries = [
        "best trravel destinations in euurop",
    "visa requirements for travling to japn",
    "affordabl vacation spot in asia",
    "top 10 thngs to do in paris, francce",
    "how to find cheep flights to thialand",
    "cultral festivlas in india",
    "travel safty tips for solo female travlers",
    "best time to visist the maldives",
    "what to pac for a trip to south ameirca",
    "currency exchnage rates in south africa",
    "travel vaccnations for southeast asia",
    "is it safe to trael to egyypt?",
    "budgget travel tips for backpacking thru europe",
    "populr street foods in mexico city",
    "how to plan a famly vacation to disny world",
    "hikng trails in new zeland",
    "luxury resorts in the caribean",
    "travel insuranc for internationl trips",
    "voluntter opoortunities abroad",
    "cruise vacatons in the mediteranean",
    "culturall etiquete in japan",
    "best beches in austrailia",
    "what to see in rome, itly",
    "adventre travel destinatoins in south ameerica",
    "travelinng with pets internationlly",
    "langage learning apps for traelers",
    "scenic trane routes in switzrland",
    "travelin on a studnt budget",
    "overcomng jet lag tips",
    "solo travel adventres in southest asia",
    "top wildife safari destinatons in africa",
    "cultral expreiences in moroco",
    "how to plan a road trip thru the usa",
    "expat comunities in spain",
    "travel photograhy tips for begnners"
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
