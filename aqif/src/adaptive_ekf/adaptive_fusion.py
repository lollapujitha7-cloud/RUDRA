def calculate_adaptive_weights(imu_health, vio_health):
    total_health = imu_health + vio_health

    if total_health == 0:
        return 0.5, 0.5

    imu_weight = imu_health / total_health
    vio_weight = vio_health / total_health

    return imu_weight, vio_weight


def adaptive_fusion(imu_estimate, vio_estimate, imu_health, vio_health):

    imu_weight, vio_weight = calculate_adaptive_weights(
        imu_health,
        vio_health
    )

    fused_estimate = (
        imu_weight * imu_estimate +
        vio_weight * vio_estimate
    )

    return fused_estimate, imu_weight, vio_weight


# Example data
imu_estimate = 10.0
vio_estimate = 12.0

imu_health = 0.9
vio_health = 0.4


fused_position, imu_weight, vio_weight = adaptive_fusion(
    imu_estimate,
    vio_estimate,
    imu_health,
    vio_health
)

print("IMU Estimate:", imu_estimate)
print("VIO Estimate:", vio_estimate)

print("\nIMU Weight:", round(imu_weight, 3))
print("VIO Weight:", round(vio_weight, 3))

print("\nAdaptive Fused Position:", round(fused_position, 3))