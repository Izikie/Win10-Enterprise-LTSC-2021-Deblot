from impl.program import *
from impl.system import *
from utils import *
import platform

system_category = {
    1: {
        "name": "Update Windows",
        "function": update_windows
    },
    2: {
        "name": "Disable Windows Defender",
        "function": disable_windows_defender
    },
    3: {
        "name": "Disable Useless Optional/Addition Features",
        "function": disable_useless_features
    },
    4: {
        "name": "Disable Boot Apps",
        "function": disable_boot_apps
    },
    5: {
        "name": "NVCleanInstall (NVIDIA GPU Driver)",
        "function": nvcleaninstall
    }
}

program_category = {
    1: {
        "name": "WinUtils (Chris Titus)",
        "function": install_winutils
    },
    2: {
        "name": "Brave Browser",
        "function": install_brave
    },
    3: {
        "name": "Discord",
        "function": install_discord
    },
    4: {
        "name": "Steam",
        "function": install_steam
    },
    5: {
        "name": "Heroic Games Launcher (Epic/GOG/Amazon Games Launcher)",
        "function": install_heroic
    },
    6: {
        "name": "7-Zip",
        "function": install_7zip
    },
    7: {
        "name": "MPV (Media Player)",
        "function": install_mpv
    },
    8: {
        "name": "ImageGlass (Photo Viewer)",
        "function": install_imageglass
    },
    9: {
        "name": "SimpleWall (Firewall)",
        "function": install_simplewall
    },
    10: {
        "name": "FDM/Free Download Manager (Download Manager)",
        "function": install_fmd
    }
}

if platform.release() != '10':
    print("This script only supports Windows 10")
    exit(1)

def print_header():
    print("#############################################\n")
    print("""########   ######   #######  ########  
##     ## ##    ## ##     ## ##     ## 
##     ## ##       ##     ## ##     ## 
########   ######  ##     ## ##     ## 
##     ##       ## ##     ## ##     ## 
##     ## ##    ## ##     ## ##     ## 
########   ######   #######  ########""")
    print("\nWORK IN PROGRESS: DO NOT USE")
    print(f"\n########## Windows 10 Setup Script ##########\n")
    print("1. System")
    print("2. Program")
    print("3. Exit")

while True:
    print_header()

    category = int_input("Category", 1, 3)
    
    if category == 3:
        break
    
    selected = None
    
    if category == 1:
        selected = system_category
    else:
        selected = program_category

    length = len(selected) + 1
        
    for i, name in selected.items():
        print(f"{i}: {name}")
    print(f"{length}: All")
        
    script = int_input("Script", 1, length)
    
    if script == length:
        for script in selected:
            selected[script]["function"]()
    else:
        selected[script]["function"]()
        
    
        