from kedro.pipeline import Pipeline
from package.pipelines.data_engineering.nodes import (
    return_greeting_node, join_statements_node
)

def create_pipeline(**kwargs):
    return Pipeline([return_greeting_node, join_statements_node])