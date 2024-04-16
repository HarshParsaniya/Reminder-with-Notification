import pandas as pd
import time
from plyer import notification


# Read Excel file into a pandas DataFrame
df = pd.read_excel('c:\\Users\\harsh\\Desktop\\Python Project\\Reminder with notification\\Routine Time Table.xlsx')

# Get the columns of the DataFrame
columns = df.columns

# Convert each column to a list and store in a list

column_lists1 = []
for i in df.columns:
    column_lists1.append(df[i].tolist())

t = time.localtime()
local_date = time.strftime("%d-%m-%Y", t)
local_time = time.strftime("%H:%M",t)
description=None
for i in range(len(df)):
    if str(df[columns[1]][i].strftime('%d-%m-%Y')) == local_date and str(df[columns[2]][i].strftime('%H:%M')) == local_time:
        description=column_lists1[0][i]

def show_notification(message):
    notification.notify(
        title='Routine Work',
        message=message,
        timeout=10  # Notification will disappear after 10 seconds
    )

if __name__ == "__main__":
    if description is not None:
        show_notification(description)
    else:
        print('Something went wrong')
    # Keep the script running for a while to show the notification
    # time.sleep(15)