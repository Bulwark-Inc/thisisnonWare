from storages.backends.gcloud import GoogleCloudStorage

class StaticStorage(GoogleCloudStorage):
    bucket_name = "nonware-demo-backend-static"
    location = "static"
    querystring_auth = False

class MediaStorage(GoogleCloudStorage):
    bucket_name = "nonware-demo-backend-media"
    location = "media"
    querystring_auth = False