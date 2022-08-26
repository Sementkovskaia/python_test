import fire
import psutil
import time
import os

def kill_process(name_process, lifetime, monitoring_frequency):
    '''This function monitors processes with a certain frequency.
       If the process of interest lives longer than the allowed time, 
       the function kills it and adds the record to the log file. 

       The function stops with 'Ctrl+c'.

       Input value:
           - name of process in lower case
           - the lifetime of the process to kill in minutes
           - monitoring frequency in minutes
           
       In the log file writes:
           - ID of process
           - name of process
           - time of killing process.
    '''

    while (True):

        try:
            # gets the folder of the current user
            homepath = os.getenv('USERPROFILE')
            # creates file
            log = open(homepath + '\\' + 'logs.txt', 'a')

            # writes notes how to stop the function and where is the log file
            print()
            print(
                f'If you want to stop the process, please, press Ctrl+c. \nThe log file (logs.txt) is here {homepath}.')

            # loop with system monitoring
            for process in psutil.process_iter():

                # calculates the lifetime of the process
                life = (time.time() - process.create_time()) / 60
                # looks for the process to kill
                if name_process in process.name().lower() and life > lifetime and len(name_process) == len(process.name()[:-4]):
                    # writes the process to log file
                    log.write(
                        f'{process.pid} {process.name()} {time.strftime("%d-%b-%Y %H:%M:%S", time.localtime())}' + '\n')
                    # kills the process
                    process.kill()

                else:
                    pass

            # falling asleep depending on the frequency of monitoring
            time.sleep(monitoring_frequency * 60)

        # with Ctrl+c, the program closes the log file and stops
        except KeyboardInterrupt:
            log.close()
            break

if __name__ == '__main__':
    fire.Fire(kill_process)