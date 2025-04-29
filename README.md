🛍️ Django Winkel
Django Winkel is a fully functional e-commerce and blog web application built with the Django framework. It supports product listings, category filtering, testimonials, blog posts, contact forms, and more. The project serves as a solid base for any online clothing store or content-driven fashion website.

🚀 Features
Product listing with pagination and filtering (by clothing and jeans)

Blog/news section with tag-based filtering and search

Product detail and news detail pages

About page with video support

Contact form with saving functionality

Testimonials section

Admin support via Django admin panel

Dynamic discount calculation for products

🧩 Models Overview
Products: Includes title, content, image, price, clothing/jeans/category relation, and optional discount

Clothing, Jeans, Category: Classifications for products

News: Blog/news posts with tags, likes, dislikes, views

Tag: Categorizes news items

Testimonial: Customer feedback

Contact: Contact form messages

Subscriber: Newsletter/email list

About: About page content

Setting: Site-wide metadata (logo, social links, etc.)

📄 Views Summary
home: Displays products and testimonials on the homepage

about: Shows company video and testimonials

contact: Handles the contact form (GET & POST)

products: Filters and paginates products based on clothing/jeans

news: Displays news list with search and tag filters

product_single, news_single: Show detail pages for products and news

search: Redirects based on search query (to news or product list)

⚙️ Setup Instructions
1. Clone the repository
bash
Copy
Edit
git clone https://github.com/nihattadilov/django_winkel/
cd django_winkel
2. Create a virtual environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Apply migrations
bash
Copy
Edit
python manage.py migrate
5. Create a superuser
bash
Copy
Edit
python manage.py createsuperuser
6. Run the development server
bash
Copy
Edit
python manage.py runserver
