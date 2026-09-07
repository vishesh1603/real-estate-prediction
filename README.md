# Real Estate Prediction Project

Two-part ML project based on the "AI-Based Prediction of Customer Purchase Intent and
Residential Plot Scheme Success" idea:

1. **Purchase Intent** - will a customer actually purchase a plot, based on their
   profile and early-funnel behaviour (site visit, previous enquiry etc). Classification.
2. **Price Prediction** - predict property price from listing features (area, location,
   amenities). Regression.
3. **Scheme Success** - given a proposed scheme's details (location, price, plot size,
   amenities, ad budget), predict a Scheme_Success_Score out of 100. Regression, with
   MinMaxScaler, PCA, GridSearchCV and ensemble models (Random Forest, Gradient Boosting,
   Voting Ensemble).

## Project structure

```
real-estate-project/
├── data/
│   ├── raw/
│   │   ├── real_estate_raw_messy.csv     customer survey data (synthetic, messy on purpose)
│   │   └── real_estate_master.csv        property listings (real, merged from 12 files)
│   ├── processed/                        created by running the notebooks
│   │   ├── cleaned_users.csv
│   │   └── cleaned_listings.csv
│   └── data_dictionary.md
├── notebooks/
│   ├── 01_data_cleaning.ipynb            cleans the customer data
│   ├── 02_purchase_intent_model.ipynb    classification models
│   ├── 03_listings_cleaning.ipynb        cleans the listings data
│   ├── 04_price_prediction_model.ipynb   regression models
│   └── 05_scheme_success_model.ipynb     scheme success score - PCA, GridSearchCV, ensembles
├── models/                               saved after running the notebooks
├── app/
│   └── app.py                            streamlit demo for both models
├── requirements.txt
└── README.md
```

## How to run

```bash
python -m venv venv
venv\Scripts\Activate.ps1      # windows
pip install -r requirements.txt
```

Run the notebooks in order (each one needs the output of the one before it):

```
01_data_cleaning.ipynb
02_purchase_intent_model.ipynb
03_listings_cleaning.ipynb
04_price_prediction_model.ipynb
```

Then the dashboard:

```bash
streamlit run app/app.py
```

## Algorithms used

Kept to what's actually covered in the syllabus (Logistic Regression, Decision Tree,
KNN, Naive Bayes, SVM, Random Forest for classification; Linear/Ridge/Lasso, Decision
Tree, Random Forest, Gradient Boosting for regression; PCA for dimensionality reduction;
GridSearchCV for hyperparameter tuning; VotingRegressor for ensembling) - no XGBoost or
anything not covered.

## Results

**Purchase intent (classification)** - best model: Random Forest, ~80% accuracy, AUC 0.85.
Logistic Regression and SVM were close behind. Site_Visit and Previous_Enquiry came out
as the strongest predictors.

**Price prediction (regression)** - best model: Random Forest, R² = 0.84. Linear models
did badly here (negative R²) since price doesn't scale linearly with the features -
area and city ended up being the main drivers.

**Scheme success (regression)** - best model: Tuned Gradient Boosting (via GridSearchCV),
R² = 0.756, MAE ≈ 7 points. A Voting Ensemble (RF + GB + Linear) came close (R² = 0.753)
but didn't beat the tuned GB alone. PCA was tested but didn't help (R² dropped slightly
with PCA vs without) - dataset only has ~19 columns after encoding, not enough redundant
dimensionality for PCA to pay off. Distance from metro and advertising budget were the
strongest real predictors (Expected_Leads/Bookings/Conversion/Demand_Level were excluded
as features since they're outputs of the same prediction, not real inputs).

Full metrics tables are in the notebooks themselves (section: "training models").

## Notes

- customer dataset is synthetic - generated for this project, does not represent real
  customers of any company
- listings dataset is real listing data merged from multiple city/property-type files
- Booking_Done / Purchase_Value / Purchase_Probability were deliberately excluded as
  features in the purchase intent model since they're only known after/alongside the
  purchase decision itself (would leak the answer)
