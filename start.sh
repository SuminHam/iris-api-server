export AWS_ACCESS_KEY_ID=mlflow_admin
export AWS_SECRET_ACCESS_KEY=mlflow_admin
export MLFLOW_TRACKING_URI=http://10.178.0.2:5000
export MLFLOW_S3_ENDPOINT_URL=http://10.178.0.2:9000

uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload