from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt


base_dir = Path(__file__).parent
sitka_file = base_dir / "weather_data" / "sitka_weather_2021_simple.csv"
death_valley_file = base_dir / "weather_data" / "death_valley_2021_simple.csv"


def get_weather_data(path, high_col, low_col):
    dates, highs, lows = [], [], []
    lines = path.read_text().splitlines()
    reader = csv.reader(lines)
    header_row = next(reader)
    for row in reader:
        try:
            current_date = datetime.strptime(row[2], "%Y-%m-%d")
            high = int(row[high_col])
            low = int(row[low_col])
        except ValueError:
            
            continue
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    return dates, highs, lows


sitka_dates, sitka_highs, sitka_lows = get_weather_data(sitka_file, 4, 5)

dv_dates, dv_highs, dv_lows = get_weather_data(death_valley_file, 3, 4)


all_highs = sitka_highs + dv_highs
all_lows = sitka_lows + dv_lows
y_min = min(all_lows) - 5  
y_max = max(all_highs) + 5


plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.plot(sitka_dates, sitka_highs, color="red", alpha=0.5, label="High")
ax.plot(sitka_dates, sitka_lows, color="blue", alpha=0.5, label="Low")
ax.fill_between(sitka_dates, sitka_highs, sitka_lows, color="blue", alpha=0.1)
ax.set_title("Daily Temperatures, 2021 — Sitka, AK", fontsize=16)
ax.set_ylabel("Temperature (°F)")
ax.set_ylim(y_min, y_max)
fig.autofmt_xdate()
ax.legend()
plt.show()


fig, ax = plt.subplots()
ax.plot(dv_dates, dv_highs, color="red", alpha=0.5, label="High")
ax.plot(dv_dates, dv_lows, color="blue", alpha=0.5, label="Low")
ax.fill_between(dv_dates, dv_highs, dv_lows, color="blue", alpha=0.1)
ax.set_title("Daily Temperatures, 2021 — Death Valley, CA", fontsize=16)
ax.set_ylabel("Temperature (°F)")
ax.set_ylim(y_min, y_max)  
fig.autofmt_xdate()
ax.legend()
plt.show()
