import meilisearch
URL = 'http://localhost:7700'
CLIENT = meilisearch.Client(url=URL)


def conf():
    CLIENT.index('communities').update_settings({
        'displayedAttributes': [
            "id",
            "title",
            "slug",
            "parent",
            "parent_id",
            "lat",
            "lng"
        ]
    })
    CLIENT.index('communities').update_filterable_attributes([
        "is_del",
        "state",
        "id"
    ])
    CLIENT.index('communities').update_sortable_attributes([
        'title'
    ])
    CLIENT.index("communities").update_searchable_attributes([
        'title'
    ])
