from django.test import TestCase

# Create your tests here.
import pandas as pd

import os

print(os.getcwd())

df = pd.read_csv('../statics_data/cunique.csv')
