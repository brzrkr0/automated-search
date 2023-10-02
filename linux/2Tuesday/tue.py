import time
import random
import webbrowser
import pyautogui

# List of search queries
queries = [
        "explore the histree of apart-hide in Sout Aferica",
    "ases the impact of globlizzation on indiginous culturs",
    "investegate the orgens of the United Nations",
    "discus the relatonship betwen religon and poltickz",
    "exlor the histry of the women's suffrag movemnt",
    "analize the consqunces of imperializm in Asa",
    "discus the role of socil media in modrn poltics",
    "examin the cultural signifikance of traditonl clothng",
    "evalut the efcts of economik ineqality on sociaty",
    "anlyze the impact of tehnological advancemnts",
    "exmine the roel of eductaion in shaping societiz",
    "discus the chalenges of sustaianable develoopment",
    "explore the historey of spaice explorashion",
    "evalute the role of art in cultral exprssion",
    "anlyze the efects of globbaliztion on the enviroment",
    "discus the relashunship betwen sciens and ethix",
    "explor the histary of sientific disqoveries",
    "examien the roel of inovation in ecnomik groth",
    "evalute the impack of socil meida on intrprsonal relashnships",
    "analize the efects of clmat change on boidiversity",
    "discus the roel of wmen in STEM feilds",
    "explore the historey of revolutins in Latn Amerika"
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
