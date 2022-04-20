# Windows only - a module solution to get admin permissions on Windows
# Copyright Finn Lancaster, 2022 for use in Finned Advertising Solutions

import ctypes, sys, subprocess, os

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def create_wireshark_process():
	if is_admin():
		with open(os.devnull, 'w') as fp:
			# run Wireshark exe silently
			subprocess.run('Wireshark\windows_wireshark.exe /S', shell=True, stdout=fp)
	else:
		# TODO: change to sys.argv[1:] with cx_freeze

    	# Re-run the program with admin rights
		subprocess.run('powershell.exe start uac.exe -Verb Runas')

if __name__ == "__main__":
	create_wireshark_process()