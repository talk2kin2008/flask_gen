import sys

def getTemplate(className):
    s = '''
import unittest

class {className}(unittest.TestCase):
    def setUp(self):
        pass
        
    def tearDown(self):
        pass
        
if __name__=="__main__":
    unittest.main()
    '''.format(className=className)
    
    return s
    
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print "Usage: unit_test.py <class name> <filepath>"
    else:
        className=sys.argv[1]
        filePath=sys.argv[2]
        f=open(filePath,'w')
        template=getTemplate(className)
        f.write(template)
        f.close
        print "{0} has been generated.".format(className)
        