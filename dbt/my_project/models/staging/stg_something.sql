-- default without config is view not table
WITH source AS (
    SELECT *
    FROM {{source("dev", "raw_weather_data")}}
)

SELECT 
    id,
    city,
    temperature
FROM source
