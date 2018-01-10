import time

class Logger:
    @classmethod
    def logit(cls, message):
        stamp = time.asctime()
        print "%s - %s" % (stamp, message)