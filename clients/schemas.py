from ninja import Schema


class ClientSchema(Schema):
    id: int
    company_name: str
    first_name: str
    last_name: str
    position: str
    phone: str
    email: str
    website: str
    address: str
    city: str
    state: str
    zipcode: str


class ClientCreateSchema(Schema):
    company_name: str
    first_name: str
    last_name: str
    position: str
    phone: str
    email: str
    website: str
    address: str
    city: str
    state: str
    zipcode: str


class ClientUpdateSchema(Schema):
    company_name: str
    first_name: str
    last_name: str
    position: str
    phone: str
    email: str
    website: str
    address: str
    city: str
    state: str
    zipcode: str
