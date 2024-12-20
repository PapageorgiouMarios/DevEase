
def rgb_text(r, g, b, text):
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"

def replace_color(text, content):
    text = text.replace(content, rgb_text(255, 255, 0, content))
    return text

def replace_color2(text, content):
    text = text.replace(content, rgb_text(255, 0, 0, content))
    return text

def print_with_rgb(text, r, g, b):
    text_with_color = rgb_text(r, g, b, text)
    print(text_with_color)

name = """
        ╔══════════════════════════════════════════════════════════════════════════╗
        ║       ((        \)) _  )  | (   //(  )   / (// )_  \   _ \  |  )         ║  
        ║       /(_))  \ |//(  \ // ) )  / ( //   )( ))  \/) )  (  _) (((          ║
        ║       (__))░(_)))__ _)((__//__/\_|_/_/_ \/_\/__/_(_)_/_)/_/\|_/          ║
        ║     ░░██████╗░███████╗██╗░░░██╗███████╗░█████╗░███████╗███████╗░         ║
        ║     ░░██╔══██╗██╔════╝██║░░░██║██╔════╝██╔══██╗██╔════╝██╔════╝░         ║
        ║     ░░██║░ ██║█████╗░ ██║░░░██║█████╗░░███████║███████╗█████╗░░░         ║
        ║     ░░██║░ ██║██╔══╝░ ╚██╗░██╔╝██╔══╝░░██╔══██║╚════██║██╔══╝░░░         ║
        ║     ░░██████╔╝███████╗░╚████╔╝░███████╗██║░░██║███████║███████╗░         ║
        ║     ░░╚═════╝░╚══════╝░╚═══╝░░╚══════╝╚═╝░░╚═╝╚══════╝╚══════╝░░         ║
        ║     ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░         ║
        ╚══════════════════════════════════════════════════════════════════════════╝

  - DevEase allow you to perform quick actions for your computer
    Skip search and clicks by typing the correct number
    Whatever you need fast we got it for you :)
"""

colors = [
    (0, 232, 108),  # Line 6
    (0, 220, 102),  # Line 7
    (0, 200, 96),   # Line 8
    (0, 185, 90),   # Line 9
    (0, 170, 83),   # Line 10
    (0, 154, 77),   # Line 11
    (0, 140, 66),   # Line 12
    (0, 121, 60),   # Line 13
    (0, 105, 52),    # Line 14
    (0, 92, 45),    # Line 15
    (0, 80, 38),    # Line 16
    (0, 75, 34),    # Line 17
    (0, 75, 34),    # Line 18
    (0, 232, 108),  # Line 19
    (0, 232, 108),  # Line 20
    (0, 232, 108)   # Line 21
]

lines = name.splitlines()

colored_lines = [ rgb_text(*colors[i % len(colors)], line) for i, line in enumerate(lines) ]

colored_name = "\n".join(colored_lines)

name = colored_name

selection_menu = """
  Selection Menu

        ╔════════════════════════════════════════════════════╗            ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ 
        ║    [1] Open Tool                                   ║          ░░███████████████▒░▒    
        ╠════════════════════════════════════════════════════╣         ░███████████████████▒▒    
        ║    [2] Open Website                                ║        ▒▒███▒░░▒████▒░░▒████▒▒    
        ╠════════════════════════════════════════════════════╣        ▒▒███████████████████▒▒    
        ║    [3] Empty recycle bin                           ║        ▒▒▒█████      ███████▒▒    
        ╠════════════════════════════════════════════════════╣          ▒▒▒█████████████▒▒▒    
        ║    [4] Review Device                               ║             ▒▒▒▒▒▒▒▒▒▒▒▒▒▒                        
        ╠════════════════════════════════════════════════════╣                        
        ║    [5] Exit                                        ║                           
        ╚════════════════════════════════════════════════════╝                         
                                                                                           
"""

color_for_selection_string = (0, 232, 108)

selection_menu_lines = selection_menu.splitlines()

colored_selection_menu = [ rgb_text(*color_for_selection_string, line) for line in selection_menu_lines ]

colored_selection_menu = "\n".join(colored_selection_menu)

selection_menu = colored_selection_menu

