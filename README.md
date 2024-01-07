# desktop_apps

Office apps.

pdf_to_xls_app is an example of using python to scrape a pdf customer order
into an excel spreadsheet.  The regex code is specific to the particular
customer order files I was scraping which have personal information and
therefore are not included.

excel_merge takes as input the paths to two excel files
and merges them (inner join) on user-specified key columns.
The application is an alternative to repeated using excel's
Vlookup function.

RGB_codes converts RGB triplet to hexcode and shows a color sample.

roll_count is an app for creating a graph of fraction of a roll
remaining based on the core size and initial outer diameter (OD).
This tool can be usefull for cycle counting inventory that
comes in rolls such as stickers, labels, tape, etc.

MD04_counts scapes the print output from the MD04 window in SAP
for a part number.  The tool separates out orders on hold. 
An order might be held for several reasons including:
-errors in processing customer payment
-overdue customer balance
-holding for future delivery date.

transparency_change takes png images in the same folder and reduces the
image transparency on each.  I frequently print out screenshots from
SAP windows, and this is to reduce ink used when printing.

ToDo List is a super light weight, but fully-functional todo list app.

