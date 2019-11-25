import api_methods
import random
import json


def test_api_invalid_endpoint(invalid_endpoint, headers, expect_code):
    response = api_methods.get(url=invalid_endpoint["url"], headers=headers)
    assert response["response_code"] == expect_code["Not_Found"]


def test_get_all_posts(url_posts, headers, expect_code):
    response = api_methods.get(url=url_posts["GET"], headers=headers)
    list_posts = response["response_content"]
    assert response["response_code"] == expect_code["OK"]
    assert type(list_posts) == list


def test_response_data_type(count_posts, url_posts, headers, post_format):
    url = url_posts["GET"] + str(count_posts)
    response = api_methods.get(url=url, headers=headers)
    assert type(response["response_content"]["id"]) == int
    assert type(response["response_content"]["title"]) == str
    assert type(response["response_content"]["body"]) == str
    assert response["response_content"]["id"] == count_posts


def test_check_rows_in_posts(count_posts, url_posts, headers, valid_post_data):
    random_id = random.randint(1, count_posts)
    url = url_posts["GET"] + str(random_id)
    current_post = api_methods.get(url=url, headers=headers)
    post = current_post["response_content"]
    for row in valid_post_data.keys():
        assert row in post
    assert current_post["response_content"]["id"] == random_id


def test_get_posts_for_user_id(url_posts, headers, valid_post_data):
    user_id = valid_post_data['userId']
    url = url_posts["GET_FILTER"] + f"userId={user_id}"
    response = api_methods.get(url=url, headers=headers)
    for post in response["response_content"]:
        assert post["userId"] == user_id


def test_get_post_more_last_id(count_posts, url_posts, headers, expect_code):
    url = url_posts["GET"] + str(count_posts + 1)
    current_post = api_methods.get(url=url, headers=headers)
    assert current_post["response_code"] == expect_code["Not_Found"]


def test_get_post_invalid_id(url_posts, headers, invalid_post_id, expect_code):
    url = url_posts["GET"] + str(invalid_post_id)
    current_post = api_methods.get(url=url, headers=headers)
    assert current_post["response_code"] == expect_code["Not_Found"]


def test_method_post(url_posts, valid_post_data, headers, expect_code):
    response = api_methods.post(url=url_posts["POST"], data=json.dumps(valid_post_data), headers=headers)
    assert response["response_code"] == expect_code["Created"]


def test_post_invalid_data(url_posts, invalid_post_data, headers, expect_code):
    response = api_methods.post(url=url_posts["POST"], data=json.dumps(invalid_post_data), headers=headers)
    assert response["response_code"] == expect_code["Bad_Request"]


def test_delete_random_post(url_posts, headers, expect_code, count_posts):
    post_id = str(random.randint(1, count_posts))
    response_post = api_methods.delete(url=url_posts["DELETE"] + post_id, headers=headers)
    assert response_post["response_code"] == expect_code["OK"]
    response_get = api_methods.get(url_posts["GET"] + post_id, headers)
    assert response_get["response_code"] == expect_code["Not_Found"]


def test_delete_post_invalid_id(url_posts, headers, expect_code, invalid_post_id):
    post_id = str(invalid_post_id)
    response = api_methods.delete(url=url_posts["DELETE"] + post_id, headers=headers)
    assert response["response_code"] == expect_code["Not_Found"]


def test_put_random_post(url_posts, count_posts, valid_post_data, headers, expect_code):
    post_id = str(random.randint(1, count_posts))
    valid_post_data["id"] = post_id
    response = api_methods.put(url_posts["PUT"] + post_id, data=json.dumps(valid_post_data), headers=headers)
    assert response["response_code"] == expect_code["OK"]


def test_put_post_invalid_id(url_posts, headers, expect_code, invalid_post_id, valid_post_data):
    post_id = str(invalid_post_id)
    valid_post_data["id"] = post_id
    response = api_methods.put(url=url_posts["PUT"] + post_id, data=json.dumps(valid_post_data), headers=headers)
    assert response["response_code"] == expect_code["Not_Found"]


def test_patch_random_post(url_posts, count_posts, valid_post_data, headers, expect_code):
    post_id = str(random.randint(1, count_posts))
    data = {"title": valid_post_data["title"]}
    response = api_methods.patch(url=url_posts["PATCH"] + post_id, data=json.dumps(data), headers=headers)
    post = response["response_content"]
    assert post["title"] == data["title"]
    response_get = api_methods.get(url_posts["GET"] + post_id, headers)
    assert response_get["response_content"]["title"] == data["title"]
    assert response["response_code"] == expect_code["OK"]


def test_patch_post_invalid_id(url_posts, invalid_post_id, valid_post_data, headers, expect_code):
    post_id = str(invalid_post_id)
    data = {"title": valid_post_data["title"]}
    response = api_methods.patch(url=url_posts["PATCH"] + post_id, data=json.dumps(data), headers=headers)
    assert response["response_code"] == expect_code["Not_Found"]
