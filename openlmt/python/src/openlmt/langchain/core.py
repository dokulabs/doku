# pylint: disable=duplicate-code, broad-exception-caught, too-many-statements, unused-argument
"""
Module for monitoring Langchain applications.
"""

import logging
from opentelemetry.trace import SpanKind
from ..__helpers import handle_exception

# Initialize logger for logging potential issues and operations
logger = logging.getLogger(__name__)

def general_wrap(gen_ai_endpoint, version, environment, application_name,
                 tracer, pricing_info, trace_content):
    """
    Creates a wrapper around a function call to trace and log its execution metrics.

    This function wraps any given function to measure its execution time,
    log its operation, and trace its execution using OpenTelemetry.
    
    Parameters:
    - gen_ai_endpoint (str): A descriptor or name for the endpoint being traced.
    - version (str): The version of the Langchain application.
    - environment (str): The deployment environment (e.g., 'production', 'development').
    - application_name (str): Name of the Langchain application.
    - tracer (opentelemetry.trace.Tracer): The tracer object used for OpenTelemetry tracing.
    - pricing_info (dict): Information about the pricing for internal metrics (currently not used).
    - trace_content (bool): Flag indicating whether to trace the content of the response.

    Returns:
    - function: A higher-order function that takes a function 'wrapped' and returns
                a new function that wraps 'wrapped' with additional tracing and logging.
    """

    def wrapper(wrapped, instance, args, kwargs):
        """
        An inner wrapper function that executes the wrapped function, measures execution
        time, and records trace data using OpenTelemetry.

        Parameters:
        - wrapped (Callable): The original function that this wrapper will execute.
        - instance (object): The instance to which the wrapped function belongs. This
                             is used for instance methods. For static and classmethods,
                             this may be None.
        - args (tuple): Positional arguments passed to the wrapped function.
        - kwargs (dict): Keyword arguments passed to the wrapped function.

        Returns:
        - The result of the wrapped function call.
        
        The wrapper initiates a span with the provided tracer, sets various attributes
        on the span based on the function's execution and response, and ensures
        errors are handled and logged appropriately.
        """
        with tracer.start_as_current_span(gen_ai_endpoint, kind= SpanKind.CLIENT) as span:
            try:
                response = wrapped(*args, **kwargs)

                try:
                    span.set_attribute("gen_ai.system", "langchain")
                    span.set_attribute("gen_ai.type", "retrieval")
                    span.set_attribute("gen_ai.endpoint", gen_ai_endpoint)
                    span.set_attribute("gen_ai.environment", environment)
                    span.set_attribute("gen_ai.application_name", application_name)
                    span.set_attribute("gen_ai.retrieval.source", response[0].metadata["source"])

                    return response

                except Exception as e:
                    handle_exception(span, e)
                    logger.error("Error in patched message creation: %s", e)

                    # Return original response
                    return response

            except Exception as e:
                handle_exception(span, e)
                raise e

    return wrapper

def hub(gen_ai_endpoint, version, environment, application_name, tracer,
        pricing_info, trace_content):
    """
    Creates a wrapper around Langchain hub operations for tracing and logging.

    Similar to `general_wrap`, this function focuses on wrapping functions involved
    in interacting with the Langchain hub, adding specific metadata relevant to
    hub operations to the span attributes.

    Parameters:
    - gen_ai_endpoint (str): A descriptor or name for the Langchain hub endpoint.
    - version (str): The version of the Langchain application.
    - environment (str): The deployment environment, such as 'production' or 'development'.
    - application_name (str): Name of the Langchain application.
    - tracer (opentelemetry.trace.Tracer): The tracer for OpenTelemetry tracing.
    - pricing_info (dict): Pricing information for the operation (not currently used).
    - trace_content (bool): Indicates if the content of the response should be traced.

    Returns:
    - function: A new function that wraps the original hub operation call with added
                logging, tracing, and metric calculation functionalities.
    """

    def wrapper(wrapped, instance, args, kwargs):
        """
        An inner wrapper specifically designed for Langchain hub operations,
        providing tracing, logging, and execution metrics.

        Parameters:
        - wrapped (Callable): The original hub operation function to be executed.
        - instance (object): The instance of the class where the hub operation
                             method is defined. May be None for static or class methods.
        - args (tuple): Positional arguments to pass to the hub operation function.
        - kwargs (dict): Keyword arguments to pass to the hub operation function.

        Returns:
        - The result of executing the hub operation function.
        
        This wrapper captures additional metadata relevant to Langchain hub operations,
        creating spans with specific attributes and metrics that reflect the nature of
        each hub call.
        """

        with tracer.start_as_current_span(gen_ai_endpoint, kind= SpanKind.CLIENT) as span:
            try:
                response = wrapped(*args, **kwargs)

                try:
                    span.set_attribute("gen_ai.system", "langchain")
                    span.set_attribute("gen_ai.type", "retrieval")
                    span.set_attribute("gen_ai.endpoint", gen_ai_endpoint)
                    span.set_attribute("gen_ai.environment", environment)
                    span.set_attribute("gen_ai.application_name", application_name)
                    span.set_attribute("gen_ai.hub.owner", response.metadata["lc_hub_owner"])
                    span.set_attribute("gen_ai.hub.repo", response.metadata["lc_hub_repo"])

                    return response

                except Exception as e:
                    handle_exception(span, e)
                    logger.error("Error in patched message creation: %s", e)

                    # Return original response
                    return response

            except Exception as e:
                handle_exception(span, e)
                raise e

    return wrapper
