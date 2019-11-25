#!/usr/bin/python3
import requests
import json


def get(url, headers):
    """
    :param url:
    :param headers:
    :return: returns a dictionary of the status, content and headers
    """

    try:
        api_response = requests.get(url=url, headers=headers)
        api_content = api_response.content
        print(" ")
        print("---------------------------------------------------")
        print("method get", api_response.status_code)
        print(url)
        response = {"response_code": api_response.status_code, "response_headers": api_response.headers}
        if api_response.status_code == 200:
            response["response_content"] = json.loads(api_response.content.decode('utf-8'))
            return response
        else:
            response["response_content"] = api_content
            return response
    except requests.exceptions.HTTPError:
        print('Oops. HTTP Error occured')


def patch(url, data, headers):

    try:
        api_data = requests.patch(url=url, data=data, headers=headers)
        print(" ")
        print("---------------------------------------------------")
        print("method patch", api_data.status_code)
        print("request data", data)
        print(url)
        try:
            api_content = json.loads(api_data.content.decode('utf-8'))

            response = {"response_code": api_data.status_code, "response_content": api_content, "response_headers": api_data.headers}
            return response
        except json.decoder.JSONDecodeError:
            print("the answer is not json", api_data)
            return
    except requests.exceptions.HTTPError:
        print('Oops. HTTP Error occured')


def put(url, data, headers):

    try:
        api_data = requests.put(url=url, data=data, headers=headers)
        print(" ")
        print("---------------------------------------------------")
        print("method put", api_data.status_code)
        print("request data", data)
        print(url)
        try:
            api_content = json.loads(api_data.content.decode('utf-8'))
            response = {"response_code": api_data.status_code, "response_content": api_content, "response_headers": api_data.headers}
            return response
        except json.decoder.JSONDecodeError:
            print("the answer is not json", api_data)
            return
    except requests.exceptions.HTTPError:
        print('Oops. HTTP Error occured')


def delete(url, headers):
    """
       :param url:
       :param headers:
       :return: returns a dictionary of the status, content and headers
    """
    try:
        api_data = requests.delete(url=url, headers=headers)
        print(" ")
        print("---------------------------------------------------")
        print("method delete", api_data.status_code)
        print(url)
        api_content = json.loads(api_data.content.decode('utf-8'))
        try:
            response = {"response_code": api_data.status_code, "response_content": api_content,
                        "response_headers": api_data.headers}
            return response
        except json.decoder.JSONDecodeError:
            print("the answer is not json", api_data)
            return
    except requests.exceptions.HTTPError:
        print('Oops. HTTP Error occured')


def post(url, data, headers):
    """
       :param url:
       :param headers:
       :param data
       :return: returns a dictionary of the status, content and headers    """

    try:
        api_data = requests.post(url=url, data=data, headers=headers)
        print(" ")
        print("---------------------------------------------------")
        print("method post", api_data.status_code)
        print("request", data)
        print(url)
        response = {"response_code": api_data.status_code, "response_content": api_data.content,
                    "response_headers": api_data.headers}
        try:
            api_content = json.loads(api_data.content.decode('utf-8'))
            response["response_content"] = api_content
            return response
        except json.decoder.JSONDecodeError:
            print("the answer is not json", api_data)
            return
    except requests.exceptions.HTTPError:
        print('Oops. HTTP Error occured')
