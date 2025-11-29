-- A workspace for cleaning and standardizing raw source tables before building final analytics models. It prepares data with consistent column names and types for downstream use.
{{ config(
    materialized="table",
    unique_key="id"
)}}

-- get the source from the sources.yml
WITH source AS (
    SELECT *
    FROM {{source("dev", "raw_weather_data")}}
),

de_dup AS (
    SELECT 
        *,
        ROW_NUMBER() OVER(PARTITION BY time ORDER BY inserted_at) AS rn
    FROM source
)

SELECT 
    id,
    city,
    temperature,
    weather_descriptions,
    wind_speed,
    time AS weather_time_local,
    (inserted_at + (utc_offset || 'hours')::interval) AS inserted_at_local
FROM de_dup
WHERE rn = 1

