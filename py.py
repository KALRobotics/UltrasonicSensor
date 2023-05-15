collected = []
sensor_data = []


def sensor_data_to_average():
    total = sum(sensor_data)
    average = total / len(sensor_data)
    if average <= 10:
        return "Stop"
    else:
        return "Continue"
