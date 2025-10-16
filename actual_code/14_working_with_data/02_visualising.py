import json
import matplotlib.pyplot as plt
import datetime

def load_data(path="weather.json"):
    with open("weather.json") as file:
        data = json.load(file)

    times = data["hourly"]["time"]
    temps = data["hourly"]["temperature_2m"]
    hums = data["hourly"]["relativehumidity_2m"]
    ts = [datetime.datetime.fromisoformat(t) for t in times]
    return ts, temps, hums



def line_plot(geneva, london):
    ts, temps, hums = geneva
    ts_lon, temps_lon, _= london
    plt.figure(figsize=(8,4))
    plt.plot(ts, temps, marker="x", color="red")
    plt.plot(ts_lon, temps_lon, marker="x", color="blue")
    plt.title("Temperature vs Time")
    plt.xlabel("Time")
    plt.ylabel("Temperature")
    plt.grid(True, alpha=0.3)
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig("temp_line.png", dpi=150)
    plt.show()
    plt.close()

def scatter_with_fit(temps, hums):
    plt.figure(figsize=(6, 5))
    plt.scatter(temps, hums)
    plt.title("Humidity vs Temperature")
    plt.xlabel("Temperature (°C)")
    plt.ylabel("Relative Humidity (%)")
    # Simple least-squares fit (manual, no NumPy)
    x, y = temps, hums
    n = len(x)
    meanx = sum(x)/n
    meany = sum(y)/n
    num = sum((xi-meanx)*(yi-meany) for xi, yi in zip(x, y))
    den = sum((xi-meanx)**2 for xi in x) or 1.0
    m = num / den
    b = meany - m*meanx
    # Fit line across range
    x0, x1 = min(x), max(x)
    y0, y1 = m*x0 + b, m*x1 + b
    plt.plot([x0, x1], [y0, y1])
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("humidity_scatter.png", dpi=150)
    plt.close()

def histogram(temps):
    plt.figure(figsize=(6, 4))
    plt.hist(temps, bins=10)
    plt.title("Temperature Distribution")
    plt.xlabel("Temperature (°C)")
    plt.ylabel("Count")
    mean = sum(temps)/len(temps)
    var = sum((t-mean)**2 for t in temps) / len(temps)
    std = var ** 0.5
    # Annotate mean ± std
    plt.axvline(mean)
    plt.text(mean, plt.ylim()[1]*0.9, f"μ={mean:.1f}, σ={std:.1f}")
    plt.tight_layout()
    plt.savefig("temp_hist.png", dpi=150)
    plt.close()

geneva_data = load_data("weather.json")
london_data = load_data("weather_london.json")
line_plot(geneva_data, london_data)

tms, temps, hums = geneva_data
scatter_with_fit(temps, hums)
histogram(temps)

def plot_weather(ts, temps, hums):
    """
    Plot 4 subplots using time stamps (ts), temperatures (temps), and humidities (hums).

    Subplots:
      (1) Temperature vs time
      (2) Humidity vs time
      (3) Temperature vs Humidity (scatter)
      (4) Combined vs time (twin y-axes)
    """
    fig, axes = plt.subplots(2, 2, figsize=(12, 7))
    ax1, ax2, ax3, ax4 = axes.ravel()

    # (1) Temperature vs time
    ax1.plot(ts, temps, marker="o", linewidth=1)
    ax1.set_title("Temperature vs Time")
    ax1.set_ylabel("Temperature (°C)")
    ax1.grid(True, alpha=0.3)

    # (2) Humidity vs time
    ax2.plot(ts, hums, marker="o", linewidth=1)
    ax2.set_title("Humidity vs Time")
    ax2.set_ylabel("Humidity (%)")
    ax2.grid(True, alpha=0.3)

    # (3) Temperature vs Humidity (scatter)
    ax3.scatter(temps, hums)
    ax3.set_title("Humidity vs Temperature")
    ax3.set_xlabel("Temperature (°C)")
    ax3.set_ylabel("Humidity (%)")
    ax3.grid(True, alpha=0.3)

    # (4) Combined vs time with twin y-axes
    ax4.plot(ts, temps, label="Temp (°C)", linewidth=1)
    ax4.set_title("Temp & Humidity vs Time")
    ax4.set_xlabel("Time")
    ax4.set_ylabel("Temperature (°C)")
    ax4.grid(True, alpha=0.3)
    ax4_twin = ax4.twinx()
    ax4_twin.plot(ts, hums, color="tab:orange", label="Humidity (%)", linewidth=1)
    ax4_twin.set_ylabel("Humidity (%)")

    # Rotate shared x-ticks for time plots
    for ax in (ax1, ax2, ax4):
        for label in ax.get_xticklabels():
            label.set_rotation(30)
            label.set_ha("right")

    fig.tight_layout()
    fig.savefig("weather_twin_vs_time.png", dpi=150)

plot_weather(tms, temps, hums)