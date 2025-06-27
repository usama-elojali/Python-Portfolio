import random

# List of server names
servers = ["Server A", "Server B", "Server C"]

# List to hold CPU usage for each server
cpu_usages = []

# Assign random CPU usage to each server
cpu1 = random.randint(10, 100)
cpu2 = random.randint(10, 100)
cpu3 = random.randint(10, 100)

cpu_usages.append(cpu1)
cpu_usages.append(cpu2)
cpu_usages.append(cpu3)

# Check and print server status
print("=== Server Status ===")

# Server A
if cpu_usages[0] < 50:
    print("Server A is Healthy ✅")
elif cpu_usages[0] < 80:
    print("Server A is Moderate ⚠️")
else:
    print("Server A is Overloaded ❌")

# Server B
if cpu_usages[1] < 50:
    print("Server B is Healthy ✅")
elif cpu_usages[1] < 80:
    print("Server B is Moderate ⚠️")
else:
    print("Server B is Overloaded ❌")

# Server C
if cpu_usages[2] < 50:
    print("Server C is Healthy ✅")
elif cpu_usages[2] < 80:
    print("Server C is Moderate ⚠️")
else:
    print("Server C is Overloaded ❌")

# Print CPU usage for each server
print("\n=== CPU Usage ===")
print(f"Server A: {cpu_usages[0]}%")
print(f"Server B: {cpu_usages[1]}%")
print(f"Server C: {cpu_usages[2]}%") 