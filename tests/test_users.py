from http import HTTPStatus
from libs.common.Assertion import Assertion
from libs.userapi.UserApi import UserApi


def TestCase_01_verify_user_can_be_created_rest_post_api_call():

    response = UserApi().create_user("Gurudatt", "SDET Engineer")
    response_status_code = response.get("status_code")
    response_body = response.get("response_body")
    Assertion.assert_equal(response_status_code, HTTPStatus.CREATED,
                           "Failed: API failed to respond with correct status code")
    Assertion.assert_equal(response_body.get("name"), "Gurudatt",
                           "Failed: Name in the response does not match with expected value")
    Assertion.assert_equal(response_body.get("job") ,"SDET Engineer",
                            "Failed: Job information in the response does not match with expected value")

def TestCase_02_Verify_user_can_be_updated_rest_put_api_call():

    response = UserApi().update_user(2,"guru","SDET")
    response_status_code = response.get("status_code")
    response_body = response.get("response_body")
    Assertion.assert_equal(response_status_code, HTTPStatus.OK,
                           "Failed: API failed to respond with correct status code")

def TestCase_03_Verify_user_can_be_fetched_using_rest_get_api_call():

    response = UserApi().get_user_by_id(2)
    response_status_code = response.get("status_code")
    response_body = response.get("response_body")

    Assertion.assert_equal(response_status_code, HTTPStatus.OK,
                           "Failed: API did not respond with correct status code")
    Assertion.assert_equal(response_body.get('data').get('email') , "janet.weaver@reqres.in",
                           "Failed: Expected user email does not match the actual")
    Assertion.assert_equal(response_body.get('data').get('first_name'), 'Janet',
                           "Failed: Expected first name does not match the actual")
    Assertion.assert_equal(response_body.get('data').get('last_name'), 'Weaver',
                           "Failed: Expected last name does not match the actual")


def TestCase_04_Verify_user_can_be_deleted_using_rest_delete_api_call():

    response = UserApi().delete_user(2)
    response_status_code = response.get("status_code")
    Assertion.assert_equal(response_status_code , HTTPStatus.NO_CONTENT,
                           "Failed: API did not respond with correct status code")


