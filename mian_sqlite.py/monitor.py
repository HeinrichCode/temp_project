import speedtest
import datetime
import csv
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation


s = speedtest.Speedtest()
fig = plt.figure()

ax1 = fig.add_subplot(1,1,1)


with open('InternetSpeed.txt', mode='w') as speedcsv:
    csv_writer = csv.DictWriter(speedcsv, fieldnames=['time', 'downspeed', 'upspeed'])
    csv_writer.writeheader()
    while True:
        time_now = datetime.datetime.now().strftime("%H:%M:%S")
        downspeed = round((round(s.download()) / 1048576), 2)
        upspeed = round((round(s.upload()) / 1048576), 2)
        csv_writer.writerow({
            'time': time_now,
            'downspeed': downspeed,
            "upspeed": upspeed
        })
        def animate(i):
            pullData = open("InternetSpeed.csv","r").read()
            dataArray = pullData.split('\n')
            xar = []
            yar = []
            for eachLine in dataArray:
                if len(eachLine)>1:
                    x,y = eachLine.split(',')
                    xar.append(int(x))
                    yar.append(int(y))
            ax1.clear()
            ax1.plot(xar,yar)

        ani = animation.FuncAnimation(fig, animate, interval=1000)
        plt.show()

        print("Downloadspeed: {}".format(downspeed))
        # 60 seconds sleep
        time.sleep(60)

        