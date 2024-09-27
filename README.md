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

2. Set up `node_modules`:
```
cd frontend/
npm install
```
```
cd routing/
npm install
```

3. Set up and activate Python virtual environment:
```
cd backend/
python3 -m venv venv
source venv/bin/activate
```
- If you want to get out of the Python virtual environment, simply run `deactivate`

4. Install all the necessary Python dependencies:
```
pip install -r requirements. txt
```

5. Setup `.env` file for environment variables and add username / password for PostgreSQL:
```
cd backend/database/
cp .env.dev .env
```

6. Set up the PostgreSQL database:
```
cd backend/database/
brew install postgresql@15
python3 create_db.py
```

### Running the servers locally

In `frontend/`:
```
npm run serve
```

In `routing/`:
```
node index.js
```

In `backend/rembg-service/`:
```
python remove-background.py
```
