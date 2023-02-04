class UploadCache:
    # list containing all the tasks
    tasks = []
    # list containing all the fileId of the upload tasks in the database
    files = []

    def create_upload(self, filename, fileId, filepath, socketAddress) -> None:
        """Function to add upload taskt to the upload cache

        Args:
            task (_dict__):
            {
                'filename':'name of the file being uploaded',
                 'fileId': 'id of the file in the client upload database',
                'filepath': 'path of the file on the client',
                'socketAddress': 'socket address where the file is upoaded to',
                'bytes': 'list containing bytes that are uploaded not added initially'
            }
        """
        upload_dict = {}
        upload_dict["filename"] = filename
        upload_dict["fileId"] = fileId
        upload_dict["filepath"] = filepath
        upload_dict["socketAddress"] = socketAddress
        bytes_list = []
        upload_dict["bytes"] = bytes_list
        self.__class__.tasks.append(upload_dict)
        self.__class__.files.append(fileId)

    def add_bytes(self, data_bytes) -> None:
        pass
