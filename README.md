# Google Sheet Automation With Python Gspread Library
This is a personal documentation repository for google spreadsheet automation using python and gspread library
# How to get credentials.json file?
1. Make the spreadsheet available on google drive
2. Open https://console.cloud.google.com/welcome and then create a project and activate that project.
3. Go to *APIs & Services* and select *Enable API and Services*
4. Enable "Google Drive API" and "Google Sheets API"
5. Come back to "APIs & Services" and create a Service account from "Manage service accounts" option.
6. This will download the JSON file as soon as you create a service account. Copy the service account email address and give this email the permission to become an editor of the spreadsheet that you want to edit with automation. 
Now rename the json file to "credentials.json" and place it with the python file and that's it!
# How to install the required libraries?
In the terminal/command window, execute:
<code>pip3 install gspread oauth2client</code>
# Where can I get the Gspread Documentation?
It's here: https://buildmedia.readthedocs.org/media/pdf/gspread/latest/gspread.pdf
