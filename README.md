# outfit_organizer

Solve your "I don't have anything to wear" problems and overconsumption with Outfit Organizer, a web application that lets you quickly create your desired outfit with the clothes and accessories already available in your closet

## Project setup

Tech stack:

- Vue.js (frontend)
- Express.js (routing)
- Python Flask (backend)
- PostgreSQL (database)

### Environment setup

1. Clone this repo and navigate to `outfit_organizer`:
```
cd outfit_organizer/
```

2. Set up `node_modules` in the `frontend/` and `backend/` directories:
```
cd frontend/
npm install
```
```
cd backend/
npm install
```

3. Set up and activate Python virtual environment in `/rembg-service`:
```
cd /rembg-service
python -m venv venv
source venv/bin/activate
```
- If you want to get out of the Python virtual environment, simply run `deactivate`

4. Install all the Python dependencies:
```
pip install -r requirements. txt
```

### Running the servers locally

In `frontend/`:
```
npm run serve
```

In `backend/`:
```
node index.js
```

In `rembg-service/`:
```
python remove-background.py
```
