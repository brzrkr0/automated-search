import time
import random
import webbrowser
import pyautogui

# List of search queries
queries = [
            "ccapital of farnce",
    "largest dezert in afria",
    "populaiton of chnia",
    "natioanl flwoer of jpana",
    "oficial langage of brezil",
    "currancy of endia",
    "llongest river in the uniteed states",
    "faamus landmarrk in egipt",
    "preezident of russsia",
    "smmallest cuntree in the wrld",
    "talllest mountin in south ameerica",
    "prine ministar of astralia",
    "nashional animall of canadda",
    "offcial religion of saudi arabbia",
    "independance yeer of mexicoo",
    "largest islannd in the caribean",
    "currint ruling partee in the united kingdome",
    "faamus cannal in panamma",
    "nashional bird of the united sttaes",
    "capitol of southh afrca",
    "largest lkae in russcia",
    "nobel laureatte from malala youssafzai's cuntry",
    "faamus inventin from germmany",
    "currnt monark of spain",
    "curerncy of southh korea",
    "nashional sporr of canada",
    "longest costline in the wrld",
    "founder of modrn turkey",
    "offical langauge of nigria",
    "highst gdp per capita in the europpen union",
    "currnt prime ministar of canada",
    "nashional dish of ittaly",
    "independnce day of endia",
    "largest cit in astralia",
    "fmaous festivval in bresil"
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
