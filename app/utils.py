import mlflow

def load_model():
    print("Loading model...")
    return mlflow.sklearn.load_model("models:/iris_model/production")
