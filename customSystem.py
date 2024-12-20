import os
import time
import webbrowser
import subprocess
import platform
import ctypes
import re
import requests
import menus

# The customSystem.py serves multiple purposes
# For starters it's better to have seperate files and methods rathen than one huge file with over 1000+ lines of code
# The file uses all necessary third party libraries where we call specific methods. In this way we avoid using any other libraries to our main file
# It is also important to point that the code must work for Windows AND Linux

# Clear screen is used to clear the screen while the program runs
# Without it, we would run the program and all previous screens and results would be displayed
def clearScreen():
    if os.name == 'nt': # If the device uses Windows
        os.system('cls')
    else: # If the device uses Linux
        os.system('clear')

# Pause the program for a few seconds
def sleep(seconds):
    time.sleep(seconds)

# Opens a url provided by the user
def open_website(url):
    webbrowser.open(url)

# Opens a file path provided by the user
def open_tool(path):
    subprocess.Popen(path)

# Empties Recycle Bin/Trash 
def empty_recycle_bin():
    try:
        if platform.system() == 'Windows': # Windows 
            # Uses a Windows API to empty the Recycle Bin
            SHEmptyRecycleBin = ctypes.windll.shell32.SHEmptyRecycleBinW

            # Arguments for SHEmptyRecycleBin:
            # - None: Window handle (not used here, so we pass None)
            # - None: Path to a specific Recycle Bin (None means all Recycle Bins)
            # - 0: No special flags (e.g., no confirmation dialog)

            result = SHEmptyRecycleBin(None, None, 0)
            menus.print_with_rgb("  Recycle Bin emptied successfully!", 0, 255, 0)
        
        elif platform.system() == 'Linux': # Linux
            # Use the 'gio trash --empty' command, which is part of GNOME's file management utilities
            # This empties all items in the Trash
            os.system('gio trash --empty')
            menus.print_with_rgb("  Trash emptied successfully!", 0, 255, 0)

        else:
            menus.print_with_rgb("  Unsupported OS!", 255, 0, 0)

    except Exception as e:
        print(f"Error: {e}")

# Searches and counts items in the device's recycle bin (Windows) or trash (Mac/Linux)
def items_in_bin():
    try:
        if platform.system() == 'Windows':
            # The path to the Recycle Bin in Windows
            recycle_bin_path = "C:\\$Recycle.Bin"
            total_files = 0  # Counter for total valid files in the Recycle Bin
            file_names = []  # List to store valid file paths

            # Walk through the Recycle Bin directory and its subdirectories
            for root, _, files in os.walk(recycle_bin_path):
                for file in files:
                    try:
                        # Construct the full path to the file
                        file_path = os.path.join(root, file)

                        # Skip the system metadata file "desktop.ini"
                        # What is desktop.ini? It is a text file which allows you to specify how a file system folder is viewed 
                        # It is not visible in the recycle bin and it can't be deleted with the default Empty bin command
                        if "desktop.ini" in file_path.lower():
                            continue

                        # Skip files that are not readable due to lack of permissions
                        # We are always careful what we delete
                        # It would be wise to check your files before deleting them
                        if not os.access(file_path, os.R_OK):
                            continue

                        # Add valid files to the list and increment the file counter
                        file_names.append(file_path)
                        total_files += 1

                    except (FileNotFoundError, PermissionError, OSError) as e:
                        # Handle specific errors, such as missing files or permission issues
                        print(f"   Skipping file due to error: {e}")
                        continue

            return total_files

        elif platform.system() == 'Linux':  # Linux system
            # Run the Linux command `gio trash --list` to list items in the Trash
            result = subprocess.run(['gio', 'trash', '--list'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            items = result.stdout.decode().splitlines()  # Decode the output and split into lines
            return len(items)

        else:
            # If the operating system is not supported
            print("  Unsupported OS!")
            return None

    except PermissionError:
        # Handle permission errors (e.g., if the user doesn't have access to the Recycle Bin)
        print("Permission Denied: Run as Administrator to access Recycle Bin contents.")
        return None

    except Exception as e:
        # Handle any other unexpected errors
        print(f"Error: {e}")
        return None
 
# The methods below are used in option 4 (Review Device)
# They display important information related to the user's device

# Display device's Operating System
def OS_Info():
    print("")
    menus.print_with_rgb("  DEVICE OPERATING SYSTEM INFO", 255, 255, 0)

    # Collect system information
    info = [
        f"System: {platform.system()}",  # e.g., Windows, Linux
        f"Node Name: {platform.node()}",  # Network name of the machine
        f"Release: {platform.release()}",  # OS Release version
        f"Version: {platform.version()}",  # OS version details
        f"Machine: {platform.machine()}",  # Architecture: x86_64, ARM, etc.
        f"Processor: {platform.processor()}",  # CPU model information
        f"Platform: {platform.platform()}",  # Full OS description
        f"OS Name (using os module): {os.name}",  # Name of the OS module interface (posix, nt, etc.)
    ]
    
    # Find the maximum length of strings to adjust the box width dynamically
    max_length = max(len(line) for line in info)
    box_width = max_length + 2  # Add padding
    
    # Print the box with the OS information
    menus.print_with_rgb(f"  ╔{'═' * box_width}╗", 0, 255, 255)

    for line in info:
        menus.print_with_rgb(f"  ║ {line.ljust(max_length)} ║", 0, 255, 255)
    menus.print_with_rgb(f"  ╚{'═' * box_width}╝", 0, 255, 255)

# Display device's RAM (Used, Total and Percentage of used RAM)
def RAM_Info():
    print("")
    menus.print_with_rgb("  DEVICE RAM SPACE INFO", 255, 255, 0)

    system = platform.system()

    ram_info = []

    if system == "Windows":
        try:
            # Fetch total RAM and free RAM using Windows Management Instrumentation Command
            total_ram = os.popen("wmic OS get TotalVisibleMemorySize /Value").read()
            free_ram = os.popen("wmic OS get FreePhysicalMemory /Value").read()

            # Extract and convert the values from the raw strings into integers
            total_ram = int(total_ram.split("=")[1].strip())  # Total RAM in kilobytes
            free_ram = int(free_ram.split("=")[1].strip())    # Free RAM in kilobytes
            used_ram = total_ram - free_ram  # Calculate used RAM

            # Convert values from kilobytes to gigabytes for easier reading
            total_gb = round(total_ram / (1024 * 1024), 2)  # Total RAM in GB
            used_gb = round(used_ram / (1024 * 1024), 2)    # Used RAM in GB
            used_percent = round((used_ram / total_ram) * 100, 2)  # Percentage of used RAM

            # Prepare RAM information for display
            ram_info = [
                f"Total RAM: {total_gb} GB",
                f"Used RAM: {used_gb} GB",
                f"RAM Usage Percentage: {used_percent}%"
            ]
        except Exception as e:
            ram_info = [f"Error fetching RAM info: {e}"]

    # Check if the operating system is Linux
    elif system == "Linux":
        try:
            with open("/proc/meminfo", "r") as meminfo:
                mem_data = {}
                for line in meminfo:
                    parts = line.split(":")
                    key = parts[0].strip()
                    value = parts[1].split()[0]
                    mem_data[key] = int(value)

            # Extract total and free memory values from the data
            total_ram = mem_data.get("MemTotal", 0)  # Total RAM in kilobytes
            free_ram = mem_data.get("MemFree", 0) + mem_data.get("Buffers", 0) + mem_data.get("Cached", 0)  # Free RAM in kilobytes
            used_ram = total_ram - free_ram  # Calculate used RAM

            # Convert values from kilobytes to gigabytes
            total_gb = round(total_ram / (1024 * 1024), 2)  # Total RAM in GB
            used_gb = round(used_ram / (1024 * 1024), 2)    # Used RAM in GB
            used_percent = round((used_ram / total_ram) * 100, 2)  # Percentage of used RAM

            # Prepare RAM information for display
            ram_info = [
                f"Total RAM: {total_gb} GB",
                f"Used RAM: {used_gb} GB",
                f"RAM Usage Percentage: {used_percent}%"
            ]

        except Exception as e:
            ram_info = [f"Error fetching RAM info: {e}"]
 
    else:
        ram_info = ["Unsupported Operating System for RAM Info."]

    max_length = max(len(line) for line in ram_info)
    box_width = max_length + 2
    
    menus.print_with_rgb(f"  ╔{'═' * box_width}╗", 0, 255, 255)

    for line in ram_info:
        menus.print_with_rgb(f"  ║ {line.ljust(max_length)} ║", 0, 255, 255)

    menus.print_with_rgb(f"  ╚{'═' * box_width}╝", 0, 255, 255)

# Display device's Disk ( Drive, Total Size (GB), Free Space (GB), Used Space (GB), Usage (%))
def Disk_Info():
    print("")

    menus.print_with_rgb("  DEVICE DISK INFO", 255, 255, 0)
    
    system = platform.system()

    disk_info = []

    if system == "Windows":
        # Get the result of disk information in Windows
        result = os.popen('wmic logicaldisk get DeviceID, FreeSpace, Size').read().splitlines()

        for line in result[1:]:
            parts = line.split()
            if len(parts) == 3:
                drive = parts[0]
                free_space = int(parts[1]) if parts[1].isdigit() else 0
                total_size = int(parts[2]) if parts[2].isdigit() else 0
                used_space = total_size - free_space
                usage_percent = (used_space / total_size) * 100 if total_size else 0

                # Add the formatted information to the list
                disk_info.append(
                    f"Drive: {drive}\n"
                    f"Total Size: {total_size / 1e9:.2f} GB\n"
                    f"Free Space: {free_space / 1e9:.2f} GB\n"
                    f"Used Space: {used_space / 1e9:.2f} GB\n"
                    f"Usage: {usage_percent:.2f}%"
                )

    elif system == "Linux":
        # Get the result of disk information in Linux/macOS
        result = os.popen("df -BG | grep '^/'").read().splitlines()

        for line in result:
            parts = line.split()
            if len(parts) >= 6:
                filesystem, size, used, avail, usage, mount = parts[:6]

                # Add the formatted information to the list
                disk_info.append(
                    f"Filesystem: {filesystem}\n"
                    f"Size: {size.strip('G')} GB\n"
                    f"Used: {used.strip('G')} GB\n"
                    f"Available: {avail.strip('G')} GB\n"
                    f"Usage: {usage}\n"
                    f"Mounted on: {mount}"
                )

    else:
        disk_info = ["Unsupported Operating System for Disk Info."]

    max_length = max(len(line) for info in disk_info for line in info.splitlines())
    box_width = max_length + 2

    menus.print_with_rgb(f"  ╔{'═' * box_width}╗", 0, 255, 255)

    for info in disk_info:
        for line in info.splitlines():
            menus.print_with_rgb(f"  ║ {line.ljust(max_length)} ║", 0, 255, 255)

    menus.print_with_rgb(f"  ╚{'═' * box_width}╝", 0, 255, 255)

# Display all Network's interfaces
def Network_Info():
    print("")
    menus.print_with_rgb("  DEVICE NETWORK INFO", 255, 255, 0)

    system = platform.system()

    network_info = []

    if system == "Windows":
        try:
            result = os.popen("ipconfig").read().splitlines()
            interfaces = []
            current_interface = None
            for line in result:
                if "adapter" in line.lower():  # Identifies the start of a new interface block
                    if current_interface:
                        interfaces.append(current_interface)
                    current_interface = {"Name": line.strip()}
                elif "IPv4" in line:  # Extracting the IPv4 address
                    current_interface["IP Address"] = line.split(":")[1].strip()
                elif "Subnet Mask" in line:  # Extracting the Subnet Mask
                    current_interface["Netmask"] = line.split(":")[1].strip()
                elif "Default Gateway" in line:  # Extracting the Default Gateway
                    current_interface["Gateway"] = line.split(":")[1].strip()

            if current_interface:
                interfaces.append(current_interface)

            # Prepare network information for display
            for interface in interfaces:
                network_info.append(
                    f"Interface: {interface.get('Name', 'N/A')}\n"
                    f"IP Address: {interface.get('IP Address', 'N/A')}\n"
                    f"Netmask: {interface.get('Netmask', 'N/A')}\n"
                    f"Gateway: {interface.get('Gateway', 'N/A')}"
                )

        except Exception as e:
            network_info = [f"Error fetching network info: {e}"]

    elif system == "Linux":
        try:
            result = None
            if os.system('which ifconfig > /dev/null 2>&1') == 0:
                result = os.popen("ifconfig").read().splitlines()
            else:
                result = os.popen("ip addr show").read().splitlines()

            interfaces = []
            current_interface = None
            for line in result:
                if "en" in line or "eth" in line or "wlan" in line:  # Identifies the start of a new interface block
                    if current_interface:
                        interfaces.append(current_interface)
                    current_interface = {"Name": line.split()[0]}
                elif "inet " in line:  # Extracting the IP address (IPv4)
                    ip_address = line.split()[1]
                    current_interface["IP Address"] = ip_address
                elif "netmask" in line:  # Extracting the netmask
                    netmask = line.split()[3]
                    current_interface["Netmask"] = netmask
                elif "broadcast" in line:  # Extracting the broadcast address
                    broadcast = line.split()[5]
                    current_interface["Broadcast"] = broadcast

            if current_interface:
                interfaces.append(current_interface)

            # Prepare network information for display
            for interface in interfaces:
                network_info.append(
                    f"Interface: {interface.get('Name', 'N/A')}\n"
                    f"IP Address: {interface.get('IP Address', 'N/A')}\n"
                    f"Netmask: {interface.get('Netmask', 'N/A')}\n"
                    f"Broadcast: {interface.get('Broadcast', 'N/A')}"
                )

        except Exception as e:
            network_info = [f"Error fetching network info: {e}"]

    else:
        network_info = ["Unsupported Operating System for Network Info."]

    # Display each interface in its own box
    for info in network_info:
        max_length = max(len(line) for line in info.splitlines())
        box_width = max_length + 2

        menus.print_with_rgb(f"  ╔{'═' * box_width}╗", 0, 255, 255)

        for line in info.splitlines():
            menus.print_with_rgb(f"  ║ {line.ljust(max_length)} ║", 0, 255, 255)

        menus.print_with_rgb(f"  ╚{'═' * box_width}╝", 0, 255, 255)
        print("")

# Display all device's antivirus programs' states (Enabled/Disabled)
def Antivirus_Info():
    print("")

    menus.print_with_rgb("  DEVICE ANTIVIRUS INFO", 255, 255, 0)

    current_os = platform.system()

    antivirus_info = []

    if current_os == 'Windows':
        try:
            # Windows-specific: Check antivirus status using the Security Center
            import win32com.client # We import here to avoid any errors while building Docker
            wmi = win32com.client.Dispatch('WbemScripting.SWbemLocator')
            service = wmi.ConnectServer('.', 'root\\securitycenter2')
            query = 'SELECT * FROM AntiVirusProduct'
            antivirus = service.ExecQuery(query)
            
            if not antivirus:
                antivirus_info.append("No antivirus found on Windows.")
            else:
                for product in antivirus:
                    name = product.displayName
                    state = "Enabled" if product.productState == 397568 else "Disabled"
                    antivirus_info.append(f"Antivirus: {name}, Status: {state}")
        
        except Exception as e:
            antivirus_info.append(f"Error checking antivirus status on Windows: {e}")

    elif current_os == 'Linux':
        try:
            # Linux-specific: Check if ClamAV (or other antivirus software) is installed
            result = subprocess.run(['clamdscan', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if result.returncode == 0:
                antivirus_info.append("ClamAV is installed on Linux.")
            else:
                antivirus_info.append("ClamAV is not installed on Linux.")
        except FileNotFoundError:
            antivirus_info.append("ClamAV is not installed on Linux.")
        except Exception as e:
            antivirus_info.append(f"Error checking antivirus status on Linux: {e}")

    else:
        antivirus_info.append("Unsupported OS for antivirus information.")

    # Calculate the maximum line length for box sizing
    max_length = max(len(line) for line in antivirus_info)
    box_width = max_length + 2

    # Print all antivirus info inside a single box
    menus.print_with_rgb(f"  ╔{'═' * box_width}╗", 0, 255, 255)

    for line in antivirus_info:
        menus.print_with_rgb(f"  ║ {line.ljust(max_length)} ║", 0, 255, 255)

    menus.print_with_rgb(f"  ╚{'═' * box_width}╝", 0, 255, 255)

# Display all saved wifi networks and their passwords
def WiFi_Info():
    print("")

    menus.print_with_rgb("  DEVICE WI-FI INFO", 255, 255, 0)

    system = platform.system()

    if system == "Windows":
        try:
            # Collect all Wi-Fi network names
            output = subprocess.getoutput(f'netsh wlan show profiles name=*')
            wifi_info = []
            for name_index in [m.start() for m in re.finditer('Name', output)]:
                wifi_name = output[name_index:name_index+output[name_index:].find('Control options')].split(':')[1].strip()

                # Retrieve the password for each Wi-Fi network
                wifi_output = subprocess.getoutput(f'netsh wlan show profile name="{wifi_name}" key=clear')
                password = "No key content"  # Default if no password found
                if "Key Content" in wifi_output:
                    password = wifi_output[wifi_output.find('Key Content') + len('Key Content') + 1:].splitlines()[0].strip()

                wifi_info.append((wifi_name, password))  # Store the Wi-Fi name and password as a tuple

            # Calculate the maximum length for formatting the box
            max_name_length = max(len(info[0]) for info in wifi_info) if wifi_info else 0
            max_password_length = max(len(info[1]) for info in wifi_info) if wifi_info else 0
            box_width = max_name_length + max_password_length + 7  # 7 for spaces and separator

            # Print the box header
            menus.print_with_rgb(f"  ╔{'═' * box_width}╗", 0, 255, 255)
            menus.print_with_rgb(f"  ║ {'Wi-Fi Name'.ljust(max_name_length)} ║ {'Password '.ljust(max_password_length)} ║", 0, 255, 255)
            menus.print_with_rgb(f"  ╠{'═' * box_width}╣", 0, 255, 255)

            # Print each Wi-Fi network name and password in the box
            for name, password in wifi_info:
                menus.print_with_rgb(f"  ║ {name.ljust(max_name_length)} ║ {password.ljust(max_password_length)} ║", 0, 255, 255)

            # Close the box
            menus.print_with_rgb(f"  ╚{'═' * box_width}╝", 0, 255, 255)

        except Exception as e:
            print(f"Error fetching Wi-Fi info: {e}")

    elif system == "Linux":
        try:
            # Use iwlist to scan for Wi-Fi networks (requires wireless-tools)
            output = subprocess.getoutput("sudo iwlist wlan0 scan")
            wifi_info = []

            # Parse the output from iwlist
            for entry in output.split("Cell"):
                if "ESSID" in entry:
                    wifi_name = re.search('ESSID:"(.*?)"', entry).group(1)
                    wifi_info.append((wifi_name, "N/A"))  # No password available from iwlist scan

            # Display Wi-Fi info
            if wifi_info:
                max_name_length = max(len(info[0]) for info in wifi_info)
                max_password_length = 2  # Just for the 'N/A' password value
                box_width = max_name_length + max_password_length + 7

                # Print the Wi-Fi network info
                menus.print_with_rgb(f"  ╔{'═' * box_width}╗", 0, 255, 255)
                menus.print_with_rgb(f"  ║ {'Wi-Fi Name'.ljust(max_name_length)} ║ {'Security'.ljust(max_password_length)} ║", 0, 255, 255)
                menus.print_with_rgb(f"  ╠{'═' * box_width}╣", 0, 255, 255)

                for name, password in wifi_info:
                    menus.print_with_rgb(f"  ║ {name.ljust(max_name_length)} ║ {password.ljust(max_password_length)} ║", 0, 255, 255)

                menus.print_with_rgb(f"  ╚{'═' * box_width}╝", 0, 255, 255)
            else:
                print("No Wi-Fi networks found.")

        except Exception as e:
            print(f"Error fetching Wi-Fi info: {e}")

    else:
        print("Unsupported OS for Wi-Fi Info.")

# Display location based on user's public IP address
# Warning: The code does NOT give the device's exact location. Only the ISP location
def Location_Info():

    print("")
    menus.print_with_rgb("  DEVICE LOCATION INFO", 255, 255, 0)

    ip_response = requests.get('http://api.ipify.org').text
    ip_info_response = requests.get(f'http://ip-api.com/json/{ip_response}').json()

    menus.print_with_rgb("  WARNING: DO NOT SHARE YOUR PUBLIC IP ADDRESS WITH ANYONE!", 255, 0, 0)
    ip_message = "  Your public IP address is: " + ip_response
    menus.print_with_rgb(ip_message, 255, 0, 0)
    print("")

    location_info = []
    
    location_info.append(f"IP Address: {ip_response}")
    for key, value in ip_info_response.items():
        location_info.append(f"{key}: {value}")
    
    max_length = max(len(line) for line in location_info)
    box_width = max_length + 2
    
    menus.print_with_rgb(f"  ╔{'═' * box_width}╗", 0, 255, 255)

    for line in location_info:
        menus.print_with_rgb(f"  ║ {line.ljust(max_length)} ║", 0, 255, 255)

    menus.print_with_rgb(f"  ╚{'═' * box_width}╝", 0, 255, 255)

# Display device's CPU
def CPU_Info():

    print("")
    menus.print_with_rgb("  DEVICE CPU INFORMATION", 255, 255, 0)

    system = platform.system()
    cpu_info = []

    try:
        if system == "Windows":
            cpu_info_raw = os.popen("wmic cpu get Name,NumberOfCores,NumberOfLogicalProcessors,MaxClockSpeed /Format:List").read().strip()
            cpu_info_dict = {}
            for line in cpu_info_raw.splitlines():
                if "=" in line:
                    key, value = line.split("=", 1)
                    cpu_info_dict[key.strip()] = value.strip()

            cpu_info.append(f"Processor Name: {cpu_info_dict.get('Name', 'N/A')}")
            cpu_info.append(f"Cores: {cpu_info_dict.get('NumberOfCores', 'N/A')}")
            cpu_info.append(f"Logical Processors: {cpu_info_dict.get('NumberOfLogicalProcessors', 'N/A')}")
            cpu_info.append(f"Max Clock Speed: {cpu_info_dict.get('MaxClockSpeed', 'N/A')} MHz")

        elif system == "Linux":
            with open("/proc/cpuinfo", "r") as cpuinfo:
                data = cpuinfo.read()
                model_name = re.search(r"model name\s+:\s+(.+)", data)
                cores = re.findall(r"^processor\s+:", data, re.MULTILINE)

                cpu_info.append(f"Processor Name: {model_name.group(1) if model_name else 'N/A'}")
                cpu_info.append(f"Cores: {len(cores)}")

            # Fetch additional details using lscpu
            lscpu_output = subprocess.getoutput("lscpu")
            for line in lscpu_output.splitlines():
                if "CPU MHz" in line:
                    cpu_info.append(f"Clock Speed: {line.split(':')[1].strip()} MHz")

        else:
            cpu_info.append("Unsupported Operating System for CPU Info.")

    except Exception as e:
        cpu_info.append(f"Error fetching CPU info: {e}")

    max_length = max(len(line) for line in cpu_info)
    box_width = max_length + 2

    menus.print_with_rgb(f"  ╔{'═' * box_width}╗", 0, 255, 255)

    for line in cpu_info:
        menus.print_with_rgb(f"  ║ {line.ljust(max_length)} ║", 0, 255, 255)

    menus.print_with_rgb(f"  ╚{'═' * box_width}╝", 0, 255, 255)

# Display device's GPU
def GPU_Info():
    menus.print_with_rgb("  DEVICE GPU INFORMATION", 255, 255, 0)

    system = platform.system()
    gpu_info = []

    try:
        if system == "Windows":
            result = subprocess.check_output("wmic path win32_VideoController get Name,AdapterRAM,DriverVersion", shell=True, universal_newlines=True)
            for line in result.splitlines()[1:]:
                if line.strip():
                    parts = line.split()
                    name = " ".join(parts[:-2])
                    adapter_ram = parts[-2] if parts[-2].isdigit() else "N/A"
                    driver_version = parts[-1]
                    adapter_ram_gb = round(int(adapter_ram) / (1024**3), 2) if adapter_ram != "N/A" else "N/A"

                    gpu_info.append(f"GPU Name: {name}")
                    gpu_info.append(f"Adapter RAM: {adapter_ram_gb} GB")
                    gpu_info.append(f"Driver Version: {driver_version}")

        elif system == "Linux":
            try:
                result = subprocess.check_output("lspci | grep -i 'vga\|3d\|2d'", shell=True, universal_newlines=True)
                for line in result.splitlines():
                    gpu_info.append(f"{line.strip()}")

                try:
                    nvidia_result = subprocess.check_output("nvidia-smi --query-gpu=name,memory.total,driver_version --format=csv,noheader,nounits", shell=True, universal_newlines=True)
                    for gpu in nvidia_result.splitlines():
                        name, memory, driver = gpu.split(", ")
                        gpu_info.append(f"GPU Name: {name}")
                        gpu_info.append(f"Total Memory: {memory} MB")
                        gpu_info.append(f"Driver Version: {driver}")
                except subprocess.CalledProcessError:
                    gpu_info.append("No NVIDIA GPUs detected.")

            except Exception as e:
                gpu_info.append(f"Error fetching GPU information: {e}")

        else:
            gpu_info.append("Unsupported Operating System for GPU Info.")

    except Exception as e:
        gpu_info.append(f"Error: {e}")

    max_length = max(len(line) for line in gpu_info)
    box_width = max_length + 2

    menus.print_with_rgb(f"  ╔{'═' * box_width}╗", 0, 255, 255)

    for line in gpu_info:
        menus.print_with_rgb(f"  ║ {line.ljust(max_length)} ║", 0, 255, 255)

    menus.print_with_rgb(f"  ╚{'═' * box_width}╝", 0, 255, 255)

# Display Signal Quality, other networks, adapter and hosted network info 
def WiFi_Config_Info():
    print("")
    menus.print_with_rgb("  DISPLAY WI-FI CONFIG INFORMATION", 255, 255, 0)
    print("")
    
    system = platform.system()

    if system == "Windows":
        try:
            # Fetch each Wi-Fi information separately
            interfaces_result = subprocess.getoutput("netsh wlan show interfaces")
            networks_result = subprocess.getoutput("netsh wlan show networks")
            drivers_result = subprocess.getoutput("netsh wlan show drivers")
            hostednetwork_result = subprocess.getoutput("netsh wlan show hostednetwork")

            # Display the results from each command in separate boxes
            menus.print_with_rgb("==== Current Wi-Fi Interface Details ====", 0, 255, 255)
            print("\n   " + interfaces_result + "\n")
            menus.print_with_rgb("=========================================", 0, 255, 255)

            menus.print_with_rgb("==== Available Wi-Fi Networks ====", 0, 255, 255)
            print("\n   " + networks_result + "\n")
            menus.print_with_rgb("===================================", 0, 255, 255)

            menus.print_with_rgb("==== Wi-Fi Adapter Information ====", 0, 255, 255)
            print("\n   " + drivers_result + "\n")
            menus.print_with_rgb("===================================", 0, 255, 255)

            menus.print_with_rgb("==== Hosted Network Details ====", 0, 255, 255)
            print("\n   " + hostednetwork_result + "\n")
            menus.print_with_rgb("===================================", 0, 255, 255)

        except Exception as e:
            menus.print_with_rgb(f"   Error fetching Wi-Fi signal information on Windows: {e}", 255, 0, 0)

    elif system == "Linux":
        try:
            iwconfig_result = subprocess.getoutput("iwconfig 2>/dev/null")
            iw_result = subprocess.getoutput("iw dev wlan0 link 2>/dev/null")

            menus.print_with_rgb("==== Wi-Fi Interface Details (iwconfig) ====", 0, 255, 255)
            print("\n   " + iwconfig_result + "\n")
            menus.print_with_rgb("===========================================", 0, 255, 255)

            menus.print_with_rgb("==== Wi-Fi Link Information (iw) ====", 0, 255, 255)
            print("\n   " + iw_result + "\n")
            menus.print_with_rgb("=======================================", 0, 255, 255)

        except Exception as e:
            menus.print_with_rgb(f"   Error fetching Wi-Fi signal information on Linux: {e}", 255, 0, 0)

    else:
        menus.print_with_rgb("   Unsupported Operating System for Wi-Fi Signal Strength.", 255, 0, 0)

# Display device's Chipset
def Chipset_Info():
    
    print("")
    menus.print_with_rgb("  DEVICE CHIPSET INFORMATION", 255, 255, 0)

    system = platform.system()
    chipset_info = []

    try:
        if system == "Windows":

            manufacturer = subprocess.getoutput("wmic baseboard get manufacturer /value").split("=")[1].strip()
            chipset_info.append(f"Manufacturer: {manufacturer}")

            product = subprocess.getoutput("wmic baseboard get product /value").split("=")[1].strip()
            chipset_info.append(f"Product: {product}")

            serial_number = subprocess.getoutput("wmic baseboard get serialnumber /value").split("=")[1].strip()
            chipset_info.append(f"Serial Number: {serial_number}")

            version = subprocess.getoutput("wmic baseboard get version /value").split("=")[1].strip()
            chipset_info.append(f"Version: {version}")


        elif system == "Linux":

            chipset_info.append("Fetching Chipset information on Linux...")
            chipset_info_output = subprocess.getoutput("lspci | grep -i chipset")
            
            chipset_info.append("==== Chipset Information (lspci) ====")
            for line in chipset_info_output.splitlines():
                chipset_info.append(f"Chipset Info: {line.strip()}")

        else:
            chipset_info.append("Unsupported Operating System for Chipset Info.")

    except Exception as e:
        chipset_info.append(f"Error fetching Chipset info: {e}")

    max_length = max(len(line) for line in chipset_info)
    box_width = max_length + 2

    menus.print_with_rgb(f"  ╔{'═' * box_width}╗", 0, 255, 255)

    for line in chipset_info:
        menus.print_with_rgb(f"  ║ {line.ljust(max_length)} ║", 0, 255, 255)

    menus.print_with_rgb(f"  ╚{'═' * box_width}╝", 0, 255, 255)

# Display all device's enviromental variables
def Environment_Variables_Info():
    print("")
    menus.print_with_rgb("  DEVICE ENVIRONMENT VARIABLES", 255, 255, 0)
    print("") 
    menus.print_with_rgb("---------------------------------------------------------------------", 0, 255, 255)

    try:
        env_vars = os.environ

        if env_vars:
            count = 1
            for var, value in env_vars.items():
                menus.print_with_rgb(f"   {count:<3}. {var:<50} |", 0, 255, 255)
                menus.print_with_rgb(f"   {' ' * 10}{value}", 0, 0, 255)
                print("") 
                count += 1
        else:
            menus.print_with_rgb("   No environment variables found.", 255, 0, 0)

    except Exception as e:
        menus.print_with_rgb(f"   Error fetching environment variables: {e}", 255, 0, 0)
    
    menus.print_with_rgb("---------------------------------------------------------------------", 0, 255, 255)
    
