import requests
import json
import xlsxwriter


# Workbook() takes one, non-optional, argument
# which is the filename that we want to create.
workbook = xlsxwriter.Workbook('reviews.xlsx')

# The workbook object is then used to add new
# worksheet via the add_worksheet() method.
worksheet = workbook.add_worksheet()

worksheet.write('A1', 'Date')
worksheet.write('B1', 'Description')
worksheet.write('C1', 'Stars')

urlNumber = 0
cellIndex = 2

while(True):
    url = 'https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=en&gl=in&pb=!1m2!1y4111766323478979231!2y1273414400129857113!2m2!1i' + \
        str(urlNumber) + \
        '0!2i10!3e1!4m5!3b1!4b1!5b1!6b1!7b1!5m2!1sRNybYaCrIaSq4t4Pi-2KgAE!7e81'

    r = requests.get(url)
    data = r.content.decode('utf-8')
    myData = data.split(")]}'")[1].strip()
    res = json.loads(myData)

    if res[2] == None:
        break

    if urlNumber > 10:
        break

    reviews = res[2]

    for review in reviews:
        # print('date:')
        # print(review[1])
        # print('desc:')
        # print(review[3])
        # print('rating:')
        # print(review[4])
        # print('\n\n')

        worksheet.write('A'+str(cellIndex), review[1])
        worksheet.write('B'+str(cellIndex), review[3])
        worksheet.write('C'+str(cellIndex), review[4])

        cellIndex = cellIndex+1

    urlNumber = urlNumber + 1


# Finally, close the Excel file
# via the close() method.
workbook.close()
