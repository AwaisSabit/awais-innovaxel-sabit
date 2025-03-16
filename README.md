# 🌐 URL Shortener API

This project is a URL shortening service built using **Django** and **Django REST Framework (DRF)**. It allows users to create short URLs, retrieve the original URL, update, delete, and track access statistics.

---

## ✨ Features

- 🔗 Shorten a long URL
- 🔍 Retrieve the original URL
- ✏️ Update an existing short URL
- 🗑️ Delete a short URL
- 📊 Get access statistics for a short URL
- 🔄 Redirect short URL to the original URL

---

## 🗄️ Database Configuration

This project uses **PostgreSQL** as the database. Ensure you have PostgreSQL installed and configured before running migrations.

### Update `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
---

## 🛠️ Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/AwaisSabit/awais-innovaxel-sabit.git
   cd awais-innovaxel-sabit
   ```
2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```
4. **Set up PostgreSQL database:**

- Create a new PostgreSQL database.
- Update `DATABASES` settings in `settings.py`.
- Apply migrations

    ```python
    python manage.py migrate
    ```
5. **Run the development server:**

    ```python
    python manage.py runserver
    ```
---

## 📡 API Endpoints

1. **Shorten a URL ✂️**
Endpoint: ```POST /api/shortener/```

### Request Body:

```bash
{
  "original_url": "https://www.example.com"
}
```
### Response:

```bash
{
  "id": 1,
  "original_url": "https://www.example.com",
  "short_code": "abc123",
  "created_at": "2025-03-16T15:06:08.124472Z"
}
```
2. **Retrieve Original URL 🔍**

Endpoint: ```GET /api/shortener/{short_code}/```

### Response:

```bash
{
  "id": 1,
  "original_url": "https://www.example.com",
  "short_code": "abc123",
  "created_at": "2025-03-16T15:06:08.124472Z"
}
```

3. **Update Short URL ✏️**

Endpoint: ```PUT /api/shortener/{short_code}/```

### Request Body:

```bash
{
  "original_url": "https://www.updated-example.com"
}
```
### Response:

```bash
{
  "message": "Short URL updated successfully",
  "data": {
    "id": 1,
    "original_url": "https://www.updated-example.com",
    "short_code": "abc123",
    "created_at": "2025-03-16T15:06:08.124472Z",
    "updated_at": "2025-03-16T16:00:00.000000Z"
  }
}
```
4. **Delete Short URL 🗑️**

Endpoint: ```DELETE /api/shortener/{short_code}/```

Response: ```204 No Content```

5. **Get URL Statistics 📊**

Endpoint: ```GET /api/shortener/{short_code}/stats/```

### Response:

```bash
{
  "id": 1,
  "original_url": "https://www.example.com",
  "short_code": "abc123",
  "created_at": "2025-03-16T15:06:08.124472Z",
  "updated_at": "2025-03-16T16:00:00.000000Z",
  "access_count": 10
}
```
6. **Redirect Short URL 🔄**

Endpoint: ```GET /{short_code}/```

### Response:

Redirects to the original URL if the short code exists, otherwise returns a ```404 Not Found``` error.

---

## 🛠 Need Help or Have Any Issues?
If you encounter any issues, have questions, or need assistance, feel free to reach out.

📧 **Contact:** [awaissabit@gmail.com]
🔗 **GitHub Issues:** https://github.com/AwaisSabit/awais-innovaxel-sabit/issues
