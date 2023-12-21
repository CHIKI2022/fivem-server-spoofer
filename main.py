import os
import sys
import uuid
import shutil
import ctypes
import string
import random
import winsound
import keyboard
import requests
import subprocess
from winreg import *
from time import sleep
from colorama import Fore,init

from helper import Helper


init()

#run as admin
def run_as_admin():
    try:
        is_admin = os.getuid() == 0
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0

    if not is_admin:
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, " ".join(sys.argv), None, 1
        )
        sys.exit()

#unlink xbox
def unlink_xbox():
    hostspath = os.path.join(os.environ['windir'], 'System32', 'drivers', 'etc', 'hosts')
    with open(hostspath, 'a') as hosts_file:
        hosts_file.write('127.0.0.1 xboxlive.com\n')
        hosts_file.write('127.0.0.1 user.auth.xboxlive.com\n')
    print(Fore.GREEN + 'Xbox unlinked successfully')
    winsound.Beep(300,200)

#clean fivem
def clean_fivem():     
    shutil.rmtree(os.path.join(os.environ['LocalAppData'], 'DigitalEntitlements'), ignore_errors=True)
    shutil.rmtree(os.path.join(os.environ['userprofile'], 'AppData', 'Roaming', 'CitizenFX'), ignore_errors=True)
    file_paths = [
        os.path.join(os.environ['LocalAppData'], 'FiveM', 'FiveM.app', 'discord.dll'),
        os.path.join(os.environ['LocalAppData'], 'FiveM', 'FiveM.app', 'CitizenFX_SubProcess_chrome.bin')
    ]
    for file_path in file_paths:
        try:
            os.remove(file_path)
        except FileNotFoundError:
            pass
    shutil.rmtree(os.path.join(os.environ['LocalAppData'], 'FiveM', 'FiveM.app', 'logs'), ignore_errors=True)
    shutil.rmtree(os.path.join(os.environ['LocalAppData'], 'FiveM', 'FiveM.app', 'crashes'), ignore_errors=True)
    print(Fore.GREEN + 'Fivem cleaned successfully')
    winsound.Beep(300,200)


#clean temp
def clean_temp(): 
    temp_directories = [
        'c:\\windows\\tempor~1',
        'c:\\windows\\temp',
        'c:\\windows\\tmp',
        'c:\\windows\\ff*.tmp',
        'c:\\windows\\history',
        'c:\\windows\\cookies',
        'c:\\windows\\recent',
        'c:\\windows\\spool\\printers'
    ]

    for temp_dir in temp_directories:
        shutil.rmtree(temp_dir, ignore_errors=True)
        
    print(Fore.GREEN + 'Temp cleaned successfully')
    winsound.Beep(300,200)

#spoofuniq
def spoof_uniq_ids():
    Helper.spoof_uniq("SOFTWARE\\Microsoft\\Cryptography", "MachineGuid")
    Helper.spoof_uniq("SYSTEM\\CurrentControlSet\\Control\\IDConfigDB\\Hardware Profiles\\0001", "HwProfileGUID")
    Helper.spoof_uniq("SYSTEM\\HardwareConfig", "LastConfig")
    Helper.spoof_uniq("SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\WindowsUpdate", "AccountDomainSid")
    Helper.spoof_uniq("SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\WindowsUpdate", "PingID")
    Helper.spoof_uniq("SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\WindowsUpdate", "SusClientId")
    Helper.spoof_uniq("SYSTEM\\CurrentControlSet\\Control\\SystemInformation", "ComputerHardwareId")
    Helper.spoof_uniq("SOFTWARE\\Microsoft\\SQMClient", "MachineId")
    Helper.spoof_uniq("SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion", "BuildGUID")
    Helper.spoof_uniq("SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion", "ProductId")
    Helper.spoof_uniq("SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion", "BuildLab")
    Helper.spoof_uniq("SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion", "BuildLabEx")
    Helper.spoof_uniq("SYSTEM\\CurrentControlSet\\Control\\Class\\{4d36e968-e325-11ce-bfc1-08002be10318}\\0000", "_DriverProviderInfo")
    Helper.spoof_uniq("SYSTEM\\CurrentControlSet\\Control\\Class\\{4d36e968-e325-11ce-bfc1-08002be10318}\\0000", "UserModeDriverGUID")
    print(Fore.GREEN + 'Uniqids spoofed successfully ')
    winsound.Beep(300,200)

def spoof_sp_serials():
    print(Fore.GREEN + 'spoofing serials...')
    winsound.Beep(300,200)
    sleep(1)
    os.system('mode con: cols=80 lines=20')
    Helper.spoof_serials()
    
#showserials
def showserials():
    os.system('mode con: cols=80 lines=20')
    winsound.Beep(200,100)
    print(Helper.find_id("SOFTWARE\\Microsoft\\Cryptography", "MachineGuid"))
    print(Helper.find_id("SYSTEM\\CurrentControlSet\\Control\\IDConfigDB\\Hardware Profiles\\0001", "HwProfileGUID"))
    print(Helper.find_id("SYSTEM\\HardwareConfig", "LastConfig"))
    print(Helper.find_id("SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\WindowsUpdate", "PingID"))
    print(Helper.find_id("SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\WindowsUpdate", "SusClientId"))
    print(Helper.find_id("SYSTEM\\CurrentControlSet\\Control\\SystemInformation", "ComputerHardwareId"))
    print(Helper.find_id("SOFTWARE\\Microsoft\\SQMClient", "MachineId"))
    print(Helper.find_id("SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion", "BuildGUID"))
    print(Helper.find_id("SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion", "ProductId"))
    print(Helper.find_id("SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion", "BuildLab"))
    print(Helper.find_id("SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion", "BuildLabEx"))
    print(Helper.find_id("SYSTEM\\CurrentControlSet\\Control\\Class\\{4d36e968-e325-11ce-bfc1-08002be10318}\\0000", "_DriverProviderInfo"))
    print(Helper.find_id("SYSTEM\\CurrentControlSet\\Control\\Class\\{4d36e968-e325-11ce-bfc1-08002be10318}\\0000", "UserModeDriverGUID"))
    sleep(20)
    os.system('mode con: cols=60 lines=20')

run_as_admin()
os.system('mode con: cols=60 lines=20')
os.system('title fivemCleaner by chikili ')

os.system("cls")
print(f"{Fore.RED}Press {Fore.WHITE}'X' {Fore.RED}to start spoofing")
print(f"{Fore.RED}Press {Fore.WHITE}'Z' {Fore.RED}to show current serials\n")

winsound.Beep(300,600)
    
while True:
    if keyboard.is_pressed('x'):
        unlink_xbox()
        clean_temp()
        clean_fivem()
        spoof_uniq_ids()
        sleep(1)
        spoof_sp_serials()
        break
        
    if keyboard.is_pressed('z'):
        showserials()
        break
        
        
        