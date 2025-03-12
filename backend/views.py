import json
import logging
from http import HTTPStatus

from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView

from backend.src import translate

logger = logging.getLogger("django")


@method_decorator(csrf_exempt, name="dispatch")
class NumToEnglishView(APIView):

    @swagger_auto_schema(
        operation_id="num_to_english",
        manual_parameters=[
            openapi.Parameter(
                "number",
                openapi.IN_QUERY,
                description="Positive integer number to be converted to English word",
                type=openapi.TYPE_STRING,
                required=True,
            ),
        ],
        responses={
            HTTPStatus.OK: "Success",
            HTTPStatus.BAD_REQUEST: "Invalid number",
        },
    )
    def get(self, request):
        logger.info(request)
        number = request.GET.get("number", "")
        return self.process_request(number)

    @swagger_auto_schema(
        operation_id="num_to_english",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "number": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="Positive integer number to be converted to English word",
                    exmaple="123",
                ),
            },
            required=["number"],
        ),
        responses={
            HTTPStatus.OK: "Success",
            HTTPStatus.BAD_REQUEST: "Invalid number or payload",
        },
    )
    def post(self, request):
        logger.info(request)
        logger.info(request.body)
        try:
            data = json.loads(request.body)
            number = data.get("number", "")
        except json.JSONDecodeError:
            logger.error(f"Invalid payload: {request.body}")
            return JsonResponse(
                {
                    "status": "error",
                    "message": "Invalid payload!",
                },
                status=HTTPStatus.BAD_REQUEST,
            )
        return self.process_request(number)

    def process_request(self, number):
        try:
            num_in_english = translate(number)
        except ValueError as e:
            logger.error(f"Invalid number: {number}")
            return JsonResponse(
                {
                    "status": "error",
                    "message": str(e),
                },
                status=HTTPStatus.BAD_REQUEST,
            )
        return JsonResponse(
            {
                "status": "ok",
                "num_in_english": num_in_english,
            },
            status=HTTPStatus.OK,
        )
