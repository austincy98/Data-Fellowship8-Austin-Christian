{{ config(materialized='table') }}

with source_data as (
    select * from {{ source('taxi_tripdata', 'taxi_tripdata01') }}
)

select * from source_data