import unittest
import pandas as pd
from pyarc import CBA
from pyarc.data_structures import (
    TransactionDB
)
import os

dataset_file = os.path.dirname(os.path.realpath(__file__)) + "/data/movies_discr.csv"

class TestCBA(unittest.TestCase):

    def test_parameter_validation(self):
        cba = CBA()

        self.assertRaises(Exception, CBA, maxlen=-1)

        self.assertRaises(Exception, CBA, confidence=-1)

        self.assertRaises(Exception, CBA, confidence=12)

        self.assertRaises(Exception, CBA, support=-1)

        self.assertRaises(Exception, CBA, support=12)

        self.assertRaises(Exception, cba.predict, None)

        self.assertRaises(Exception, cba.rule_model_accuracy, None)

        self.assertRaises(Exception, cba.fit, None)

    def test_fitting(self):
        cba = CBA()

        test_dataframe = pd.read_csv(dataset_file, sep=";")
        
        transactions = TransactionDB.from_DataFrame(test_dataframe)

        cba.fit(transactions)


    def test_accuracy(self):
        expected_accuracy = 0.5

        cba = CBA(algorithm="m2")

        test_dataframe = pd.read_csv(dataset_file, sep=";")
        
        transactions = TransactionDB.from_DataFrame(test_dataframe)
        transactions_test = TransactionDB.from_DataFrame(test_dataframe[:2])

        cba.fit(transactions)

        accuracy = cba.rule_model_accuracy(transactions_test)

        self.assertAlmostEqual(accuracy, expected_accuracy, places=3)