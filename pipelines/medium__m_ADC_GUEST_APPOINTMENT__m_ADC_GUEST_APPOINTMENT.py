from prophecy_pipeline_sdk.graph import *
from prophecy_pipeline_sdk.properties import *
args = PipelineArgs(label = "medium__m_ADC_GUEST_APPOINTMENT__m_ADC_GUEST_APPOINTMENT", version = 1, auto_layout = False)

with Pipeline(args) as pipeline:
    medium__m_ADC_GUEST_APPOINTMENT__m_ADC_GUEST_APPOINTMENT__main = Process(
        name = "medium__m_ADC_GUEST_APPOINTMENT__m_ADC_GUEST_APPOINTMENT__main",
        properties = ModelTransform(modelName = "medium__m_ADC_GUEST_APPOINTMENT__m_ADC_GUEST_APPOINTMENT__main"),
        input_ports = ["in_0"]
    )

