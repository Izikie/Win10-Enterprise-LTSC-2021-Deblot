from utils import *

def install_winutils():
    """Install Chris Titus Tech WinUtils"""
    run("irm \"https://christitus.com/win\" | iex", powershell=True)

def install_brave():
    """Install Brave Browser"""
    install_app("brave")

def install_discord():
    """Install Discord"""
    install_app("discord")

    # TODO: Install Vencord

def install_steam():
    """Install Steam"""
    install_app("steam")

def install_heroic():
    """Install Heroic Games Launcher (Epic/GOG/Amazon Games Launcher)"""
    # TODO: Download sepretly as it's not available in Chocolatey

def install_7zip():
    """Install 7-Zip"""
    install_app("7zip")

def install_mpv():
    """Install MPV (Media Player)"""
    install_app("mpv")
    
    # TODO: Set as default media player

def install_imageglass():
    """Install ImageGlass (Photo Viewer)"""
    install_app("imageglass")

    # TODO: Set as default photo viewer

def install_simplewall():
    """Install SimpleWall (Firewall)"""
    install_app("simplewall")

def install_fmd():
    """Install FDM/Free Download Manager (Download Manager)"""
    install_app("freedownloadmanager")

     # TODO: Install extention for brave