from multiprocessing import Pool, TimeoutError
import time
import os
import definitionFunctions as df
import fnmatch
import re


if __name__ == '__main__':
    # start 4 worker processes

    includes = ['*.jpg', '*.gif'] # for files only
    includes = r'|'.join([fnmatch.translate(x) for x in includes])
    
    processingFiles = []

    #for root, dirs, files in os.walk("i:\\imagens"):
    for root, dirs, files in os.walk("/mnt/i/imagens"):
        files = [f for f in files if re.match(includes, f)] #filter files from the regexp
        for file in files:
            processingFiles += [ os.path.join(root,file) ]



    with Pool(processes=32) as pool:
        pass
        # print "[0, 1, 4,..., 81]"
        #print(pool.map(df.imageToProcess, range(1000)))

        # print same numbers in arbitrary order
        for i in pool.imap_unordered(df.imageToProcess, processingFiles):
            print(i)

        # evaluate "f(20)" asynchronously
        #res = pool.apply_async(df.f, (20,))      # runs in *only* one process
        #print(res.get(timeout=1))             # prints "400"

        # evaluate "os.getpid()" asynchronously
        #res = pool.apply_async(os.getpid, ()) # runs in *only* one process
        #print(res.get(timeout=1))             # prints the PID of that process

        # launching multiple evaluations asynchronously *may* use more processes
        #multiple_results = [pool.apply_async(os.getpid, ()) for i in range(4)]
        #print([res.get(timeout=1) for res in multiple_results])

        # make a single worker sleep for 10 secs
        #res = pool.apply_async(time.sleep, (10,))
        #try:
        #    print(res.get(timeout=1))
        #except TimeoutError:
        #    print("We lacked patience and got a multiprocessing.TimeoutError")

        #print("For the moment, the pool remains available for more work")

    # exiting the 'with'-block has stopped the pool
    #print("Now the pool is closed and no longer available")
