# Book Finder
A search app written purely in Python 3.


## Features
- Search book by any keyword or combination of keywords.
- Support multiple search queries in one api call.
- Supports only 'complete term' search


## Installation
- clone this repository.
- create virtualenv
- Run `pip install -r requirements.pip`
- Run `cd src`
- Run `python app.py`.
- check at `http://localhost:5000/ping`


## Test
- `cd src`
- `py.test book_finder/tests`


## API Docs
<b>Base URL</b> - http://localhost:5000<br>
### API endpoints:
* `/search` - Search books.<br>
   - POST /search
   - Content-Type - application/json
   - body params -
       - queries - list of queries
       - k - number of result to fetch

   ```bash
   $ curl -X POST \
       http://localhost:5000/search \
       -H 'Content-Type: application/json' \
       -d '{"queries": ["take your book", "achieve book"], "k": 3}'
   ```
