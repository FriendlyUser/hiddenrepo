"
 I need your help with this task code using Flask and PostgreSQL. It's giving me headaches. Here's what I have:
 

 ```python
 import psycopg2
 from flask import Flask, jsonify
 

 app = Flask(__name__)
 

 @app.route('/inventory-status')
 def inventory_status():
  connection = psycopg2.connect(
  host='postgres.c58u848ggx5b.us-west-1.rds.amazonaws.com',
  port=5432,
  user='readonly_user',
  password='dummy_password',
  database='pagila'
  )
  cursor = connection.cursor()
  cursor.execute('SELECT inventory_id, film_id, store_id, last_update FROM inventory')
  inventory_data = cursor.fetchall()
  cursor.close()
  connection.close()
  return jsonify(inventory_data)
 

 if __name__ == '__main__':
  app.run(debug=True)
 ```
 

 The problem is that sometimes the inventory data doesn't display correctly, especially when multiple requests come in at once. Maybe it's a race condition or something? Also, I want to add logging to monitor execution times and catch any exceptions, but I'm not sure how to implement that.
 

 Could you refactor this code to handle these issues? Also, if possible, can you make it support bulk queries so we can process multiple items in one request?"