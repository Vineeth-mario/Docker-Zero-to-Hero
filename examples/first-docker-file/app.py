import psutil
import time

def get_system_metrics():
    """Collects system resource usage metrics."""
    metrics = {
        "CPU Usage (%)": psutil.cpu_percent(interval=1),
        "Memory Usage (%)": psutil.virtual_memory().percent,
        "Disk Usage (%)": psutil.disk_usage('/').percent
    }
    return metrics

if __name__ == "__main__":
    print("Starting System Monitoring...")
    while True:
        metrics = get_system_metrics()
        print(metrics)
        time.sleep(5)  # Adjust interval as needed

