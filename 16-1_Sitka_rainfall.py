from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt


base_dir = Path(__file__).parent
path = base_dir / "weather_data" / "sitka_weather_2021_full.csv"


lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)


dates, rainfall = [], []
for row in reader:
    current_date = datetime.strptime(row[2], "%Y-%m-%d")
    try:
        prcp = float(row[5])
    except ValueError:
        print(f"Missing rainfall data for {current_date}")
    else:
        dates.append(current_date)
        rainfall.append(prcp)


plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.plot(dates, rainfall, color="blue", alpha=0.6)
ax.fill_between(dates, rainfall, facecolor="blue", alpha=0.2)


title = "Daily Rainfall, 2021\nSitka, AK"
ax.set_title(title, fontsize=20)
fig.autofmt_xdate()
ax.set_ylabel("Rainfall (inches)", fontsize=16)
ax.tick_params(labelsize=14)

plt.show()
