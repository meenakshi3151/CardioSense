# CardioSense

**CardioSense** is a web application that predicts the risk of **heart disease** based on user-provided health parameters.  
It features an elegant **frontend built with HTML, CSS, and JavaScript**, and a **Flask-based backend** that hosts the prediction API.

---

## Features
- Predicts heart disease using a trained **Deep Learning model** (`heart_disease_model.joblib`).  
- Backend powered by **Flask API** for real-time prediction requests.  
- Interactive and user-friendly **frontend** built with HTML, CSS, and JavaScript.  
- Accepts multiple health and lifestyle parameters as input.  
- Provides instant, clear, and accurate prediction results in a simple web interface.  

---

## Features Used in Prediction

The model predicts heart disease based on the following health and lifestyle parameters:

- **Age** — The person’s age in years.  
- **Gender** — Biological sex of the individual (Male/Female).  
- **Diabetes** — Indicates whether the person has diabetes or not.  
- **Health-Insurance** — Availability of health insurance coverage.  
- **Blood-Rel-Stroke** — Family history of stroke among blood relatives.  
- **Vigorous-work** — Engagement in high-intensity physical activities.  
- **Annual-Family-Income** — Total yearly income of the family.  
- **Uric.Acid** — Level of uric acid in the blood (mg/dL).  
- **Blood-Rel-Diabetes** — Family history of diabetes among blood relatives.  
- **Glucose** — Blood glucose level (mg/dL), indicating sugar concentration.  
- **Creatinine** — Serum creatinine level reflecting kidney function.  
- **Total-Cholesterol** — Total cholesterol level in the blood (mg/dL).  
- **Glycohemoglobin** — HbA1c level representing long-term glucose control.  
- **Lymphocyte** — Percentage of lymphocytes in total white blood cells.  
- **Platelet-count** — Number of platelets in the blood (10⁹/L).  
- **Cholesterol** — LDL/HDL ratio or specific cholesterol measurement.  
- **Moderate-work** — Frequency of moderate-intensity physical activities.  
- **Red-Cell-Distribution-Width (RDW)** — Variation in size of red blood cells.  
- **X60-sec-pulse** — Pulse rate measured over 60 seconds (beats per minute).  
- **HDL** — High-Density Lipoprotein ("good cholesterol") level (mg/dL).  
- **Diastolic** — Diastolic blood pressure (mmHg), the lower value in BP readings.  
- **Systolic** — Systolic blood pressure (mmHg), the upper value in BP readings.  
- **Monocyte** — Percentage of monocytes in total white blood cells.  
- **Eosinophils** — Percentage of eosinophil cells, associated with immune response.  

> These parameters collectively help the model evaluate cardiovascular health and estimate the likelihood of heart disease.

---

## Technologies Used
### Frontend
- **HTML5**
- **CSS3**
- **JavaScript**

### Backend
- **Flask (Python Framework)**
- **Deep Learning Model (joblib)**
- **Machine Learning Libraries (scikit-learn, numpy, pandas)**

---

## Installation & Setup

### Backend Setup
```bash
# 1. Clone the repository
git clone https://github.com/meenakshi3151/Heartlytics.git
cd Heartlytics/backend

# 2. Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate     # On macOS/Linux
# venv\Scripts\activate      # On Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Flask backend
python app.py
```
The Flask server will start at http://127.0.0.1:5000 and expose the /predict API endpoint.

