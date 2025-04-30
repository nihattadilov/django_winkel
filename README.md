🛍️ Django Winkel
Django Winkel is a multilingual (🇺🇸 English, 🇦🇿 Azerbaijani, 🇹🇷 Turkish) full-featured e-commerce and blog web application built with Django. It is designed for online clothing stores and content-focused fashion platforms.

🚀 Features
✅ Product listing with pagination & filtering (by clothing and jeans)

📰 Blog/news section with tag-based filtering and search

🔍 Search function redirects to related product or news

📦 Product and news detail pages

🧾 About page with video support

📬 Contact form (saved to DB)

🗣️ Customer testimonials

🛠️ Admin support via Django Admin Panel

📉 Dynamic discount price calculation

🌍 Multilingual support: English, Azerbaijani, Turkish

👤 User features:

Registration with password confirmation

Login and logout support

Form validations and error handling

🧩 Models Overview
Products: Title, description, price, image, clothing/jeans/category relation, discount

Clothing / Jeans / Category: Product classifications

News: Blog posts with tag, like, dislike, view count

Tag: Tags for news filtering

Testimonial: Customer feedback

Contact: Contact form submissions

Subscriber: Newsletter subscriptions

About: About page content

Setting: Global metadata (social links, logo, etc.)

📄 Views Summary

View Name	Description
home	Homepage with products & testimonials
about	About page with video and testimonials
contact	GET/POST contact form with save to DB
products	Product list, filtered and paginated
news	News/blog with search and tag filtering
product_single	Product detail page
news_single	News detail page
search	Redirects to news/products based on search input
register	User registration with password match check
login	User authentication/login
logout_view	Logs out user and redirects to home



⚙️ Setup Instructions


Clone the repository

git clone https://github.com/nihattadilov/django_winkel/
cd django_winkel


Create a virtual environment

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate


Install dependencies

pip install -r requirements.txt


Apply migrations

python manage.py migrate
Create a superuser


python manage.py createsuperuser
Run the development server


python manage.py runserver
