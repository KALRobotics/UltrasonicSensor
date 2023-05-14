collected = []
sensor_data = []

def sensor_data_to_average():
    total = sum(sensor_data)
    average = total / len(sensor_data)
    if average <= 10:
        return "Stop"
    else:
        return "Continue"

def sensor_data_check():
    if len(sensor_data) > 20:
        sensor_data.pop(0)

def collect_sensor_data(data_point):
    sensor_data.append(data_point)
    sensor_data_check()
    collected.append(sensor_data_to_average())

if __name__ == "__main__":
    sensor_data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    data_points = [12, 23, 34, 56, 73, 23, 45, 67, 23, 45, 12, 34, 12, 34, 56, 34]
    
    for data_point in data_points:
        collect_sensor_data(data_point)

    print(collected[-1])