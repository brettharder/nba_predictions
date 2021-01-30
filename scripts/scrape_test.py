"""
Test to get data from basketball reference
"""
import pandas as pd

URL =  'https://www.basketball-reference.com/players/h/hardeja01/gamelog/2011/'
tables = pd.read_html(URL)

tables

l_tables = [
    table for table in tables if table.shape[0] > 59
]

df = l_tables[0]
df