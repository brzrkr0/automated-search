import time
import random
import webbrowser
import pyautogui

# List of search queries
queries = [
            "bset Python libraris for dat vizualisatoin",
    "optmize SQL quereis for perfomrance",
    "Reatc vs. Agnular cmparison",
    "latets JavaScipt framewok 2023",
    "implemnt OAuth 2.0 ina Node.js aplication",
    "desin paterns for microservie archtectrue",
    "top clud providers for hostng web aplicatons",
    "best practces for securig REST APIs",
    "deploya Flsk aplcation on AWS",
    "GitHb Actons vs. Jenkin fr CI/CD",
    "intorduction to GrphQL and its advantge",
    "use Dcer for conteinrzation",
    "machne learnig tutrials for beginers",
    "poplar front-ed web deveopmnt tools in 2023",
    "moblie app develpment trens in 2023",
    "implent multi-factor authntictin in a web app",
    "whaat is DevOp and its key priciples",
    "intergrte a chatbot intoa wesite",
    "best practces for code reveiws",
    "Pythn vs. Jva for backend developmnt",
    "scl a web aplcatin usng Kuberntes",
    "introducton to Prgessive Web Aps (PWAs)",
    "web scrping with Pythn usng Beautful Soup",
    "chose the rght databse for your projct",
    "serverls arhitectre and its benfits",
    "optmize imgs for web prformance",
    "understandng RESTful API desgn prnciples",
    "cross-platorm moble app deveopemnt tools",
    "use verison cntrol with Git and GitHb",
    "cybersecrity best prctces for develoer",
    "introducton to Agil softare developmen mthodolgies",
    "buld a rel-time chat aplcation",
    "best IDEs for web develpment in 2023",
    "testig stratgies for microsrves",
    "buld a resonsive web dsign lyout"
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

        # Sleep for a random time interval (between 4 to 8 seconds)
        sleep_time = random.uniform(6, 10)
        time.sleep(sleep_time)
    except Exception as e:
        print(f"Error processing query: {query}")
        print(f"Error message: {str(e)}")

# End of script
