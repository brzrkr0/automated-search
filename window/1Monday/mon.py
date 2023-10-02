import time
import random
import webbrowser
import pyautogui

# List of search queries
queries = [    "historey of the Unted States in the 18th centry",
    "maor world wars and thier impact on societey",
    "influentl politcal fgrues of the 20th centery",
    "impac of the Industrail Revolution on workng conditins",
    "key evnts of the civil rigths movemet in the USA",
    "cultural difrences in East and Westrn societies",
    "economc princples of market and commnd economis",
    "globalizaton and its affect on locl communites",
    "role of gvernment in providig public servcies",
    "enviromental consrvation and sustinabilty effrots",
    "influentl philosphers of the Enlghtenment perod",
    "impct of colnialsm on Africn nations",
    "womn's suffrage movemet and its laders",
    "origins and deelopment of major world rligions",
    "migraton paterns and urbaniztion trnds",
    "impact of mass media on poltical opnions",
    "worldwide effrts to combat povrty and inequity",
    "geopolitical conflcts in the Midle East regin",
    "cultural difrences betwen Eastern and Western hritage",
    "historey of the European Union and its chalenges",
    "impact of the Industrail Revolutin on socety",
    "evolution of legal sysm and human rights"
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
