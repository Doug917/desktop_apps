'''

'''
#------------------------------------------------------------------------------

import PySimpleGUI as sg
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



def image_window():
	layout = [[sg.Image('ROLL_PICTURE.png')]]
	return sg.Window('Roll Dimensions', layout)

def chart_window(pn, od, core):
	xrange = np.linspace(core, od, 100)
	baseval = od**2 - core**2
	yrange = (xrange**2 - core**2) / baseval
	plt.plot(xrange, yrange, '-k')
	plt.title(pn)
	plt.xlabel('OD')
	plt.ylabel('Roll Fraction')
	plt.grid(axis='both')
	plt.show()

	

def main():
	#import existing data from xlsx
	data = pd.read_excel('Roll_Data.xlsx', converters={'Part Number':str,'OD':float,'CORE':float})
	data = data.set_index('Part Number')
	
	#data.set_index('Part Number')
	layout = [\
			sg.Text("ROLL COUNTER")\
	 	],\
	 	[\
			sg.Text("Part Number: "),\
			sg.In(size=(25, 1), enable_events=True, key="-PN-"),\
			sg.Button("Show Chart"),\
	 	],\
		[\
			sg.Text("Part Number Not Found.  Please re-enter.", text_color='red', background_color='#DAE0E6', visible=False, key="-Error-")\
		],\
	 	[\
			sg.Button("Display Diagram")\
	 	]

	window = sg.Window("DATA ASSIST WIDGETS", layout, size=(1000,500), background_color='#DAE0E6')

	while True:
		event, values = window.read()
		if event == "Exit" or event == sg.WIN_CLOSED:
        		break
		if event == "Show Chart":
			try:
				pn = values["-PN-"]
				od = data.loc[pn][0]
				core = data.loc[pn][1]
			except:
				window["-Error-"].update(visible=True)
			else:
				window["-Error-"].update(visible=False)
				chart_window(pn, od, core)
		if event == "Display Diagram":
			windowImage = image_window()
			windowImage.read()	#must include this command to see new window

	window.close()

if __name__ == "__main__":
	main()
















