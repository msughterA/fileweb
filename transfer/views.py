from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import os


MEDIA_DIR = ""
FILE_SEND_COLLECTION = os.path.join(MEDIA_DIR, "filesend/collections")
FILE_SEND_QUESTION_AND_ANSWER = os.path.join(MEDIA_DIR, "filesend/questionAndAnswer")
FILE_RECEIVE_COLLECTION = os.path.join(MEDIA_DIR, "filereceive/collections")
FILE_RECEIVE_QUESTION_AND_ANSWER = os.path.join(
    MEDIA_DIR, "filereceive/questionAndAnswer"
)


# Create your views here.
# class FileReceiveView(APIView):
#     def post(self, request):
#         filetype = request.data["type"]
#         fileId = request.data["fileId"]
#         userId = request.data["userId"]
#         deviceId = request.data["deviceId"]

#         if filetype == "collection":
#             # create a file at media/filereceive/collections/userId_fileId.json
#             filepath = os.path.join(
#                 FILE_RECEIVE_COLLECTION, f"{userId}_{deviceId}_{fileId}.json"
#             )
#             with open(filepath, "w") as f:
#                 print("json send file created")

#         else:
#             # create a file at media/filereceive/collections/userId_fileId.json
#             filepath = os.path.join(
#                 FILE_RECEIVE_QUESTION_AND_ANSWER, f"{userId}_{deviceId}_{fileId}.json"
#             )
#             with open(filepath, "w") as f:
#                 print("json reception file created")
#         return Response(
#             {
#                 "message": "success",
#                 "data": {"socket": f"ws/filereceive/{userId}/{deviceId}/{fileId}"},
#             },
#             status=status.HTTP_200_OK,
#         )


class FileReceiveView(APIView):
    def post(self, request):
        filetype = request.data["type"]
        fileId = request.data["filename"]
        userId = request.data["userId"]
        deviceId = request.data["deviceId"]

        if filetype == "collection":
            # create a file at media/filereceive/collections/userId_fileId.json
            filepath = os.path.join(
                FILE_RECEIVE_COLLECTION, f"{userId}_{deviceId}_{fileId}.json"
            )
            with open(filepath, "w") as f:
                print("json send file created")

        else:
            # create a file at media/filereceive/collections/userId_fileId.json
            filepath = os.path.join(
                FILE_RECEIVE_QUESTION_AND_ANSWER, f"{userId}_{deviceId}_{fileId}.json"
            )
            with open(filepath, "w") as f:
                print("json reception file created")
        return Response(
            {
                "message": "success",
                "data": {"socket": f"ws/filereceive/{userId}/{deviceId}/{fileId}"},
            },
            status=status.HTTP_200_OK,
        )
