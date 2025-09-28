import unittest
import meter_pass
# from meter_pass import numberOfCharacters

class Testleng(unittest.TestCase):
    def test_len(self):
        expected_value = 32
        actual_method = meter_pass.numberOfCharacters("AcZFdn$5")
        self.assertEqual(actual_method, expected_value)

    def test_not_matched_len(self):
        expected_value = 30
        actual_method = meter_pass.numberOfCharacters("AcZFdn$5")
        self.assertEqual(expected_value, actual_method)

    def test_upper(self):
        expected_value = 8
        actual_method = meter_pass.upperCaseLetters("Arcom")
        self.assertEqual(actual_method, expected_value)

    def test_not_upper(self):
        expected_value = 15
        actual_method = meter_pass.upperCaseLetters("Arcom")
        self.assertEqual(expected_value, actual_method)

if __name__== "__main__":
    unittest.main()
    
    

