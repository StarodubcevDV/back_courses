from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.exceptions import ValidationException
from transport.sanic.base import SanicEndpoint


class BaseEndpoint(SanicEndpoint):

    async def _method(self, request: Request, body: dict, *args, **kwargs) -> BaseHTTPResponse:

        database = self.context.database
        session = database.make_session()

        try:
            return await super()._method(request, body,session, *args, **kwargs)
        except ValidationException as e:
            return await self.make_response_json(status=e.status_code, message=str(e))
