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
