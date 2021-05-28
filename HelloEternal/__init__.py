# This function is not intended to be invoked directly. Instead it will be
# triggered by an HTTP starter function.
# Before running this sample, please:
# - create a Durable activity function (default name is "Hello")
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import json
import random
import azure.functions as func
import azure.durable_functions as df
from typing import Dict
from datetime import timedelta

def orchestrator_function(context: df.DurableOrchestrationContext):
    input: Dict[str,str] = context.get_input()
    newInput = yield context.call_activity("HelloEternalActivity",input)
    
    # sleep for one hour between cleanups
    next_cleanup = context.current_utc_datetime + timedelta(seconds=random.randint(30,120))
    yield context.create_timer(next_cleanup)
    logging.info('hello')
    context.continue_as_new(newInput)

main = df.Orchestrator.create(orchestrator_function)