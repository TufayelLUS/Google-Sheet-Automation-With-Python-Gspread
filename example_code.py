from oauth2client.service_account import ServiceAccountCredentials
import gspread



sheet_name = 'Copy of Formula'  # change the sheet name here
gsheet_creds_file = 'credentials.json'  # change creds file if needed


def readSKUFromSheet():
    scope = ['https://www.googleapis.com/auth/spreadsheets',
             'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        gsheet_creds_file, scope)
    client = gspread.authorize(creds)
    sheet = client.open(sheet_name).sheet1
    print(sheet.cell(11, 3).value) # this line reads the cell
    sheet.update_cell(11, 3, 1.5) # this value updates the cell again


if __name__ == "__main__":
    readSKUFromSheet()
