# Simple URL Shortener in Python (with Flask)

## Usage

### Installation

Tested on Python 3.10

```
pip3 install -r requirements.txt
```

### Configuration

Copy the given example .env.example file into .env and set your SQL Database URL (any DB supported by SQLAlchemy should work)

### Running

Run with e.g. Gunicorn via
```
gunicorn "main:app"
```

### Handling DB migrations
Run "flask db init" if using a fresh database.

To migrate run "flask db migrate" and "flask db upgrade"

### Available endpoints

* / -> Handles a POST request, with application/json body and a "url" param (which must begin with 'http://' or 'https://'), e.g.:

```
{
    "url": "https://google.com"
}
```
Returns 400 if the request body is malformed.

* /<shortened> -> Redirects to full URL corresponding to given shortened URL, if no full URL is found returns 404.