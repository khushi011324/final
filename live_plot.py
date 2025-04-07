import matplotlib.pyplot as plt
import matplotlib.animation as animation
import csv

x_data, y_data = [], []

def animate(i):
    with open('i2c_data_log.csv') as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        x_data.clear()
        y_data.clear()
        for row in reader:
            if len(row) == 2:
                x_data.append(row[0])
                y_data.append(int(row[1]))
        x_data[:] = x_data[-50:]
        y_data[:] = y_data[-50:]

    ax.clear()
    ax.plot(x_data, y_data, color='blue')
    ax.set_title('Live Sensor Data')
    ax.set_xlabel('Time')
    ax.set_ylabel('Value')
    plt.xticks(rotation=45)

fig, ax = plt.subplots()
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.tight_layout()
plt.show()
