 from flask import Flask, jsonify
 import psycopg2
 

 app = Flask(__name__)
 

 @app.route('/data')
 def get_data():
  # Database connection details
  host = 'postgres.c58u848ggx5b.us-west-1.rds.amazonaws.com'
  username = 'readonly_user'
  port = '5432'
  password = 'your_password' # Dummy password
  database = 'pagila'
 

  # Connect to the PostgreSQL database
  try:
  conn = psycopg2.connect(
  host=host,
  port=port,
  user=username,
  password=password,
  database=database
  )
  cur = conn.cursor()
 

  # Execute a SELECT query
  cur.execute('SELECT * FROM actor LIMIT 10;')
  rows = cur.fetchall()
 

  # Close the cursor and connection
  cur.close()
  conn.close()
 

  return jsonify(rows)
  except Exception as e:
  return jsonify({'error': str(e)})
 

 if __name__ == '__main__':
  app.run()