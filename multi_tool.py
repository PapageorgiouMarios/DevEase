# Use custom .py files
import menus
import customSystem

# Use the menus as strings
# They can be edited in menus.py in case the design does not fit your taste
name = menus.name
selection_menu = menus.selection_menu
option_1_menu = menus.option_1_menu
option_2_menu = menus.option_2_menu
option_3_menu = menus.option_3_menu
option_4_menu = menus.option_4_menu

# Here we have a list of all .exe files of tools that you might use
# It's the same as double clicking the application icon
tool_paths = {
    '1': "Your .exe file path",
    '2': "Your .exe file path",
    '3': "Your .exe file path",
    '4': "Your .exe file path",
    '5': "Your .exe file path",
    '6': "Your .exe file path",
    '7': "Your .exe file path",
    '8': "Your .exe file path",
    '9': "Your .exe file path",
    '10': "Your .exe file path",
    '11': "Your .exe file path",
    '12': "Your .exe file path",
    '13': "Your .exe file path",
    '14': "Your .exe file path",
    '15': "Your .exe file path",
    '16': "Your .exe file path",
    '17': "Your .exe file path"
}

# Here are some known websites that many users visit occasionally
# All we need to open them are their links
website_urls = {
    '1': "https://www.google.com",
    '2': "https://mail.google.com",
    '3': "https://teams.microsoft.com",
    '4': "https://www.dropbox.com",
    '5': "https://drive.google.com",
    '6': "https://github.com",
    '7': "https://www.youtube.com",
    '8': "https://www.draw.io",
    '9': "https://www.facebook.com",
    '10': "https://www.instagram.com",
    '11': "https://gitlab.com",
    '12': "https://www.udemy.com",
    '13': "https://chat.openai.com",
    '14': "https://stackoverflow.com"
}

def handle_option_1():

    while True:

        customSystem.clearScreen()
        print(name)
        print(option_1_menu)
        print("")
        tool_input = input("  Select tool: ")

        if tool_input not in map(str, range(1, 19)):
            menus.print_with_rgb("  Invalid tool selection! Try again.", 255, 0, 0)
            customSystem.sleep(2)
            continue
        else:
                    
            if int(tool_input) == 18:

                print("  Returning to menu", end="")
                for i in range(3):
                    print(".", end="", flush=True) 
                    customSystem.sleep(1)
                print()
                break
                    
            selected_tool_path = tool_paths.get(tool_input)

            if selected_tool_path:
                try:
                    print(f"  Opening selected tool")
                    customSystem.open_tool(selected_tool_path)
                    customSystem.sleep(2)  
                    continue
                except Exception as e:
                    print(f"  Error opening the tool: {e}")
                    customSystem.sleep(2)
                    continue

def handle_option_2():
    while True:

        customSystem.clearScreen()
        print(name)
        print(option_2_menu)
        print("")
        tool_input = input("  Select website: ")

        if tool_input not in map(str, range(1, 16)):
            menus.print_with_rgb("  Invalid input! Try again.", 255, 0, 0)
            customSystem.sleep(2)
            continue
        else:
                    
            if int(tool_input) == 15:
                print("  Returning to menu", end="")
                for i in range(3):
                    print(".", end="", flush=True) 
                    customSystem.sleep(1)
                print()
                break
                    
            print(f"  Opening {tool_input}: {website_urls[tool_input]}")
            customSystem.open_website(website_urls[tool_input])
            customSystem.sleep(2)
            continue

def handle_option_3():
    while True:

        customSystem.clearScreen()
        print(name)
        print(option_3_menu)

        menus.print_with_rgb("  Scanning bin", 255, 255, 0)
        items_in_bin = customSystem.items_in_bin()

        if items_in_bin == 0:
            menus.print_with_rgb("  Trash bin is empty", 0, 255, 0)
            print("  Returning to menu", end="")
            for i in range(3):
                print(".", end="", flush=True) 
                customSystem.sleep(1)
            print()
            break
        else:
            empty_input = input("  Empty recycle bin? (Y/N): ")

            if empty_input == "Y":
                customSystem.empty_recycle_bin()
                print("  Returning to menu", end="")
                for i in range(3):
                    print(".", end="", flush=True) 
                    customSystem.sleep(1)
                print()
                break
            elif empty_input == "N":
                print("  Returning to menu", end="")
                for i in range(3):
                    print(".", end="", flush=True) 
                    customSystem.sleep(1)
                print()
                break
            else:
                menus.print_with_rgb("  Invalid input try again", 255, 0, 0)
                customSystem.sleep(1)
                continue

