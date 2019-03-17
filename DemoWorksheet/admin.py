import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://www.googleapis.com/auth/drive','https://spreadsheets.google.com/feeds']
cr=ServiceAccountCredentials.from_json_keyfile_name('key1.json',scope)
gc=gspread.authorize(cr)

wks=gc.open('testsheet').sheet1
print(wks.acell('c1'))

#print(wks.get_all_records())
