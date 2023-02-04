import json
from channels.generic.websocket import WebsocketConsumer
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async

# from .models import FileReceive, FileSend
# from .models import FileSend
import ast
import asyncio


class FileReceiveSocket(AsyncConsumer):
    async def websocket_connect(self, event):
        # get all the keyword arguments
        self.userId = self.scope["url_route"]["kwargs"]["userId"]
        self.fileId = self.scope["url_route"]["kwargs"]["fileId"]
        self.pointer = self.scope["url_route"]["kwargs"]["pointer"]
        # is_user_valid = self.validate_user(self.userId)
        # if is_user_valid:
        #     pass
        # else:
        #     await self.send({"type": "websocket.disconnect"})

    async def websocket_receive(self, event):
        # nitiate the file receieve from a http put request
        # create a filesend with pointer 0 and also create
        # an empty file with userId_fileId
        # containing a list string
        # then pass the socket link and continue from there
        print(event["text"])
        # filepath = f"filereceive/{self.userId}_{self.fileId}.txt"
        # # open the file in append mode
        # with open(filepath, "a") as fr:
        #     data = json.loads(event["text"])
        #     chunk = data["data"]
        #    fr.write(f"{chunk}\n")

    async def websocket_disconnect(self, event):
        self.send({"type": "websocket.disconnect"})

    # @database_sync_to_async
    # def validate_user(self, id):
    #     # if the user exists in the database return true
    #     # else return false
    #     if Account.objects.filter(pk=id).exists():
    #         return True
    #     else:
    #         return False

    @database_sync_to_async
    def increment_pointer(self, fileId):
        pass

    @database_sync_to_async
    def unpack_data(self, filepath):
        # This function is responsible for doing the following
        # reading the bytes line by line from the filepath
        # converting the bytes string into json
        # saving the questions and answers one after the other into the database
        pass
