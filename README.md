# Credit Risk Prediction Across Two Financial Products

## Project Overview

This project develops supervised machine learning classification models to predict default risk across two financial products: **credit card clients** and **loan borrowers**.

The goal is not only to build predictive models, but also to transform the model outputs into business-oriented dashboards that can support credit risk monitoring, early risk detection, and decision-making.

The final outputs include:

- Machine learning models for default prediction
- Model evaluation and comparison
- Feature importance analysis
- Tableau dashboards for credit risk monitoring
- Final presentation explaining the business problem, methodology, results, and recommendations

## Presentation

Final project presentation:

[Canva Presentation](https://www.canva.com/design/DAHK86OCqkI/dJ98k_MQPSwQgu6nH3y-3Q/edit?ui=eyJBIjp7fX0)

## Tableau Public Dashboards

Add the Tableau Public links here after publishing the dashboards:

- Credit Card Default Dashboard: [`ADD TABLEAU PUBLIC LINK HERE`](https://public.tableau.com/views/Final_project_2_17799170177340/Story1?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

- Loan Default Risk Dashboard:[`ADD TABLEAU PUBLIC LINK HERE`] (https://public.tableau.com/views/Final_porject_loan/Story1?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

## Business Problem

Financial institutions need to identify clients with a higher probability of default before the default occurs. Traditional credit risk analysis can be improved by using machine learning models that estimate default probability and classify clients into risk segments.

This project answers the following business question:

> Can machine learning help identify high-risk clients across different financial products and support better credit risk monitoring?

## Datasets

This project uses two public datasets from Kaggle.

### 1. Loan Default Dataset

Source: [Loan Default Dataset - Kaggle](https://www.kaggle.com/datasets/nikhil1e9/loan-default)

Main variables include:

- Age
- Income
- Loan amount
- Credit score
- Interest rate
- Loan term
- Debt-to-income ratio
- Employment type
- Loan purpose
- Mortgage status
- Dependents
- Cosigner
- Default status

### 2. Credit Card Default Dataset

Source: [Default of Credit Card Clients Dataset - Kaggle](https://www.kaggle.com/datasets/uciml/default-of-credit-card-clients-dataset)

Main variables include:

- Credit limit
- Gender
- Education
- Marital status
- Age
- Repayment status
- Bill amounts
- Payment amounts
- Default payment next month

## Machine Learning Approach

Both datasets were treated as **supervised classification problems** because the target variable is binary:

- `0` = No default
- `1` = Default

The models were trained to predict:

- Whether a client will default
- The probability of default
- The risk segment of each client

## Methodology

The project followed these steps:

1. Data cleaning and preprocessing
2. Exploratory data analysis
3. Feature engineering
4. Train-test split
5. Model training and comparison
6. Hyperparameter tuning
7. Model evaluation
8. Feature importance analysis
9. Dashboard preparation
10. Business interpretation

## Final Model

The final model used for the dashboards was a **Random Forest Classifier** with hyperparameter tuning using `RandomizedSearchCV`.

The model was optimized using the **F1-score**, which balances precision and recall. This is useful for default prediction because the goal is to detect risky clients while controlling false positives.

## Evaluation Metrics

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC
- Confusion matrix

For credit risk, recall and F1-score are especially important because failing to identify default clients can be costly for a financial institution.

## Dashboard Outputs

The prediction datasets include the following model output variables:

- `actual_default`
- `predicted_default`
- `default_probability`
- `risk_segment`

These outputs were used to build Tableau dashboards.

### Credit Card Default Dashboard

Main dashboard components:

- Total clients
- Actual default rate
- Predicted default rate
- Average default probability
- High-risk clients
- Clients by risk segment
- Actual default rate by risk segment
- Confusion matrix
- Feature importance

### Loan Default Risk Dashboard

Main dashboard components:

- Total loan clients
- Actual default rate
- Predicted default rate
- Average default probability
- High-risk clients
- Risk segment distribution
- Actual default rate by risk segment
- Default probability by income group
- Actual default vs predicted probability by interest rate group
- Actual default rate by age group
- Feature importance

## Key Insights

### Credit Card Default

Payment history variables were among the most important predictors of default risk. The most recent repayment status was especially relevant for the Random Forest model.

### Loan Default

Loan default risk was associated with borrower profile and financial variables such as income, credit score, interest rate, loan amount, debt-to-income ratio, and employment-related information.

### Business Interpretation

The dashboards show that machine learning predictions can be translated into practical business tools. Instead of only reporting model metrics, the dashboards help identify which clients or groups require closer monitoring.

## Business Recommendations

The model should be used as a decision-support tool for credit risk monitoring. Recommended actions include:

- Monitor high-risk clients more closely
- Apply additional affordability checks
- Prioritize early repayment reminders
- Offer personalized repayment support
- Use risk segments to support portfolio-level analysis

The model should not be used as the only basis for automatic rejection decisions.

## Project Structure

```text
project-folder/
│
├── Data/
│   ├── loan_default.csv
│   └── UCI_Credit_Card.csv
│
├── Results/
│   ├── credit_dashboard_predictions.csv
│   ├── loan_dashboard_predictions.csv
│   ├── model_comparison_credit.csv
│   └── model_comparison_loan.csv
│
├── data_0_cleaning.py
├── data_1_EDA_Credit_Card.py
├── data_2_EDA_Loan.py
│
└── README.md
```

## Tools and Libraries

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Tableau
- Canva

## Conclusion

This project shows how supervised classification models can support credit risk prediction across two financial products. By combining machine learning with Tableau dashboards, the project translates technical model outputs into business insights that can help financial institutions monitor risk and prioritize clients for preventive actions.
