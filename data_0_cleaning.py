
## CLEANING Python code for the two data sets. ##

import pandas as pd 

def clean_datasets(loan_df, credit_df):
    """
    Cleaning loan and credit card datasets.
    Returns the cleaned loan_df and credit_df.
    """

    # Clean column names
    loan_df.columns = loan_df.columns.str.lower().str.strip().str.replace(" ", "_")
    credit_df.columns = (
        credit_df.columns
        .str.lower()
        .str.strip()
        .str.replace(" ", "_")
        .str.replace(".", "_")
    )

    # Rename columns
    loan_df = loan_df.rename(columns={
        "loanid": "customer_id"
    })

    credit_df = credit_df.rename(columns={
        "id": "customer_id",
        "default_payment_next_month": "default"
    })

    # Add product type to compare later in the dashboard
    loan_df["product_type"] = "Loan"
    credit_df["product_type"] = "Credit Card"

    # Remove duplicates
    loan_df = loan_df.drop_duplicates()
    credit_df = credit_df.drop_duplicates()

    # Reset index
    loan_df = loan_df.reset_index(drop=True)
    credit_df = credit_df.reset_index(drop=True)

    return loan_df, credit_df









