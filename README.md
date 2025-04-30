
# 🛍️ Django Winkel

**Django Winkel** is a multilingual (🇺🇸 English, 🇦🇿 Azerbaijani, 🇹🇷 Turkish) full-featured **e-commerce** and **blog** web application built with Django. It is designed for online clothing stores and content-focused fashion platforms.

---

## 🚀 Features

### 🛒 E-Commerce
- ✅ Product listing with pagination & filtering (clothing, jeans)
- 📦 Product detail pages
- 📉 Dynamic discount price calculation
- 👤 User registration, login, logout
- ✅ Form validations and error handling
- 🗣️ Customer testimonials

### 📰 Blog
- 📰 News/blog section with tag-based filtering and search
- 🔍 Smart search that redirects to related product or blog post
- 📄 News detail pages

### 🌐 General
- 🧾 About page with embedded video
- 📬 Contact form (saved to database)
- 🛠️ Admin support via Django Admin Panel
- 🌍 Multilingual support: English, Azerbaijani, Turkish

---

## 🧩 Data Models

- **Product**: title, description, price, image, category, discount
- **Clothing / Jeans / Category**: product classifications
- **News**: title, content, tag, like/dislike, view count
- **Tag**: associated with news articles
- **Testimonial**: customer feedback
- **Contact**: contact form submissions
- **Subscriber**: newsletter emails
- **About**: about page content
- **Setting**: global site data (logo, social links, etc.)

---

## 🧭 Views Summary

| View Name      | Description                                                |
|----------------|------------------------------------------------------------|
| `home`         | Homepage with products and testimonials                    |
| `about`        | About page with video and testimonials                     |
| `contact`      | Contact form (GET/POST) saved to database                  |
| `products`     | Product list with pagination and filtering                 |
| `news`         | News/blog list with tag filtering and search               |
| `product_single` | Detailed product page                                   |
| `news_single`  | Detailed news/blog page                                    |
| `search`       | Redirect to product/news based on input                    |
| `register`     | User registration with password confirmation               |
| `login`        | User authentication                                        |
| `logout_view`  | Logs out user and redirects to homepage                    |

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/nihattadilov/django_winkel.git
cd django_winkel
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply Migrations
```bash
python manage.py migrate
```

### 5. Create a Superuser
```bash
python manage.py createsuperuser
```

### 6. Run the Development Server
```bash
python manage.py runserver
```


