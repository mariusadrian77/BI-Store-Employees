# AnalitiQs-Assignment

## Notes:

- Lampertheim is both in france and germany.

- Employee contains data of individual employess
Stores contains information about stores.
Stores_ltm contains aggregated store data from the last 12 months per unique location-country combination named as store_area.

- So, 1 store can have multiple employees (1 to many, stores --> employee)
One store-area can have multiple individual stores in the same store_area (1 to many, store ltm --> stores)

- So a store_id needed the following columns: country + location + store_opening + reference_date.

- The reference date was needed because there were stores that opened at the same time in the same store_area.
