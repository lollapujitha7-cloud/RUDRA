def calculate_sensor_confidence(imu_health, vio_health):
    """
    Combine IMU and VIO health scores.
    Both inputs should be between 0 and 1.
    """

    imu_weight = 0.5
    vio_weight = 0.5

    confidence = (
        imu_health * imu_weight +
        vio_health * vio_weight
    )

    return float(confidence)


# Example sensor health values
imu_health = 0.90
vio_health = 0.60

confidence = calculate_sensor_confidence(
    imu_health,
    vio_health
)

print("IMU Health:", imu_health)
print("VIO Health:", vio_health)
print("Overall Sensor Confidence:", round(confidence, 3))