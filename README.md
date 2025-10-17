## Lawtech_project — Django App Suite

This directory contains the Django project and two apps: `compoundInterest` and `pythegoreanTriplet`.

Features:
- **Compound interest (annual)** visualization with a step-by-step layout
- Two **Pythagorean ratio templates**

### Requirements
- Python 3.11+
- pip

### Setup and Run (Windows PowerShell)
```bash
# From the repository root (one level up from this folder):
python -m venv .
./Scripts/Activate.ps1

pip install "Django==5.2.7"

# Apply migrations
python Lawtech_project/manage.py migrate

# Start the dev server
python Lawtech_project/manage.py runserver
```

Visit `http://127.0.0.1:8000/` and open the endpoints below.

### Endpoints
- `GET /calculate_interest_v1` — Example with P=8000, A=9856, years=3 (in `compoundInterest`)
- `GET /calculate_interest_v2` — Example with P=5000, A=6050, years=2 (in `compoundInterest`)
- `GET /calculate_pythegorean_template_v1` — Pythagorean layout (AC=17, AB=8, BC=15) (in `pythegoreanTriplet`)
- `GET /calculate_pythegorean_template_v2` — Pythagorean layout (AC=13, AB=5, BC=12) (in `pythegoreanTriplet`)

All routes are defined in `Lawtech_project/urls.py` and implemented in their respective apps' `views.py`.

### Templates and Static Files
- Compound interest UI: `compoundInterest/templates/interestcompounded.html`
- Compound interest images: `compoundInterest/static/compoundInterest/images/`
- Pythagorean template UI: `pythegoreanTriplet/templates/temp1.html`
- Pythagorean images: `pythegoreanTriplet/static/pythegoreanTriplet/images/`
- Static config: see `Lawtech_project/settings.py` (`STATIC_URL`, `STATICFILES_DIRS`).

With `DEBUG = True`, Django serves static files in development. For production, configure a static host and run `collectstatic`.

### Structure (key parts)
```
Lawtech_project/
├─ Lawtech_project/      # settings, urls, wsgi/asgi
├─ compoundInterest/     # app: views, templates, static, migrations
├─ pythegoreanTriplet/   # app: views, templates, static, migrations
└─ manage.py             # Django management
```

### Admin
```bash
python Lawtech_project/manage.py createsuperuser
# Admin UI: http://127.0.0.1:8000/admin/
```

### Notes
- `DEBUG = True` and a development `SECRET_KEY` are present; change for production.
- SQLite (`db.sqlite3`) is used by default.


