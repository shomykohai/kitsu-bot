OBJECT_QUERY_ANIME = """
        query animeByTitle($title: String!, $limit: Int) {
            searchAnimeByTitle(first: $limit, title: $title) {
            nodes {
                id
                animesub: subtype
                titles{
                    canonical
                }
            }
            }
        }
"""

OBJECT_QUERY_MANGA = """
        query mangaByTitle($title: String!, $limit: Int) {
            searchMangaByTitle(first: $limit, title: $title) {
            nodes {
                id
                mangasub: subtype
                titles{
                    canonical
                }
            }
            }
        }
"""

ENTRY_TITLE = {
    "searchAnimeByTitle": OBJECT_QUERY_ANIME,
    "searchMangaByTitle": OBJECT_QUERY_MANGA,
}

QUERY_METHODS = {
    "anime_search": "searchAnimeByTitle",
    "manga_search": "searchMangaByTitle",
}