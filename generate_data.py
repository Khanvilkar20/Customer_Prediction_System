from faker import Faker
import random
import mysql.connector

fake = Faker()

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="customer_db"
)

cursor = conn.cursor()

for i in range(1000):

    age = random.randint(18, 60)

    gender = random.choice(["Male", "Female"])

    pages_viewed = random.randint(1, 20)

    time_spent = random.randint(1, 60)

    previous_purchases = random.randint(0, 10)

    product_category = random.choice([
        "Electronics",
        "Fashion",
        "Sports",
        "Books"
    ])

    # Logic for purchase
    if (
        pages_viewed > 10
        and time_spent > 20
        and previous_purchases > 2
    ):
        purchased = 1
    else:
        purchased = 0

    query = """
    INSERT INTO customer_activity
    (age, gender, pages_viewed,
     time_spent, previous_purchases,
     product_category, purchased)
    VALUES (%s,%s,%s,%s,%s,%s,%s)
    """

    values = (
        age,
        gender,
        pages_viewed,
        time_spent,
        previous_purchases,
        product_category,
        purchased
    )

    cursor.execute(query, values)

conn.commit()

print("1000 records inserted successfully!")

cursor.close()
conn.close()