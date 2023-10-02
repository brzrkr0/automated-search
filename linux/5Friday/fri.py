import time
import random
import webbrowser
import pyautogui

# List of search queries
queries = [
        "who sculped the venus de miloo",
    "wat is the importence of the reformattion movemant in histery",
    "describ the architctural styl of the partinon in athns, greee",
    "who pionerd the cubism art movemnt, and what were its charactristics",
    "explan the concept of 'abstrak expresionism' in modrn artt",
    "who painted the famus artwork 'guernca,' and what dose it depct",
    "wat is the differnce between clasical and romantc musc",
    "how did the inventon of the printng pres revoluzionize comunication",
    "who ar some influencial femal scienstists in the feeld of physsics",
    "describ the impct of the Civil Rights Act of 1964 on Amercan socity",
    "wat rol did the Spaace Race play in the Cold War rivalry between the U.S. and the Soviet Union",
    "who wer the key leders in the women's suffrag movment",
    "explan the concpt of 'culturall relativism' in anthropolgy",
    "wat ar the major theems in the novels of Jane Austen",
    "describ the architctural inovations of Frank Lloyd Wrightt",
    "who composd the 'Ode to Joy,' and what is its signifcance",
    "wat were the consekwnces of the Industril Revoluton on urbanizaton",
    "who wer the majer playrs in the Apollo 11 moon landng misson",
    "explan the princples of Freuddian psychoanalisis",
    "wat is the signifcance of the Magna Cart in the histroy of legal rits",
    "describ the ecolgical impct of deforsttion in the Amazn rainforst",
    "who ar some notabl contemprary artists knwn for their instllations and mixd media artt"
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
