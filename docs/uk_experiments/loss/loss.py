from .categories.households import Households
from .categories.populations import Populations
from .categories.country_level_programs import (
    country_level_programs,
)
from survey_enhance.reweight import LossCategory
from policyengine_core.parameters import ParameterNode, uprate_parameters
from pathlib import Path


class Demographics(LossCategory):
    weight = 1
    subcategories = [Households, Populations]


class Programs(LossCategory):
    weight = 1
    subcategories = country_level_programs


class Loss(LossCategory):
    subcategories = [
        Demographics,
        Programs,
    ]


calibration_parameters = ParameterNode(
    directory_path=Path(__file__).parent / "calibration_parameters",
    name="calibration",
)

calibration_parameters = uprate_parameters(calibration_parameters).calibration
