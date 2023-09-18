'''
User-input:

field1 >>		name of first excel file
field2 >>		name of second excel file
index column >>		key column for merging

Run >>			run program to write output excel file
'''
#------------------------------------------------------------------------------

import PySimpleGUI as sg
import os.path
import pandas as pd

layout = [\
		sg.Text("XLSX MERGE")\
	 ],\
	 [\
		sg.In("File1", size=(25, 1), enable_events=True, key="-FOLDER1-"),\
		sg.FileBrowse(),\
		sg.In("File2", size=(25, 1), enable_events=True, key="-FOLDER2-"),\
		sg.FileBrowse()\
	 ],\
	 [\
		sg.Text("Enter name of Left Key Column: "),\
		sg.In(size=(25, 1), enable_events=True, key="-KEY1-")\
	 ],\
	 [\
		sg.Text("Enter name of Right Key Column: "),\
		sg.In(size=(25, 1), enable_events=True, key="-KEY2-")\
	 ],\
	 [\
		sg.Button("Run")\
	 ]\

window = sg.Window("DATA ASSIST WIDGETS", layout, size=(1000,500), background_color='#DAE0E6')


while True:
	event, values = window.read()
	if event == "Exit" or event == sg.WIN_CLOSED:
        	break
	if event == "-FOLDER1-":
		file1 = values["-FOLDER1-"]
	if event == "-FOLDER2-":
		file2 = values["-FOLDER2-"]
	if event == "-KEY1-":
		index_col_left = values["-KEY1-"]
	if event == "-KEY2-":
		index_col_right = values["-KEY2-"]
	if event == "Run":
		df1 = pd.read_excel(file1)
		df2 = pd.read_excel(file2)

		#set index columns for join to be same
		#df1 = df1.set_index(f"{index_col_left}")
		#df2 = df2.set_index(f"{index_col_right}")

		#merge table on index
		output = df1.merge(df2, left_on=f"{index_col_left}", right_on=f"{index_col_right}", how="inner")
		output.to_excel('out.xlsx')
window.close()
















