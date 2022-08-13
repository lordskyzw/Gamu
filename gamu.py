from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import argparse
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

intro ='This is an Instagram bot built by Engineer Chiwara (@the.ip.boy.friend on Instagram). It goes to a targets recent post, goes through the people who liked it and follows them in hopes of them following back.'

#defining arguments 
parser =argparse.ArgumentParser(description=intro, usage='python gamu.py [target] [username] [password]', add_help=True)
#adding arguments
parser.add_argument('target', help='target account')
parser.add_argument('username', help='username of your account')
parser.add_argument('password', help='password of your account')
#read arguments from command line
args = parser.parse_args()
#setting arguments into variables. RIP to RAM 
target = args.target
username = args.username
password = args.password

#just to show that arguments were taken
logo = r'''
...::::::^^^~~~^^^^^^^~~~^~~!77!!^^^~~~!!777!!!!!!!!~~!~~~~~~~^^^^^^^^^^^^^^^~~~^^:.:J&&P77G&
    ..:^~~~!~~~~~~~!!~~~~^^^^^^^::::^^~~~^^~~~!!!!!!!!!!!!!!!!!!!!~~~~~~~~^^^^^^^^^^^^^^^::75BP7?B&@
   ..:::^^^~!!!!7777777!!!!~~~^^^:...::::::::^^^::::^~~~!!!~!!!!!!!!!~~~~~^^^~~~~~~^^^:::.:::~7YB&#G
.  ....::^~~!!!!!!7777777777777!^:..........:::::::::::^^^^^~~~~~~~~~~~~^^^^^~~~^^^^^^::::::.:!Y?!:.
:::::.. ...:^^^~~~~~!!~~~!!!!!!~:.     ..::^^~~~~~~~^:.....:^^^^^^^^^^^::::::::::::::............:..
!~~~~^^:.................::::.....  ..::^^~~~~~~~~^^^::......::::..:::..................    ...:::::
~^:........::^:.       ..:::^^~~~~~~~~!!!!~~~~^^^::::::..  .........:::..................     ...::^
.......::.......     ..:::::^^^~~^^^^^^^^^^^::.........    .....:::...............   ..::.. ...:::::
...:^^^~~~^^:::::::....::............  ..:...    ....:::::::::::::::::....  ..........:^^::......:::
:::::^^^~~!!!!!!~~^::....   ..::::...........   ........:::::^^^^^^^^^^:.....::^^^^^^^^~~^^:::....::
!!!~~^^~~~~~!!777!!!7!!!~~^:....:::...::::.    ........:::^^^^^^^^^^^^::.....:::::::::........::::::
7777777777!!!!!!!!!~~~~~~~^^^::^~~!!!!!~:.   .:::^^^::::::::::::^^^^^^::........::...  .....::^^^^^^
!!!~~~~~~!~~~~~^^^::.   .:^^~~~~~~~^^~~^:...:::::::::::::^^^:::::::::.....:::^^::::::::^^^^^^^^^^^^^
^^^^^^~~~~~~~~~~~~~^:.......................:.........:^~?JJ??7!^:...:::::::::::::::::::::::::::::::
~~~~!!!!!!!~~~~~^^^~~~~~~:...  .......... .....    ..^~!?JYY5P55YJ!:...............  ....   ........
~~!!!!!!!!~~~~~^^^^^~~~~^^:::....:::...............^!?5B&&&&&&&#GG5Y~.    ...  .....................
~~~~~~~~~~~~~~^^::.........::^^^^::::............:!5#&@@@@@@@@@@@@&BP7..............................
~~~~~^^^^^^^^^^^^::^::.. ...::::::^^:::::::.....^5&@@&&&&&@@@@@@@@@@&B!.....  ......................
^^^^^::^^^:::::::^^^^::......:::::::::::::::...!B@@@&&@@@@@@@&#@@@@@@@B~............................
....::::::::::::^^^^^^^^^:::::::........::::..^#@@@&&&&@@@@@@@&@@@@@@@&5:...........................
.::::::^::::::::::::::::......................^&@@@&&&@@@@&&&&&@@&&&@@@#7.....:.....................
.......::..................::::::.......:::.. :&@@&&@@@@@@&&&&@@&##@@@@#J....::::........^^^...:~7^:
.....  ...............::^~7?J?77!~:.::::::^^:.^#@@&@&&&&@&&#&&@&&&&&&&@GJ!7!^~?7~:^~7JJ!!?YY?777?J?!
~~~~~~~!~^::^^^~~~^~!77!!!!!!!???77~!!~^^~!7!!7B&@@#GPPGPP5Y5PPP5555G&&PYPBG55G5JJY5GGGGGB#BBGGPP555
7!!!7JJYPGGBG5J?7777777777?5555YYY?77JJJYY55YY?Y&&&&5^^^^^^^~7???JJYP&&5YG##BBBBGGGBBGPBB#BBBBBBBBBB
YJJY5?77YBBPJ!~~~~!!::~!!75BBBGBBBBBGGBBBBGPPPPYG###P^:!GGBBBBBBBGY55BBYYPBB###BBBBBBBB#########BBBB
P5J5BBPJJ5JYP55PGGPGGGBBBBB#BBGBBBBBB###B#BBBGBBPG##57^5&&&&##B##&Y5B#G?YGBBBBBGBBBGPPPGBBBGGB#BGGGP
###&&&&B########BBBBBBBBB###BBGGBBBBBBBBBBGGBB##B55#BGYG&&#GPG#&&&GG##5J5PBBGGPPGPP5YYYPGGP5Y5PYJPPG
&&&&&&&B#&&&######BBBBBGGGBGGGGGP5YY555PYY5555P5?^^JBBG####BYP#&&&&##PY55Y5YJ??J?7!7??7?J?7777777???
##&##&BPBBGGGGGGGG5YYYYY5YYJJJYJ777777??77!~~~!5J^~!?PG##B###&&&&&&&PYPGY!77777!7?J?????777????J??77
55GP5GP555555PPP55YY5Y5555Y55Y5YJJYYJJJ???!7YPG#BY7~!75G5G#&&&&&&&&BYPGP55YYYYYJY555JJ????JJJJJ????J
YYYYY5YYYY555YYYY555P5PPP5555YPP5PPPY?YGPGGB#&&&#57~~!!5B&&&&&&&&&G5PPP5G##BGGG5YYYYY????JJJJJJJJJ?J
P55YYY555555555555555555555PP5PP555Y??B#&##&&&&&&G7!^!5B#&&####&&#BPPPP5G&&#####PYYJJJJJJYYYYJYYJJJJ
555YYYYY5Y5555YYYYYJJJJJJJJJ???77!7YGB&#&&&&&&&&&&B7^?JP####&&&&&#GPGPP5Y#&&&#####GY??JYY555YYYYYYYJ
YJYY?JJY55YYYYY5YYYYYYJJ77!!~~~~~7PG#&&&&@@@@&&&&&B^7YGB####&&&&&#GGG555PB&&&#&#&##BYJJYYYYJY5YYY555
??J?7!7?JJJJ??????7?77!~~~^^^^:^!P###&&&&&&&&&&&&B!75GBB###&&&&#BP5P55P55P#&&#&&#&&&5777!77!!7777777
J?77!77!!!!~^^:^^^^^^^^^^^^^~^:.75B##&&&#&&&&&&&P~!5GBBB##&#GGGGP55P5555Y5B&&&&&&&&&5^^^^^^~~~~~~~~~
!!!~~!!!!77!~~^^~~~~~~~~~~~:.  :JPPB###&######BB7!5GGBB##BPYJY5PPP5555Y5Y5B&&&&&&@&&G~~~~~~~~~~~~!!!
?JJ??JJJY5555Y??77777!!!!~:    !5GGGBB#&&#&#B5GBG5PGBBBBPYY5JJJJY55555555PG&&&@@@&&&#7!!!!!!!!!!!!!!
5YY5PPPP555Y55YY555YY?7!~.....:JPGB###&&&&&B5G#&&##&&&&#GPPGP555555555555PG&@@@@@@@@@Y77777777!!7!77
P5PPPP5YYJ?777?7!!~~~~~~^.:::^~YG#&&&&&&&&#PB&&@@@@@@@@@&BBBBGPPPPPPPP5PGGB&@@@@@@@@@G77777777777777
7!!!!!~~~~^^^~~~^^^^^~~^...:::!5B#&&&@&#&&B#&&@@@@@@@@@@@#BBBBGPPGGGGBGPPG#&@@@@@@@@@#7777777777????
7!!!!!!~~~~~~~~~~~~~~~~~~!!~^^7P##&&&@&&#&@@&&@@@@@@@@@@@&###BGP55PGGBGGGGB&@@@@@@@@@&JJ????????JJJJ
777!!!!!!!!!!!!!!!!!!!!!JGGGGYY#&&&@@#&@&&@@@&@@@@@@@@@@@&#BBGGPPPP55PP5PB#&@@@@@@@@@&YJJJJJYYYYYYYY
????77777777!!!!!!!!!!!!7JY5PY#@&@@@&#&@@@@@@@@@@@@@@@@@@@#BBBBGPGG55P5PGB#&@@@@@@@@@@5JJJJJ?JJYYYJJ
??7777777777777777777777?5#&#B@@&&#&&&@@@@@@@@@@@@@@@@@@@@&#BBGGPPGGGGPPPB#&@@@@@@@@@@PJJJJJ????????
???????7777777777777777??JP##&&&&&&&&&@@@@@@@@@@@@@@@@@@@@&BBGP55PP55PPPPG#&@@@@@@@@@@BJJJJJ????????
??JJJJJ???????????7777??JY5PPG&@&&@@@@@@@@@@@@@&@@@@@@@@@@@BBGPPPPPP5GP55G#&@@@@@@@@@@#JJJJ?JJJ?????
YYJJJ?7??7777777????JJJJJJJJ5#@&&&@@@@@@@@@@@@@@@@@@@@@@@@@#GGGP5PP55PPPGGB&@@@@@@@@@@#J????J???????
J???7???777?????JJJ????JJ???5@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&BBBG5YYY55PPGBB&@@@@@@@@@@&JJ??????JJYYY
???7?JJ??JJJYJYYYYYYYYYYYYJJ5&@@@@@&@@@@@@@@@@@@@@@@@@@@@@@@BPP5JJY5555PPGB&@@@@@@@@@@&5YJYYJYYJJYY5
JJJJY55555555555YYY5555555YYJP&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@#P55YYYYJJY5PGB&@@@@@@@@@@#5YYYYYYJJJY55
PPP55555555YYYYY5PPP5YYYYJJ???Y#&@@@@@&@@@@&&&@@@@&@@&&@&&&@&G555555Y?Y5PPP#&@@@@@@@@@#YYYYYJJJJJJJY
55J?YYYYJYYY55PPP5YYJYYYJJJ???J5G#&&@@@&&&&&#@@@@@@&&&@&&&&&&BYYYY555555PGGB&@@@@@@@@@&YYJJYJ??JYJ??
55YYJJYYY555555YYJYYYJJYYYJJJJYYYY5PGGGG#&&##@@@@@@&&@@&&&&@&BJJ?Y5PP5YYYPG#&@@@@@@@@@@PJJJJ??JJJYYJ
5YYJJ55555YYYYYYJ??JJJJYJ??JJJJJJJJJ?JYB&&&B&&&&@@@@&@@@@&&@&#YY55P5YYY55PGB&@@@@@@@@@@BJJJJJ?JJJYJY
YYY5YJJJJJYYYYYJJ????JJJJJYYYYYJJJJJJJP&@&&#@@&&&&@@@@@@@&&&&&5YYY5YJJJY555B&@@@@@@@@@@#YYYYJJJJJJJJ
YJJJ?JYYY555YYYJJJ??J?????JYYYYYJYYJYY#&&&#&@&&&&@@&@@@@@&&&&&PYYYYJJJJYY555B&@@@@@@@@@&5555YYYYJJYY
JJJY555555YYYYYJJ?????JJJJJYYJYYYYJJJ5&&#&&&&&&&@@@@@@@@@@@&&&P5YYJ???YY555YP&@@@@@@@@@@#PPPP555YYYY
Y5555555YJ?JYJYYYYJ?JJYYYYYYY5YYYYYYYY#&#&#&&&@@@@@@@@@@@@@@@@BP55Y???JJ55YY5B@@@@@@@@@@&PPPPPPPPPP5
555P5P555YJYY555YYYYYYY5P555YY55555555G&&&&&@@@@@@@@@@@@@@@@@@GYYJYJJJYYJY555G@@@@@@@@@@&P5PPPGGPPYY
PPPPPPPPPP55Y5555P5555555YYYYYPGPP5PGPPG&&&&@@@@@@@@@@@@@@@@@@GYJJY55YJY5Y55PB&@@@@@@@@@#PP5PPPPGPPP
5555Y5PPPPP5P55PP555555YYYY5YYPBGGP5P5Y5#&&&@@@@@@@@@@@@@@@&@@B5JJJ?JJ?J5555G#&@@@@@@@@&GPP5PPPPPPPP
'''
print(logo)
options = Options()
options.headless = True
driver = webdriver.Chrome(options=options, service=Service(r'C:\Users\im_bradley\Downloads\chromedriver_win32\chromedriver.exe'))



def login(username, password):
    driver.get('https://instagram.com')
    driver.find_element(By.NAME, 'username').send_keys(username)
    driver.find_element(By.NAME, 'password').send_keys(password)
    driver.find_element(By.TAG_NAME, 'form').submit()
    time.sleep(30)   
    return driver

def search(target):
    
    driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/div/div/button').click()
    #clearing notifiation thingy and searching
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]').click()
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[2]/input').send_keys(target)
    time.sleep(10)
    return driver
    
    

if __name__ == '__main__':
    login(username, password)
    search(target)