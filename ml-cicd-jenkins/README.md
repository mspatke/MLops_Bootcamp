#setup virtual environment

```Python
conda create -n jenkins-env python=3.10 -y
conda activate jenkins env
pip install -r requirements.txt
pip install .
```

# Test the FASTAPI
```json
{
  "Gender": "Male",
  "Married": "No",
  "Dependents": "2",
  "Education": "Graduate",
  "Self_Employed": "No",
  "ApplicantIncome": 5849,
  "CoapplicantIncome": 0,
  "LoanAmount": 1000,
  "Loan_Amount_Term": 1,
  "Credit_History": "1.0",
  "Property_Area": "Rural"
}
```
