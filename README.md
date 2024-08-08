
# Customer Churn Prediction App

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Data](#data)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Modeling](#modeling)
- [Pipeline Persistence](#pipeline-persistence)
- [Model Evaluation](#model-evaluation)
- [Git Workflow](#git-workflow)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Project Overview

The Customer Churn Prediction App is designed to predict whether a customer will churn based on various features. The project leverages machine learning models to analyze customer data and provides a robust solution for businesses to anticipate customer behavior, allowing for proactive retention strategies.

This repository includes all the necessary scripts, models, and documentation to understand, run, and extend the churn prediction pipeline.

## Features

- **Data Preprocessing Pipeline:** Handles missing data, feature scaling, encoding, and more.
- **Multiple Machine Learning Models:** Includes RandomForest, XGBoost, and LightGBM models.
- **Pipeline Persistence:** Save and load pipelines with models for easy deployment.
- **AUC Evaluation:** All models are evaluated using the AUC metric to ensure performance is consistent and measurable.
- **Integration with Git:** Properly configured to handle large model files using Git LFS.

## Data

The dataset used in this project contains the following features:

- `user_id`: Unique identifier for each customer (dropped during preprocessing)
- `REGION`: Categorical feature representing customer's region
- `TENURE`: Numeric feature representing the length of time the customer has been with the service
- `MONTANT`: Numeric feature representing the monetary amount spent by the customer
- `FREQUENCE_RECH`: Numeric feature representing the frequency of recharges
- `REVENUE`: Numeric feature representing the revenue generated by the customer
- `ARPU_SEGMENT`: Numeric feature related to the customer's average revenue per user
- `FREQUENCE`: Numeric feature representing general frequency of interaction
- `DATA_VOLUME`: Numeric feature representing the data usage volume
- `ON_NET`, `ORANGE`, `TIGO`, `ZONE1`, `ZONE2`: Categorical features related to network usage
- `MRG`: Categorical feature representing margin
- `REGULARITY`: Categorical feature representing customer regularity, segmented into `low` and `high`
- `TOP_PACK`: Categorical feature representing the top package used by the customer
- `FREQ_TOP_PACK`: Numeric feature related to frequency of top package usage
- `CHURN`: Target variable, indicating whether the customer has churned (1) or not (0)

## Installation

### Prerequisites

Ensure you have the following installed:

- Python 3.8+
- Git
- Virtualenv (optional but recommended)

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/parockson/customer-churn-prediction-app.git
   cd customer-churn-prediction-app
   ```

2. **Create and Activate a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Download Pre-trained Models**

   Run the `download_models.py` script to fetch pre-trained models from Google Drive:

   ```bash
   python download_models.py
   ```

## Usage

### Running the App

The application will be run locally using streamlit:

```bash
streamlit run app.py
```

This will start the Streamlit server, and you can interact with the customer churn prediction models through a web interface.

### Predicting Churn

To make predictions, use the provided interface to input customer data, and the app will display the probability of churn using the best-performing model.

### Customization

You can modify the preprocessing steps, try different models, or integrate the pipeline into other applications by editing the respective Python scripts.

## Project Structure

```
customer-churn-prediction-app/
│
├── best_models/               # Directory containing persisted pipelines
├── datasets/                      # Directory for storing raw and processed data
├── modelling/                 # Jupyter notebooks and scripts for data exploration and model training
├── app.py                     # Main application file
├── download_models.py         # Script to download pre-trained models from Google Drive
├── README.md                  # Project documentation
├── requirements.txt           # Python dependencies
└── .gitattributes             # Git LFS tracking for large files
```

## Modeling

The project includes several machine learning models, with a focus on handling class imbalance, high variability, and skewed distributions. The following models are implemented:

- **RandomForestClassifier**
- **XGBClassifier**
- **LGBMClassifier**

Each model is trained with a preprocessing pipeline that handles missing data, encodes categorical variables, and scales numerical features. The best-performing model is selected based on the AUC score.

## Pipeline Persistence

The preprocessing pipelines and trained models are saved using `joblib`. This ensures that the exact preprocessing steps and model parameters can be reused or deployed without retraining.

The saved pipelines are located in the `best_models/` directory, but large files are tracked using Git LFS and not included in the repository.

## Model Evaluation

All models are evaluated using the AUC (Area Under the ROC Curve) metric. The AUC score provides a robust measure of model performance, especially in scenarios with class imbalance.

## Git Workflow

### Branches

- **`main`**: The production-ready branch containing the stable version of the app.
- **`modelling`**: Branch used for model development and data exploration.

### Handling Large Files

Large files, such as model artifacts, are managed using Git LFS. Ensure you have Git LFS installed and configured before working with the repository.

### Common Commands

- **Commit and Push Changes**

  ```bash
  git add .
  git commit -m "Your commit message"
  git push origin branch_name
  ```

- **Deleting a Branch**

  ```bash
  git branch -d branch_name
  git push origin --delete branch_name
  ```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Write clear, concise commit messages.
4. Push your changes and open a pull request.
5. Ensure all code passes linting and tests before submitting.

or contact me on [LinkedIn](linkedin.com/in/prince-acquah-rockson) 
                 [email](parockson@gmail.com)
                 [whatsapp](wa.me//233348065337)
                 [phone](+233248065337)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments

-Thanks to [Azubi Africa (GetInnotized GmBH)](https://azubiafrica.org) for support and resources.

- Special thanks to contributors and the open-source community for their invaluable tools and libraries.
