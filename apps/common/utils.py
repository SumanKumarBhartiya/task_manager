from rest_framework.response import Response


def api_response(
    data=None,
    message="Success",
    status_code=200,
):

    return Response(
        {
            "success": True,
            "message": message,
            "data": data,
        },
        status=status_code,
    )