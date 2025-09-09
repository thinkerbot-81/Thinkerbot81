import mimetypes

def what(file_path):
    mime, _ = mimetypes.guess_type(file_path)
    if mime and mime.startswith("image/"):
        return mime.split("/")[-1]
    return None