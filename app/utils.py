import mlflow
from starlette.concurrency import run_in_threadpool
from app.core.model_registry import model_registry
from mlflow.tracking import MlflowClient


def load_model():
    print("Loading model...")
    return mlflow.sklearn.load_model("models:/iris_model/production")


async def reload_model():
    print("Reloading model...")
    new_model = await run_in_threadpool(load_model)
    model_registry.register_model("iris_model", new_model)
    print("Model reloaded successfully.")


def get_current_model_version():
    """
    Fetch the current model version in use from a running MLflow server.
    Assumes that the model is tagged appropriately in MLflow.
    """
    client = MlflowClient()
    model_name = (
        "iris_model"  # Change this to your actual registered model name in MLflow
    )
    model_versions = client.search_model_versions(f"name='{model_name}'")
    current_version = max(
        [int(v.version) for v in model_versions if v.current_stage == "Production"]
    )
    return current_version


def get_production_model_version():
    """
    Fetch the latest production version of the model from MLflow.
    This could be the same as the current version if there have been no updates.
    """
    client = MlflowClient()
    model_name = (
        "iris_model"  # Change this to your actual registered model name in MLflow
    )
    model_versions = client.search_model_versions(f"name='{model_name}'")
    production_version = max(
        [int(v.version) for v in model_versions if v.current_stage == "Production"]
    )
    return production_version
