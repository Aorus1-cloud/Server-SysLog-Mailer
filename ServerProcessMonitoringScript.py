import ServerProcessMonitoringModules
from sys import argv
import schedule
import time

def intermediate():
    ServerProcessMonitoringModules.Log(argv[1])
    
def main():
    if len(argv)==2:
        if argv[1].lower() == "--h":
            print("This is a system info logging script which sends the log file to the user through mail.")
            print("This is a automation script.")
            return

        if argv[1].lower() == "--u":
            print("Use the given script as:")
            print("ScriptName.py Argument1 Argument2")
            print("Argument 1 : Directory_Name")
            print("Argument 2 : Time interval in minutes")
            

            return

        else:
            print("Use the given flags as :")
            print("--u: use to display the usage")
            print("--h: use to display the help")
            return

    elif len(argv) <= 1 or len(argv) > 3:
        print("Invalid number of command line arguments")
        print("Use the given flags as :")
        print("--u: use to display the usage")
        print("--h: use to display the help")
        return

    else:
        print("The script is running.")
        print("Press Ctrl + C to stop the execution")
        try:
            interval = int(argv[2])
        except ValueError:
            print("Error: interval must be an integer (minutes).")
            return
        schedule.every(interval).minutes.do(intermediate)
 
        while True:
            schedule.run_pending()
            time.sleep(1)
            

if __name__ == "__main__":
    main()