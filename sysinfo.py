import platform

# Get system information
system_info = {
    'system': platform.system(),
    'node': platform.node(),
    'release': platform.release(),
    'version': platform.version(),
    'machine': platform.machine(),
    'processor': platform.processor()
}

print("System Information:")
for key, value in system_info.items():
    print(f"{key}: {value}")
