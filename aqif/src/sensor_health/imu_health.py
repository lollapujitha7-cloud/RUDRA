import numpy as np


def calculate_imu_health(acceleration, gyroscope):
    accel_noise = np.std(acceleration)
    gyro_noise = np.std(gyroscope)

    total_noise = accel_noise + gyro_noise

    health_score = 1 / (1 + total_noise)

    return float(health_score)


# Healthy IMU data
healthy_acceleration = np.random.normal(0, 0.05, 100)
healthy_gyroscope = np.random.normal(0, 0.02, 100)

healthy_score = calculate_imu_health(
    healthy_acceleration,
    healthy_gyroscope
)

print("Healthy IMU Score:", round(healthy_score, 3))


# Noisy IMU data
noisy_acceleration = np.random.normal(0, 0.5, 100)
noisy_gyroscope = np.random.normal(0, 0.3, 100)

noisy_score = calculate_imu_health(
    noisy_acceleration,
    noisy_gyroscope
)

print("Noisy IMU Score:", round(noisy_score, 3))