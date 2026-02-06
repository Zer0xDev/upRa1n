import os
import shutil
from colorama import *
import subprocess
from art import text2art
from zipfile import ZipFile
import sys
import paramiko
from scp import SCPClient
import time
from tqdm import tqdm
import datetime

def send_file_to_ssh(local_path: str, remote_path: str):
    hostname = "localhost"
    port = 2222
    username = "root"
    password = "alpine"

    client = paramiko.SSHClient()

    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    client.connect(
        hostname=hostname,
        port=port,
        username=username,
        password=password,
        timeout=3
    )
    
    scp = SCPClient(client.get_transport())
    scp.put(local_path, remote_path)
    scp.close()
    log(message="[==================================================] 100.0%", type="success")



def download_file_from_device(file: str):
    hostname = "localhost"
    port = 2222
    username = "root"
    password = "alpine"

    client = paramiko.SSHClient()

    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    client.connect(
        hostname=hostname,
        port=port,
        username=username,
        password=password,
        timeout=3
    )
    
    scp = SCPClient(client.get_transport())
    scp.get(file, os.getcwd())
    scp.close()
    log(message="[==================================================] 100.0%", type="success")

def execute_palera1n_command_with_output(command: str):
    hostname = "localhost"
    port = 2222
    username = "root"
    password = "alpine"

    client = paramiko.SSHClient()

    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(
            hostname=hostname,
            port=port,
            username=username,
            password=password,
            timeout=3
        )

        stdin, stdout, stderr = client.exec_command(command)

        output = stdout.read().decode('utf-8')
        errors = stderr.read().decode('utf-8')


    except Exception as e:
        log(message=f"Could not connect to server! {e}", type="error")
        sys.exit()
    finally:
        client.close()

def execute_palera1n_command(command: str):
    hostname = "localhost"
    port = 2222
    username = "root"
    password = "alpine"

    client = paramiko.SSHClient()

    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(
            hostname=hostname,
            port=port,
            username=username,
            password=password,
            timeout=3
        )

        stdin, stdout, stderr = client.exec_command(command)

        output = stdout.read().decode('utf-8')
        errors = stderr.read().decode('utf-8')


    except Exception as e:
        log(message=f"Could not connect to server! {e}", type="error")
        sys.exit()
    finally:
        client.close()

def check_dependencies():
    result = subprocess.run(['aea'],
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE,
                       text=True)


    output = result.stderr.strip()

    aea = False
    img4 = False
    iBootpatch2 = False
    palera1n = False
    brew = False
    devicetree = False

    if "Usage: aea command <options>" in output:
        log(message="aea installed", type="success")
        aea = True
    else:
        log(message="aea is not installed", type="error")

    ######

    result = subprocess.run(['img4'],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        text=True)


    output = result.stderr.strip()

    if "[e] no input file name" in output:
        log(message="img4 installed", type="success")
        img4 = True
    else:
        log(message="img4 is not installed", type="error")


    ######

    result = subprocess.run(['iBootPatch2'],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        text=True)


    output = result.stdout.strip()

    if "iBootPatch2" in output:
        log(message="iBootPatch2 installed", type="success")
        iBootpatch2 = True
    else:
        log(message="iBootPatch2 is not installed", type="error")

    ######

    result = subprocess.run(['palera1n'],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        text=True)


    output = result.stderr.strip()

    if "palera1n:" in output:
        log(message="palera1n installed", type="success")
        palera1n = True
    else:
        log(message="palera1n is not installed", type="error")

    ######

    result = subprocess.run(['devicetree-parse'],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        text=True)


    output = result.stdout.strip()

    if "usage: devicetree-parse" in output:
        log(message="devicetree-parse installed", type="success")
        devicetree = True
    else:
        log(message="devicetree-parse is not installed", type="error")

    if img4 and iBootpatch2 and palera1n and aea and devicetree:
        log(message="All dependencies have been installed successfully!", type="success")
        return True
    else:
        sys.exit()

