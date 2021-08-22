from threading import Thread

class ThreadedPool:
    def __init__(self, number_of_threads: int):
        """
        Executes a given function over array with *args
        :param number_of_threads: number of instances
        """
        self._number_of_threads = number_of_threads

    def map(self, func, work):
        """
        Maps threads to work to be done, does not return values returned by 
        function
        :param func: a callable that will be called with *args from work
        :param work: List of lists with args
        """
        jobs = []
        i = 0
        for args in work:
            if len(jobs) < self._number_of_threads:
                pass
            else:
                old_thread = jobs.pop(0)
                old_thread.join()
            thread = Thread(target=func, args=args)
            thread.start()
            jobs.append(thread)
            i += 1
            print("\r{}/{}".format(i, len(work)), end="")
        for job in jobs:
            job.join()
        print()

