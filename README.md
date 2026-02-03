# Chemical Visualizer

A small project for visualizing chemical/equipment and sensor data.

Structure
- backend/ → Django REST API (includes `api/`, `models.py`, `views.py`, `serializers.py`, `urls.py`)
- web-frontend/ → React + Chart.js
- desktop-app/ → PyQt5 + Matplotlib
- `sample_sensor_data.csv` → example sensor dataset used by the upload API

Getting started (quick):

Backend
1. Create and activate a virtual environment.
2. Install dependencies:
   ```bash
   pip install django djangorestframework pandas reportlab django-cors-headers djangorestframework-authtoken
   ```
3. Run migrations and create a default test user+token:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python create_default_user.py
   ```
   The script prints a token for user `test` with password `testpass`.
4. Run the server:
   ```bash
   python manage.py runserver
   ```

Frontend
1. Copy the `web-frontend/src` files into a React app (or create a new CRA app) and install:
   ```bash
   npm install axios chart.js react-chartjs-2
   ```
2. Start with `npm start`.

Desktop
1. Install dependencies and run the app:
   ```bash
   pip install pyqt5 matplotlib requests
   python desktop-app/app.py
   ```

Authentication
- The API uses token authentication. Obtain a token by POSTing `{'username': 'test', 'password': 'testpass'}` to `/api/login/`.
- Include the header `Authorization: Token <token>` in requests to protected endpoints (upload, history, report).

Sample data
- `sample_sensor_data.csv` contains `Flowrate,Pressure,Temperature,Type` and can be used to test the upload endpoint.

Notes
- Replace `SECRET_KEY` in `backend/visualizer/settings.py` for production.
- Feel free to ask me to add social logins, registration flow, or a prettier React UI.
