from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt


path = Path("weather_data/san_francisco_2026_simple.csv")
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)


dates, highs, lows = [], [], []
for row in reader:
    try:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        high = int(row[3])
        low = int(row[4])
    except ValueError:
        print(f"Missing data for {row[2]}")
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)


plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.plot(dates, highs, color="red", alpha=0.6, label="High")
ax.plot(dates, lows, color="blue", alpha=0.6, label="Low")
ax.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)


ax.set_title("Daily High and Low Temperatures, 2026\nSan Francisco, CA", fontsize=20)
ax.set_ylabel("Temperature (F)", fontsize=16)
fig.autofmt_xdate()
ax.tick_params(labelsize=12)
ax.legend()

plt.show()
