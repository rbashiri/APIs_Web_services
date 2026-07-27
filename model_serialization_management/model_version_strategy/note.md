### Model Versioning — Key Highlights

Model versioning means saving each trained model as a separate file instead of overwriting the previous model.

**Train new model → Evaluate → Save as a new version → Deploy** 

*Example:*

customer_model_v1.joblib  # January data, 85% accuracy
customer_model_v2.joblib  # More data, 91% accuracy
customer_model_v3.joblib  # New features, 93% accuracy

Why versioning matters:

Keeps previous models available.
Allows you to compare different models.
Helps reproduce earlier results.
Lets you quickly return to a reliable model if the new model has problems. This is called a rollback.
Shows which model was used at a particular time.
Prevents accidentally overwriting a working model.

**Practical rule: never repeatedly save every model as my_model.joblib**

#### Version Numbers in Model Filenames

Save every model with `a different version number instead of` overwriting the existing model.

`import joblib`

`joblib.dump(model, "customer_churn_model_v1.joblib")`

After retraining:

joblib.dump(new_model, "customer_churn_model_v2.joblib")

Example:

customer_churn_model_v1.joblib
customer_churn_model_v2.joblib
customer_churn_model_v3.joblib

This simple approach lets you:

Keep previous models.
Compare different versions.
Identify which model was deployed.
Return to an older working model if the new one has a problem.

Practical rule: increase the version number whenever you retrain the model, change its features, adjust important parameters, or use new data.
=================================================================

### Semantic Versioning for ML Models

Semantic versioning uses:

MAJOR.MINOR.PATCH

Example: 2.1.3

MAJOR — Breaking change. The new model requires changes to the application or input data.
Example: adding or removing input features
1.5.3 → 2.0.0
MINOR — Model improvement without changing the required input format.
Example: retraining with more data or improving accuracy
1.0.0 → 1.1.0
PATCH — Small correction that does not significantly change the model.
Example: fixing a minor preprocessing bug
1.1.0 → 1.1.1

Example filenames:

customer_model_1.0.0.joblib  # Initial model
customer_model_1.1.0.joblib  # Retrained with more data
customer_model_1.1.1.joblib  # Small preprocessing fix
customer_model_2.0.0.joblib  # Input features changed

Practical rule:

Input requirements changed → MAJOR
Model improved, same inputs → MINOR
Small fix → PATCH

====================================================================

### Complete Model Versioning Workflow — Practical Summary

Save every trained model as a new version and create a metadata file explaining what changed.

Train → Evaluate → Assign version → Save model
→ Save metadata → Test → Deploy → Keep old version for rollback
import joblib
import json

version = "1.1.0"

# Save the trained model
joblib.dump(model, f"ad_click_model_v{version}.joblib")

# Save information about the model
metadata = {
    "version": version,
    "date": "2025-03-20",
    "dataset": "ad_clicks_q1.csv",
    "samples": 15000,
    "accuracy": 0.82,
    "features": ["age", "location", "device_type"],
    "description": "Retrained using more data"
}

with open(f"ad_click_model_v{version}_metadata.json", "w") as file:
    json.dump(metadata, file, indent=2)

Use semantic versioning:

MAJOR.MINOR.PATCH
1.0.0 — initial model
1.1.0 — improvement using the same input features
1.1.1 — small correction or bug fix
2.0.0 — breaking change, such as adding a required input feature

Key practical rules:

Never overwrite an existing model.
Save metadata for every version.
Record the data, features, model type, metrics, date, and changes.
Test a new version before deployment.
Keep the previous working model so you can roll back if needed.
Higher accuracy alone does not guarantee better production performance.