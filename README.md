# Tech with Tanvir — Product & Order REST API

A Django REST Framework backend project for managing products and orders. Built with Python 3.13 and Django 6.0.

---

## 📁 Project Structure

```
backend_project/
├── api_app/
│   ├── models.py          # ProductModel, OrderModel, OrderItem
│   ├── serializers.py     # ProductSerializer, OrderSerializer, OrderItemSerializer
│   ├── views.py           # ViewSets for Products and Orders
│   ├── urls.py            # Router-based URL registration
│   ├── admin.py           # Django admin configuration
│   └── migrations/        # Database migrations
├── backend_project/
│   ├── settings.py        # Project settings
│   ├── urls.py            # Root URL configuration
│   ├── asgi.py
│   └── wsgi.py
├── product/               # Media upload folder (product images)
├── db.sqlite3             # SQLite database
└── manage.py
```

---

## 🧩 Data Models

### `ProductModel`
| Field         | Type              | Description                        |
|---------------|-------------------|------------------------------------|
| `id`          | AutoField (PK)    | Auto-generated primary key         |
| `name`        | CharField(100)    | Product name                       |
| `description` | TextField         | Product description                |
| `price`       | DecimalField      | Price (max 10 digits, 2 decimals)  |
| `stock`       | PositiveIntegerField | Available quantity              |
| `image`       | ImageField        | Optional product image             |
| `in_stock`    | property (bool)   | True if stock > 0                  |

### `OrderModel`
| Field        | Type              | Description                                |
|--------------|-------------------|--------------------------------------------|
| `order_id`   | UUIDField (PK)    | Auto-generated UUID primary key            |
| `user`       | ForeignKey(User)  | Linked Django auth user                    |
| `created_at` | DateTimeField     | Auto-set on creation                       |
| `status`     | CharField         | `pending` / `confirmed` / `cancelled`      |
| `products`   | ManyToManyField   | Products via `OrderItem` through model     |

### `OrderItem`
| Field      | Type                     | Description                         |
|------------|--------------------------|-------------------------------------|
| `order`    | ForeignKey(OrderModel)   | Related order                       |
| `product`  | ForeignKey(ProductModel) | Related product                     |
| `quantity` | PositiveIntegerField     | Quantity ordered                    |
| `item_subtotal` | property (Decimal)  | `price × quantity`                  |

---

## 🔌 API Endpoints

All endpoints are prefixed with `/api/`.

### Products — `/api/products/`

| Method   | URL                    | Description              |
|----------|------------------------|--------------------------|
| `GET`    | `/api/products/`       | List all products        |
| `POST`   | `/api/products/`       | Create a new product     |
| `GET`    | `/api/products/{id}/`  | Retrieve a product       |
| `PUT`    | `/api/products/{id}/`  | Full update a product    |
| `PATCH`  | `/api/products/{id}/`  | Partial update a product |
| `DELETE` | `/api/products/{id}/`  | Delete a product         |

### Orders — `/api/order/`

| Method   | URL                  | Description          |
|----------|----------------------|----------------------|
| `GET`    | `/api/order/`        | List all orders      |
| `POST`   | `/api/order/`        | Create a new order   |
| `GET`    | `/api/order/{uuid}/` | Retrieve an order    |
| `PUT`    | `/api/order/{uuid}/` | Full update an order |
| `PATCH`  | `/api/order/{uuid}/` | Partial update       |
| `DELETE` | `/api/order/{uuid}/` | Delete an order      |

### Admin Panel

| URL       | Description              |
|-----------|--------------------------|
| `/admin/` | Django admin interface   |

---

## ⚙️ Tech Stack

- **Python** 3.13
- **Django** 6.0.4
- **Django REST Framework** (DRF)
- **SQLite** (development database)
- **Pillow** (image upload support)

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd "Tech with Tanvir Project"
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv env
   # Windows
   env\Scripts\activate
   # macOS/Linux
   source env/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install django djangorestframework pillow
   ```

4. **Navigate to the backend project**
   ```bash
   cd backend_project
   ```

5. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser** (for admin access)
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

The API will be available at `http://127.0.0.1:8000/`.

---

## 📋 Example API Usage

### Create a Product
```http
POST /api/products/
Content-Type: application/json

{
  "name": "Wireless Headphones",
  "description": "Noise-cancelling over-ear headphones",
  "price": "49.99",
  "stock": 100
}
```

### List All Orders
```http
GET /api/order/
```

**Response includes:**
- Order UUID, user, status, created date
- Nested order items (product name, price, quantity, subtotal)
- Computed `total_price` for the whole order

---

## 🔒 Notes

- **DEBUG** is currently set to `True` — change to `False` before deploying to production.
- Replace the `SECRET_KEY` in `settings.py` with a secure, environment-variable-based key before production deployment.
- Media files (product images) are stored in the `product/` directory under `MEDIA_ROOT`.
- Authentication is not yet configured on API endpoints — consider adding `TokenAuthentication` or `SessionAuthentication` via DRF settings.

---


