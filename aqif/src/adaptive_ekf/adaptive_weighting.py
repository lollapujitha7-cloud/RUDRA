def calculate_adaptive_weights(imu_health, vio_health):
    """
    Calculate adaptive sensor weights based on health scores.
    """

    total_health = imu_health + vio_health

    # Safety check
    if total_health == 0:
        return 0.5, 0.5

    imu_weight = imu_health / total_health
    vio_weight = vio_health / total_health

    return float(imu_weight), float(vio_weight)


# Test Case 1: IMU is healthier
imu_health = 0.9
vio_health = 0.4

imu_weight, vio_weight = calculate_adaptive_weights(
    imu_health,
    vio_health
)

print("IMU Weight:", round(imu_weight, 3))
print("VIO Weight:", round(vio_weight, 3))