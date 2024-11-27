Prompt:

 I have a task where I need to build a microservice using Flask that's both scalable and fault-tolerant. Can you help me write a Python function that handles incoming POST requests with JSON payloads containing lists of floating-point numbers? The function should validate the input data, handle any errors gracefully, and process the data asynchronously for performance. Additionally, please include code to connect to the PostgreSQL database using the following credentials:
 

 - host: postgres.c58u848ggx5b.us-west-1.rds.amazonaws.com
 - username: readonly_user
 - port: 5432
 - password: [dummy password]
 - database: pagila
 

 Ensure that the function performs only read (SELECT) operations on the database, such as querying relevant tables based on the input data. Also, please make sure to include proper logging and exception handling according to microservices best practices."