option_1_menu = """
  Selection Menu > Open Tool

  Hint: By selecting one of the options below, the device will instantly open the selected option.
  To return to the main menu just write Back (18)

        ╔═══════════════════════════╦══╦════════════════════════════╦══╦════════════════════════════╗
        ║╔════════════════════════╗ ║  ║ ╔════════════════════════╗ ║  ║ ╔════════════════════════╗ ║
        ║║ [1] Visual Studio      ║ ║  ║ ║ [7] Microsoft SQL      ║ ║  ║ ║ [13] Oracle VM         ║ ║
        ║╚════════════════════════╝ ║  ║ ╚════════════════════════╝ ║  ║ ╚════════════════════════╝ ║
        ║╔════════════════════════╗ ║  ║ ╔════════════════════════╗ ║  ║ ╔════════════════════════╗ ║
        ║║ [2] Visual Studio Code ║ ║  ║ ║ [8] Microsoft Word     ║ ║  ║ ║ [14] Unity             ║ ║
        ║╚════════════════════════╝ ║  ║ ╚════════════════════════╝ ║  ║ ╚════════════════════════╝ ║
        ║╔════════════════════════╗ ║  ║ ╔════════════════════════╗ ║  ║ ╔════════════════════════╗ ║
        ║║ [3] PyCharm            ║ ║  ║ ║ [9] Microsoft Excel    ║ ║  ║ ║ [15] Paint             ║ ║
        ║╚════════════════════════╝ ║  ║ ╚════════════════════════╝ ║  ║ ╚════════════════════════╝ ║
        ║╔════════════════════════╗ ║  ║ ╔════════════════════════╗ ║  ║ ╔════════════════════════╗ ║
        ║║ [4] IntelliJ           ║ ║  ║ ║ [10] Power Point       ║ ║  ║ ║ [16] Calculator        ║ ║
        ║╚════════════════════════╝ ║  ║ ╚════════════════════════╝ ║  ║ ╚════════════════════════╝ ║
        ║╔════════════════════════╗ ║  ║ ╔════════════════════════╗ ║  ║ ╔════════════════════════╗ ║
        ║║ [5] Notepad++          ║ ║  ║ ║ [11] Power BI          ║ ║  ║ ║ [17] Github Desktop    ║ ║
        ║╚════════════════════════╝ ║  ║ ╚════════════════════════╝ ║  ║ ╚════════════════════════╝ ║
        ║╔════════════════════════╗ ║  ║ ╔════════════════════════╗ ║  ║ ╔════════════════════════╗ ║
        ║║ [6] Android Studio     ║ ║  ║ ║ [12] CCleaner          ║ ║  ║ ║ [18] Back              ║ ║
        ║╚════════════════════════╝ ║  ║ ╚════════════════════════╝ ║  ║ ╚════════════════════════╝ ║
        ╚═══════════════════════════╩══╩════════════════════════════╩══╩════════════════════════════╝
"""

color_for_option_1 = (0, 232, 108)

option_menu_1_lines = option_1_menu.splitlines()

colored_option_1_menu = [ rgb_text(*color_for_selection_string, line) for line in option_menu_1_lines ]

colored_option_1_menu = "\n".join(colored_option_1_menu)

option_1_menu = colored_option_1_menu

option_1_menu = replace_color(option_1_menu, "  Hint: By selecting one of the options below, the device will instantly open the selected option.")
option_1_menu = replace_color(option_1_menu, "  To return to the main menu just write Back (18)")

option_2_menu = """
  Selection Menu > Open Website

  Hint: By selecting one of the options below, the device will instantly connect to the selected website
  To return to the main menu just write Back (15)
  
  Warning: Connect to a wifi network before trying to open a website

        ╔═══════════════════════════╦══╦════════════════════════════╦══╦════════════════════════════╗
        ║╔════════════════════════╗ ║  ║ ╔════════════════════════╗ ║  ║ ╔════════════════════════╗ ║
        ║║ [1] Google             ║ ║  ║ ║ [7] YouTube            ║ ║  ║ ║ [13] Chat GPT          ║ ║
        ║╚════════════════════════╝ ║  ║ ╚════════════════════════╝ ║  ║ ╚════════════════════════╝ ║
        ║╔════════════════════════╗ ║  ║ ╔════════════════════════╗ ║  ║ ╔════════════════════════╗ ║
        ║║ [2] Gmail              ║ ║  ║ ║ [8] Draw.io            ║ ║  ║ ║ [14] Stack Overflow    ║ ║
        ║╚════════════════════════╝ ║  ║ ╚════════════════════════╝ ║  ║ ╚════════════════════════╝ ║
        ║╔════════════════════════╗ ║  ║ ╔════════════════════════╗ ║  ║ ╔════════════════════════╗ ║
        ║║ [3] Microsoft Teams    ║ ║  ║ ║ [9] Facebook           ║ ║  ║ ║ [15] Back              ║ ║
        ║╚════════════════════════╝ ║  ║ ╚════════════════════════╝ ║  ║ ╚════════════════════════╝ ║
        ║╔════════════════════════╗ ║  ║ ╔════════════════════════╗ ║  ║                            ║
        ║║ [4] Dropbox            ║ ║  ║ ║ [10] Instagram         ║ ║  ║                            ║
        ║╚════════════════════════╝ ║  ║ ╚════════════════════════╝ ║  ║                            ║
        ║╔════════════════════════╗ ║  ║ ╔════════════════════════╗ ║  ║                            ║
        ║║ [5] Google Drive       ║ ║  ║ ║ [11] Gitlab            ║ ║  ║                            ║
        ║╚════════════════════════╝ ║  ║ ╚════════════════════════╝ ║  ║                            ║
        ║╔════════════════════════╗ ║  ║ ╔════════════════════════╗ ║  ║                            ║
        ║║ [6] Github             ║ ║  ║ ║ [12] Udemy             ║ ║  ║                            ║
        ║╚════════════════════════╝ ║  ║ ╚════════════════════════╝ ║  ║                            ║
        ╚═══════════════════════════╩══╩════════════════════════════╩══╩════════════════════════════╝
"""

