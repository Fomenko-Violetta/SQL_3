from sqlalchemy import Column, DECIMAL, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Модель для таблиці Animals
class Animal(Base):
    __tablename__ = 'Animals'

    AnimalID = Column(Integer, primary_key=True)
    Name = Column(String(50), nullable=False)
    Type = Column(String(50), nullable=False)
    Age = Column(Integer, nullable=False)
    Price = Column(DECIMAL(10, 2), nullable=False)


# Модель для таблиці Products
class Product(Base):
    __tablename__ = 'Products'

    ProductID = Column(Integer, primary_key=True)
    Name = Column(String(50), nullable=False)
    Category = Column(String(50), nullable=False)
    Quantity = Column(Integer, nullable=False)
    Price = Column(DECIMAL(10, 2), nullable=False)


# Модель для таблиці Customers
class Customer(Base):
    __tablename__ = 'Customers'

    CustomerID = Column(Integer, primary_key=True)
    Name = Column(String(50), nullable=False)
    Phone = Column(String(20), nullable=False)
    Email = Column(String(50))
    City = Column(String(50), nullable=False)


# Модель для таблиці Orders
class Order(Base):
    __tablename__ = 'Orders'

    OrderID = Column(Integer, primary_key=True)
    CustomerID = Column(ForeignKey('Customers.CustomerID'), index=True, nullable=False)
    OrderDate = Column(Date, nullable=False)
    TotalAmount = Column(DECIMAL(10, 2), nullable=False)

    Customer = relationship('Customer')


# Модель для таблиці OrderDetails
class OrderDetail(Base):
    __tablename__ = 'OrderDetails'

    OrderDetailID = Column(Integer, primary_key=True)
    OrderID = Column(ForeignKey('Orders.OrderID'), index=True, nullable=False)
    ProductID = Column(ForeignKey('Products.ProductID'), index=True, nullable=False)
    Quantity = Column(Integer, nullable=False)
    Price = Column(DECIMAL(10, 2), nullable=False)

    Order = relationship('Order')
    Product = relationship('Product')
