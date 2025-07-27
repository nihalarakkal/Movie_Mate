**🎬 MovieMate (Backend)**
This is the backend API for the MovieMate project, built using Django and Django REST Framework. It handles user data, movie/show tracking, and recommendation logic.

**✅ Features**
Add movies/TV shows (title, director, genre, platform)

Track status (watching, completed, wishlist)

TV show progress tracking (episodes watched)

Rate and review content

Recommendation-ready model

Admin panel for data management

Created/updated timestamps

**⚙️ Setup Instructions**
**Clone the repo**
git clone https://github.com/your-username/moviemate-backend.git
cd moviemate-backend
Create a virtual environment
python -m venv env
env\Scripts\activate  # Windows
source env/bin/activate  # macOS/Linux
**Install dependencies**
pip install -r requirements.txt
**Run migrations**
python manage.py makemigrations
python manage.py migrate
**Create a superuser**

python manage.py createsuperuser
**Run the server**
python manage.py runserver
API is available at: http://localhost:8000/api/
