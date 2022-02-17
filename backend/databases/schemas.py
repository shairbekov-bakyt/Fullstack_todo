import pydantic as _pydantic

class TodoRequest(_pydantic.BaseModel):
    title  : str
    description : str
    completed : bool 