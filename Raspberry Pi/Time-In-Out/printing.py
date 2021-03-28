def logo():
    print(
        """
    `/ooooooooo-        -ooooooooo/`         
    m-/:::::::.          .:::..-./-m         
    M o                          o M         
    M -                          o M         
    M o                          o M         
    M -     h      //      h     o M         
    - .     N      oo      N     . -         
                   oo                        
                   oo                        
                 -oho                        
    -                            . -         
    M         .+`      `+.       - M         
    M o        -+ooooooo-        / M         
    M o                          - M         
    M o                          o M         
    m-/- .:::::.        .::::::::/-m         
    `/ooooooooo-        -ooooooooo/`         
    """
    )


def welcomeToFaceIt():
    line()
    print(

        """

 __          __  _                            _          __  __             _      
 \ \        / / | |                          | |        |  \/  |           | |     
  \ \  /\  / /__| | ___ ___  _ __ ___   ___  | |_ ___   | \  / | __ _ _ __ | | ___ 
   \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  | |\/| |/ _` | '_ \| |/ _ \\
    \  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) | | |  | | (_| | |_) | |  __/
     \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/  |_|  |_|\__,_| .__/|_|\___|
                                                                     | |           
                                                                     |_|           

                                                                            BY- VIRAJ BHARTIYA                                                                             
    """

    )
    line()


def line():
    print("""= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = """)


def chooseADirectory():
    print("""
    
  _____  _                        _____ _                                       _____  _               _                   
 |  __ \| |                      / ____| |                              /\     |  __ \(_)             | |                  
 | |__) | | ___  __ _ ___  ___  | |    | |__   ___   ___  ___  ___     /  \    | |  | |_ _ __ ___  ___| |_ ___  _ __ _   _ 
 |  ___/| |/ _ \/ _` / __|/ _ \ | |    | '_ \ / _ \ / _ \/ __|/ _ \   / /\ \   | |  | | | '__/ _ \/ __| __/ _ \| '__| | | |
 | |    | |  __/ (_| \__ \  __/ | |____| | | | (_) | (_) \__ \  __/  / ____ \  | |__| | | | |  __/ (__| || (_) | |  | |_| |
 |_|    |_|\___|\__,_|___/\___|  \_____|_| |_|\___/ \___/|___/\___| /_/    \_\ |_____/|_|_|  \___|\___|\__\___/|_|   \__, |
                                                                                                                      __/ |
                                                                                                                     |___/ 
                                                                                                 
        """

          )
    line()


def creatingDatabase():
    line()
    print(
        """
        
   _____                    _    _                  _____          _          _                       
  / ____|                  | |  (_)                |  __ \        | |        | |                      
 | |      _ __  ___   __ _ | |_  _  _ __    __ _   | |  | |  __ _ | |_  __ _ | |__    __ _  ___   ___ 
 | |     | '__|/ _ \ / _` || __|| || '_ \  / _` |  | |  | | / _` || __|/ _` || '_ \  / _` |/ __| / _ \\
 | |____ | |  |  __/| (_| || |_ | || | | || (_| |  | |__| || (_| || |_| (_| || |_) || (_| |\__ \|  __/
  \_____||_|   \___| \__,_| \__||_||_| |_| \__, |  |_____/  \__,_| \__|\__,_||_.__/  \__,_||___/ \___|
                                            __/ |                                                    
                                           |___/                                                     

        """
    )
    line()


def progressBar(iterable, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd="\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    total = len(iterable)
    # Progress Bar Printing Function

    def printProgressBar(iteration):
        percent = ("{0:." + str(decimals) + "f}").format(100 *
                                                         (iteration / (total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=printEnd)
    # Initial Call
    printProgressBar(0)
    # Update Progress Bar
    for i, item in enumerate(iterable):
        yield item
        printProgressBar(i + 1)
    # Print New Line on Complete
    print()


def productKeyInUse():
    print(
        """
        
  _____               _            _     _  __            _                        
 |  __ \             | |          | |   | |/ /           (_)                       
 | |__) | __ ___   __| |_   _  ___| |_  | ' / ___ _   _   _ _ __    _   _ ___  ___ 
 |  ___/ '__/ _ \ / _` | | | |/ __| __| |  < / _ \ | | | | | '_ \  | | | / __|/ _ \\
 | |   | | | (_) | (_| | |_| | (__| |_  | . \  __/ |_| | | | | | | | |_| \__ \  __/
 |_|   |_|  \___/ \__,_|\__,_|\___|\__| |_|\_\___|\__, | |_|_| |_|  \__,_|___/\___|
                                                   __/ |                           
                                                  |___/                            

        """
    )


def invalidKey():
    print(
        """
  _  __                        _     ______                    _ 
 | |/ /                       | |   |  ____|                  | |
 | ' / ___ _   _   _ __   ___ | |_  | |__ ___  _   _ _ __   __| |
 |  < / _ \ | | | | '_ \ / _ \| __| |  __/ _ \| | | | '_ \ / _` |
 | . \  __/ |_| | | | | | (_) | |_  | | | (_) | |_| | | | | (_| |
 |_|\_\___|\__, | |_| |_|\___/ \__| |_|  \___/ \__,_|_| |_|\__,_|
            __/ |                                                
           |___/                                                 
        """
    )


def close():
    print()
    line()
    print(
        """       

   _____ _           _             
  / ____| |         (_)            
 | |    | | ___  ___ _ _ __   __ _ 
 | |    | |/ _ \/ __| | '_ \ / _` |
 | |____| | (_) \__ \ | | | | (_| |
  \_____|_|\___/|___/_|_| |_|\__, |
                              __/ |
                             |___/ 
                 

        """
    )
    line()
