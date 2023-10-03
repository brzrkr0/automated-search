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

time.sleep(5)

# List of search queries
queries1 = [
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
