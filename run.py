from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Animal, Product, Customer, Order, OrderDetail

# Підключення до бази даних через зазначену конект-стрічку
DATABASE_URL = "mysql+pymysql://avnadmin:AVNS_hyEK_ZTRmq86zeLCAa4@mysql-32c408f5-ladbsbd.g.aivencloud.com:27163/Zooshop"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Функція для створення таблиць у БД
def create_database():
    Base.metadata.create_all(engine)
    print("База даних створена або оновлена.")

# Функція для виведення даних з усіх таблиць
def display_table_data():
    print("\nТварини:")
    animals = session.query(Animal).all()
    for animal in animals:
        print(f"ID: {animal.AnimalID}, Name: {animal.Name}, Type: {animal.Type}, Age: {animal.Age}, Price: {animal.Price}")

    print("\nПродукти:")
    products = session.query(Product).all()
    for product in products:
        print(f"ID: {product.ProductID}, Name: {product.Name}, Category: {product.Category}, Quantity: {product.Quantity}, Price: {product.Price}")

    print("\nКористувачі:")
    customers = session.query(Customer).all()
    for customer in customers:
        print(f"ID: {customer.CustomerID}, Name: {customer.Name}, Phone: {customer.Phone}, Email: {customer.Email}, City: {customer.City}")

    print("\nЗамовлення:")
    orders = session.query(Order).all()
    for order in orders:
        print(f"Order ID: {order.OrderID}, Customer ID: {order.CustomerID}, Order Date: {order.OrderDate}, Total Amount: {order.TotalAmount}")

    print("\nДеталі замовлень:")
    order_details = session.query(OrderDetail).all()
    for detail in order_details:
        print(f"OrderDetailID: {detail.OrderDetailID}, OrderID: {detail.OrderID}, ProductID: {detail.ProductID}, Quantity: {detail.Quantity}, Price: {detail.Price}")

# Функція для додавання нового продукту за фіксованими даними
def add_new_product():
    name = "Корм для собак"
    category = "Харчування"
    quantity = 50
    price = 25.99

    new_product = Product(Name=name, Category=category, Quantity=quantity, Price=price)
    session.add(new_product)
    session.commit()
    print(f"Продукт '{name}' додано.")
    display_table_data()

# Функція для видалення запису з таблиці OrderDetail за ID
def delete_order_detail():
    order_detail_id = 2  # Задайте ID деталі замовлення, яку потрібно видалити
    order_detail = session.query(OrderDetail).filter(OrderDetail.OrderDetailID == order_detail_id).first()
    if order_detail:
        session.delete(order_detail)
        session.commit()
        print(f"Деталь замовлення з ID {order_detail_id} видалено.")
        display_table_data()
    else:
        print(f"Деталь замовлення з ID {order_detail_id} не знайдено.")


# Функція для каскадного видалення тварини за ID
def delete_animal_cascade():
    animal_id = 3
    animal = session.query(Animal).filter(Animal.AnimalID == animal_id).first()
    if animal:
        session.delete(animal)
        session.commit()
        print(f"Тварину з ID {animal_id} видалено каскадно.")
        display_table_data()
    else:
        print(f"Тварину з ID {animal_id} не знайдено.")

# Функція для оновлення ціни продукту за фіксованими даними
def update_product_price():
    product_id = 1
    new_price = 19.99
    product = session.query(Product).filter(Product.ProductID == product_id).first()
    if product:
        product.Price = new_price
        session.commit()
        print(f"Ціна для продукту з ID {product_id} оновлена до {new_price} USD.")
        display_table_data()
    else:
        print(f"Продукт з ID {product_id} не знайдено.")

# Функція для роботи з меню
def menu():
    while True:
        print("\nМеню:")
        print("1. Вивести дані таблиць")
        print("2. Додати новий продукт")
        print("3. Видалити деталь замовлення")  # Змінено назву
        print("4. Каскадне видалення тварини")
        print("5. Оновити ціну продукту")
        print("0. Вихід")

        choice = input("Оберіть опцію: ")

        if choice == "1":
            display_table_data()
        elif choice == "2":
            add_new_product()
        elif choice == "3":
            delete_order_detail()  # Виклик нової функції
        elif choice == "4":
            delete_animal_cascade()
        elif choice == "5":
            update_product_price()
        elif choice == "0":
            print("Вихід з програми.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

# Основна частина програми
if __name__ == "__main__":
    create_database()
    menu()
