import time
import random
import webbrowser
import pyautogui

# List of search queries
queries = [
    "explen globalization's impact on loacl cultrues",
    "comapre economic systmes: captialism vs socalism",
    "analzye the cauess of the Grat Depression",
    "disscus the effcts of colonilism in Afirca",
    "expolre the histroy of the Civl Righs Movemet",
    "evalute the roel of women in ancint civlizatons",
    "exmanie the culturl signifcanec of religous festivls",
    "investigt the orgins of democrac in ancint Grece",
    "trce the develpment of human rigts over tme",
    "descrbe the effcts of urbniztion on socity",
    "assess the imact of clmate chnage on vulnreble communties",
    "analize the role of propganda in wartime",
    "exlpre the histoy of immigraton in the Uniteed Sttes",
    "disscuss the pros and cns of globlization",
    "investiigate the causs of politcal revolutons",
    "comapre diffrnt forms of govrenment: monrchy vs dmoecracy",
    "examin the effcts of colnization in Soth Amerca",
    "explin the cncept of socail stratficaton",
    "analize the role of media in shapng publc opinon",
    "disscus the histroy of the Europen Unoin",
    "exlpre the impact of tehcnology on socity",
    "evalute the role of non-govrnmental orgnizatons (NGOs)",
    "trace the evoluton of human rights movemnts",
    "exmane the signifcance of cltural diffusin",
    "disscus the effcts of war on cvilian populatons",
    "analize the role of propoganda in shapng publc percption",
    "explore the histroy of aparteid in Sout Afrca",
    "assess the impact of globalzation on indigneous cultres",
    "investgat the orgins of the Unied Ntions",
    "disscus the relatonship between religon and poltics",
    "exlpre the histoy of the women's suffrage movemnt",
    "analze the consqunces of imperalism in Asia",
    "disscus the role of social media in modern poltics",
    "exmane the culturl signifcance of traditonal clothng",
    "evalute the effcts of economc inequalty on socity"
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

# List of search queries for mobile searches
queries1 = [
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
