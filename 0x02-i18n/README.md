0x02. Internationalization (i18n)
Project Overview
This project implements internationalization (i18n) in a Flask web application, enabling support for multiple languages and timezones. The application uses Flask-Babel for translation and localization, allowing dynamic language selection based on URL parameters, user settings, or request headers. It also supports timezone-aware timestamp display and mock user login functionality.

Project Start: May 20, 2025, 6:00 AM
Project End: May 21, 2025, 6:00 AM
Environment: Ubuntu 18.04 LTS, Python 3.7
Repository: alx-backend
Directory: 0x02-i18n

Learning Objectives

Parametrize Flask templates to display content in different languages.
Infer the correct locale based on URL parameters, user settings, or request headers.
Localize timestamps using user-preferred or URL-specified timezones.
Implement mock user login with locale and timezone preferences.

Requirements

All files are interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
Files end with a new line.
Code adheres to pycodestyle (version 2.5).
First line of Python files: #!/usr/bin/env python3.
All Python files are executable.
Modules, classes, and functions have proper documentation.
Functions and coroutines are type-annotated.

Setup Instructions

Install Dependencies:
pip3 install flask flask_babel==2.0.0


Initialize Translations:
pybabel extract -F babel.cfg -o messages.pot .
pybabel init -i messages.pot -d translations -l en
pybabel init -i messages.pot -d translations -l fr


Edit Translation Files:Update translations/en/LC_MESSAGES/messages.po and translations/fr/LC_MESSAGES/messages.po with the translations provided in the project tasks.

Compile Translations:
pybabel compile -d translations


Run the Application:
python3 app.py

Access the app at http://127.0.0.1:5000.


File Structure

0-app.py, templates/0-index.html: Basic Flask app with a simple route and template.
1-app.py, templates/1-index.html: Flask app with Babel setup for language support.
2-app.py, templates/2-index.html: Locale selection based on request headers.
3-app.py, templates/3-index.html, babel.cfg, translations/[en|fr]/LC_MESSAGES/messages.[po|mo]: Template parameterization with translations.
4-app.py, templates/4-index.html: Force locale via URL parameter (locale=fr).
5-app.py, templates/5-index.html: Mock user login with user-specific messages.
6-app.py, templates/6-index.html: Prioritize user-preferred locale.
7-app.py, templates/7-index.html: Timezone selection with validation.
app.py, templates/index.html: Display current time in the user's timezone.
README.md: This file.

Tasks

Basic Flask App: Set up a Flask app with a / route rendering "Welcome to ALX" as the title and "Hello world!" as the header.
Basic Babel Setup: Integrate Flask-Babel with supported languages (en, fr) and default settings (locale: en, timezone: UTC).
Get Locale from Request: Implement locale selection using request headers.
Parametrize Templates: Use gettext for translations and set up translation files for English and French.
Force Locale with URL Parameter: Allow locale override via ?locale=[fr|en] in the URL.
Mock Logging In: Implement a mock user table and display login status messages.
Use User Locale: Prioritize user-preferred locale if supported.
Infer Appropriate Timezone: Select timezone from URL parameters or user settings, with validation using pytz.
Display Current Time: Show the current time in the user's timezone, formatted according to the locale.

Testing

Test language switching: http://127.0.0.1:5000/?locale=fr or http://127.0.0.1:5000/?locale=en.
Test user login: http://127.0.0.1:5000/?login_as=1 (e.g., user Balou with French locale).
Test timezone: http://127.0.0.1:5000/?timezone=Europe/Paris.
Verify translations and timezone-aware timestamps in the browser.

Notes

Ensure the Vulcan timezone falls back to UTC due to validation.
Request a manual QA review upon project completion.
Push all files to the alx-backend repository in the 0x02-i18n directory.

