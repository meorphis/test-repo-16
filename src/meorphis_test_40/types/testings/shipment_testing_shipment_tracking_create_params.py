# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ShipmentTestingShipmentTrackingCreateParams", "TrackingDetail"]


class ShipmentTestingShipmentTrackingCreateParams(TypedDict, total=False):
    status: Required[Literal["in_transit", "cancelled", "failure", "delivered"]]
    """The shipment's status."""

    tracking_details: Required[Iterable[TrackingDetail]]
    """
    A list of tracking updates that contain the shipment's status, location, and any
    unique messages.
    """

    tracking_number: Required[str]
    """The carrier's tracking number for the shipment.

    Must be prefixed with `MockBolt`.
    """

    delivery_date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The shipment's actual or estimated delivery date."""


class TrackingDetail(TypedDict, total=False):
    country_code: str
    """The country associated this this set of tracking details, if any."""

    event_date: str
    """The tracking detail's timestamp."""

    locality: str
    """The locality associated this this set of tracking details, if any."""

    message: str
    """
    An arbitrary, human-readable message associated with this set of tracking
    details.
    """

    postal_code: str
    """The postal associated this this set of tracking details, if any."""

    region: str
    """The region associated this this set of tracking details, if any."""

    status: Literal[
        "unknown",
        "pre_transit",
        "in_transit",
        "out_for_delivery",
        "delivered",
        "available_for_pickup",
        "return_to_sender",
        "failure",
        "cancelled",
        "error",
    ]
