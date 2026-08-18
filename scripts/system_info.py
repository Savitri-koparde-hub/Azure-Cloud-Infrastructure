import platform
import shutil

print("=== Vision Board System Information ===")
print(f"OS: {platform.system()} {platform.release()}")
print(f"Python: {platform.python_version()}")
print(f"CPU cores: {__import__('os').cpu_count()}")
total, used, free = shutil.disk_usage(".")
print(f"Disk free: {free / (1024**3):.2f} GB")
