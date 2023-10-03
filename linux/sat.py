import time
import random
import webbrowser
import pyautogui

# List of search queries
queries = [
        "main events in the history of the united states during the american revloution",
    "how did the british emprie influenc indias history",
    "major contributons of the ottoman emmpire to world history",
    "key devolpments during the meji restoration in japan",
    "how did the french revloution impact the history of frnace and the world",
    "key momments in the history of ancient greeece",
    "how did the russian empirre expand its teritory over the centuries",
    "casues and consequences of the spanish colonizaion of latin amerca",
    "how did the ming dynasti contribute to chinas cultral and historial legacy",
    "signifcant events in the history of ancient rom",
    "how did the viking age influene the history of scadinavia and europe",
    "major acheivements of the gupta empir in india",
    "how did the silk raod contrbute to the exchange of ideass and cultrues in histor",
    "major devlopments during the renaissnace peroid in itly",
    "how did the mongol empiire shape the history of euraisa",
    "key evnts in the history of south afrcia including aparteid and its end",
    "how did the inca empir rise and fall in south amercia",
    "major contrbutions of acient mesopotamia to humn civilzation",
    "how did the byzantine emprie impact the history of the estern mediterranen",
    "casues and effects of the mexican war of indepndence",
    "how did the history of austalia unfold incluing coloniztion and indiginous peoples experinces",
    "signficant evnts in the history of acient egyt incluing the constrction of the pyramds",
    "how did the history of vietnam involve resistnce against foregin powers like france and the united states",
    "major develoments during the hein peroid in japnese history",
    "how did the history of grece include the persan wars and the pelopnnesian war",
    "key momnts in the history of the byzantine emprie includng justinians reign",
    "how did the spanish conqistadors impact the history of centrl and south america",
    "contrbutions of the maurya empie to acient indias history",
    "how did the history of the caribbean involve europeen coloniztion and the transatlntic slave trade",
    "major achevements of the abbasid caliphte in the islamic worlds history",
    "how did the history of canaa include interacions between indiginous peple and european setlers",
    "signficant evnts in the history of acient persia includng the achaemenid emprie",
    "how did the history of etiopia include erly christian influenes and resistnce against colonialsm",
    "key devlopments in the history of acient maya civiliztion in mesoamercia",
    "how did the history of new zealand involve the treat of waitangi and its implcations for indiginous rights"


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
    "signifcant evnts in the histry of ancent Egpt, incluing the constructn of the pyrmids"


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
