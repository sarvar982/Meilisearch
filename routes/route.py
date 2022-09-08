from fastapi import APIRouter
from core.config import CLIENT
from typing import Union
from fastapi import Query
from core.models import Item, Community


router = APIRouter(prefix="/api", tags=['search'])


@router.get("/")
async def make_search(search: Union[str, None] = Query(default=None,
                                                       min_length=2,
                                                       max_length=50)):
    response = CLIENT.index('communities').search(search, {
        'sort':['title:asc']
    })
    return response


@router.post("/create/docs/")
async def creation_of_docs(item: Item):
    item_dict = item.dict()
    response = CLIENT.index('communities').add_documents([item_dict])
    return response


# документы по одному индексу
@router.get("/documents/{index_title}")
async def get_docs(index_title: str):
    response = CLIENT.index(index_title).get_documents()
    return response


@router.post("/create")
async def creation_of_new_docs(doc: Community):
    doc_dict = doc.dict()
    doc_dict['_geo'] = doc_dict.pop('geo')
    response = CLIENT.index('communities').add_documents([doc_dict])
    return response


@router.put("/add/synonyms/")
async def insert_list_of_synonyms(sylist: dict):
    response = CLIENT.index('communities').update_synonyms(
        sylist
    )
    return response



