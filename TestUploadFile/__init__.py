import logging
from logging import FileHandler
from mimetypes import MimeTypes

import azure.functions as func
import mimetypes


def main(req: func.HttpRequest,context: func.Context) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    if req.method == "GET":
        filename = f"TestUploadFile/upload.html"
        with open(filename,"rb") as f:
            return func.HttpResponse(f.read(),mimetype='text/html')        

    if req.method == "POST":
        if req.files:
            try:
                fl = req.files.get("file")
            except ValueError:
                return func.HttpResponse(
                    "file not found."
                    ,status_code=200
                )
            
            #print(fl.filename)

            return func.HttpResponse(
                f"{fl.filename} uploaded."
                    + f"\n\nContent: \n{fl.read()}"
                ,status_code=200
            )
    
