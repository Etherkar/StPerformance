from __future__ import print_function

import os.path

import pandas as pd
# from google.auth.transport.requests import Request
# from google.oauth2.credentials import Credentials
# from google_auth_oauthlib.flow import InstalledAppFlow
# from googleapiclient.discovery import build
# from googleapiclient.errors import HttpError
#
# # If modifying these scopes, delete the file token.json.
# SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
#
# # The ID and range of a sample spreadsheet.
# SAMPLE_SPREADSHEET_ID = 'ID своей гугл таблицы'
# SAMPLE_RANGE_NAME = 'Performance2023'


def read():
    # """Shows basic usage of the Sheets API.
    # Prints values from a sample spreadsheet.
    # """
    # creds = None
    # # The file token.json stores the user's access and refresh tokens, and is
    # # created automatically when the authorization flow completes for the first
    # # time.
    # if os.path.exists('Путь к токену, или клиенту\\token.json'):
    #     creds = Credentials.from_authorized_user_file('Путь к токену, или клиенту\\token.json', SCOPES)
    # # If there are no (valid) credentials available, let the user log in.
    # if not creds or not creds.valid:
    #     if creds and creds.expired and creds.refresh_token:
    #         creds.refresh(Request())
    #     else:
    #         flow = InstalledAppFlow.from_client_secrets_file(
    #             'Путь к токену, или клиенту\\client.json', SCOPES)
    #         creds = flow.run_local_server(port=0)
    #     # Save the credentials for the next run
    #     with open('Путь к токену, или клиенту\\token.json', 'w') as token:
    #         token.write(creds.to_json())
    #
    # try:
    #     service = build('sheets', 'v4', credentials=creds)
    #
    #     # Call the Sheets API
    #     sheet = service.spreadsheets()
    #     result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
    #                                 range=SAMPLE_RANGE_NAME).execute()
    #     values = result.get('values', [])
    #
    #     if not values:
    #         print('No data found.')
    #         return
    #     #print('Name, Major:')
    #     #print(values[1:])
    #     # for row in values:
    #     #     # Print columns A and E, which correspond to indices 0 and 4.
    #     #     print(row)
        values = [  [""],
                    ["FIO"],
                    ["Гнеушев Максим Степанович"],
                    ["Коротовских Сергей Игоревич"],
                    ["Малкова Александра Михайловна"],
                    ["Муртазалиев Арсен Гаджимурадович"],
                    ["Сандрюков Андрей Максимович"],
                    ["Сапожникова Анастасия Павловна"],
                    ["Солиева Малика Комиловна"],
                    ["Трубин Павел Сергеевич"],
                    ["Федосеева Ульяна Сергеевна"],
                    ["Хафизов Тимур Дамирович"],
                    ["Шаков Антон Эдуардович"],
                    ["Шукаев Павел Андреевич"],
                    ["Щинников Артём Валерьевич"],
                    ["Аношенко Анастасия Леонидовна"],
                    ["Бурхацкий Дмитрий Николаевич"],
                    ["Высоцкий Константин Сергеевич"],
                    ["Голева Марина Михайловна"],
                    ["Горшков Илья Сергеевич"],
                    ["Гринько Дарья Павловна"],
                    ["Данаев Адлан Магомедович"],
                    ["Дельмамбетов Арслан Меньлялиевич"],
                    ["Еськова Полина Сергеевна"],
                    ["Касымов Осим Комилович"],
                    ["Масюкова Виктория Алексеевна"],
                    ["Мкртчян Шогерь Бориковна"],
                    ["Мороз Владислав Николаевич"],
                    ["Шагалеева Алина Илфаковна"],
                    ["Якшибаева Эльза Хакимовна"],
                    ["Акулинина Регина Рафисовна"],
                    ["Андреева Мария Вячеславовна"],
                    ["Барбулат Руслан Григорьевич"],
                    ["Блинова Юлия Сергеевна"],
                    ["Борисов Иван Борисович"],
                    ["Мамедова Нурай Енар кызы"],
                    ["Рыцев Артур Эдуардович"],
                    ["Сагура Ксения Викторовна"],
                    ["Семенкова Екатерина Витальевна"],
                    ["Смирнов Даниил Романович"],
                    ["Альмухаметова Лейсян Рустамовна"],
                    ["Стародубцева Ирина Вадимовна"],
                    ["Ткачева Вера Андреевна"],
                    ["Тымцуник Мария Александровна"],
                    ["Швырёва Виктория Александровна"],
                    ["Губская Карина Игоревна"],
                    ["Гибадуллин Эрнест Рустамович"],
                    ["Каримов Тагир Миннурович"],
                    ["Еременко Анастасия Андреевна"],
                    ["Саитгазиева Маликахон Шакаралиевна"],
                    ["Кузнецов Матвей Андреевич"],
                    ["Рахманин Антон Евгеньевич"],
                    ["Балсарин Даниил Евгеньевич"],
                    ["Кустов Андрей Андреевич"],
                    ["Вострокнутов Виталий Юрьевич"],
                    ["Смолина Юлия Александровна"],
                    ["Зайцев Артем Леонидович"],
                    ["Нурияхметова Алсу Мударисовна"],
                    ["Никитина Екатерина Сергеевна"],
                    ["Антипина Анна Александровна"],
                    ["Дударева Полина Ивановна"],
                    ["Асямолова Анастасия Михайловна"],
                    ["Явтушенко Николай Олегович"],
                    ["Сметанин Никита Александрович"],
                    ["Комарова Ангелина Юрьевна"],
                    ["Багаутдинова Екатерина Эдуардовна"],
                    ["Нестеров Николай Сергеевич"],
                    ["Кондратьева Валерия Альбертовна"],
                    ["Генералова Анастасия Сергеевна"],
                    ["Энгельман Филипп Владимирович"],
                    ["Лагутенко Артём Русланович"],
                    ["Королев Богдан Сергеевич"],
                    ["Хафизов Тимур Дамирович"]]
        columns = values[1]
        data = values[2:]
        df = pd.DataFrame(data, columns=columns)
        return df
    # except HttpError as err:
    #     print(err)

# def write(data, sheetname=SAMPLE_RANGE_NAME):
#     """Shows basic usage of the Sheets API.
#     Prints values from a sample spreadsheet.
#     """
#     creds = None
#     # The file token.json stores the user's access and refresh tokens, and is
#     # created automatically when the authorization flow completes for the first
#     # time.
#     if os.path.exists('Путь к токену, или клиенту\\token.json'):
#         creds = Credentials.from_authorized_user_file('Путь к токену, или клиенту\\token.json', SCOPES)
#     # If there are no (valid) credentials available, let the user log in.
#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             flow = InstalledAppFlow.from_client_secrets_file(
#                 'Путь к токену, или клиенту\\client.json', SCOPES)
#             creds = flow.run_local_server(port=0)
#         # Save the credentials for the next run
#         with open('Путь к токену, или клиенту\\token.json', 'w') as token:
#             token.write(creds.to_json())
#
#     try:
#         service = build('sheets', 'v4', credentials=creds)
#
#         # Call the Sheets API
#         sheet = service.spreadsheets()
#         vr_data = {
#             'majorDimension': 'ROWS',
#             'values': data
#         }
#         sheet.values().update(
#             spreadsheetId=SAMPLE_SPREADSHEET_ID,
#             valueInputOption='USER_ENTERED',
#             range=sheetname + '!A3',
#             body=vr_data
#         ).execute()
#     except HttpError as err:
#         print(err)

##print(__name__)