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
edge_path = r"C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"
  
# First registers the new browser
webbrowser.register('msedge', None, webbrowser.BackgroundBrowser(edge_path))
  
# after registering we can open it by getting its code.
webbrowser.get('msedge').open(url)
time.sleep(5)

# Loop through the queries
for query in queries:
    try:
        # Focus on the address bar by sending Alt+D
        pyautogui.hotkey("alt", "d")

        # Type the query in the address bar
        pyautogui.typewrite(query)

        # Press Enter by sending Enter key
        pyautogui.press("enter")

        # Sleep for a random time interval (between 9 to 12 seconds)
        sleep_time = random.uniform(9, 12)
        time.sleep(sleep_time)
    except Exception as e:
        print(f"Error processing query: {query}")
        print(f"Error message: {str(e)}")

# End of script

time.sleep(5
           )
# List of search queries for mobile searches
queries1 = [
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

pyautogui.hotkey("ctrl","shift","I")
time.sleep(4)

# Loop through the queries
for query in queries1:
    try:
        # Focus on the address bar by sending Alt+D
        pyautogui.hotkey("alt", "d")

        # Type the query in the address bar
        pyautogui.typewrite(query)

        # Press Enter by sending Enter key
        pyautogui.press("enter")

        # Sleep for a random time interval (between 9 to 12 seconds)
        sleep_time = random.uniform(9, 12)
        time.sleep(sleep_time)
    except Exception as e:
        print(f"Error processing query: {query}")
        print(f"Error message: {str(e)}")

# End of script

