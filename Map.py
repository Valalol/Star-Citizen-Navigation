import csv
import os
import time


import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation as animation

from mpl_toolkits.basemap import Basemap

print(f'Searching for the Logs.csv file')

while not os.path.isdir(r'Logs') or not os.path.isfile(r'Logs/Logs.csv'):
    time.sleep(2)

print(f'Logs.csv file found !')
time.sleep(1)
print(f'Start plotting ...')



def split_at_value(list, value):
    indices = [i for i, x in enumerate(list) if x['Key'] == value]
    for start, end in zip([0, *indices], [*indices, len(list)]):
        yield list[start+1:end]



fig = plt.figure(figsize=[8,4])
fig.subplots_adjust(left=0, bottom=0, right=1, top=1)
plt.get_current_fig_manager().window.wm_iconbitmap(r"Images/icon.ico")
plt.gcf().canvas.manager.set_window_title('Navigation Map')


m = Basemap(projection='cyl', resolution=None,
            llcrnrlat=-90, urcrnrlat=90,
            llcrnrlon=-180, urcrnrlon=180)

old_data = []

def animate (i):
    global old_data
    new_data = []
    with open(r'Logs/Logs.csv', 'rt') as csv_file:
        reader = csv.DictReader(csv_file)
        row_index = 0
        for row in reader:
            if row:
                row_index += 1
                new_data.append(row)
    
    Runs = []
    for run in split_at_value(new_data, 'New_Run'):
        Runs.append(run)
    Current_run = Runs[-1]
    
    container = Current_run[-1]['Container']
    
    lats = []
    longs = []
    
    for row in Current_run:
        lat = float(row['Latitude'])
        long = float(row['Longitude'])
        
        lats.append(lat)
        longs.append(long)
    
    
    if new_data != old_data:
        print('Updating ...')
        plt.cla()
        
        if container != 'None':
            m.warpimage(f"Images/{container}_sheet.png")
        m.plot(longs, lats, latlon=True, color='c', marker='.', markersize=9, markeredgecolor='k', markeredgewidth=0.5, linestyle='-', linewidth=0.8, alpha=0.75)
        
        old_data = new_data

ani = animation(fig, animate, interval=1000)

plt.show()
