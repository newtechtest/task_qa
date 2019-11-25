#!/usr/bin/python
import pytest
from faker import Faker
import api_methods


fake = Faker('en_US')
fake_title = fake.name().replace(" ", "")
fake_body = fake.text()

"  -----------------------------------------url START------------------------------"

url_api = "https://jsonplaceholder.typicode.com"


@pytest.fixture()
def url_posts():
    url = {"GET": f"{url_api}/posts/",
           "GET_FILTER": f"{url_api}/posts?",
           "POST": f"{url_api}/posts/",
           "PATCH": f"{url_api}/posts/",
           "PUT": f"{url_api}/posts/",
           "DELETE": f"{url_api}/posts/"}
    return url


@pytest.fixture()
def url_comments():
    url = {"GET": f"{url_api}/comments/",
           "POST": f"{url_api}/comments",
           "PATCH": f"{url_api}/comments",
           "PUT": f"{url_api}/comments/",
           "DELETE": f"{url_api}/comments"}
    return url


@pytest.fixture(params=[{"url": f"{url_api}/commentss"}, {"url": f"{url_api}/commen"}, {"url": f"{url_api}/comment"},
                        {"url": f"{url_api}/postss"}, {"url": f"{url_api}/post"}, {"url": f"{url_api}/osts"}])
def invalid_endpoint(request):
    return request.param


@pytest.fixture()
def post_format():
    post_format = {"title": None, "body": None, "userId": None}
    return post_format


@pytest.fixture()
def count_posts(url_posts, headers):
    response = api_methods.get(url=url_posts["GET"], headers=headers)
    number_of_posts = len(response["response_content"])
    return number_of_posts


@pytest.fixture()
def valid_post_data(url_posts, headers, post_format):
    response = api_methods.get(url=url_posts["GET"], headers=headers)
    try:
        user_id = response["response_content"][0]["userId"]
        post_format["userId"] = user_id
        post_format["title"] = fake_title
        post_format["body"] = fake_body
        return post_format
    except KeyError:
        print("userId not found")
        return post_format


@pytest.fixture(params=[0, -1, None, [], {}, " "])
def invalid_post_id(request):
    return request.param


@pytest.fixture(params=[{"title": fake_title, "body": fake_body, "userId": -1},
                        {"title": fake_title, "body": fake_body, "userId": None},
                        {"title": fake_title, "body": fake_body, "userId": " "},
                        {"title": fake_title, "body": 1, "userId": 1},
                        {"title": fake_title, "body": None, "userId": 1},
                        {"title": 1, "body": fake_body, "userId": 1},
                        {"title": None, "body": fake_body, "userId": 1},
                        {"title": fake_title},
                        {"body": fake_body},
                        {"userId": 1},
                        {" ": " "},
                        {}])
def invalid_post_data(request):
    return request.param


@pytest.fixture()
def headers():
    api_headers = {"Content-type": "application/json; charset=UTF-8"}
    return api_headers


@pytest.fixture()
def expect_code():
    status_code = {"OK": 200,
                   "Created": 201,
                   "Not_Modified": 304,
                   "Bad_Request": 400,
                   "Unauthorized": 401,
                   "Not_Found": 404,
                   "Not_Acceptable": 406,
                   "Conflict": 409,
                   "Internal_Server_Error": 500}
    return status_code
