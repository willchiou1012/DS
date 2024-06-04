import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
from zoneinfo import ZoneInfo
from type import type

def storeFallData():
    scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive.file']

    creds = Credentials.from_service_account_file('', scopes=scope)
    client = gspread.authorize(creds)

    sheet_id = ''
    sheet = client.open_by_key(sheet_id).sheet1

    tz = ZoneInfo("Asia/Taipei")

    # 存入資料以日期時間為例，可再往下添加需要塞入資料庫的資料
    today_date = datetime.now(tz).strftime('%Y-%m-%d')
    today_time = datetime.now(tz).strftime('%H:%M:%S')
    type = type.ball('找到球了')
    type = type.food('碗為空的')
    type = type.sofa('沙發遭受到破損')

    row_data = [today_date, today_time]
    sheet.append_row(row_data)

    last_row_values = sheet.get_all_records()[-1]
    return 0
