"""import command
import streamlit as st
import os
import sys
from streamlit import cli as stcli"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import io
import streamlit as st
import plotly.figure_factory as ff

st.header("test app")
st.write("This is sub header")
from streamlit.web import cli as stcli

import sys

df = pd.read_csv(r"C:\Users\HP\Downloads\Opportunities (2).csv")
df[' "Solution"'] = df[' "Solution"'].str.replace("Services::::", "")
df[' "Partenaire"'] = df[' "Partenaire"'].str.replace("Vendors::::", "")
df[' "Assigned To"'] = df[' "Assigned To"'].str.replace("@ineos.ma", "")
df[' "Organization Name"'] = df[' "Organization Name"'].str.replace("Accounts::::", " ")
df[' "Organization Name"']
df[' "Contexte"']
df[' "Description"']
df[' "Campaign Source"'] = df[' "Campaign Source"'].str.replace("Campaigns::::", " ")
df[' "Campaign Source"']
df[' "Last Modified By"'] = df[' "Last Modified By"'].str.replace("@ineos.ma", "")
df[' "Last Modified By"'] = df[' "Last Modified By"'].str.replace(".", " ")
df[' "Last Modified By"']


st.header("graphe1")





l1 = []
for x in df['Rappel du partenaire technologique']:
    if x not in l1:
        l1.append(x)
l2 = []
v1 = 0
v2 = 0
v3 = 0
v4 = 0
v5 = 0
v6 = 0
v7 = 0
v8 = 0
v9 = 0
v10 = 0
v11 = 0
v12 = 0
v13 = 0
v14 = 0
v15 = 0
v16 = 0
v17 = 0
for i in range(len(df['Rappel du partenaire technologique'])):
    if df['Rappel du partenaire technologique'][i] == 'DELL EMC':
        v1 = v1 + df[' "Amount"'][i]
    if df['Rappel du partenaire technologique'][i] == 'NaN':
        V2 = v2 + df[' "Amount"'][i]
    if df['Rappel du partenaire technologique'][i] == 'VEEAM':
        v3 = v3 + df[' "Amount"'][i]
    if df['Rappel du partenaire technologique'][i] == 'HUAWEI':
        v4 = v4 + df[' "Amount"'][i]
    if df['Rappel du partenaire technologique'][i] == 'JIRA':
        v5 = v5 + df[' "Amount"'][i]
    if df['Rappel du partenaire technologique'][i] == 'IPC':
        v6 = v6 + df[' "Amount"'][i]
    if df['Rappel du partenaire technologique'][i] == 'CISCO':
        v7 = v7 + df[' "Amount"'][i]
    if df['Rappel du partenaire technologique'][i] == 'FORTINET':
        v8 = v8 + df[' "Amount"'][i]
    if df['Rappel du partenaire technologique'][i] == 'CHECK POINT':
        v9 = v9 + df[' "Amount"'][i]
    if df['Rappel du partenaire technologique'][i] == 'Symantec':
        v10 = v10 + df[' "Amount"'][i]
    if df['Rappel du partenaire technologique'][i] == 'Trend Micro':
        v11 = v11 + df[' "Amount"'][i]
    if df['Rappel du partenaire technologique'][i] == 'Beyondtrust':
        v12 = v12 + df[' "Amount"'][i]
    if df['Rappel du partenaire technologique'][i] == 'Dynatrace':
        v13 = v13 + df[' "Amount"'][i]
    if df['Rappel du partenaire technologique'][i] == 'Dell':
        v14 = v14 + df[' "Amount"'][i]
    if df['Rappel du partenaire technologique'][i] == 'Microsoft':
        v15 = v15 + df[' "Amount"'][i]
    if df['Rappel du partenaire technologique'][i] == 'Solarwinds':
        v16 = v16 + df[' "Amount"'][i]
    if df['Rappel du partenaire technologique'][i] == 'DELL EMC':
        v17 = v17 + df[' "Amount"'][i]

l2.append(v1)
l2.append(v2)
l2.append(v3)
l2.append(v4)
l2.append(v5)
l2.append(v6)
l2.append(v7)
l2.append(v8)
l2.append(v9)
l2.append(v10)
l2.append(v11)
l2.append(v12)
l2.append(v13)
l2.append(v14)
l2.append(v15)
l2.append(v16)
l2.append(v17)

d = []

for i in range(len(l1)):
    d.append([l1[i], l2[i]])
fig, ax = plt.subplots()
t = pd.DataFrame(d, columns=['Rappel du partenaire technologique', 'Amount'])
t=pd.DataFrame(d,columns=['Rappel du partenaire technologique','Amount'])
ax = t.plot(x='Rappel du partenaire technologique',y='Amount',kind='bar')
st.pyplot(fig)


if __name__ == '__main__':
    sys.argv = ["streamlit", "run", "Streamlit.py"]
    sys.exit(stcli.main())
