# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["WebhookRetrieveResponse", "Event", "EventEventGroup", "EventEventList"]


class EventEventGroup(BaseModel):
    tag: Literal["group"] = FieldInfo(alias=".tag")

    event_group: Literal["all"]


class EventEventList(BaseModel):
    tag: Literal["list"] = FieldInfo(alias=".tag")

    event_list: List[
        Literal[
            "payment",
            "credit",
            "capture",
            "void",
            "auth",
            "pending",
            "rejected_irreversible",
            "rejected_reversible",
            "failed_payment",
            "newsletter_subscription",
            "risk_insights",
            "credit_card_deleted",
        ]
    ]


Event = Union[EventEventGroup, EventEventList]


class WebhookRetrieveResponse(BaseModel):
    event: Event

    url: str
    """The webhook's URL"""

    id: Optional[str] = None
    """The webhook's ID"""

    created_at: Optional[datetime] = None
    """The time at which the webhook was created"""
