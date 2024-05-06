# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["WebhookCreateParams", "Event", "EventEventGroup", "EventEventList"]


class WebhookCreateParams(TypedDict, total=False):
    event: Required[Event]

    url: Required[str]
    """The webhook's URL"""


class EventEventGroup(TypedDict, total=False):
    tag: Required[Annotated[Literal["group"], PropertyInfo(alias=".tag")]]

    event_group: Required[Literal["all"]]


class EventEventList(TypedDict, total=False):
    tag: Required[Annotated[Literal["list"], PropertyInfo(alias=".tag")]]

    event_list: Required[
        List[
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
    ]


Event = Union[EventEventGroup, EventEventList]
