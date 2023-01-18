from pydantic import BaseModel


class StatefunTimeCreateRequest(BaseModel):
    time_ns: int
    type_timer: str
    type_test_case: str
