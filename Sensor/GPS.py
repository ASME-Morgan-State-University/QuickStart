import random
def getGPS():
    try:
        random_numbers = [float(random.randint(1, 100)) for _ in range(3)]
        Lon = random_numbers[0]
        lat = random_numbers[1]
        SC = random_numbers[2]
        return Lon, lat, SC
    except Exception as e:
        print(f"Error getting IMU data: {e}")
        return 0