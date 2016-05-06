
import unittest
import flask_gen.util as util
import os
import shutil

class Test_util(unittest.TestCase):
    rootDir="c:/temp/MyFlaskApp"
    def setUp(self):
        shutil.rmtree(self.rootDir)
        
    def tearDown(self):
        pass
        
    def test_create_dir(self):
        util.create_directories(self.rootDir)
        listOfDir = os.listdir(self.rootDir)
        #print listOfDir
        targetDir=['app','tests','migrations']
        found = True
        failed2create=""
        for d in targetDir:
            if d not in listOfDir:
                found = False
                failed2create=d
                break
        self.assertTrue(found==True,"Failed to create {0}".format(failed2create))
        
        
if __name__=="__main__":
    unittest.main()
    