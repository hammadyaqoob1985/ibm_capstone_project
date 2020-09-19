# -*- coding: utf-8 -*-
import pandas as pd # primary data structure library
import matplotlib as mpl
import matplotlib.pyplot as plt
import folium

df = pd.read_csv("Data-Collisions.csv", index_col=0)
print(df.columns)
print(df['ROADCOND'].isnull().sum())
