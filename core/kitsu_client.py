import aiohttp
import askitsu #type: ignore
import config
from askitsu import Client
from askitsu import InvalidArgument
from typing import List, Literal, Optional
from .queries import ENTRY_TITLE, QUERY_METHODS


class Object(askitsu.Object):
    def __init__(self, id: int, type: str = None, name: str = None, **kwargs) -> None:
        self.canonical_title = name
        self.subtype = kwargs.pop("subtype")
        super().__init__(id, type=type)


class KitsuClient(Client):
    def __init__(
        self,
        token: str = config.kitsu_token,
        *,
        session: Optional[aiohttp.ClientSession] = None,
        cache_expiration: int = config.askitsu_cache_expiration,
    ) -> None:
        super().__init__(token, session=session, cache_expiration=cache_expiration)

    async def __search_entry(
        self, type: str, query: str, limit: int, method: str
    ) -> Optional[List[Object]]:
        cache_res = await self.http._cache.get(f"{type}_{query.replace(' ', '_')}_{limit}")
        if cache_res:
            return cache_res.value
        variables = {"title": query, "limit": limit}
        query_fetch = ENTRY_TITLE.get(method)
        data = await self.http.post_data(
            data={"query": query_fetch, "variables": variables}
        )
        try:
            data["data"]
        except (KeyError, TypeError):
            return None
        if not data["data"][method]["nodes"]:
            return None
        fetched = [
            Object(
                attributes["id"],
                type,
                attributes["titles"]["canonical"],
                subtype=attributes[f"{type}sub"],
            )
            for attributes in data["data"][method]["nodes"]
        ]
        await self.http._cache.add(
            f"{type}_{query.replace(' ', '_')}_{limit}",
            fetched,
            remove_after=config.askitsu_cache_expiration,
        )
        return fetched

    async def search(
        self, type: Literal["anime", "manga"], query: str, limit: int = 10
    ) -> Optional[List[Object]]:
        type_lower = type.lower()
        try:
            method = QUERY_METHODS[f"{type_lower}_search"]
        except (KeyError, TypeError):
            raise InvalidArgument
        else:
            return await self.__search_entry(
                type=type_lower, query=query, limit=limit, method=method
            )

    async def search_anime(self, query: str, limit: int = 10) -> Optional[List[Object]]:
        return await self.search("anime", query=query, limit=limit)

    async def search_manga(self, query: str, limit: int = 10) -> Optional[List[Object]]:
        return await self.search("manga", query=query, limit=limit)