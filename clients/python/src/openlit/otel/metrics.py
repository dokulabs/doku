"""
Setups up OpenTelemetry Meter
"""
import os
from opentelemetry import metrics
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader, ConsoleMetricExporter
from opentelemetry.sdk.resources import Resource, SERVICE_NAME
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter

from openlit.semcov import SemanticConvetion

# Global flag to check if the meter provider initialization is complete.
METER_SET = False

def setup_meter(application_name="default", meter=None, otlp_endpoint=None, otlp_headers=None):
    """
    Sets up OpenTelemetry metrics with a counter for total requests.

    Params:
        application_name (str): The name of the application for which metrics are being collected.
        otlp_endpoint (str): The OTLP exporter endpoint for metrics.
        otlp_headers (dict): Headers for the OTLP request.

    Returns:
        A dictionary containing the meter and created metrics for easy access.
    """

    # pylint: disable=global-statement
    global METER_SET

    try:
        if meter is None and not METER_SET:
            resource = Resource.create(attributes={SERVICE_NAME: application_name})

            otlp_endpoint = otlp_endpoint or os.getenv("OTEL_EXPORTER_OTLP_ENDPOINT")
            otlp_headers = otlp_headers or os.getenv("OTEL_EXPORTER_OTLP_HEADERS")

            if otlp_endpoint:
                metric_exporter = OTLPMetricExporter(endpoint=otlp_endpoint, headers=otlp_headers)
            else:
                metric_exporter = ConsoleMetricExporter()

            metric_reader = PeriodicExportingMetricReader(metric_exporter)

            meter_provider = MeterProvider(resource=resource, metric_readers=[metric_reader])

            metrics.set_meter_provider(meter_provider)

            meter = metrics.get_meter(__name__, version="0.1.0")

            METER_SET = True

        # Define and create the metrics
        metrics_dict = {
            "genai_requests": meter.create_counter(
                name=SemanticConvetion.GEN_AI_REQUESTS,
                description="Number of requests to OpenAI",
                unit="1",
            ),
            "genai_prompt_tokens": meter.create_counter(
                name=SemanticConvetion.GEN_AI_USAGE_PROMPT_TOKENS,
                description="Number of prompt tokens processed.",
                unit="1",
            ),
            "genai_completion_tokens": meter.create_counter(
                name=SemanticConvetion.GEN_AI_USAGE_COMPLETION_TOKENS,
                description="Number of completion tokens processed.",
                unit="1",
            ),
            "genai_total_tokens": meter.create_counter(
                name=SemanticConvetion.GEN_AI_USAGE_TOTAL_TOKENS,
                description="Number of total tokens processed.",
                unit="1",
            ),
            "genai_cost": meter.create_histogram(
                name=SemanticConvetion.GEN_AI_USAGE_COST,
                description="The distribution of OpenAI request costs.",
                unit="USD",
            ),
        }

        return metrics_dict

    # pylint: disable=bare-except
    except:
        return None
