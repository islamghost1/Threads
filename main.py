import logging
import threading
import time
import concurrent.futures

list = [    ["magnitude.gif",False],
            ["labour.gif",False],
            [ "character.gif",False],
            ["beneficiary.gif",False],
            ["arch.gif",False],
            ["jealous.gif",False],
            ["justice.gif",False],
            [ "flatware.gif",False],
            ["cut.gif",False],
            ["element.gif",False],
            ["aa.gif",False],
            ["magnitude.gif",False],
            ["labour.gif",False],
            [ "character.gif",False],
            ["beneficiary.gif",False],
            ["arch.gif",False],
            ["jealous.gif",False],
            ["justice.gif",False],
            [ "flatware.gif",False],    
        ]
            
        
def thread_function(name):
    for i in range(len(list)):
        File = list[i][0]
        File_Cecked = list[i][1]
        if File_Cecked  : 
            logging.info("Thread :  {} , File : {} , ***File already checked*** ".format(name,File))
            time.sleep(1)
            #pass
        else : 
            list[i][1] = True      
            logging.info("Thread :  {} , File : {} ".format(name,File))


if __name__ == "__main__":
    start_time = time.time()
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    """
        x = threading.Thread(target=thread_function, args=(1,), daemon=True)
        x.start()

        # x.join()

        x1 = threading.Thread(target=thread_function, args=(2,), daemon=True)
        x1.start()

        # x1.join()

    """
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.map(thread_function, range(1))
    print("--- %s seconds ---" % (time.time() - start_time))