def execute_ssh_command_without_output(command: str):
    hostname = "localhost"
    port = 2222
    username = "root"
    password = "alpine"

    client = paramiko.SSHClient()

    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(
            hostname=hostname,
            port=port,
            username=username,
            password=password,
            timeout=3
        )

        stdin, stdout, stderr = client.exec_command(command)

        output = stdout.read().decode('utf-8')
        errors = stderr.read().decode('utf-8')


    except Exception as e:
        log(message=f"Could not connect to server! {e}", type="error")
        sys.exit()
    finally:
        client.close()

def execute_ssh_command_with_output(command: str):
    hostname = "localhost"
    port = 2222
    username = "root"
    password = "alpine"

    client = paramiko.SSHClient()

    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(
            hostname=hostname,
            port=port,
            username=username,
            password=password,
            timeout=3
        )

        stdin, stdout, stderr = client.exec_command(command)

        output = stdout.read().decode('utf-8')
        errors = stderr.read().decode('utf-8')

        return output
    except Exception as e:
        log(message=f"Could not connect to server! {e}", type="error")
        sys.exit()
    finally:
        client.close()

def log(message: str, type: str):
    if type == "error":
        print(f"[{Fore.RED}{datetime.datetime.now().strftime("%H:%M:%S")}{Fore.RESET}] {message}")
    elif type == "warning":
        print(f"[{Fore.YELLOW}{datetime.datetime.now().strftime("%H:%M:%S")}{Fore.RESET}] {message}")
    elif type == "success":
        print(f"[{Fore.GREEN}{datetime.datetime.now().strftime("%H:%M:%S")}{Fore.RESET}] {message}")
    elif type == "progress":
        print(f"[{Fore.BLUE}{datetime.datetime.now().strftime("%H:%M:%S")}{Fore.RESET}] {message}")

def check_and_delete(filename: str):
    if os.path.exists(filename):
        os.remove(filename)

