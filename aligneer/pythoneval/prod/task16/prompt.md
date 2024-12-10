In our backend Python project, we need to implement a function called aggregate_payments that connects to the PostgreSQL database using the provided credentials. This function should retrieve payment data from the payment table and aggregate the payments into buckets based on a given interval parameter (which can be 'hourly', 'daily', or 'monthly').

The function should compute the average payment amount within each time bucket and return a list of dictionaries with the time bucket label and the average payment amount.

The database connection details are:

host: postgres.c58u848ggx5b.us-west-1.rds.amazonaws.com
username: readonly_user
port: 5432
password: ``
database: pagila
The payment table schema is as follows:

payment_id (PK)
customer_id (FK)
staff_id (FK)
rental_id (FK)
amount
payment_date
Could you provide the implementation code for the aggregate_payments function?