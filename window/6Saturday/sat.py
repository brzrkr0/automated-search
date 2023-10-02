import time
import random
import webbrowser
import pyautogui

# List of search queries
queries = [
    "evnts in the histoy of the Unted Sttes durin the Amercan Revlution",
    "Britsh Empir influenc Indias hstory",
    "contribtions of the Otmn Empr to wrld histroy",
    "develpmnts durin the Meji Rstoration in Japn",
    "Frnch Revluton imapct the histry of France and the wrld",
    "key momnts in the hstory of ancent Grec",
    "Rusian Empir expand its terrtory ovr the centries",
    "causs and consqunces of the Spansh coloniztion of Latin Amerca",
    "Mng Dynsty contrbute to Chnas cultral and histricl legcy",
    "signficnt evnts in the hstry of ancent Rom",
    "Vking Age influnce the hstry of Scndnavia and Europ",
    "majr achevements of the Gupt Empir in India",
    "Sil Road contrbut to the exchage of ide and cltures in hstry",
    "major develpmnts durin the Renasance periode in Itly",
    "Mongl Emire shap the histry of Eursia",
    "key evnts in the hstry of Suth Afrca, includding aprtheid and its end",
    "Inca Empie rse and fal in Suth America",
    "majr contibutions of ancent Mesoatamia to humn civiliztion",
    "Byzanine Empre impct the hstory of the Estrn Mediterranen",
    "caus and efects of the Mexcan War of Indepednce",
    "histroy of Austrla unfolde, incluing clonization and indigneus peoles' expriences",
    "signifcant evnts in the histry of ancent Egpt, incluing the constructn of the pyrmids,


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
