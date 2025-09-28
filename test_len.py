import unittest
import meter_pass
# from meter_pass import numberOfCharacters

class Testleng(unittest.TestCase):
    def test_len(self):
        expected_value = 20
        actual_method = meter_pass.numberOfCharacters("Arcom")
        self.assertEqual(actual_method, expected_value)

    def test_not_matched_len(self):
        expected_value = 22
        actual_method = meter_pass.numberOfCharacters("Arcom")
        self.assertEqual(actual_method, expected_value)

    def test_upper(self):
        expected_value = 15
        actual_method = meter_pass.upperCaseLetters("Arcom")
        self.assertEqual(actual_method, expected_value)

    def test_not_upper(self):
        expected_value = 8
        actual_method = meter_pass.upperCaseLetters("Arcom")
        self.assertEqual(actual_method, expected_value)

if __name__== "__main__":
    unittest.main()
    
    

