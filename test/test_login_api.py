# coding: utf-8

"""
    dream3d

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest

import dream3d
from dream3d.api.login_api import LoginApi  # noqa: E501
from dream3d.rest import ApiException


class TestLoginApi(unittest.TestCase):
    """LoginApi unit test stubs"""

    def setUp(self):
        self.api = dream3d.api.login_api.LoginApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_login_access_token_api_v1_login_access_token_post(self):
        """Test case for login_access_token_api_v1_login_access_token_post

        Login Access Token  # noqa: E501
        """
        pass

    def test_reset_password_email_api_v1_login_reset_password_email_post(self):
        """Test case for reset_password_email_api_v1_login_reset_password_email_post

        Reset Password Email  # noqa: E501
        """
        pass

    def test_test_token_api_v1_login_test_token_post(self):
        """Test case for test_token_api_v1_login_test_token_post

        Test Token  # noqa: E501
        """
        pass

    def test_update_credentials_api_v1_login_me_put(self):
        """Test case for update_credentials_api_v1_login_me_put

        Update Credentials  # noqa: E501
        """
        pass

    def test_update_password_api_v1_login_update_password_put(self):
        """Test case for update_password_api_v1_login_update_password_put

        Update Password  # noqa: E501
        """
        pass

    def test_validate_password_reset_token_api_v1_login_validate_password_reset_token_post(self):
        """Test case for validate_password_reset_token_api_v1_login_validate_password_reset_token_post

        Validate Password Reset Token  # noqa: E501
        """
        pass

    def test_verify_phone_api_v1_login_verify_phone_post(self):
        """Test case for verify_phone_api_v1_login_verify_phone_post

        Verify Phone  # noqa: E501
        """
        pass

    def test_verify_phone_code_api_v1_login_verify_phone_code_post(self):
        """Test case for verify_phone_code_api_v1_login_verify_phone_code_post

        Verify Phone Code  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