def handle_option_4():
    
    while True:
        customSystem.clearScreen()
        print(name)
        print(option_4_menu)

        info_input = input("  Select category: ")

        if info_input not in map(str, range(1, 14)):
            menus.print_with_rgb("  Invalid selection! Try again.", 255, 255, 0)
            customSystem.sleep(2)
            continue
        else:
            if int(info_input) == 1:
                customSystem.clearScreen()
                customSystem.OS_Info()
                print("")
                continue_input = input("Press any key to exit")
                continue

            if int(info_input) == 2:
                customSystem.clearScreen()
                customSystem.RAM_Info()
                print("")
                continue_input = input("Press any key to exit")
                continue

            if int(info_input) == 3:
                customSystem.clearScreen()
                customSystem.Disk_Info()
                print("")
                continue_input = input("Press any key to exit")
                continue

            if int(info_input) == 4:
                customSystem.clearScreen()
                customSystem.Network_Info()
                print("")
                continue_input = input("Press any key to exit")
                continue

            if int(info_input) == 5:
                customSystem.clearScreen()
                customSystem.Antivirus_Info()
                print("")
                continue_input = input("Press any key to exit")
                continue


            if int(info_input) == 6:
                customSystem.clearScreen()
                customSystem.WiFi_Info()
                print("")
                continue_input = input("Press any key to exit")
                continue
                    
            if int(info_input) == 7:
                customSystem.clearScreen()
                customSystem.Location_Info()
                print("")
                continue_input = input("Press any key to exit")
                continue

            if int(info_input) == 8:
                customSystem.clearScreen()
                customSystem.CPU_Info()
                print("")
                continue_input = input("Press any key to exit")
                continue

            if int(info_input) == 9:
                customSystem.clearScreen()
                customSystem.GPU_Info()
                print("")
                continue_input = input("Press any key to exit")
                continue

            if int(info_input) == 10:
                customSystem.clearScreen()
                customSystem.WiFi_Config_Info()
                print("")
                continue_input = input("Press any key to exit")
                continue


            if int(info_input) == 11:
                customSystem.clearScreen()
                customSystem.Chipset_Info()
                print("")
                continue_input = input("Press any key to exit")
                continue

            if int(info_input) == 12:
                customSystem.clearScreen()
                customSystem.Environment_Variables_Info()
                print("")
                continue_input = input("Press any key to exit")
                continue
                        
                        
            if int(info_input) == 13:
                print("  Returning to menu", end="")
                for i in range(3):
                    print(".", end="", flush=True) 
                    customSystem.sleep(1)
                print()
                break

while True:
    customSystem.clearScreen() # We always make sure to have a clean work
    print(name)
    print(selection_menu)
    user_input = input("  Select option: ")

    try:
        user_input = int(user_input)
    except ValueError:
        menus.print_with_rgb("  Invalid input! Please enter a number.", 255, 0, 0)
        print("")
        customSystem.sleep(2)
        continue

    if user_input not in [1, 2, 3, 4, 5]:
        menus.print_with_rgb("  User input wrong! Try again", 255, 0, 0)
        print("")
        customSystem.sleep(2)
        continue
    else:
        if user_input == 1:
            handle_option_1()
        
        if user_input == 2:
            handle_option_2()
            
        if user_input == 3:
            handle_option_3()
                
        if user_input == 4:
            handle_option_4()

        if user_input == 5:
            print("  Closing", end="")
            for i in range(3):
                print(".", end="", flush=True) 
                customSystem.sleep(1)
            print()
            break


    





