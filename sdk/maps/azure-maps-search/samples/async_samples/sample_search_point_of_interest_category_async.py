# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
FILE: sample_search_point_of_interest_category_async.py
DESCRIPTION:
    This sample demonstrates search POI by given target such as `RESTAURANT` and coordinates.
USAGE:
    python sample_search_point_of_interest_category_async.py

    Set the environment variables with your own values before running the sample:
    - AZURE_SUBSCRIPTION_KEY - your subscription key
"""
import asyncio
import os

subscription_key = os.getenv("AZURE_SUBSCRIPTION_KEY")


async def search_point_of_interest_category_async():
    # [START search_point_of_interest_category_async]
    from azure.core.credentials import AzureKeyCredential
    from azure.maps.search.aio import MapsSearchClient

    maps_search_client = MapsSearchClient(credential=AzureKeyCredential(subscription_key))
    async with maps_search_client:
        result = await maps_search_client.search_point_of_interest_category("RESTAURANT", coordinates=(25.0338053, 121.5640089))

    print("Get Search POI Category:")
    print(result)
    # [END search_point_of_interest_category_async]


if __name__ == '__main__':
    asyncio.run(search_point_of_interest_category_async())