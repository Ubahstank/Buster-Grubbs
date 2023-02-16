import sys
import random
import json
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

screen_width = 100


# PLAYER CLASS
class Player:
    def __init__(self):
        self.name = 'Buster Grubbs'
        self.location = "Room 1"
        self.inventory = ["Unsolicited Advice"]
        self.game_over = False


myPlayer = Player()


# TITLE SCREEN ###
def title_screen_selections():
    option = input("> ")
    if option.lower() == "play":
        setup_game()
    elif option.lower() == "help":
        help_menu()
    elif option.lower() == "quit":
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print("Please enter a valid command")
        option = input("> ")
        if option.lower() == "play":
            setup_game()
        elif option.lower() == "help":
            help_menu()
        elif option.lower() == "quit":
            sys.exit()


def title_screen():
    print(f"      {Fore.LIGHTRED_EX}{Style.BRIGHT}______    __    __    _____   ________    _____   ______     ")
    print(f"     {Fore.LIGHTRED_EX}{Style.BRIGHT}(_   _ \   ) )  ( (   / ____\ (___  ___)  / ___/  (   __ \    ")
    print(f"       {Style.BRIGHT}) (_) ) ( (    ) ) ( (___       ) )    ( (__     ) (__) )   ")
    print(f"       {Style.BRIGHT}\   _/   ) )  ( (   \___ \     ( (      ) __)   (    __/    ")
    print(f"       {Style.BRIGHT}/  _ \  ( (    ) )      ) )     ) )    ( (       ) \ \  _   ")
    print(f"      {Fore.BLUE}{Style.BRIGHT}_) (_) )  ) \__/ (   ___/ /     ( (      \ \___  ( ( \ \_))  ")
    print(f"     {Fore.BLUE}{Style.BRIGHT}(______/   \______/  /____/      /__\      \____\  )_) \__/   ")
    print(f"\n:::::::::::-=======---{Style.BRIGHT}{Fore.LIGHTWHITE_EX}:::::-------------:.  {Fore.LIGHTBLACK_EX}*@@@@%%*+==+#@@@@@@@@@@@@@@@@@@@@@@@@@@:::::::")
    print(f":::::::::::-------{Style.BRIGHT}{Fore.LIGHTWHITE_EX}::---=================++++=++{Fore.LIGHTBLACK_EX}*##%%@@@@%%%@@@@@@@@@@@@@@@@@@@@@@@%:::::::")
    print(f"::::::::::::--{Style.BRIGHT}{Fore.LIGHTWHITE_EX}::----=====================++++++++++++**{Fore.LIGHTBLACK_EX}#%@@%%@@@@@@@@@@@@@@@@@@@@@#:::::::")
    print(f" ...      {Style.BRIGHT}{Fore.LIGHTWHITE_EX}::--=========================+++++++++++++++++++{Fore.LIGHTBLACK_EX}**#%%%@@@@@@@@@@@@@@@@@@+:::::::")
    print(f"         {Style.BRIGHT}{Fore.LIGHTWHITE_EX}.-=====--==============+=+++++++++****************++++{Fore.LIGHTBLACK_EX}@%%@@@@@@@@@@@@@@@@= ...:::")
    print(f"       {Style.BRIGHT}{Fore.LIGHTWHITE_EX}.--=================++++{Style.RESET_ALL}***###%%@@@@@@@@@@@%%##***+++**%@{Fore.LIGHTBLACK_EX}@@%%%%%%%%%%@@%@@%.....:::")
    print(f"     {Style.BRIGHT}{Fore.LIGHTWHITE_EX}.--==============+++{Style.RESET_ALL}**##%@@@@@@@@@@@@@@@@@@@@@*****#%@@@@@@@@{Fore.LIGHTBLACK_EX}@@%@@@%@@@@%%%%*=. . .::")
    print(f" .  {Style.BRIGHT}{Fore.LIGHTWHITE_EX}:-============+++{Style.RESET_ALL}**#%@@@@@%***#@@@@@@@@@@@@@@@@*-***##%%%##%@@@{Fore.LIGHTBLACK_EX}@@@@@@@%%%%%%%%%%+: ...")
    print(f"   {Style.BRIGHT}{Fore.LIGHTWHITE_EX}-============+++*{Style.RESET_ALL}#%@@@@@@@%+#===+#@%#%@@@@@@@@@@@#-+=-++++++**#@@@@@@@@@@{Fore.LIGHTBLACK_EX}%%%%%%%@@%+.. ")
    print(f"  {Style.BRIGHT}{Fore.LIGHTWHITE_EX}-==========+++*{Style.RESET_ALL}##***#@@@@@%*==**==+*+++*%@@@@@@@@@@*::.::-==+**###%%@@@@@@@@@@@@@@{Fore.LIGHTBLACK_EX}%%%%+=")
    print(f" {Style.BRIGHT}{Fore.LIGHTWHITE_EX}-========+++*{Style.RESET_ALL}###*+++=+*###%@*==*#+==*====+#@@@@@@@@@%: ..:-==++**#%%%@%###@@%%%@@%%{Fore.LIGHTBLACK_EX}%#####")
    print(f"{Style.BRIGHT}{Fore.LIGHTWHITE_EX}.======++++*{Style.RESET_ALL}%%#***++=====++#*====*=-=*=====*#%@@@@@@@#:..:-==++++********#*%#-  ..:::::.. ")
    print(f"{Style.BRIGHT}{Fore.LIGHTWHITE_EX}-====+++++*{Style.RESET_ALL}#%###*+==================++=====+*#%@@@%@@%%%%#*++++++++***++**==-             ")
    print(f"{Style.BRIGHT}{Fore.LIGHTWHITE_EX}===++++++***+-+{Style.RESET_ALL}#++#*=====================+++*##%%%@@@@@@@@@@@#=++++*#*++++::              ")
    print(f"{Style.BRIGHT}{Fore.LIGHTWHITE_EX}-+++++++=-:{Style.RESET_ALL}     .*#+===================+++**##%%%%%@@@@@@@%%%#=++*****#*+=:               ")
    print(f"{Style.BRIGHT}{Fore.LIGHTWHITE_EX}.====-:.{Style.RESET_ALL}         =++============++++++++***#%@%@@@@@@@@@@@%%%%+***+*****+:             .. ")
    print(f" {Style.BRIGHT}{Fore.LIGHTWHITE_EX}...{Style.RESET_ALL}             ++++========+=+++********%%%@@@@@@@@@%%%%%%##*+++**##*=.              ...")
    print(f"                 =+++*=========++**##**#%@@@@@@@@@@@%##**++-=----+****+::.          .....:")
    print(f"                 .--:-=====+++++**####%@@@@@@@@@@@@@%#+*=--=-:::::=##%%==::.........:::--=")
    print(f"                      :=+==+++++*#%%%%@@@@@@@@@@@@%%#===:::-::::--::=%@**++=---:.:---===++")
    print(f"                        :-==++=#%%@@@@@@@@@@@@@@@%*+--==:....::::---..=%%**+++**+=-=++++**")
    print(f"        ...               -=+*##%%@@@@@@@@@@@@%#++++-=+-:::::::-:::::::-#@%%%%%%%##**#####")
    print(f"      . ......             -=+*+=:*@@@@@@@@@%#++++**==+=----==--:--------=#@@%%@%%%%%#%%#%")
    print(f".... ....:...... ...        ......%@@@@@@@%#*+++*******#*+**+--==++++++====#@@@@@@@@@%%%%%")
    print(f"::.::::: ....::.....    ... ......*%%%%%%#*****+**#####%##**++#%#**####**++%%@@@@@@@@@@@@@")
    print(f"=-===-::::-----:::::.....::::::----#%#%#*****++**#%#*###%%%%##*+##%%%%%###%%#%@@@@@@@@@@@@")
    print(f"+==+==+**++++++=------------------*%%####*#****#%@@%%%@%%%%@@%%@@%##@@%%%%@%@%%@@@@@@@@@@@")
    print(f"++***+##**%%*****+++++=======+===+@%#%###%#####%%@@@%@@@@@@@@@%%@@@@@%%%@@@@@@@@@@@@@@@@@@")
    print(f"**###*#%#*#%##**######******##*+*%%%%%%#%%%%#%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print(f"##%%#########################%%#@@%%%@%@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print(f"\n         {Fore.LIGHTRED_EX}{Style.BRIGHT}_____    ______     __    __   ______    ______     _____ ")
    print(f"        {Fore.LIGHTRED_EX}{Style.BRIGHT}/ ___ \  (   __ \    ) )  ( (  (_   _ \  (_   _ \   / ____\ ")
    print(f"       {Style.BRIGHT}/ /   \_)  ) (__) )  ( (    ) )   ) (_) )   ) (_) ) ( (___  ")
    print(f"      {Style.BRIGHT}( (  ____  (    __/    ) )  ( (    \   _/    \   _/   \___ \ ")
    print(f"      {Style.BRIGHT}( ( (__  )  ) \ \  _  ( (    ) )   /  _ \    /  _ \       ) )")
    print(f"       {Fore.BLUE}{Style.BRIGHT}\ \__/ /  ( ( \ \_))  ) \__/ (   _) (_) )  _) (_) )  ___/ / ")
    print(f"        {Fore.BLUE}{Style.BRIGHT}\____/    )_) \__/   \______/  (______/  (______/  /____/  ")
    print(f"\n                              {Fore.LIGHTYELLOW_EX}{Style.BRIGHT}-_PLAY_-{Style.RESET_ALL}")
    print(f"\n                              {Fore.LIGHTYELLOW_EX}{Style.BRIGHT}-_HELP_-{Style.RESET_ALL}")
    print(f"\n                              {Fore.LIGHTYELLOW_EX}{Style.BRIGHT}-_QUIT_-{Style.RESET_ALL}")
    title_screen_selections()


def help_menu():
    print(player_guide)
    title_screen_selections()


ZONENAME = ''
DESCRIPTION = 'description'
NORTH = 'up', 'north'
SOUTH = 'down', 'south'
WEST = 'left', 'west'
EAST = 'right', 'east'

player_guide = (f"""
                                        {Fore.LIGHTWHITE_EX}{Style.BRIGHT}**************{Style.RESET_ALL}
                                        {Fore.LIGHTWHITE_EX}{Style.BRIGHT}*PLAYER GUIDE*{Style.RESET_ALL}
                                        {Fore.LIGHTWHITE_EX}{Style.BRIGHT}**************{Style.RESET_ALL}
        Welcome back {Fore.BLUE}{Style.BRIGHT}Buster{Style.RESET_ALL}! In case you may have forgotten you have the ability to
        {Fore.LIGHTBLUE_EX}{Style.BRIGHT}'speak'{Style.RESET_ALL}, {Fore.LIGHTBLUE_EX}{Style.BRIGHT}'trade'{Style.RESET_ALL}, {Style.BRIGHT}{Fore.LIGHTRED_EX}'fight'{Style.RESET_ALL}, and check your {Fore.LIGHTBLUE_EX}{Style.BRIGHT}'inventory'{Style.RESET_ALL}. Feeling a little lost?
        Not to fear! Try using your {Fore.LIGHTBLUE_EX}{Style.BRIGHT}'map'{Style.RESET_ALL} if things get confusing, or give the room a {Fore.LIGHTBLUE_EX}{Style.BRIGHT}'look'{Style.RESET_ALL}.
        Not every character you come across will interact with you in the same way. Traverse
        your way throughout the 13 available rooms using cardinal directions {Fore.LIGHTBLUE_EX}{Style.BRIGHT}['n', 's', 'e', 'w']{Style.RESET_ALL}
        coupled with the above mentioned abilities to obtain items, trade, and defeat
        enemies to receive their held items. Pay close attention to your surroundings 
        as they provide hints to your next action. If you want to see this Player Guide 
        again try asking for {Fore.LIGHTBLUE_EX}{Style.BRIGHT}'help'{Style.RESET_ALL}. To end the game utilize the {Fore.LIGHTBLUE_EX}{Style.BRIGHT}'use'{Style.RESET_ALL} command as instructed!
        If you get bored because I'm a terrible story designer just {Style.BRIGHT}{Fore.LIGHTRED_EX}'quit'{Style.RESET_ALL}! Good luck {Fore.BLUE}{Style.BRIGHT}Buster{Style.RESET_ALL}!
    """)

# Set the list of fightable characters
fightable_characters = ["black sheep"]
speakable_characters = ["dipcoin dan", "mcallstar"]


zonemap = {
    "Room 1": {
        ZONENAME: "Room 1",
        DESCRIPTION: f"""
        You look around and see you're standing in a familiar place.
        While still on the thought of familiar, a recognizable voice pipes up,
        {Fore.GREEN}'Hey bro you buy any {Fore.YELLOW}{Style.BRIGHT}'Dipcoin'{Style.RESET_ALL}{Fore.GREEN}? I've got one to get you started!'{Fore.RESET} None other
        than {Fore.LIGHTGREEN_EX}{Style.BRIGHT}'Dipcoin Dan'{Style.RESET_ALL} stands in front of you daring you to take a chance on the
        market!""",
        NORTH: "Room 5",
        SOUTH: "Boundary",
        WEST: "Boundary",
        EAST: "Room 2",
        "CHARACTER_NAME": "Dipcoin Dan",
        "ITEM_NAME": "Dipcoin"

    },
    "Room 2": {
        ZONENAME: "Room 2",
        DESCRIPTION: f"""
        A restaurant? Not sure how I ended up here. Who else would be sporting a pair 
        of shorts that apparently only fit halfway up their butt... The infamous {Fore.LIGHTGREEN_EX}{Style.BRIGHT}'Shane'{Style.RESET_ALL}! 
        {Fore.GREEN}'HEY BUBBY WOOKS WIKE SHANEY WEFT HIS WALLY, I bet I ate a whole 
        {Fore.YELLOW}{Style.BRIGHT}"Dipcoin"{Style.RESET_ALL}{Fore.GREEN} worth of food!'{Fore.RESET}""",
        NORTH: "Room 6",
        SOUTH: "Boundary",
        WEST: "Room 1",
        EAST: "Room 3",
        "CHARACTER_NAME": "Shane",
        "ITEM_NAME": "Note on Hand",
        "CHARACTER_TRADE_ITEM": "Dipcoin"

    },
    "Room 3": {
        ZONENAME: "Room 3",
        DESCRIPTION: f"""
        Gaming PC, empty fast food containers, and is that a 
        blanket and pillow in the corner? Looks like {Fore.LIGHTGREEN_EX}{Style.BRIGHT}'Huck Thin'{Style.RESET_ALL} has 
        been on another binger. One thing about old Huck, man makes 
        a fire sauce. I think he is a little too glued to his game 
        at the moment. He really needs to take a break on something
        {Fore.YELLOW}comfy{Style.RESET_ALL}...""",
        NORTH: "Room 7",
        SOUTH: "Boundary",
        WEST: "Room 2",
        EAST: "Room 4",
        "CHARACTER_NAME": "Huck Thin",
        "ITEM_NAME": "Tom Sauce",
        "CHARACTER_TRADE_ITEM": "Couches"

    },
    "Room 4": {
        ZONENAME: "Room 4",
        DESCRIPTION: f"""
        Ah... home sweet home, at least it was... Just like I remember,
        stupid Yadi prancing around all innocent while {Fore.LIGHTGREEN_EX}{Style.BRIGHT}'Rocket'{Style.RESET_ALL} and {Fore.LIGHTGREEN_EX}{Style.BRIGHT}'Trace 
        Markem'{Style.RESET_ALL} are betting over who would beat who in any given sports game.
        Are they seriously arguing over {Fore.YELLOW}{Style.BRIGHT}'Astro Goggles'{Style.RESET_ALL} or {Fore.YELLOW}{Style.BRIGHT}'Can of Dip'{Style.RESET_ALL} being
        a bigger game changer? {Fore.LIGHTGREEN_EX}{Style.BRIGHT}'Trace Markem'{Style.RESET_ALL} turns to you, {Fore.GREEN}'Hey Buster! Shane
        has been killing it on League of Legos. I'd give anything for those
        cheats he keeps written on his hand!'{Fore.RESET}""",
        NORTH: "Room 8",
        SOUTH: "Boundary",
        WEST: "Room 3",
        EAST: "Room 4.5",
        "CHARACTER_NAME": "Trace Markem",
        "ITEM_NAME": "Astro Goggles",
        "CHARACTER_TRADE_ITEM": "Note on Hand"

    },
    "Room 4.5": {
        ZONENAME: "Room 4.5",
        DESCRIPTION: f"""
        Ah... home sweet home, at least it was... wait a minute wasn't i just here?
        I still hear {Fore.LIGHTGREEN_EX}{Style.BRIGHT}'Trace Markem'{Style.RESET_ALL} in the background. You know what that means! LAN PARTY!!!
        Oh {Fore.LIGHTGREEN_EX}{Style.BRIGHT}'Rocket'{Style.RESET_ALL} was just playing in the other room! Wonder if he'd let go of
        that {Fore.YELLOW}{Style.BRIGHT}'Can of Dip'{Style.RESET_ALL} for these {Fore.YELLOW}{Style.BRIGHT}'Astro Goggles'{Style.RESET_ALL}? He pipes up {Fore.GREEN}'Hey Buster have you seen
        my new Land Speeder? I got it for the kids!' """,
        NORTH: "Boundary",
        SOUTH: "Boundary",
        WEST: "Room 4",
        EAST: "Boundary",
        "CHARACTER_NAME": "Rocket",
        "ITEM_NAME": "Can of Dip",
        "CHARACTER_TRADE_ITEM": "Astro Goggles"

    },
    "Room 5": {
        ZONENAME: "Room 5",
        DESCRIPTION: f"""
        You are in... the bathroom? OK... what is going on? Whatever, I'll 
        just make my way out... Upon exiting the bathroom you see a stone 
        cold figure leaned against the wall. {Fore.GREEN}'Oh hey stupid, ditch those flip
        flops and try on these {Fore.YELLOW}{Style.BRIGHT}"Steel Toe Boots!"{Style.RESET_ALL} {Fore.GREEN}It will cost you though, I'm
        hungry as can be bubby, get me some {Fore.YELLOW}{Style.BRIGHT}"Tom Sauce"{Style.RESET_ALL}{Fore.GREEN}!'{Fore.RESET} Yup, its him {Fore.LIGHTGREEN_EX}{Style.BRIGHT}'Eric 
        the Admirable'{Style.RESET_ALL}!!! """,
        NORTH: "Room 9",
        SOUTH: "Room 1",
        WEST: "Boundary",
        EAST: "Room 6",
        "CHARACTER_NAME": "Eric the Admirable",
        "ITEM_NAME": "Steel Toe Boots",
        "CHARACTER_TRADE_ITEM": "Tom Sauce"

    },
    "Room 6": {
        ZONENAME: "Room 6",
        DESCRIPTION: f"""
        Look at all these sweet puppy dogs! Is that Darnell? He isn't in this game!?
        A voice from the kitchen echoes through, {Fore.GREEN}'What's going on Buster? I have
        been cooking for days! To be honest with you, I'm cooked out! Look bubby,
        I've got this entire {Fore.YELLOW}{Style.BRIGHT}"Bag of Flour"{Style.RESET_ALL}{Fore.GREEN} and I'd much rather have those {Fore.YELLOW}{Style.BRIGHT}"Steel
        Toe Boots"{Style.RESET_ALL}{Fore.GREEN} so I can finish building this deck!' {Fore.LIGHTGREEN_EX}{Style.BRIGHT}'Rich Ross'{Style.RESET_ALL} always working
        on something! """,
        NORTH: "Room 10",
        SOUTH: "Room 2",
        WEST: "Room 5",
        EAST: "Room 7",
        "CHARACTER_NAME": "Rich Ross",
        "ITEM_NAME": "Bag of Flour",
        "CHARACTER_TRADE_ITEM": "Steel Toe Boots"

    },
    "Room 7": {
        ZONENAME: "Room 7",
        DESCRIPTION: f"""
        What is that smell?!! And why is the floor completely littered with empty
        packs of hotdogs? A sticky note lays on the floor inscribed with the words, 
        {Style.BRIGHT}'MawMaw's secret sandwich recipe'{Style.RESET_ALL}, I guess that clears things up. {Fore.LIGHTGREEN_EX}{Style.BRIGHT}'Colby Haze'{Style.RESET_ALL} 
        is cuddled up on the couch snoring away with his favorite {Fore.YELLOW}{Style.BRIGHT}'Pack of Hotdogs'{Style.RESET_ALL} 
        tucked in close. Doesn't he like {Fore.YELLOW}{Style.BRIGHT}'Dip'{Style.RESET_ALL}?""",
        NORTH: "Room 11",
        SOUTH: "Room 3",
        WEST: "Room 6",
        EAST: "Room 8",
        "CHARACTER_NAME": "Colby Haze",
        "ITEM_NAME": "Pack of Hotdogs",
        "CHARACTER_TRADE_ITEM": "Can of Dip"

    },
    "Room 8": {
        ZONENAME: "Room 8",
        DESCRIPTION: f"""
        {Fore.YELLOW}Blonde hair{Fore.RESET}, {Fore.BLUE}blue eyes{Fore.RESET}, {Fore.LIGHTBLACK_EX}{Back.BLACK}chiseled bod{Style.RESET_ALL}... is this Hitler's fantasy or your own Buster?
        You hear a voice, but that's about it. {Fore.LIGHTMAGENTA_EX}M{Fore.MAGENTA}E{Fore.BLUE}S{Fore.LIGHTBLUE_EX}M{Fore.CYAN}E{Fore.GREEN}R{Fore.LIGHTGREEN_EX}I{Fore.LIGHTYELLOW_EX}Z{Fore.YELLOW}I{Fore.LIGHTRED_EX}N{Fore.RED}G{Fore.RESET}! {Fore.GREEN}'BUSTER..BUSSSSTEEEEERR, dude are
        you even listening to anything I'm saying? Bro what is it with you and spacing out when
        I'm around? Anywaaay, I've got these {Fore.YELLOW}{Style.BRIGHT}"Couches"{Style.RESET_ALL}{Fore.GREEN} whenever you snap out of it and decide to
        {Back.LIGHTBLACK_EX}{Fore.BLUE}"speak"{Style.RESET_ALL}{Fore.GREEN} to me.'{Style.RESET_ALL} That {Fore.LIGHTGREEN_EX}{Style.BRIGHT}'McAllstar'{Style.RESET_ALL} such a silly tease all the time.""",
        NORTH: "Room 12",
        SOUTH: "Room 4",
        WEST: "Room 7",
        EAST: "Boundary",
        "CHARACTER_NAME": "McAllstar",
        "ITEM_NAME": "Couches"

    },
    "Room 9": {
        ZONENAME: "Room 9",
        DESCRIPTION: f"""
        Plates thrown about, dumbbells lined across the wall, college boys sitting on machines 
        trying to get that next sexy little selfie for their instagram... The Gym. Is that {Fore.LIGHTGREEN_EX}{Style.BRIGHT}'Huge
        Jackedman'{Style.RESET_ALL} benching 800 pounds!? {Fore.GREEN}'Hey bubby, I'm just about to finish my workout. I forgot
        I brought this {Fore.YELLOW}{Style.BRIGHT}"Bang"{Style.RESET_ALL}{Fore.GREEN} in with me and I'm all fibered out! I've been wanting to do some baking
        but I'm completely out of {Fore.YELLOW}flour{Style.RESET_ALL}...'""",
        NORTH: "Boundary",
        SOUTH: "Room 5",
        WEST: "Boundary",
        EAST: "Room 10",
        "CHARACTER_NAME": "Huge Jackedman",
        "ITEM_NAME": "Bang",
        "CHARACTER_TRADE_ITEM": "Bag of Flour"

    },
    "Room 10": {
        ZONENAME: "Room 10",
        DESCRIPTION: f"""
        There is a pallet spread across the floor. The pallet seems to contain a human being, but
        are they even alive? You move a little closer and see {Fore.LIGHTGREEN_EX}{Style.BRIGHT}'The Burnout'{Style.RESET_ALL} wide eyed and frozen in
        place. This dude could use a major {Fore.YELLOW}pick-me-up{Fore.RESET}. I'm not helping him for nothing though. He
        better at least be willing to {Back.LIGHTBLACK_EX}{Fore.BLUE}'trade'{Style.RESET_ALL} that super cool {Fore.YELLOW}{Style.BRIGHT}'Lighter'{Style.RESET_ALL} of his!""",
        NORTH: "Boundary",
        SOUTH: "Room 6",
        WEST: "Room 9",
        EAST: "Room 11",
        "CHARACTER_NAME": "The Burnout",
        "ITEM_NAME": "Lighter",
        "CHARACTER_TRADE_ITEM": "Bang"

    },
    "Room 11": {
        ZONENAME: "Room 11",
        DESCRIPTION: f""" 
        {Fore.RED}{Style.BRIGHT}                                                                                                                                                                                                                                           
                                          .@@#   *@@   %%.+@*                             
                             :=-           %@#  .+@@. :@+  @@.                            
                       .-:  -@@@%+.       .#@%*##*%@. *@#  %@=                           
                 -==.  .#@%:  +%   #-      =@%    =@. @@@%#*@#            :*@%-                   
                 -%@@=   -%@*. +%  %*%*-   .@%    .@.=@-    +@.+ =    .-:  #@#@*.                 
                   -#@%: .+%%%= =@%:  :+#+. #@     %:#%     .@+=*+:   .@@#  %+  %-                
                     :*@##-  -##:=%:     :+==@     +:%=      *%.#@@.   *@@: +%  %@#.              
                       .+%=    :*+=%:       .@     ..@       :@:.@@*   .@@+ :@@%=:#@=             
                         .+#:    .=-*:       *      :+        *- =@@.   +@%  %*    =@#.           
                            ==       -  =+=         ..    :.  :=  #@#.-=*@@# =%     .#%:-=--:     
                    .  *%*    :.       *@@@#:           :-@%.  . =*@@#+==@@+  #:     .%%*+%@@#:   
                    *% *@@+        .#*- +@=*@#:    :   .@ # %.     :@#   :@%  .+    =*++%@@@@@+   
             ##     #% +  @..##=    %@%  %   %@*.  %*   %.# .#      -@:   =@:     -+*%@@@@@%*:    
             %@:    ## %   * *@@-   :@@= =@*@#+#%- -@::=%-*=.-*      =#    +*   -+#@@@@@%+.       
             *@-  .:%*.@%##@: #@%=+#@%@@. %#.   -#*:#%=-+==:  :-      +:    *:=##@@@@@@#.         
            .*@%#@@@@+-@#+:=# =%@%-.  %@= -@.     -#-#: .+.:   .       +   -+#*@@@@@@@*           
              @#....@.-#    *- :@@:   :@%  **       ==+  .             .=+++*@%@@@@@@#:           
              +#    % -=     *  -@%    =@- .%.        -.       .:..-+++=-+%@%%%@@@@@%             
              .%   .* ::     :   -@+    #%  .:          .=+*#@@@@@@+-:=*%%@@#*%@@@@%:             
               *. .               =@.    %-         :=++@@@@@@@@%*++#@##%%###+#@@@@*              
           .=*%%@@@#*+++=-         =#    .*     .=*%@@@@%#*++**+*%@%%+%=+#****%@@@%.    
           *%=#@@@@@@@%****+-::.    -=:::-*++*#@@@@@@@@%%%%#**=:+#+%=+**=*+*#%#@@@=     
           +--%@@@@@@@@@@@@%*+++=--::-::==::.   :=**##===:-:+=*=*--+==++***#%##@@#   
            :=--=+*%%#%@@@@@@@@%@%%%%%%###*=+**+=#**-:-*=*+:=:-+*::-+-=+*##**@@@@:     
                   .-=*#%@@@@%*#*##*%%####%=-++-==-++=+---=#+.::-..-+-=+%%**#@@@:     
                      .:*#%@@#**+*+-++-*#-=#+-=++:----#::::-*..:.-.-=#*%**##@@@=           
                         -#@@#+*+*+=+---+:-+----*.:--.+:.:::==...=++%*+++*+#%@=             
                          :*@@%%+*+++---=:---:-:+.:::.:-.:::-*+:-*%=++-+:++#%:            
                           .*@@%#%###:-:=::-=:::+.-....=.::-+***+=*:-+++++%%:        
                            -%@%%#*######=+#=:-*++-:--##***+=-+:-+=*-++*@*.      
                              +@@@@@##+*-++=####*#*+==-*--=*::+=+-=+=+@%=.        
                                .+@@@##%@+-%:-+-+*-:+---+*:====--+==+@%+.         
                                  ..*@@%**++%%*%=+==:+=:.+-+***+=+*%@#=     
                                   :.=+#%@#+====++++*-+++-:-=*%@%*-#       
                                        .==*##%@%#**++++***##+=:.   
        {Style.RESET_ALL}
        Oh man do I have an itch... I've had an item this whole game and no one has wanted it!
        I'll bet my good ol' buddy {Fore.LIGHTGREEN_EX}{Style.BRIGHT}'John Briscoe'{Style.RESET_ALL} would love to have it! Speaking of the devil,
        here he sits playing the latest Souls game. That winged creature he's fighting looks
        tough!... Or is it wing-ed? Oh well, I'm chomping at the bit to {Back.LIGHTBLACK_EX}{Fore.BLUE}'trade'{Style.RESET_ALL} Briscoe this gift!
        """,
        NORTH: "Boundary",
        SOUTH: "Room 7",
        WEST: "Room 10",
        EAST: "Room 12",
        "CHARACTER_NAME": "John Briscoe",
        "ITEM_NAME": "Friendship",
        "HEALTH": 100,
        "CHARACTER_TRADE_ITEM": ""

    },
    "Room 12": {
        ZONENAME: "Room 12",
        DESCRIPTION: f""" {Fore.LIGHTBLACK_EX}
        .______    __           ___        ______  __  ___ 
        |   _  \  |  |         /   \      /      ||  |/  / 
        |  |_)  | |  |        /  ^  \    |  ,----'|  '  /  
        |   _  <  |  |       /  /_\  \   |  |     |    <   
        |  |_)  | |  `----. /  _____  \  |  `----.|  .  \  
        |______/  |_______|/__/     \__\  \______||__|\__\ 

                        _______. __    __   _______  _______ .______   
                       /       ||  |  |  | |   ____||   ____||   _  \  
                      |   (----`|  |__|  | |  |__   |  |__   |  |_)  | 
                       \   \    |   __   | |   __|  |   __|  |   ___/  
                    .----)   |  |  |  |  | |  |____ |  |____ |  |      
                    |_______/   |__|  |__| |_______||_______|| _|      

                                .___  ___.   ______        ___      .__   __. 
                                |   \/   |  /  __  \      /   \     |  \ |  | 
                                |  \  /  | |  |  |  |    /  ^  \    |   \|  | 
                                |  |\/|  | |  |  |  |   /  /_\  \   |  . `  | 
                                |  |  |  | |  `--'  |  /  _____  \  |  |\   | 
                                |__|  |__|  \______/  /__/     \__\ |__| \__|                                                                       
        {Style.RESET_ALL}
        It sounds like an assembly line here. Wait... that looks familiar. Across the way
        an individual appears to be performing some mash-up of slam dancing and ballet.
        Whatever it is, it isn't good... It speaks up squeaky and shaken. {Fore.RED}{Style.BRIGHT}"Black Sheep"{Style.RESET_ALL}: 
        {Fore.RED}'Hey man you can't be here! According to my {Fore.YELLOW}{Style.BRIGHT}"ECP Guidelines"{Style.RESET_ALL}{Fore.RED} I HAVE TO PUNISH YOU!!!'{Style.RESET_ALL}                                    
        """,
        NORTH: "Boundary",
        SOUTH: "Room 8",
        WEST: "Room 11",
        EAST: "Boundary",
        "CHARACTER_NAME": "Black Sheep",
        "ITEM_NAME": "ECP Guidelines",
        "HEALTH": 100

    }
}


# GAME INTERACTIVITY
def print_location():
    if zonemap[myPlayer.location][NORTH] == "Boundary":
        print(f"{Style.BRIGHT}{Fore.LIGHTRED_EX}North: {Fore.RED}" + zonemap[myPlayer.location][NORTH])
    else:
        print(f"{Style.BRIGHT}{Fore.LIGHTBLUE_EX}North: {Fore.BLUE}" + zonemap[myPlayer.location][NORTH])

    if zonemap[myPlayer.location][SOUTH] == "Boundary":
        print(f"{Style.BRIGHT}{Fore.LIGHTRED_EX}South: {Fore.RED}" + zonemap[myPlayer.location][SOUTH])
    else:
        print(f"{Style.BRIGHT}{Fore.LIGHTBLUE_EX}South: {Fore.BLUE}" + zonemap[myPlayer.location][SOUTH])

    if zonemap[myPlayer.location][EAST] == "Boundary":
        print(f"{Style.BRIGHT}{Fore.LIGHTRED_EX}East: {Fore.RED}" + zonemap[myPlayer.location][EAST])
    else:
        print(f"{Style.BRIGHT}{Fore.LIGHTBLUE_EX}East: {Fore.BLUE}" + zonemap[myPlayer.location][EAST])

    if zonemap[myPlayer.location][WEST] == "Boundary":
        print(f"{Style.BRIGHT}{Fore.LIGHTRED_EX}West: {Fore.RED}" + zonemap[myPlayer.location][WEST])
    else:
        print(f"{Style.BRIGHT}{Fore.LIGHTBLUE_EX}West: {Fore.BLUE}" + zonemap[myPlayer.location][WEST])
    print(zonemap[myPlayer.location][DESCRIPTION])


def prompt():
    acceptable_actions = ['look', 'n', 's', 'e', 'w', 'speak', 'trade', 'use', 'fight', 'inventory', 'map', 'help',
                          'quit']
    print(f"\n{Fore.LIGHTBLUE_EX}{Back.BLACK}{Style.BRIGHT}Movement Commands:{Style.RESET_ALL}{Back.BLACK}{Fore.BLUE}{acceptable_actions[1:5]}{Style.RESET_ALL}")
    print("What will you do, or where will you go?")
    action = input("> ")
    while action.lower() not in acceptable_actions:
        print("Unknown command, try something else.")
        action = input("> ")
    if action.lower() == 'quit':
        # sys.exit()
        title_screen()
    elif action.lower() in ['n', 's', 'e', 'w']:
        player_move(action.lower())
    elif action.lower() == 'speak':
        player_speak()
    elif action.lower() == 'trade':
        player_trade()
    elif action.lower() == 'fight':
        player_fight(myPlayer, zonemap[myPlayer.location]['CHARACTER_NAME'], zonemap[myPlayer.location]['ITEM_NAME'])
    elif action.lower() == 'use':
        player_use()
    elif action.lower() == 'inventory':
        player_inventory()
    elif action.lower() == 'map':
        player_map()
    elif action.lower() == 'help':
        player_help()
    elif action.lower() == 'look':
        player_look()
    else:
        print(f"That is not an acceptable action. If you're stuck try {Back.LIGHTBLACK_EX}{Fore.BLUE}'help'{Style.RESET_ALL}!")


def player_move(myaction):
    if myaction in ['n', 'north']:
        destination = zonemap[myPlayer.location][NORTH]
        movement_handler(destination)
    elif myaction in ['s', 'south']:
        destination = zonemap[myPlayer.location][SOUTH]
        movement_handler(destination)
    elif myaction in ['w', 'west']:
        destination = zonemap[myPlayer.location][WEST]
        movement_handler(destination)
    elif myaction in ['e', 'east']:
        destination = zonemap[myPlayer.location][EAST]
        movement_handler(destination)


def movement_handler(destination):
    if destination == "Room 12":
        if "Friendship" in myPlayer.inventory:
            # Allow the player to enter the room and update their position
            print(f"You used the power of {Fore.YELLOW}{Style.BRIGHT}Friendship{Style.RESET_ALL} to open the door and entered the room.")
            myPlayer.location = destination
            print_location()
        else:
            # Print a message indicating that the player needs "Friendship" to enter the room
            print(
                f"You need the {Fore.YELLOW}{Style.BRIGHT}Friendship{Style.RESET_ALL} of {Fore.LIGHTGREEN_EX}{Style.BRIGHT}John Briscoe{Style.RESET_ALL} to enter this room.")
    elif destination != "Boundary":
        print("\n" + f"You have moved to {Style.BRIGHT}{Fore.LIGHTWHITE_EX}" + destination + ".")
        myPlayer.location = destination
        print_location()
    else:
        print(
            f"{Back.BLACK}{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}Now now Buster, you know I'm {Fore.GREEN}monetizing{Fore.RESET}{Back.BLACK}{Fore.LIGHTYELLOW_EX}{Style.BRIGHT} that DLC!{Style.RESET_ALL}")


def player_speak():
    # Get the character the user wants to speak to
    character_speak = input("Who do you want to speak to? ").lower().strip()
    # Check if the character is in the list of acceptable characters
    if character_speak in speakable_characters:
        # Print a message indicating that the user is speaking to the character
        print(f"\n{Fore.GREEN}'Sure Grubbs... Go ahead help yourself...'")
        # Check if the character has any items
        if zonemap[myPlayer.location]['ITEM_NAME']:
            # Print a list of the character's items
            print(
                f"\n{Fore.LIGHTGREEN_EX}{Style.BRIGHT}{zonemap[myPlayer.location]['CHARACTER_NAME']}{Style.RESET_ALL} has the following items:")
            # Get the item value from the dictionary
            item = zonemap[myPlayer.location]['ITEM_NAME']
            print(f"{Fore.YELLOW}{Style.BRIGHT}{Back.LIGHTBLACK_EX}{item}")
            # Prompt the user to choose an item
            choice = input("\nWhich item do you want to receive? ")
            if choice == item.lower():
                # Remove the item with the specified name from the character's inventory
                myPlayer.inventory.append(item)
                zonemap[myPlayer.location]['ITEM_NAME'] = "Nothing"
                print(
                    f"{Fore.LIGHTGREEN_EX}{Style.BRIGHT}{zonemap[myPlayer.location]['CHARACTER_NAME']}{Style.RESET_ALL} gave you the {Fore.YELLOW}{Style.BRIGHT}{item}{Style.RESET_ALL}.")
            else:
                print("Try spelling the item correctly!")
        else:
            print(f"{Fore.LIGHTGREEN_EX}{Style.BRIGHT}{zonemap[myPlayer.location]['CHARACTER_NAME']}{Style.RESET_ALL} has no items.")
    else:
        print("Sorry, you are not allowed to speak to that character.")


def player_trade():
    character_trade = input("Who do you want to trade with? ").lower().strip()

    if character_trade not in ['dipcoin dan', 'mcallstar', 'black sheep']:
        # Check if the character is in the current room
        if character_trade in zonemap[myPlayer.location]['CHARACTER_NAME'].lower():
            # Print a message indicating that the user is trading with the character
            print(
                f"\n{Back.BLACK}{Fore.YELLOW}Wow, you're actually offering to trade {Fore.LIGHTGREEN_EX}{Style.BRIGHT}{zonemap[myPlayer.location]['CHARACTER_NAME']}{Style.NORMAL}{Fore.YELLOW} instead of just taking it? Maybe you have grown up Buster!{Style.RESET_ALL}")

            # Print a list of the player's items
            print(f"\n{Fore.LIGHTBLUE_EX}{myPlayer.name}{Fore.RESET} has the following items:")
            for item in myPlayer.inventory:
                print(f"{Back.LIGHTBLACK_EX}{Fore.YELLOW}{Style.BRIGHT}{item}")
                print('\n')

            # Prompt the user to choose an item to trade
            choice = input("Which item do you want to trade? ").lower().strip()

            # Check if the player is trading with "John Briscoe" and if the item is "Unsolicited Advice"
            if character_trade == "john briscoe" and choice == "unsolicited advice":

                # Add "John Briscoe" to the fightable_characters list
                fightable_characters.append(character_trade)

                # Cancel the trade and start a fight with "John Briscoe"
                print(
                    f"{Fore.RED}{Back.BLACK}This.. is the...LAST TIIIIIIIMMMMMMEEEEEE! I'm taking my Shelby back! {Back.LIGHTBLACK_EX}{Fore.LIGHTRED_EX}'FIGHT'{Fore.RED}{Back.BLACK} ME!!!")

            # Check if the choice is a valid item in the player's inventory
            if choice.title() in myPlayer.inventory:
                if choice in zonemap[myPlayer.location]["CHARACTER_TRADE_ITEM"].lower():
                    # Check if the character has any items
                    if zonemap[myPlayer.location]['ITEM_NAME'] != "Nothing":

                        # Print a list of the character's items
                        print(
                            f"\n{Fore.LIGHTGREEN_EX}{Style.BRIGHT}{zonemap[myPlayer.location]['CHARACTER_NAME']}{Style.RESET_ALL} has the following items:")

                        # Get the item value from the dictionary
                        item = zonemap[myPlayer.location]['ITEM_NAME']
                        print(f"{Fore.YELLOW}{Style.BRIGHT}{Back.LIGHTBLACK_EX}{item}")

                    # Give the player the chosen item from the character
                    character_item = input(f"\nWhat item do you want from the character? ").lower().strip()
                    if character_item in zonemap[myPlayer.location]['ITEM_NAME'].lower():
                        myPlayer.inventory.append(character_item.title())
                        zonemap[myPlayer.location]['ITEM_NAME'] = "Nothing"

                        # Remove the traded item from the player's inventory
                        myPlayer.inventory.remove(choice.title())
                        print(f"You successfully traded for {Fore.YELLOW}{Style.BRIGHT}{character_item.title()}.")
                    else:
                        print("The character does not have that item.")
                else:
                    print("\nThe character is not willing to trade for that item.")
            else:
                print("You don't have that item.")
        else:
            print("No character here with that name.")
    else:
        print("This character is not willing to trade!")


def player_fight(attacker, defender, zone_items):
    character = input("Who do you want to attack? ").lower().strip()
    attacker = myPlayer.name
    defender = character.capitalize()

    # Check if the character is in the list of acceptable characters
    if character in fightable_characters:
        # Check if the character is in the current room
        if character in zonemap[myPlayer.location]["CHARACTER_NAME"].lower():
            in_battle = True
            while in_battle:
                if int(zonemap[myPlayer.location]['HEALTH']) > 0:
                    # Calculate the damage dealt by the attacker
                    damage = random.randint(50, 99)
                    # Subtract the damage from the defender's health points
                    zonemap[myPlayer.location]['HEALTH'] -= damage
                    # Save the updated character health points to the file
                    with open("zone_items.json", "w") as f:
                        json.dump(zone_items, f)
                    # Print a message indicating the amount of damage dealt
                    print(
                        f"\n{Fore.LIGHTBLUE_EX}{attacker}{Fore.RESET} dealt {Back.BLACK}{Fore.RED}{damage}{Style.RESET_ALL} points of damage to {Fore.RED}{defender}{Fore.RESET}.")
                    # Check if the defender is defeated
                    if int(zonemap[myPlayer.location]['HEALTH']) <= 0:
                        print(f"{Fore.RED}{defender}{Fore.RESET} has been defeated!")
                        # Give the player the item held by the defeated character
                        myPlayer.inventory.append(zonemap[myPlayer.location]['ITEM_NAME'].title())
                        print(
                            f"You received {Fore.YELLOW}{Style.BRIGHT}{zonemap[myPlayer.location]['ITEM_NAME'].title()}{Style.RESET_ALL} from {Fore.RED}{defender}{Fore.RESET}.")
                        # Check if the defender is John Briscoe
                        if character == "john briscoe":
                            print(f"\n{Fore.GREEN}OK FINE BRO! You can have Shelby...But you gotta give me the {Back.BLACK}{Fore.RED}Suicide Squad{Style.RESET_ALL}{Fore.GREEN} thing!")
                            zonemap[myPlayer.location]['ITEM_NAME'] = "Nothing"
                        else:
                            print(f"{Fore.LIGHTRED_EX}Please, have mercy on me! I'll do anything you want, just don't hurt me!{Fore.RESET}")
                            print(f"\nBet he'd love to see me {Back.LIGHTBLACK_EX}{Fore.BLUE}'use'{Style.RESET_ALL} this {Fore.YELLOW}{Style.BRIGHT}'Lighter'{Style.RESET_ALL} on his beloved {Fore.YELLOW}{Style.BRIGHT}'ECP Guidelines'{Style.RESET_ALL}.")
                            zonemap[myPlayer.location]['ITEM_NAME'] = "Nothing"
                        break
                    else:
                        print(
                            f"{Fore.RED}{defender}{Style.RESET_ALL} has {Back.BLACK}{Fore.RED}{zonemap[myPlayer.location]['HEALTH']}{Style.RESET_ALL} health points remaining.")
                    if int(zonemap[myPlayer.location]['HEALTH']) > 0:
                        finish_move = input(f"\n{Back.BLACK}{Fore.RED}Yes Buster, let it consume you! {Fore.YELLOW}Will you apply the finishing blow Y/N?!{Style.RESET_ALL}").lower()
                        if finish_move == "y":
                            print(f"\n{Back.LIGHTWHITE_EX}{Fore.LIGHTBLUE_EX}{Style.BRIGHT}{attacker} {Fore.BLACK}enters a trance like state. An ancient word lost to the ages passes his lips.{Style.RESET_ALL}")
                        else:
                            print(f"You've grown weaker {Fore.BLUE}{Style.BRIGHT}Buster{Style.RESET_ALL}...no longer the showman we once knew...")
                            break
                elif int(zonemap[myPlayer.location]['HEALTH']) <= 0:
                    break
        else:
            print("There is no character here with that name.")
    else:
        print("Sorry, you are not allowed to attack that character.")
# Load the character health points and items from the file, if it exists
    try:
        with open("zone_items.json", "r") as f:
            zone_items = json.load(f)
    except FileNotFoundError:
        pass


def player_use():
    use_item = input("What item do you want to use?").lower()
    on_what = input("What do you want to use {} on?".format(use_item.title())).lower()

    if use_item == "lighter" and on_what == "ecp guidelines":
        if use_item.title() in myPlayer.inventory and on_what.title() in myPlayer.inventory:
            myPlayer.inventory.remove("Lighter")
            myPlayer.inventory.remove("Ecp Guidelines")
            myPlayer.inventory.append("Locker Room Portal")
            print(f"\nThe {Fore.YELLOW}{Style.BRIGHT}ECP Guidelines{Style.RESET_ALL} have been lit! All thats left is this {Fore.YELLOW}{Style.BRIGHT}Locker Room Portal{Style.RESET_ALL}.")
            print(f"\n50/50 chance for a 50/50 guy! Maybe I ought to use this {Fore.YELLOW}portal{Fore.RESET} on {Fore.LIGHTBLUE_EX}myself{Fore.RESET}...")
        else:
            print("Invalid use. You don't have the item")
    elif use_item == "locker room portal" and on_what == "buster grubbs":
        if use_item.title() in myPlayer.inventory:
            # player_items.remove(use_item)
            print(f"\nYou used the Locker Room Portal. So that's what this {Fore.YELLOW}{Style.BRIGHT}Pack of Hotdogs{Style.RESET_ALL} was for all along...")
            print(f"You've done gone and done it {Fore.LIGHTBLUE_EX}Buster{Fore.RESET}. {Back.BLACK}{Fore.RED}GAME OVER!{Style.RESET_ALL}")
            game_over_dec = input(f"\nUntil next time Buster.. Close the game {Back.BLACK}{Fore.RED}Y/N{Style.RESET_ALL}? >").lower()
            if game_over_dec == "y":
                sys.exit()
            else:
                print("Go ahead and do some exploring Buster, everyone knows portals last forever...")

        else:
            print("Invalid use. You don't have the Locker Room Portal.")
    else:
        print("Invalid use for this combination")


def player_inventory():
    if myPlayer.inventory:
        print("You have the following items:")
        for item in myPlayer.inventory:
            print(f"{Fore.YELLOW}{Style.BRIGHT}{Back.LIGHTBLACK_EX}{item}")
    else:
        print("You have no items.")


def player_map():
    print(f"""
               {Fore.LIGHTBLACK_EX}{Back.LIGHTWHITE_EX} ----------------------------------------------------- {Back.RESET}
               {Back.LIGHTWHITE_EX} )  Room  9   |  Room  10  |  Room  11  |  Room  12  ( {Back.RESET}  
               {Back.LIGHTWHITE_EX}(             |            |            |             ){Back.RESET}
               {Back.LIGHTWHITE_EX} )   {Back.LIGHTBLACK_EX}{Fore.BLUE}Trade{Fore.LIGHTBLACK_EX}{Back.LIGHTWHITE_EX}    |   {Back.LIGHTBLACK_EX}{Fore.BLUE}Trade{Fore.LIGHTBLACK_EX}{Back.LIGHTWHITE_EX}    |   {Back.LIGHTBLACK_EX}{Fore.BLUE}Trade{Fore.LIGHTBLACK_EX}{Back.LIGHTWHITE_EX}    |   {Back.BLACK}{Fore.RED}Fight{Fore.LIGHTBLACK_EX}{Back.LIGHTWHITE_EX}    ( {Back.RESET}
               {Back.LIGHTWHITE_EX}(             |            |   {Back.BLACK}{Fore.RED}Fight{Fore.LIGHTBLACK_EX}{Back.LIGHTWHITE_EX}    |             ){Back.RESET}
               {Back.LIGHTWHITE_EX} )---------------------------------------------------( {Back.RESET}
               {Back.LIGHTWHITE_EX}(    Room 5   |   Room 6   |   Room 7   |   Room  8   ){Back.RESET}
               {Back.LIGHTWHITE_EX} )            |            |            |            ( {Back.RESET}
               {Back.LIGHTWHITE_EX}(    {Back.LIGHTBLACK_EX}{Fore.BLUE}Trade{Fore.LIGHTBLACK_EX}{Back.LIGHTWHITE_EX}    |   {Back.LIGHTBLACK_EX}{Fore.BLUE}Trade{Fore.LIGHTBLACK_EX}{Back.LIGHTWHITE_EX}    |   {Back.LIGHTBLACK_EX}{Fore.BLUE}Trade{Fore.LIGHTBLACK_EX}{Back.LIGHTWHITE_EX}    |    {Back.LIGHTBLACK_EX}{Fore.BLUE}Speak{Fore.LIGHTBLACK_EX}{Back.LIGHTWHITE_EX}    ){Back.RESET}
               {Back.LIGHTWHITE_EX} )            |            |            |            ( {Back.RESET}
               {Back.LIGHTWHITE_EX}(------------------------------------------------------------------{Back.RESET}
               {Back.LIGHTWHITE_EX} )   Room 1   |   Room 2   |   Room 3   |   Room 4   |  Room 4.5  |{Back.RESET}
               {Back.LIGHTWHITE_EX}(             |            |            |            |            |{Back.RESET}
               {Back.LIGHTWHITE_EX} )   {Back.LIGHTBLACK_EX}{Fore.BLUE}Speak{Fore.LIGHTBLACK_EX}{Back.LIGHTWHITE_EX}    |   {Back.LIGHTBLACK_EX}{Fore.BLUE}Trade{Fore.LIGHTBLACK_EX}{Back.LIGHTWHITE_EX}    |   {Back.LIGHTBLACK_EX}{Fore.BLUE}Trade{Fore.LIGHTBLACK_EX}{Back.LIGHTWHITE_EX}    |   {Back.LIGHTBLACK_EX}{Fore.BLUE}Trade{Fore.LIGHTBLACK_EX}{Back.LIGHTWHITE_EX}    |   {Back.LIGHTBLACK_EX}{Fore.BLUE}Trade{Fore.LIGHTBLACK_EX}{Back.LIGHTWHITE_EX}    |{Back.RESET}
               {Back.LIGHTWHITE_EX}(_____________|____________|____________|____________|____________|{Back.RESET} 
    """)


def player_help():
    print(player_guide)


def player_look():
    if zonemap[myPlayer.location]["CHARACTER_NAME"].lower() not in fightable_characters:
        print(f"\nUpon further inspection you see{Fore.LIGHTGREEN_EX}{Style.BRIGHT} " + zonemap[myPlayer.location]["CHARACTER_NAME"] +
              f" {Style.RESET_ALL}standing in front of you.")
        print(f"They're holding tight to their{Fore.YELLOW}{Style.BRIGHT} " + zonemap[myPlayer.location]["ITEM_NAME"] + f"{Style.RESET_ALL}!")
    else:
        print(f"\nUpon further inspection you see{Fore.RED}{Style.BRIGHT} " + zonemap[myPlayer.location][
            "CHARACTER_NAME"] +
              f" {Style.RESET_ALL}standing in front of you.")
        print(f"They're holding tight to their{Fore.YELLOW}{Style.BRIGHT} " + zonemap[myPlayer.location][
            "ITEM_NAME"] + f"{Style.RESET_ALL}!")


def main_game_loop():
    while not myPlayer.game_over:
        prompt()


# Game Func
def setup_game():
    # INTRO
    print(player_guide)
    print(f"You are in {Style.BRIGHT}{Fore.LIGHTWHITE_EX}" + str(zonemap[myPlayer.location][ZONENAME]))
    print_location()
    main_game_loop()


title_screen()
