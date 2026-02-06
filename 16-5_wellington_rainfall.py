from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt


path = Path(__file__).parent / "weather_data" / "wellington_rainfall.csv"
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)


date_index = header_row.index("Observation time UTC")
rain_index = header_row.index("Rainfall [mm]")

dates, rainfall = [], []

for row in reader:
    try:
        
        current_date = datetime.strptime(row[date_index], "%Y-%m-%dT%H:%M:%SZ")
        rain = float(row[rain_index])
    except ValueError:
        print(f"Missing or invalid data for {row[date_index]}")
    else:
        dates.append(current_date)
        rainfall.append(rain)


plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()

ax.plot(dates, rainfall, color="blue", alpha=0.7)


ax.set_title("Daily Rainfall\nWellington, New Zealand", fontsize=20)
ax.set_ylabel("Rainfall (mm)", fontsize=16)
fig.autofmt_xdate()
ax.tick_params(labelsize=12)

plt.show()
