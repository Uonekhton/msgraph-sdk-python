# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from __future__ import unicode_literals
from ..collection_base import CollectionRequestBase, CollectionResponseBase, CollectionPageBase
from ..request_builder_base import RequestBuilderBase
from ..request import mail_folder_request_builder 
from ..model.mail_folder import MailFolder
import json
import asyncio

class MailFoldersCollectionRequest(CollectionRequestBase):

    def __init__(self, request_url, client, options):
        """Initialize the MailFoldersCollectionRequest
        
        Args:
            request_url (str): The url to perform the MailFoldersCollectionRequest
                on
            client (:class:`GraphClient<msgraph.request.graph_client.GraphClient>`):
                The client which will be used for the request
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request
        """
        super(MailFoldersCollectionRequest, self).__init__(request_url, client, options)

    def get(self):
        """Gets the MailFoldersCollectionPage

        Returns: 
            :class:`MailFoldersCollectionPage<msgraph.request.mail_folders_collection.MailFoldersCollectionPage>`:
                The MailFoldersCollectionPage
        """
        self.method = "GET"
        collection_response = MailFoldersCollectionResponse(json.loads(self.send().content))
        return self._page_from_response(collection_response)

    @asyncio.coroutine
    def get_async(self):
        """Gets the MailFoldersCollectionPage in async

        Yields: 
            :class:`MailFoldersCollectionPage<msgraph.request.mail_folders_collection.MailFoldersCollectionPage>`:
                The MailFoldersCollectionPage
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.get)
        collection_page = yield from future
        return collection_page

class MailFoldersCollectionRequestBuilder(RequestBuilderBase):

    def __getitem__(self, key):
        """Get the MailFolderRequestBuilder with the specified key
        
        Args:
            key (str): The key to get a MailFolderRequestBuilder for
        
        Returns: 
            :class:`MailFolderRequestBuilder<msgraph.request.mail_folder_request_builder.MailFolderRequestBuilder>`:
                A MailFolderRequestBuilder for that key
        """
        return mail_folder_request_builder.MailFolderRequestBuilder(self.append_to_request_url(str(key)), self._client)

    def request(self,select=None, filter=None, top=None, skip=None, order_by=None, options=None):
        """Builds the MailFoldersCollectionRequest
        
        Args:
            expand (str): Default None, comma-separated list of relationships
                to expand in the response.
            select (str): Default None, comma-separated list of properties to
                include in the response.
            top (int): Default None, the number of items to return in a result.
            order_by (str): Default None, comma-separated list of properties
                that are used to sort the order of items in the response.
            options (list of :class:`Option<msgraph.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Returns:
            :class:`MailFoldersCollectionRequest<msgraph.request.mail_folders_collection.MailFoldersCollectionRequest>`:
                The MailFoldersCollectionRequest
        """
        req = MailFoldersCollectionRequest(self._request_url, self._client, options)
        req._set_query_options(select=select, filter=filter, top=top, skip=skip, order_by=order_by, )
        return req

    def get(self):
        """Gets the MailFoldersCollectionPage

        Returns: 
            :class:`MailFoldersCollectionPage<msgraph.request.mail_folders_collection.MailFoldersCollectionPage>`:
                The MailFoldersCollectionPage
        """
        return self.request().get()

    @asyncio.coroutine
    def get_async(self):
        """Gets the MailFoldersCollectionPage in async

        Yields: 
            :class:`MailFoldersCollectionPage<msgraph.request.mail_folders_collection.MailFoldersCollectionPage>`:
                The MailFoldersCollectionPage
        """
        collection_page = yield from self.request().get_async()
        return collection_page


class MailFoldersCollectionResponse(CollectionResponseBase):

    @property
    def collection_page(self):
        """The collection page stored in the response JSON
        
        Returns:
            :class:`MailFoldersCollectionPage<msgraph.request.mail_folders_collection.MailFoldersCollectionPage>`:
                The collection page
        """
        if self._collection_page:
            self._collection_page._prop_list = self._prop_dict["value"]
        else:
            self._collection_page = MailFoldersCollectionPage(self._prop_dict["value"])

        return self._collection_page


class MailFoldersCollectionPage(CollectionPageBase):

    def __getitem__(self, index):
        """Get the MailFolder at the index specified
        
        Args:
            index (int): The index of the item to get from the MailFoldersCollectionPage

        Returns:
            :class:`MailFolder<msgraph.model.mail_folder.MailFolder>`:
                The MailFolder at the index
        """
        return MailFolder(self._prop_list[index])

    def mail_folders(self):
        """Get a generator of MailFolder within the MailFoldersCollectionPage
        
        Yields:
            :class:`MailFolder<msgraph.model.mail_folder.MailFolder>`:
                The next MailFolder in the collection
        """
        for item in self._prop_list:
            yield MailFolder(item)

    def _init_next_page_request(self, next_page_link, client, options):
        """Initialize the next page request for the MailFoldersCollectionPage
        
        Args:
            next_page_link (str): The URL for the next page request
                to be sent to
            client (:class:`GraphClient<msgraph.model.graph_client.GraphClient>`:
                The client to be used for the request
            options (list of :class:`Option<msgraph.options.Option>`:
                A list of options
        """
        self._next_page_request = MailFoldersCollectionRequest(next_page_link, client, options)