color_for_option_2 = (0, 232, 108)

option_menu_2_lines = option_2_menu.splitlines()

colored_option_2_menu = [ rgb_text(*color_for_selection_string, line) for line in option_menu_2_lines ]

colored_option_2_menu = "\n".join(colored_option_2_menu)

option_2_menu = colored_option_2_menu

option_2_menu = replace_color(option_2_menu, "  Hint: By selecting one of the options below, the device will instantly connect to the selected website")
option_2_menu = replace_color(option_2_menu, "  To return to the main menu just write Back (15)")
option_2_menu = replace_color2(option_2_menu, "  Warning: Connect to a wifi network before trying to open a website")

option_3_menu = """
  Selection Menu > Empty Recycle Bin

  Hint: If there are any files inside your recycle bin, you can easily delete them permanently by
  selecting Y. If you wish to go back press N.

  Warning: Before procceeding, it is important to check your bin for any accidental deletes

"""

color_for_option_3 = (0, 232, 108)

option_menu_3_lines = option_3_menu.splitlines()

colored_option_3_menu = [ rgb_text(*color_for_selection_string, line) for line in option_menu_3_lines ]

colored_option_3_menu = "\n".join(colored_option_3_menu)

option_3_menu = colored_option_3_menu

option_3_menu = replace_color(option_3_menu, "  Hint: If there are any files inside your recycle bin, you can easily delete them permanently by")
option_3_menu = replace_color(option_3_menu, "  selecting Y. If you wish to go back press N.")
option_3_menu = replace_color2(option_3_menu, "  Warning: Before procceeding, it is important to check your bin for any accidental deletes")

option_4_menu = """
  Selection Menu > Review Device

  Hint: In case you wish to get easily important information for your device, choose one of the options
  below and we'll provide you with everything we can.
  To return to the main menu just write Back (13)

        ╔═══════════════════════════╦══╦════════════════════════════╦══╦════════════════════════════╗
        ║╔════════════════════════╗ ║  ║ ╔════════════════════════╗ ║  ║ ╔════════════════════════╗ ║
        ║║ [1] OS                 ║ ║  ║ ║ [7] Location           ║ ║  ║ ║ [13] Back              ║ ║
        ║╚════════════════════════╝ ║  ║ ╚════════════════════════╝ ║  ║ ╚════════════════════════╝ ║
        ║╔════════════════════════╗ ║  ║ ╔════════════════════════╗ ║  ║                            ║
        ║║ [2] RAM                ║ ║  ║ ║ [8] CPU                ║ ║  ║                            ║
        ║╚════════════════════════╝ ║  ║ ╚════════════════════════╝ ║  ║                            ║
        ║╔════════════════════════╗ ║  ║ ╔════════════════════════╗ ║  ║                            ║
        ║║ [3] Disk               ║ ║  ║ ║ [9] GPU                ║ ║  ║                            ║
        ║╚════════════════════════╝ ║  ║ ╚════════════════════════╝ ║  ║                            ║
        ║╔════════════════════════╗ ║  ║ ╔════════════════════════╗ ║  ║                            ║
        ║║ [4] Network            ║ ║  ║ ║ [10] Wi-Fi Config      ║ ║  ║                            ║
        ║╚════════════════════════╝ ║  ║ ╚════════════════════════╝ ║  ║                            ║
        ║╔════════════════════════╗ ║  ║ ╔════════════════════════╗ ║  ║                            ║
        ║║ [5] Antivirus Status   ║ ║  ║ ║ [11] Chipset           ║ ║  ║                            ║
        ║╚════════════════════════╝ ║  ║ ╚════════════════════════╝ ║  ║                            ║
        ║╔════════════════════════╗ ║  ║ ╔════════════════════════╗ ║  ║                            ║
        ║║ [6] Wi-fi Credentials  ║ ║  ║ ║ [12] Enviromental Vars ║ ║  ║                            ║
        ║╚════════════════════════╝ ║  ║ ╚════════════════════════╝ ║  ║                            ║
        ╚═══════════════════════════╩══╩════════════════════════════╩══╩════════════════════════════╝
"""

color_for_option_4 = (0, 232, 108)

option_menu_4_lines = option_4_menu.splitlines()

colored_option_4_menu = [ rgb_text(*color_for_selection_string, line) for line in option_menu_4_lines ]

colored_option_4_menu = "\n".join(colored_option_4_menu)

option_4_menu = colored_option_4_menu

option_4_menu = replace_color(option_4_menu, "  Hint: In case you wish to get easily important information for your device, choose one of the options")
option_4_menu = replace_color(option_4_menu, "  below and we'll provide you with everything we can.")
option_4_menu = replace_color(option_4_menu, "  To return to the main menu just write Back (13)")