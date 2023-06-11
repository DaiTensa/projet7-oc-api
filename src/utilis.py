import dill
import requests
import io

########################################SERVER##########################################################################
def load_object(url_path):
    response = requests.get(url_path)
    content = response.content
    return dill.load(io.BytesIO(content))


########################################LOCAL##########################################################################
# def load_object(url_path):
#     with open(url_path, "rb") as file_obj:
#         return dill.load(file_obj)

