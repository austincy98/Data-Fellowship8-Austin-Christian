{{ config(materialized='table', SCHEMA='staging') }}

with source_data as (
    select * from {{ source('taxi_tripdata', 'taxi_tripdata01') }}
),

renamed as(
    Select VendorID,
    tpep_pickup_datetime as pickup_datetime,
    tpep_dropoff_datetime as dropoff_datetime,
    RatecodeID as rate_code,
    PULocationID as pickup_location,
    DOLocationID as drop_location

    from source_data

)

select * from renamed