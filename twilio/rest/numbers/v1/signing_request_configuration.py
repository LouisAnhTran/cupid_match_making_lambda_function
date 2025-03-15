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

from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class SigningRequestConfigurationInstance(InstanceResource):
    """
    :ivar logo_sid: The SID of the document  that includes the logo that will appear in the LOA. To upload documents follow the following guide: https://www.twilio.com/docs/phone-numbers/regulatory/getting-started/create-new-bundle-public-rest-apis#supporting-document-create
    :ivar friendly_name: This is the string that you assigned as a friendly name for describing the creation of the configuration.
    :ivar product: The product or service for which is requesting the signature.
    :ivar country: The country ISO code to apply the configuration.
    :ivar email_subject: Subject of the email that the end client will receive ex: “Twilio Hosting Request”, maximum length of 255 characters.
    :ivar email_message: Content of the email that the end client will receive ex: “This is a Hosting request from Twilio, please check the document and sign it”, maximum length of 5,000 characters.
    :ivar url_redirection: Url the end client will be redirected after signing a document.
    :ivar url:
    """

    def __init__(self, version: Version, payload: Dict[str, Any]):
        super().__init__(version)

        self.logo_sid: Optional[str] = payload.get("logo_sid")
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.product: Optional[str] = payload.get("product")
        self.country: Optional[str] = payload.get("country")
        self.email_subject: Optional[str] = payload.get("email_subject")
        self.email_message: Optional[str] = payload.get("email_message")
        self.url_redirection: Optional[str] = payload.get("url_redirection")
        self.url: Optional[str] = payload.get("url")

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """

        return "<Twilio.Numbers.V1.SigningRequestConfigurationInstance>"


class SigningRequestConfigurationPage(Page):

    def get_instance(
        self, payload: Dict[str, Any]
    ) -> SigningRequestConfigurationInstance:
        """
        Build an instance of SigningRequestConfigurationInstance

        :param payload: Payload response from the API
        """
        return SigningRequestConfigurationInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Numbers.V1.SigningRequestConfigurationPage>"


class SigningRequestConfigurationList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the SigningRequestConfigurationList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/SigningRequest/Configuration"

    def create(
        self, body: Union[object, object] = values.unset
    ) -> SigningRequestConfigurationInstance:
        """
        Create the SigningRequestConfigurationInstance

        :param body:

        :returns: The created SigningRequestConfigurationInstance
        """
        data = body.to_dict()

        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        headers["Content-Type"] = "application/json"

        headers["Accept"] = "application/json"

        payload = self._version.create(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return SigningRequestConfigurationInstance(self._version, payload)

    async def create_async(
        self, body: Union[object, object] = values.unset
    ) -> SigningRequestConfigurationInstance:
        """
        Asynchronously create the SigningRequestConfigurationInstance

        :param body:

        :returns: The created SigningRequestConfigurationInstance
        """
        data = body.to_dict()

        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        headers["Content-Type"] = "application/json"

        headers["Accept"] = "application/json"

        payload = await self._version.create_async(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return SigningRequestConfigurationInstance(self._version, payload)

    def stream(
        self,
        country: Union[str, object] = values.unset,
        product: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[SigningRequestConfigurationInstance]:
        """
        Streams SigningRequestConfigurationInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str country: The country ISO code to apply this configuration, this is an optional field, Example: US, MX
        :param str product: The product or service for which is requesting the signature, this is an optional field, Example: Porting, Hosting
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            country=country, product=product, page_size=limits["page_size"]
        )

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        country: Union[str, object] = values.unset,
        product: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[SigningRequestConfigurationInstance]:
        """
        Asynchronously streams SigningRequestConfigurationInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str country: The country ISO code to apply this configuration, this is an optional field, Example: US, MX
        :param str product: The product or service for which is requesting the signature, this is an optional field, Example: Porting, Hosting
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            country=country, product=product, page_size=limits["page_size"]
        )

        return self._version.stream_async(page, limits["limit"])

    def list(
        self,
        country: Union[str, object] = values.unset,
        product: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[SigningRequestConfigurationInstance]:
        """
        Lists SigningRequestConfigurationInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str country: The country ISO code to apply this configuration, this is an optional field, Example: US, MX
        :param str product: The product or service for which is requesting the signature, this is an optional field, Example: Porting, Hosting
        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return list(
            self.stream(
                country=country,
                product=product,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        country: Union[str, object] = values.unset,
        product: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[SigningRequestConfigurationInstance]:
        """
        Asynchronously lists SigningRequestConfigurationInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str country: The country ISO code to apply this configuration, this is an optional field, Example: US, MX
        :param str product: The product or service for which is requesting the signature, this is an optional field, Example: Porting, Hosting
        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return [
            record
            async for record in await self.stream_async(
                country=country,
                product=product,
                limit=limit,
                page_size=page_size,
            )
        ]

    def page(
        self,
        country: Union[str, object] = values.unset,
        product: Union[str, object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> SigningRequestConfigurationPage:
        """
        Retrieve a single page of SigningRequestConfigurationInstance records from the API.
        Request is executed immediately

        :param country: The country ISO code to apply this configuration, this is an optional field, Example: US, MX
        :param product: The product or service for which is requesting the signature, this is an optional field, Example: Porting, Hosting
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of SigningRequestConfigurationInstance
        """
        data = values.of(
            {
                "Country": country,
                "Product": product,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        headers["Accept"] = "application/json"

        response = self._version.page(
            method="GET", uri=self._uri, params=data, headers=headers
        )
        return SigningRequestConfigurationPage(self._version, response)

    async def page_async(
        self,
        country: Union[str, object] = values.unset,
        product: Union[str, object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> SigningRequestConfigurationPage:
        """
        Asynchronously retrieve a single page of SigningRequestConfigurationInstance records from the API.
        Request is executed immediately

        :param country: The country ISO code to apply this configuration, this is an optional field, Example: US, MX
        :param product: The product or service for which is requesting the signature, this is an optional field, Example: Porting, Hosting
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of SigningRequestConfigurationInstance
        """
        data = values.of(
            {
                "Country": country,
                "Product": product,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        headers["Accept"] = "application/json"

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data, headers=headers
        )
        return SigningRequestConfigurationPage(self._version, response)

    def get_page(self, target_url: str) -> SigningRequestConfigurationPage:
        """
        Retrieve a specific page of SigningRequestConfigurationInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of SigningRequestConfigurationInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return SigningRequestConfigurationPage(self._version, response)

    async def get_page_async(self, target_url: str) -> SigningRequestConfigurationPage:
        """
        Asynchronously retrieve a specific page of SigningRequestConfigurationInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of SigningRequestConfigurationInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return SigningRequestConfigurationPage(self._version, response)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Numbers.V1.SigningRequestConfigurationList>"
