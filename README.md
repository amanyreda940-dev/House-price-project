🏠 House Price Prediction

📌 Project Overview

This project is an end-to-end Machine Learning application that predicts house prices based on different property features. The project includes data preprocessing, exploratory data analysis (EDA), model training, model evaluation, a FastAPI backend, and a React frontend for user interaction.

---

🚀 Features

- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Machine Learning Model Training
- Model Evaluation
- FastAPI REST API
- React Frontend
- House Price Prediction

---

🛠️ Technologies Used

Machine Learning

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib

Backend

- FastAPI
- Uvicorn

Frontend

- React
- TypeScript
- Vite

---

📂 Project Structure

House-Price-Prediction/
│
├── backend/
├── frontend/
├── notebooks/
├── models/
├── README.md
└── house_price.pkl

---

📊 Dataset

Dataset Name: House Price Dataset

Source:
https://www.kaggle.com/datasets/juhibhojani/house-price

---

⚙️ Installation

Clone Repository

git clone https://github.com/<amanyreda940>/<House-price-project>.git

Backend

cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload

Open:

http://127.0.0.1:8000

Swagger API:

http://127.0.0.1:8000/docs

---

Frontend

cd frontend
npm install
npm run dev

Open:

http://localhost:5173

---

📈 Machine Learning Workflow

1. Load Dataset
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Train Machine Learning Model
6. Evaluate Model
7. Save Trained Model
8. Deploy with FastAPI

---

📉 Model Evaluation

Metric| Value
MAE| 1,261,173.56
RMSE| 3,443,166.16
R² Score| 0.9113

Best Model: Random Forest Regressor

---

🌐 API Endpoints

GET /health

Returns the API status.

POST /predict

Predicts the house price based on the input features.

---

📷 Screenshots

Exploratory Data Analysis

![alt text](<screenshots/Screenshot 2026-08-05 011919.png>)
![alt text](<screenshots/Screenshot 2026-08-05 011949.png>)
![alt text](<screenshots/Screenshot 2026-08-05 012024.png>)
---

Model Evaluation

![alt text](<screenshots/Screenshot 2026-08-05 013909.png>)
![alt text](<screenshots/Screenshot 2026-08-05 012529.png>)
---

FastAPI Swagger

![alt text](<screenshots/Screenshot 2026-08-05 012805.png>)
---

Home Page

![alt text](<screenshots/Screenshot 2026-08-05 013237.png>)

---

Prediction Result

«ضع صورة نتيجة التنبؤ هنا.»

"Prediction" (screenshots/result.png)

---

📌 Future Improvements

- Improve model accuracy.
- Add more house features.
- Deploy the application online.
- Add user authentication.
- Connect the application to a database.

---

👩‍💻 Author

Amany Reda

Faculty of Computers and Information

---

🔗 GitHub Repository

Repository Link:
https://github.com/amanyreda940-dev/House-price-project
https://github.com/<amanyreda940>/<>

---

📄 License

This project was developed for educational purposes.