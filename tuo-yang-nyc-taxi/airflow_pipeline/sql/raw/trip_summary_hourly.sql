SELECT
    date_trunc('hour', tpep_pickup_datetime) AS pickup_hour,
    COUNT(*) AS trip_count,
    ROUND(AVG(fare_amount), 2) AS avg_fare,
    ROUND(AVG(tip_amount), 2) AS avg_tip,
    SUM(passenger_count) AS total_passengers,
    ROUND(AVG(trip_distance), 2) AS avg_distance,
    AVG(total_amount) AS avg_total_amount,
    AVG(EXTRACT(EPOCH FROM tpep_dropoff_datetime - tpep_pickup_datetime)/60.0) AS avg_duration_min
FROM yellow_taxi
WHERE trip_distance > 0 AND total_amount > 0
    AND tpep_pickup_datetime BETWEEN '2023-01-01' AND '2023-04-01'
GROUP BY date_trunc('hour', tpep_pickup_datetime)
ORDER BY pickup_hour;