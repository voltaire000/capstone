# imports
import cv2
from pyzbar import pyzbar
import pandas as pd
csv = pd.read_csv('C:/Users/Jonathan/dsi/Capstone/csv/values.csv', index_col = 'data')
def read_barcodes(frame):
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x, y , w, h = barcode.rect
        #1
        barcode_info = barcode.data.decode('utf-8')
        cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 255, 0), 2)

        #2
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, barcode_info, (x + 6, y - 6), font, 2.0, (255, 255, 255), 1)
        #3
        barcode_info = int(barcode_info)
        with open("barcode_result.txt", mode ='w') as file:
            file.write(str(csv.loc[barcode_info][0]))
            file.write(str(csv.loc[barcode_info][1]))
            file.write(str(csv.loc[barcode_info][2]))
            file.write(str(csv.loc[barcode_info][3]))
            file.write(str(csv.loc[barcode_info][4]))
            file.write(str(csv.loc[barcode_info][5]))
            file.write(str(csv.loc[barcode_info][6]))
            file.write(str(csv.loc[barcode_info][7]))
    return frame

def main():
    #1
    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()
    #2
    while ret:
        ret, frame = camera.read()
        frame = read_barcodes(frame)
        cv2.imshow('Barcode/QR code reader', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    #3
    camera.release()
    cv2.destroyAllWindows()
#4
if __name__ == '__main__':
    main()
