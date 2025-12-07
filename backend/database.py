import mysql.connector
HOST = "localhost"
USER = "root"
PASSWORD = ""  
DB_NAME = "taxi_services"
connection = mysql.connector.connect(
    host=HOST,
    user=USER,
    password=PASSWORD
)

cursor = connection.cursor()
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
print(f"✔ Database '{DB_NAME}' ready")
cursor.execute(f"USE {DB_NAME}")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        email VARCHAR(100) UNIQUE NOT NULL,
        phone VARCHAR(20) UNIQUE NOT NULL,
        password VARCHAR(100) NOT NULL,
        role VARCHAR(20) DEFAULT 'user',
        is_driver TINYINT(1) DEFAULT 0
    )
""")
print("✔ Table 'users' ready")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS driver_profiles (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT NOT NULL,
        vehicle_model VARCHAR(50),
        vehicle_number VARCHAR(20),
        license_number VARCHAR(30),
        status VARCHAR(20) DEFAULT 'pending',
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
""")
print("✔ Table 'driver_profiles' ready")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS beverages (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        price DECIMAL(10,2) NOT NULL,
        stock INT DEFAULT 0
    )
""")
print("✔ Table 'beverages' ready")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS rides (
        id INT AUTO_INCREMENT PRIMARY KEY,
        passenger_id INT NOT NULL,
        driver_id INT,
        pickup VARCHAR(255) NOT NULL,
        drop_location VARCHAR(255) NOT NULL,
        vehicle_type VARCHAR(20),
        beverage_id INT,
        total_amount DECIMAL(10,2),
        status VARCHAR(20) DEFAULT 'pending',
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (passenger_id) REFERENCES users(id),
        FOREIGN KEY (driver_id) REFERENCES users(id),
        FOREIGN KEY (beverage_id) REFERENCES beverages(id)
    )
""")
print("✔ Table 'rides' ready")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS payments (
        id INT AUTO_INCREMENT PRIMARY KEY,
        ride_id INT NOT NULL,
        amount DECIMAL(10,2) NOT NULL,
        method VARCHAR(20),
        paid_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (ride_id) REFERENCES rides(id)
    )
""")
print("✔ Table 'payments' ready")

connection.commit()
cursor.close()
connection.close()
print("\n🎉 All tables created successfully! Backend database setup complete.")