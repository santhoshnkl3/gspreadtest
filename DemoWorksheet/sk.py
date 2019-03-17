import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('Worksheet-07c30993ff5e.json', 'scope')
gc = gspread.authorize(credentials)
sheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/1QSmKaJxFacAmRt8HmSsYQHp21KPtofDp0jAzwAFs0wI')
worksheet = sheet.get_worksheet('0')
