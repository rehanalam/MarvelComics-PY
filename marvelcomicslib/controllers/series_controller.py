# -*- coding: utf-8 -*-

"""
    marvelcomicslib.controllers.series_controller

    This file was automatically generated by APIMATIC BETA v2.0 on 07/21/2016
"""

from marvelcomicslib.controllers.base_controller import *

from marvelcomicslib.models.series_data_wrapper import SeriesDataWrapper
from marvelcomicslib.models.series import Series


class SeriesController(BaseController):

    """A Controller to access Endpoints in the marvelcomicslib API."""

    def __init__(self, http_client = None, http_call_back = None):
        """Constructor which allows a different HTTP client for this controller."""
        BaseController.__init__(self, http_client, http_call_back)

    def get_character_series_collection(self,
                                        character_id,
                                        comics = None,
                                        contains = "comic",
                                        creators = None,
                                        events = None,
                                        limit = None,
                                        modified_since = None,
                                        offset = None,
                                        order_by = "title",
                                        series_type = "collection",
                                        start_year = None,
                                        stories = None,
                                        title = None,
                                        title_starts_with = None):
        """Does a GET request to /v1/public/characters/{characterId}/series.

        Fetches lists of series filtered by a character id.

        Args:
            character_id (string): The character ID
            comics (string, optional): Return only series which contain the
                specified comics (accepts a comma-separated list of ids).
            contains (string, optional): Return only series containing one or
                more comics with the specified format. (Acceptable values are:
                "comic", "magazine", "trade paperback", "hardcover", "digest",
                "graphic novel", "digital comic", "infinite comic")
            creators (string, optional): Return only series which feature work
                by the specified creators (accepts a comma-separated list of
                ids).
            events (string, optional): Return only series which have comics
                that take place during the specified events (accepts a
                comma-separated list of ids).
            limit (string, optional): Limit the result set to the specified
                number of resources.
            modified_since (string, optional): Return only series which have
                been modified since the specified date.
            offset (string, optional): Skip the specified number of resources
                in the result set.
            order_by (string, optional): Order the result set by a field or
                fields. Add a "-" to the value sort in descending order.
                Multiple values are given priority in the order in which they
                are passed. (Acceptable values are: "title", "modified",
                "startYear", "-title", "-modified", "-startYear")
            series_type (string, optional): Filter the series by publication
                frequency type. (Acceptable values are: "collection", "one
                shot", "limited", "ongoing")
            start_year (string, optional): Return only series matching the
                specified start year.
            stories (string, optional): Return only series which contain the
                specified stories (accepts a comma-separated list of ids).
            title (string, optional): Filter by series title.
            title_starts_with (string, optional): Return series with titles
                that begin with the specified string (e.g. Sp).

        Returns:
            SeriesDataWrapper: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += "/v1/public/characters/{characterId}/series"

        # Process optional template parameters
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            "characterId": character_id
        })

        # Process optional query parameters
        _query_parameters = {
            "comics": comics,
            "contains": contains,
            "creators": creators,
            "events": events,
            "limit": limit,
            "modifiedSince": modified_since,
            "offset": offset,
            "orderBy": order_by,
            "seriesType": series_type,
            "startYear": start_year,
            "stories": stories,
            "title": title,
            "titleStartsWith": title_starts_with,
            "apikey": Configuration.apikey
        }
        
        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            "user-agent": "APIMATIC 2.0",
            "accept": "application/json",
            "referer": Configuration.referer
        }

        # Prepare the API call.
        _http_request = self.http_client.get(_query_url, headers=_headers, query_parameters=_query_parameters)

        # Invoke the on before request HttpCallBack if specified
        if self.http_call_back != None:
            self.http_call_back.on_before_request(_http_request)

        # Invoke the API call  to fetch the response.
        _response = self.http_client.execute_as_string(_http_request)

        # Invoke the on after response HttpCallBack if specified
        if self.http_call_back != None:
            self.http_call_back.on_after_response(_response)

        # Endpoint error handling using HTTP status codes.
        if _response.status_code == 409:
            raise APIException("Limit greater than 100.", 409, _response.raw_body)

        # Global error handling using HTTP status codes.
        self.validate_response(_response)    

        # Return appropriate type
        return APIHelper.json_deserialize(_response.raw_body, SeriesDataWrapper.from_dictionary)



    def get_creator_series_collection(self,
                                      creator_id,
                                      characters = None,
                                      comics = None,
                                      contains = "comic",
                                      events = None,
                                      limit = None,
                                      modified_since = None,
                                      offset = None,
                                      order_by = "title",
                                      series_type = "collection",
                                      start_year = None,
                                      stories = None,
                                      title = None,
                                      title_starts_with = None):
        """Does a GET request to /v1/public/creators/{creatorId}/series.

        Fetches lists of series filtered by a creator id.

        Args:
            creator_id (string): The creator ID.
            characters (string, optional): Return only series which feature
                the specified characters (accepts a comma-separated list of
                ids).
            comics (string, optional): Return only series which contain the
                specified comics (accepts a comma-separated list of ids).
            contains (string, optional): Return only series containing one or
                more comics with the specified format. (Acceptable values are:
                "comic", "magazine", "trade paperback", "hardcover", "digest",
                "graphic novel", "digital comic", "infinite comic")
            events (string, optional): Return only series which have comics
                that take place during the specified events (accepts a
                comma-separated list of ids).
            limit (string, optional): Limit the result set to the specified
                number of resources.
            modified_since (string, optional): Return only series which have
                been modified since the specified date.
            offset (string, optional): Skip the specified number of resources
                in the result set.
            order_by (string, optional): Order the result set by a field or
                fields. Add a "-" to the value sort in descending order.
                Multiple values are given priority in the order in which they
                are passed. (Acceptable values are: "title", "modified",
                "startYear", "-title", "-modified", "-startYear")
            series_type (string, optional): Filter the series by publication
                frequency type. (Acceptable values are: "collection", "one
                shot", "limited", "ongoing")
            start_year (string, optional): Return only series matching the
                specified start year.
            stories (string, optional): Return only series which contain the
                specified stories (accepts a comma-separated list of ids).
            title (string, optional): Filter by series title.
            title_starts_with (string, optional): Return series with titles
                that begin with the specified string (e.g. Sp).

        Returns:
            SeriesDataWrapper: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += "/v1/public/creators/{creatorId}/series"

        # Process optional template parameters
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            "creatorId": creator_id
        })

        # Process optional query parameters
        _query_parameters = {
            "characters": characters,
            "comics": comics,
            "contains": contains,
            "events": events,
            "limit": limit,
            "modifiedSince": modified_since,
            "offset": offset,
            "orderBy": order_by,
            "seriesType": series_type,
            "startYear": start_year,
            "stories": stories,
            "title": title,
            "titleStartsWith": title_starts_with,
            "apikey": Configuration.apikey
        }
        
        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            "user-agent": "APIMATIC 2.0",
            "accept": "application/json",
            "referer": Configuration.referer
        }

        # Prepare the API call.
        _http_request = self.http_client.get(_query_url, headers=_headers, query_parameters=_query_parameters)

        # Invoke the on before request HttpCallBack if specified
        if self.http_call_back != None:
            self.http_call_back.on_before_request(_http_request)

        # Invoke the API call  to fetch the response.
        _response = self.http_client.execute_as_string(_http_request)

        # Invoke the on after response HttpCallBack if specified
        if self.http_call_back != None:
            self.http_call_back.on_after_response(_response)

        # Endpoint error handling using HTTP status codes.
        if _response.status_code == 409:
            raise APIException("Limit greater than 100.", 409, _response.raw_body)

        # Global error handling using HTTP status codes.
        self.validate_response(_response)    

        # Return appropriate type
        return APIHelper.json_deserialize(_response.raw_body, SeriesDataWrapper.from_dictionary)



    def get_event_series_collection(self,
                                    event_id,
                                    characters = None,
                                    comics = None,
                                    contains = "comic",
                                    creators = None,
                                    limit = None,
                                    modified_since = None,
                                    offset = None,
                                    order_by = "title",
                                    series_type = "collection",
                                    start_year = None,
                                    stories = None,
                                    title = None,
                                    title_starts_with = None):
        """Does a GET request to /v1/public/events/{eventId}/series.

        Fetches lists of series filtered by an event id.

        Args:
            event_id (string): The event ID.
            characters (string, optional): Return only series which feature
                the specified characters (accepts a comma-separated list of
                ids).
            comics (string, optional): Return only series which contain the
                specified comics (accepts a comma-separated list of ids).
            contains (string, optional): Return only series containing one or
                more comics with the specified format. (Acceptable values are:
                "comic", "magazine", "trade paperback", "hardcover", "digest",
                "graphic novel", "digital comic", "infinite comic")
            creators (string, optional): Return only series which feature work
                by the specified creators (accepts a comma-separated list of
                ids).
            limit (string, optional): Limit the result set to the specified
                number of resources.
            modified_since (string, optional): Return only series which have
                been modified since the specified date.
            offset (string, optional): Skip the specified number of resources
                in the result set.
            order_by (string, optional): Order the result set by a field or
                fields. Add a "-" to the value sort in descending order.
                Multiple values are given priority in the order in which they
                are passed. (Acceptable values are: "title", "modified",
                "startYear", "-title", "-modified", "-startYear")
            series_type (string, optional): Filter the series by publication
                frequency type. (Acceptable values are: "collection", "one
                shot", "limited", "ongoing")
            start_year (string, optional): Return only series matching the
                specified start year.
            stories (string, optional): Return only series which contain the
                specified stories (accepts a comma-separated list of ids).
            title (string, optional): Filter by series title.
            title_starts_with (string, optional): Return series with titles
                that begin with the specified string (e.g. Sp).

        Returns:
            SeriesDataWrapper: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += "/v1/public/events/{eventId}/series"

        # Process optional template parameters
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            "eventId": event_id
        })

        # Process optional query parameters
        _query_parameters = {
            "characters": characters,
            "comics": comics,
            "contains": contains,
            "creators": creators,
            "limit": limit,
            "modifiedSince": modified_since,
            "offset": offset,
            "orderBy": order_by,
            "seriesType": series_type,
            "startYear": start_year,
            "stories": stories,
            "title": title,
            "titleStartsWith": title_starts_with,
            "apikey": Configuration.apikey
        }
        
        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            "user-agent": "APIMATIC 2.0",
            "accept": "application/json",
            "referer": Configuration.referer
        }

        # Prepare the API call.
        _http_request = self.http_client.get(_query_url, headers=_headers, query_parameters=_query_parameters)

        # Invoke the on before request HttpCallBack if specified
        if self.http_call_back != None:
            self.http_call_back.on_before_request(_http_request)

        # Invoke the API call  to fetch the response.
        _response = self.http_client.execute_as_string(_http_request)

        # Invoke the on after response HttpCallBack if specified
        if self.http_call_back != None:
            self.http_call_back.on_after_response(_response)

        # Endpoint error handling using HTTP status codes.
        if _response.status_code == 409:
            raise APIException("Limit greater than 100.", 409, _response.raw_body)

        # Global error handling using HTTP status codes.
        self.validate_response(_response)    

        # Return appropriate type
        return APIHelper.json_deserialize(_response.raw_body, SeriesDataWrapper.from_dictionary)



    def get_series_collection(self,
                              characters = None,
                              comics = None,
                              contains = "comic",
                              creators = None,
                              events = None,
                              limit = None,
                              modified_since = None,
                              offset = None,
                              order_by = "title",
                              series_type = "collection",
                              start_year = None,
                              stories = None,
                              title = None,
                              title_starts_with = None):
        """Does a GET request to /v1/public/series.

        Fetches lists of series.

        Args:
            characters (string, optional): Return only series which feature
                the specified characters (accepts a comma-separated list of
                ids).
            comics (string, optional): Return only series which contain the
                specified comics (accepts a comma-separated list of ids).
            contains (string, optional): Return only series containing one or
                more comics with the specified format. (Acceptable values are:
                "comic", "magazine", "trade paperback", "hardcover", "digest",
                "graphic novel", "digital comic", "infinite comic")
            creators (string, optional): Return only series which feature work
                by the specified creators (accepts a comma-separated list of
                ids).
            events (string, optional): Return only series which have comics
                that take place during the specified events (accepts a
                comma-separated list of ids).
            limit (string, optional): Limit the result set to the specified
                number of resources.
            modified_since (string, optional): Return only series which have
                been modified since the specified date.
            offset (string, optional): Skip the specified number of resources
                in the result set.
            order_by (string, optional): Order the result set by a field or
                fields. Add a "-" to the value sort in descending order.
                Multiple values are given priority in the order in which they
                are passed. (Acceptable values are: "title", "modified",
                "startYear", "-title", "-modified", "-startYear")
            series_type (string, optional): Filter the series by publication
                frequency type. (Acceptable values are: "collection", "one
                shot", "limited", "ongoing")
            start_year (string, optional): Return only series matching the
                specified start year.
            stories (string, optional): Return only series which contain the
                specified stories (accepts a comma-separated list of ids).
            title (string, optional): Return only series matching the
                specified title.
            title_starts_with (string, optional): Return series with titles
                that begin with the specified string (e.g. Sp).

        Returns:
            SeriesDataWrapper: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += "/v1/public/series"

        # Process optional query parameters
        _query_parameters = {
            "characters": characters,
            "comics": comics,
            "contains": contains,
            "creators": creators,
            "events": events,
            "limit": limit,
            "modifiedSince": modified_since,
            "offset": offset,
            "orderBy": order_by,
            "seriesType": series_type,
            "startYear": start_year,
            "stories": stories,
            "title": title,
            "titleStartsWith": title_starts_with,
            "apikey": Configuration.apikey
        }
        
        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            "user-agent": "APIMATIC 2.0",
            "accept": "application/json",
            "referer": Configuration.referer
        }

        # Prepare the API call.
        _http_request = self.http_client.get(_query_url, headers=_headers, query_parameters=_query_parameters)

        # Invoke the on before request HttpCallBack if specified
        if self.http_call_back != None:
            self.http_call_back.on_before_request(_http_request)

        # Invoke the API call  to fetch the response.
        _response = self.http_client.execute_as_string(_http_request)

        # Invoke the on after response HttpCallBack if specified
        if self.http_call_back != None:
            self.http_call_back.on_after_response(_response)

        # Endpoint error handling using HTTP status codes.
        if _response.status_code == 409:
            raise APIException("Limit greater than 100.", 409, _response.raw_body)

        # Global error handling using HTTP status codes.
        self.validate_response(_response)    

        # Return appropriate type
        return APIHelper.json_deserialize(_response.raw_body, SeriesDataWrapper.from_dictionary)



    def get_series_individual(self,
                              series_id):
        """Does a GET request to /v1/public/series/{seriesId}.

        Fetches a single comic series by id.

        Args:
            series_id (string): Filter by series title.

        Returns:
            Series: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += "/v1/public/series/{seriesId}"

        # Process optional template parameters
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            "seriesId": series_id
        })

        # Process optional query parameters
        _query_parameters = {
            "apikey": Configuration.apikey
        }
        
        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            "user-agent": "APIMATIC 2.0",
            "accept": "application/json",
            "referer": Configuration.referer
        }

        # Prepare the API call.
        _http_request = self.http_client.get(_query_url, headers=_headers, query_parameters=_query_parameters)

        # Invoke the on before request HttpCallBack if specified
        if self.http_call_back != None:
            self.http_call_back.on_before_request(_http_request)

        # Invoke the API call  to fetch the response.
        _response = self.http_client.execute_as_string(_http_request)

        # Invoke the on after response HttpCallBack if specified
        if self.http_call_back != None:
            self.http_call_back.on_after_response(_response)

        # Endpoint error handling using HTTP status codes.
        if _response.status_code == 404:
            raise APIException("Series not found.", 404, _response.raw_body)

        # Global error handling using HTTP status codes.
        self.validate_response(_response)    

        # Return appropriate type
        return APIHelper.json_deserialize(_response.raw_body, Series.from_dictionary)



    def get_story_series_collection(self,
                                    story_id,
                                    characters = None,
                                    comics = None,
                                    contains = "comic",
                                    creators = None,
                                    events = None,
                                    limit = None,
                                    modified_since = None,
                                    offset = None,
                                    order_by = "title",
                                    series_type = "collection",
                                    start_year = None,
                                    title = None,
                                    title_starts_with = None):
        """Does a GET request to /v1/public/stories/{storyId}/series.

        Fetches lists of series filtered by a story id.

        Args:
            story_id (string): The story ID.
            characters (string, optional): Return only series which feature
                the specified characters (accepts a comma-separated list of
                ids).
            comics (string, optional): Return only series which contain the
                specified comics (accepts a comma-separated list of ids).
            contains (string, optional): Return only series containing one or
                more comics with the specified format. (Acceptable values are:
                "comic", "magazine", "trade paperback", "hardcover", "digest",
                "graphic novel", "digital comic", "infinite comic")
            creators (string, optional): Return only series which feature work
                by the specified creators (accepts a comma-separated list of
                ids).
            events (string, optional): Return only series which have comics
                that take place during the specified events (accepts a
                comma-separated list of ids).
            limit (string, optional): Limit the result set to the specified
                number of resources.
            modified_since (string, optional): Return only series which have
                been modified since the specified date.
            offset (string, optional): Skip the specified number of resources
                in the result set.
            order_by (string, optional): Order the result set by a field or
                fields. Add a "-" to the value sort in descending order.
                Multiple values are given priority in the order in which they
                are passed. (Acceptable values are: "title", "modified",
                "startYear", "-title", "-modified", "-startYear")
            series_type (string, optional): Filter the series by publication
                frequency type. (Acceptable values are: "collection", "one
                shot", "limited", "ongoing")
            start_year (string, optional): Return only series matching the
                specified start year.
            title (string, optional): Filter by series title.
            title_starts_with (string, optional): Return series with titles
                that begin with the specified string (e.g. Sp).

        Returns:
            SeriesDataWrapper: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += "/v1/public/stories/{storyId}/series"

        # Process optional template parameters
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            "storyId": story_id
        })

        # Process optional query parameters
        _query_parameters = {
            "characters": characters,
            "comics": comics,
            "contains": contains,
            "creators": creators,
            "events": events,
            "limit": limit,
            "modifiedSince": modified_since,
            "offset": offset,
            "orderBy": order_by,
            "seriesType": series_type,
            "startYear": start_year,
            "title": title,
            "titleStartsWith": title_starts_with,
            "apikey": Configuration.apikey
        }
        
        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            "user-agent": "APIMATIC 2.0",
            "accept": "application/json",
            "referer": Configuration.referer
        }

        # Prepare the API call.
        _http_request = self.http_client.get(_query_url, headers=_headers, query_parameters=_query_parameters)

        # Invoke the on before request HttpCallBack if specified
        if self.http_call_back != None:
            self.http_call_back.on_before_request(_http_request)

        # Invoke the API call  to fetch the response.
        _response = self.http_client.execute_as_string(_http_request)

        # Invoke the on after response HttpCallBack if specified
        if self.http_call_back != None:
            self.http_call_back.on_after_response(_response)

        # Endpoint error handling using HTTP status codes.
        if _response.status_code == 409:
            raise APIException("Limit greater than 100.", 409, _response.raw_body)

        # Global error handling using HTTP status codes.
        self.validate_response(_response)    

        # Return appropriate type
        return APIHelper.json_deserialize(_response.raw_body, SeriesDataWrapper.from_dictionary)


