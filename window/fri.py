import time
import random
import webbrowser
import pyautogui

# List of search queries
queries = [
                "who paentd the mona lissaa",
    "wat is the signifikance of the impreshonist art movemant",
    "descrybe the styl of vincent van goghs paintinsg",
    "wat is abstrakt art, and who r some famus abstract artistss",
    "explane the conceprt of 'renaisance art'",
    "who is the artist behind the famouss painting 'stary nighht'",
    "wat is the diffrence between baroq and rococo artt",
    "how did the inventon of fotography impact the artt wrld",
    "who ar some renwnd female artist throughout histroy",
    "wat is the purpuse of performanc artt",
    "describ the artistik contributons of the surrealist movemntt",
    "wat is the signifikance of the cave painitngs in laskaouxx, frnce",
    "who designd the iffel tower, and when was it constrcted",
    "discuss the influnce of african artt on modrn western artt",
    "explane the concpt of 'pop artt' and nam som key artist asocated with itt",
    "describ the causes and consquences of the french revoluton",
    "who wr the ancent mayns, and wat wr their majr achievemnts",
    "wat rol did the silk rode play in ancent trad and cultural exchnge",
    "explane the impct of the indstrial revoluton on socity and economyy",
    "discuss the evnts and outcmes of the american civil wr",
    "who wr the key figures in the civil rights movemnt in the unitd states",
    "describ the signifikance of the berln wall in the cold wr era",
    "wat wr the majr consqunces of world wr I",
    "explane the concpt of 'manifst destiny' in amerian histroy",
    "discuss the rise and fal of the roman empiire",
    "who was nelson mandela, and wat rol did he play in south afrcan histroy",
    "describ the signifikance of the cuban misil crisis during the cold wr",
    "wat wr the main causess of the great deprssion in the 1930s",
    "discuss the impct of the renaissnce on europen cultre and socityy",
    "who wr the vikngs, and wat wr their contributons to histroy",
    "explan the imporance of the magna carta in the developmnt of constitutonal law",
    "wat was the signifikance of the ancent city of troyy",
    "describ the culturl traditons of the indigennous peple of australiia",
    "wat ar some traditonal japans tea ceremny custms",
    "explane the concpt of 'culturl apropriation' and its contrversies in modrn socityy"
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
