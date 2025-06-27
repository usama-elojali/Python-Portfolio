# Server names and CPU usage pecentages
server_1 = int(input("Enter CPU usage for Server 1: "))
server_2 = int(input("Enter CPU usage for Server 2: "))
server_3 = int(input("Enter CPU usage for Server 3: "))

# Check server_1
if server_1 < 50:
    print("Server 1 is running smoothly. ✅")
elif 50 <= server_1 < 80:
    print("Server 1 is under moderate load. ⚠️")
else:
    print("Server 1 is under heavy load! ❌")

# Check server_2
if server_2 < 50:
    print("Server 2 is running smoothly. ✅")
elif 50 <= server_2 < 80:
    print("Server 2 is under moderate load. ⚠️")
else:
    print("Server 2 is under heavy load! ❌")

# Check server_3
if server_3 < 50:
    print("Server 3 is running smoothly. ✅")
elif 50 <= server_3 < 80:
    print("Server 3 is under moderate load. ⚠️")
else:
    print("Server 3 is under heavy load! ❌")