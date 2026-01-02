from __future__ import annotations
from typing import List
from pydantic import BaseModel
from .installation_response import InstallationResponse


class CampaignRowInstallation(BaseModel):
    """Represents the installation status of a specific carrier/component in a location."""
    campaignRowId: int
    carrierName: str
    componentName: str
    quantityInstalled: int
    quantityToInstall: int
    responses: List[InstallationResponse]
