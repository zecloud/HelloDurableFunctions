# This function is not intended to be invoked directly. Instead it will be
# triggered by an HTTP starter function.
# Before running this sample, please:
# - create a Durable activity function (default name is "Hello")
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import json

import azure.functions as func
import azure.durable_functions as df
from typing import Dict

def orchestrator_function(context: df.DurableOrchestrationContext):
    monitoring_request: Dict[str] = context.get_input()
    name: str = monitoring_request["name"]
    result1 = yield context.call_activity('HelloDurableActivity', name)

    return [result1]

main = df.Orchestrator.create(orchestrator_function)