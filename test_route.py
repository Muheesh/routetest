import sqlite3
import unittest
class checkroutes(unittest.TestCase):
    def setUp(self):
        self.Name = "airasia"
        self.price = "30000"
        self.place = "bom"
        self.connection = sqlite3.connect("routes.db")
    def tearDown(self):
        self.Name=" "
        self.price = " "
        self.place = " "
        self.connection.close()
    def test_verify_name(self):
        result  = self.connection.execute("select airline from flight where price="+self.price)
        for i in result:
            fetcheddata = i[0]

        self.assertEqual(self.Name,fetcheddata)
if __name__ =="__main__":
    unittest.main()

