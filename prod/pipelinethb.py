# Databricks notebook source
import pandas as pd
import math
import os
import configparser

# Get the parent path of the notebook
notebook_path = dbutils.entry_point.getDbutils().notebook().getContext().notebookPath().get()
parent_path = os.path.dirname('/Workspace' + notebook_path)
os.chdir(parent_path)

# read config file
config = configparser.ConfigParser()
config.read('./pipeline.conf')
inputPath = config.get('DEFAULT', 'INPUT_PATH')
outputPath = config.get('DEFAULT', 'OUTPUT_PATH')

# Extract
tracks = pd.read_csv(inputPath)

# function
def currency_converter(amount, from_currency, to_currency, conversion_rate):
    converted_amount = amount * conversion_rate
    return converted_amount    

# Example usage:
# amount = 100  # Amount in original currency
# from_currency = "USD"  # Original currency
# to_currency = "EUR"  # Target currency
# conversion_rate = 0.85  # Conversion rate from USD to EUR
# converted_amount = currency_converter(amount, from_currency, to_currency, 0.0296)
# Transform
tracks["UnitPrice"] = tracks["UnitPrice"].apply(lambda x: currency_converter(x, 'USD', 'THB', 33.74))
                             
# Load
tracks.to_csv(outputPath, index=False)
