import time
import sys
def delay(phrase):
    for i in phrase:
        sys.stdout.write('%s' %i)
        sys.stdout.flush()
        time.sleep(0.008)
