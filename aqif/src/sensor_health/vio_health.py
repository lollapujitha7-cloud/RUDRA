def calculate_vio_health(feature_count, tracking_quality):
    """
    Calculate VIO health score.

    feature_count: number of visual features detected
    tracking_quality: tracking quality between 0 and 1
    """

    # Normalize feature count
    feature_score = min(feature_count / 100, 1.0)

    # Combine feature quality and tracking quality
    health_score = (
        0.5 * feature_score +
        0.5 * tracking_quality
    )

    return float(health_score)


# Healthy VIO
healthy_score = calculate_vio_health(
    feature_count=90,
    tracking_quality=0.95
)

print("Healthy VIO Score:", round(healthy_score, 3))


# Poor VIO
poor_score = calculate_vio_health(
    feature_count=20,
    tracking_quality=0.40
)

print("Poor VIO Score:", round(poor_score, 3))