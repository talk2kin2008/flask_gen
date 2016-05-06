#startup script
import os
import sys

root = os.path.abspath("..")
if root not in sys.path:
    sys.path.append(root)
    print "added {0} to sys.path".format(root)
else:
    print "{0} is already in sys.path".format(root)