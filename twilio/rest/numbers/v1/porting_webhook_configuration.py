r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Numbers
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from typing import Any, Dict, List, Optional, Union
from twilio.base import values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class PortingWebhookConfigurationInstance(InstanceResource):
    """
    :ivar url: The URL of the webhook configuration request
    :ivar port_in_target_url: The complete webhook url that will be called when a notification event for port in request or port in phone number happens
    :ivar port_out_target_url: The complete webhook url that will be called when a notification event for a port out phone number happens.
    :ivar notifications_of: A list to filter what notification events to receive for this account and its sub accounts. If it is an empty list, then it means that there are no filters for the notifications events to send in each webhook and all events will get sent.
    """

    def __init__(self, version: Version, payload: Dict[str, Any]):
        super().__init__(version)

        self.url: Optional[str] = payload.get("url")
        self.port_in_target_url: Optional[str] = payload.get("port_in_target_url")
        self.port_out_target_url: Optional[str] = payload.get("port_out_target_url")
        self.notifications_of: Optional[List[str]] = payload.get("notifications_of")

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """

        return "<Twilio.Numbers.V1.PortingWebhookConfigurationInstance>"


class PortingWebhookConfigurationList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the PortingWebhookConfigurationList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/Porting/Configuration/Webhook"

    def create(
        self, body: Union[object, object] = values.unset
    ) -> PortingWebhookConfigurationInstance:
        """
        Create the PortingWebhookConfigurationInstance

        :param body:

        :returns: The created PortingWebhookConfigurationInstance
        """
        data = body.to_dict()

        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        headers["Content-Type"] = "application/json"

        headers["Accept"] = "application/json"

        payload = self._version.create(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return PortingWebhookConfigurationInstance(self._version, payload)

    async def create_async(
        self, body: Union[object, object] = values.unset
    ) -> PortingWebhookConfigurationInstance:
        """
        Asynchronously create the PortingWebhookConfigurationInstance

        :param body:

        :returns: The created PortingWebhookConfigurationInstance
        """
        data = body.to_dict()

        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        headers["Content-Type"] = "application/json"

        headers["Accept"] = "application/json"

        payload = await self._version.create_async(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return PortingWebhookConfigurationInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Numbers.V1.PortingWebhookConfigurationList>"