def main():
    os.system("sudo killall iproxy")
    os.system("clear")
    print(text2art("upRa1n"))
    print("# Tethered dualboot iPadOS 18 for iPad 6")
    print("# Developed by ZeroxDev")
    print("#===== Thanks to =====")
    print("# asdfugil for the installation guide")
    print("# Nathan (verygenericname) for SSHRD Script")
    print("#=====================\n\n")
    result = check_dependencies()
    if not result:
        ask = input(f"[{datetime.datetime.now().strftime("%H:%M:%S")}] Do you want to force skip dependencies check? (Y/n): ")
        log(message="WARNING! This may break installation process!", type="warning")
        if "y" or "Y" in ask:
            log(message="Force skipping dependencies check ...", type="warning")
        else:
            sys.exit()
    if os.path.exists("17.7.10"):
        pass
    else:
        log(message="Could not find unpacked iOS 17.7.10 IPSW. Download iPad 6 iOS 17.7.10 IPSW and extract it into /17.7.10 folder !", type="error")
        sys.exit()
    try:
        if "boot" in sys.argv[1]:
            boot_device()
        elif "restore" in sys.argv[1]:
            pass
        else:
            print("Usage: python3 upRa1n.py <options>\n\nCommands:\n\n   restore               Tethered dualboot iOS 18 on iPad 6\n   boot                  Boot your device into iOS 18\n\nExample:\n\n   python3 upRa1n.py restore\n   python3 upRa1n.py boot\n")
            sys.exit()
    except Exception as e:
        print("Usage: python3 upRa1n.py <options>\n\nCommands:\n\n   restore               Tethered dualboot iOS 18 on iPad 6\n   boot                  Boot your device into iOS 18\n\nExample:\n\n   python3 upRa1n.py restore\n   python3 upRa1n.py boot\n")
        sys.exit()


    if os.path.exists("disk2.bin"):
        ask = input(f"[{datetime.datetime.now().strftime("%H:%M:%S")}] Do you want to clean old files? (Y/n): ")
        if "y" in ask or "Y" in ask:
            check_and_delete("IM4M")
            check_and_delete("devicetred")
            check_and_delete("devicetred.img4")
            check_and_delete("DeviceTree")
            check_and_delete("DeviceTree_j71bap.jsonc")
            check_and_delete("disk2.bin")
            check_and_delete("EVA.img4")
            check_and_delete("IM4M")
            check_and_delete("kernelcachd")
            check_and_delete("LLB.bin")
            check_and_delete("LLB.img4")
            check_and_delete("LLB2.bin")
            check_and_delete("LLB3.bin")
            check_and_delete("sep-firmware.im4p")
            print("\n")

    print("\n")

    files = os.listdir(os.getcwd())

    ipsw_files = []

    for file in files:
        if ".ipsw" in file:
            ipsw_files.append(file)
    count = 0

    for item in ipsw_files:
        count += 1
        print(f"{count}.    {ipsw_files[(count - 1)]}")

    if count == 0:
        log(message="Could not find iOS 18 IPSW File! Place it into upRa1n folder.", type="error")
        sys.exit()

    ipsw_file_input = int(input("\n==> Select iOS 18 IPSW file: "))
    version = input("\n==> Enter iOS Version: ")
    model = input("\n==> Enter iPad model (1 -- WiFi, 2 -- Cellular): ")
    volume_number = 0
    ipad_file = ""
    if model == "1":
        volume_number = 8
        ipad_file = "71"
        log(message="Selected iPad 6 WiFi model!", type="success")
    else:
        volume_number = 9
        ipad_file = "72"
        log(message="Selected iPad 6 Cellular model!", type="success")
    print("\n")
    ipsw_file = ipsw_files[ipsw_file_input - 1]
    if os.path.exists(version):
        log(message=f"{ipsw_file} are already unpacked! Checking the required files...", type="success")
        if os.path.exists(f"{version}/root.dmg"):
            pass
        else:
            log(message=f"Required files not found! Folder {version} cleared. Rerun the script to generate new ones.", type="error")
            shutil.rmtree(version)
            sys.exit()
    else:
        log(message="Unpacking IPSW file...", type="progress")
        try:
            ipsw = ZipFile(file=ipsw_file)
            os.mkdir(version)
            shutil.copy2("get_key.py", f"{version}")
            os.chdir(version)
            ipsw.extractall()
            ipsw.close()
            log(message=f"Successfully unpacked {ipsw_file} to {version} folder!", type="success")
        except Exception as e:
            log(message=f"Failed to unpack IPSW! {e}", type="error")
        
        log(message="Unpacking DMG files...", type="progress")

        files = os.listdir(os.getcwd())

        for file in files:
            if ".aea" in file:
                if os.path.getsize(file) < 3000000000:
                    log(message=f"Found OS.dmg! Decrypting {file} ...", type="progress")
                    os.system(f'aea decrypt -i {file} -o os.dmg -key-value "base64:$(python3 get_key.py {file})"')
                    log(message=f"Successfully unpacked {file} to OS.dmg!", type="success")
                else:
                    log(message=f"Found ROOT.dmg! Decrypting {file} ...", type="progress")
                    os.system(f'aea decrypt -i {file} -o root.dmg -key-value "base64:$(python3 get_key.py {file})"')
                    log(message=f"Successfully unpacked {file} to ROOT.dmg!", type="success")
            else:
                if ".dmg" in file:
                    if os.path.getsize(file) < 20000000:
                        log(message=f"Found App Cryptex! Renaming to app.dmg ...", type="progress")
                        os.rename(file, "app.dmg")
                
        os.chdir("..")
    

    os.chdir("SSHRD_Script")

    user_put_dfu = input(f"[{datetime.datetime.now().strftime("%H:%M:%S")}] Put your device into Recovery Mode, then into DFU mode and then press [ENTER/Return]: ")

    log(message="Downloading iOS 17.7 ramdisk...", type="progress")

    try:
        if ("17.7" in open("sshramdisk/version.txt", "r").readline()):
            log(message="Ramdisk already downloaded!", type="success")
        else:
            os.system("./sshrd.sh 17.7")
    except Exception as e:
        os.system("./sshrd.sh 17.7")

    log(message="Booting!", type="progress")
    os.system("./sshrd.sh boot")


    log(message="Successfully booted into ramdisk! Connecting to device...", type="success")

    process = subprocess.Popen(
        ["iproxy", "2222", "22"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    time.sleep(12)

    os.chdir("..")

    log(message="Mounting tmpfs to /mnt5 ...", type="progress")
    execute_ssh_command_without_output(command="/sbin/mount_tmpfs /mnt5")
    execute_ssh_command_without_output(command="dd if=/dev/disk2 of=/mnt5/disk2.bin")

    log(message="Downloading /mnt5/disk2.bin to host...", type="progress")
    download_file_from_device(file="/mnt5/disk2.bin")
    log(message="Successfully downloaded DISK2.bin !", type="success")

    log(message="Downloading bootloader from iPad 6 IPSW...", type="progress")
    os.system(f"img4 -i 17.7.10/Firmware/all_flash/LLB.ipad7b.RELEASE.im4p -k 07e6e3098054425fcdc83d47351a7d9439512c4e0297ac7162250e6d543f5d55fda2fefed210aa446c70e6d529292861 -o LLB.bin")
    log(message="Successfully downloaded LLB.bin !", type="success")

    log(message="Patching signature checks...", type="progress")
    os.system("./SSHRD_Script/Darwin/iBoot64Patcher LLB.bin LLB2.bin")

    os.system("iBootPatch2 LLB2.bin LLB3.bin")
    os.system("img4 -i disk2.bin -m IM4M")
    os.system("img4 -i LLB3.bin -A -T ibss -M IM4M -o LLB.img4")
    log(message="Successfully patched signature checks!", type="success")

    log(message="Mounting /dev/disk1s5 to /mnt6/ ...", type="progress")
    execute_ssh_command_without_output(command="/sbin/mount_apfs /dev/disk1s5 /mnt6")

    time.sleep(3)

    lines = execute_ssh_command_with_output(command="ls /mnt6")

    boot_manifest_hash = ""

    log(message="Scanning for boot manifest hash in /mnt6 ...", type="progress")

    for line in lines.splitlines():
        if len(line) > 20:
            log(message=f"Found boot manifest hash: {line} !", type="success")
            boot_manifest_hash = line

    log(message="Copying files...", type="progress")

    execute_ssh_command_without_output(command="mkdir -p /mnt6/cryptex1/currend")
    time.sleep(2)
    execute_ssh_command_without_output(command="cp -a /mnt6/cryptex1/current/apticket.*.im4m /mnt6/cryptex1/currend")
    time.sleep(2)
    execute_ssh_command_without_output(command="cp -a /mnt6/cryptex1/current/*.{root_hash,trustcache} /mnt6/cryptex1/currend")
    time.sleep(2)

    log(message="Creating file system...", type="progress")

    execute_ssh_command_without_output(command="/sbin/newfs_apfs -A -D -o role=r -v Xystem /dev/disk0s1")
    time.sleep(2)

    log(message="Mounting new volume...", type="progress")

    execute_ssh_command_without_output(command=f"/sbin/mount_apfs /dev/disk1s{volume_number} /mnt8")
    time.sleep(2)

    time.sleep(3)

    log(message="Uploading root.dmg to /mnt8/. This may take up to 15 minutes... ", type="progress")

    send_file_to_ssh(local_path=f"{version}/root.dmg", remote_path="/mnt8/")


    log(message="Unmounting /mnt8 ...", type="progress")
    execute_ssh_command_without_output(command="/sbin/umount /mnt8")
    time.sleep(2)
    log(message="Unmounting /mnt6 ...", type="progress")
    execute_ssh_command_without_output(command="/sbin/umount /mnt6")
    time.sleep(2)

    log(message="APFS invert. This may take a few minutes... ", type="progress")
    execute_ssh_command_without_output(command=f"/System/Library/Filesystems/apfs.fs/apfs_invert -d /dev/disk0s1 -s {volume_number} -n root.dmg")
    time.sleep(2)

    log(message=f"Mounting /dev/disk1s5 and /dev/disk1s{volume_number} ...", type="progress")
    execute_ssh_command_without_output(command="/sbin/mount_apfs /dev/disk1s5 /mnt6")
    time.sleep(2)
    execute_ssh_command_without_output(command=f"/sbin/mount_apfs /dev/disk1s{volume_number} /mnt8")
    time.sleep(2)

    log(message="Uploading system cryptex. This may take up to 15 minutes... ", type="progress")
    send_file_to_ssh(f"{version}/os.dmg", "/mnt6/cryptex1/currend/")

    time.sleep(2)

    log(message="Uploading app cryptex. This may take a few minutes... ", type="progress")
    send_file_to_ssh(f"{version}/app.dmg", "/mnt6/cryptex1/currend/")

    time.sleep(2)


    log(message="Mounting iOS 17...", type="progress")
    execute_ssh_command_without_output(command="/sbin/mount_apfs -o ro /dev/disk1s1 /mnt1")

    time.sleep(2)

    log(message="Finding iPad 6 specific files. This may take up to 5 minutes...", type="progress")

    find_command = "find /mnt1 -iregex '.*j7[1-2]b.*' -type f -exec /bin/sh -c 'dirname=" + '"$(echo "{}" | sed -E ' + "'\\''s|^/mnt1(/.+)/.+$|\\1|'\\'')" + '"; filename="$(echo "{}" | sed -E ' + "'\\''s|/mnt1/.+/(.+)$|\\1|'\\'')" + '"; mkdir -p ' + '"/mnt8/${dirname}"; cp -an "{}" "/mnt8/${dirname}/${filename}";' + "' \\;"

    execute_ssh_command_without_output(command=find_command)
    
    time.sleep(2)


    log(message="Adding iPad 6 specific files...", type="progress")
    execute_ssh_command_without_output(command="ln -s J171.Default.plist /mnt8/System/Library/EventTimingProfiles/J71b.Default.plist")
    time.sleep(2)
    execute_ssh_command_without_output(command="ln -s J171.Touch.plist /mnt8/System/Library/EventTimingProfiles/J71b.Touch.plist")
    time.sleep(2)
    execute_ssh_command_without_output(command="ln -s J171.Pencil.plist /mnt8/System/Library/EventTimingProfiles/J71b.Pencil.plist")
    time.sleep(2)
    execute_ssh_command_without_output(command="ln -s J172.Default.plist /mnt8/System/Library/EventTimingProfiles/J72b.Default.plist")
    time.sleep(2)
    execute_ssh_command_without_output(command="ln -s J172.Touch.plist /mnt8/System/Library/EventTimingProfiles/J72b.Touch.plist")
    time.sleep(2)
    execute_ssh_command_without_output(command="ln -s J172.Pencil.plist /mnt8/System/Library/EventTimingProfiles/J72b.Pencil.plist")
    time.sleep(2)

    log(message="Downgrading components ...", type="progress")
    time.sleep(2)
    execute_ssh_command_without_output(command="mv /mnt8/Library/Audio/Plug-Ins{,.bak}")
    execute_ssh_command_without_output(command="cp -a /mnt1/Library/Audio/Plug-Ins /mnt8/Library/Audio")
    time.sleep(2)
    execute_ssh_command_without_output(command="mv /mnt8/usr/sbin/BlueTool{,.bak}")
    execute_ssh_command_without_output(command="cp -a /mnt1/usr/sbin/BlueTool /mnt8/usr/sbin")
    time.sleep(2)

    log(message="Patching RootFS ...", type="progress")

    execute_ssh_command_without_output(command="sed -i -e 's|cryptex1/current|cryptex1/currend|' /mnt8/usr/lib/dyld")
    time.sleep(2)
    execute_ssh_command_without_output(command="ldid -Icom.apple.dyld -S /mnt8/usr/lib/dyld")
    time.sleep(2)

    log(message="Patching device tree...", type="progress")
    os.system(f"img4 -i 17.7.10/Firmware/all_flash/DeviceTree.j{ipad_file}bap.im4p -o DeviceTree")
    os.system(f"devicetree-parse DeviceTree > DeviceTree_j{ipad_file}bap.jsonc")
    os.system(f"patch DeviceTree_j{ipad_file}bap.jsonc dt-j{ipad_file}bap.diff")

    log(message="Wrapping up files...", type="progress")
    os.system(f"img4 -i {version}/kernelcache.release.ipad7c -M IM4M -o kernelcachd")
    os.system("devicetree-repack DeviceTree_j71bap.jsonc devicetred")
    os.system("img4 -i devicetred -M IM4M -A -T dtre -o devicetred.img4")

    log(message="Uploading kernelcachd ...", type="progress")
    send_file_to_ssh("kernelcachd", f"/mnt6/{boot_manifest_hash}/System/Library/Caches/com.apple.kernelcaches/")
    log(message="Uploading devicetred.img4 ...", type="progress")
    send_file_to_ssh("devicetred.img4", f"/mnt6/{boot_manifest_hash}/usr/standalone/firmware/")
    log(message="Copying SEP ...", type="progress")
    os.system(f"cp {version}/Firmware/all_flash/sep-firmware.j1{ipad_file}.RELEASE.im4p sep-firmware.im4p")
    log(message="Creating AVE firmware...", type="progress")
    os.system(f"img4 -i {version}/Firmware/ave/AppleAVE2FW_H9.im4p -M IM4M -o EVA.img4")
    log(message="Uploading EVA.img4 ...", type="progress")
    send_file_to_ssh(local_path="EVA.img4", remote_path=f"/mnt6/{boot_manifest_hash}/usr/standalone/firmware/FUD/")
    log(message="Setting up NVRam ...", type="progress")
    execute_ssh_command_without_output(f"nvram p1-fakefs-rootdev=disk1s{volume_number}")
    log(message="Rebooting ...", type="progress")
    time.sleep(4)
    execute_ssh_command_without_output(command="/sbin/reboot")
    os.system("palera1n -l")
    when_ready_to_palera1n = input("\n#### STEP 2\n\nOnce your device boots into iOS 17, press [ENTER/Return] ")
    reconnect = input("Reconnect the cable and then press [ENTER/Return] ")
    log(message="Waiting 15s ...", type="progress")

    time.sleep(15)

    os.system("clear")
    print(text2art("upRa1n"))

    process.terminate()
    os.system("killall iproxy")
    time.sleep(2)
    process = subprocess.Popen(
        ["iproxy", "2222", "44"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    time.sleep(4)

    log(message="Fixing up var ...", type="progress")
    time.sleep(2)
    execute_palera1n_command(command=f"mount_apfs /dev/disk1s{volume_number} /cores/fs/fake")
    time.sleep(3)
    execute_palera1n_command(command="rm -rf /private/var/staged_system_apps")
    time.sleep(5)
    execute_palera1n_command(command="mv /cores/fs/fake/private/var/staged_system_apps /private/var")
    time.sleep(5)
    execute_palera1n_command(command=f"nvram p1-fakefs-rootdev=disk1s{volume_number}")
    time.sleep(3)
    execute_palera1n_command(command="snaputil -c orig-fs /cores/fs/fake")
    time.sleep(5)
    log(message="Rebooting ...", type="progress")
    time.sleep(3)
    execute_palera1n_command("reboot")

    boot_device()


def boot_device():
    os.system("clear")
    print(text2art("upRa1n"))
    print("# Tethered dualboot iPadOS 18 for iPad 6")
    print("# Developed by ZeroxDev")
    print("#===== Thanks to =====")
    print("# asdfugil for the installation guide")
    print("# Nathan (verygenericname) for SSHRD Script")
    print("#=====================\n\n")
    enter = input(f"[{datetime.datetime.now().strftime("%H:%M:%S")}] To boot your device into iOS 18, put your device into Recovery Mode and then press [ENTER/Return] ")
    os.system("sudo sh boot.sh")
    print("\n\nDONE!")
    print("[==================================================] 100.0%")
    sys.exit()
    

    
    
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n")
        log(message="Quitting...", type="error")
    except Exception as e:
        log(message=f"An unknown error has occurred! {e}", type="error")
