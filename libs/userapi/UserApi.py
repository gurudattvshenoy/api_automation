from libs.common.ApiHelper import ApiHelper
from libs.common.Logger import logger
from libs.common.ExecTime import exec_log

class UserApi:
    """ Helper function for User CRUD operation """
    def __init__(self):
        self.api_object = ApiHelper()
        self.end_point = "users/"

    @exec_log
    def create_user(self, name, job):
        """
        Creates the user using POST call to endpoint based on name and job input
        """
        payload = {
            "name": name,
            "job": job
         }
        logger.debug("Attempting to create user with payload {}".format(payload))
        return self.api_object.post(self.end_point, json_obj=payload)

    @exec_log
    def update_user(self, id, name, job):
        """
        Updates the user info. using PUT call to endpoint based on input name and job
        """
        payload = {
                "name": name,
                "job": job
            }
        logger.debug("Attempting to update user {} using payload {}".format(id,payload))
        return self.api_object.put(self.end_point+'{}'.format(id),payload)

    @exec_log
    def delete_user(self, id):
        """
        Deletes the user info. based on input id
        """
        logger.debug("Attempting to delete user with id - {} ".format(id))
        return self.api_object.delete(self.end_point+"{}".format(id))

    @exec_log
    def get_all_users(self):
        """
        Fetches all the users in the system
        """
        logger.debug("Attempting to fetch all the users ")
        return self.api_object.get("users")

    @exec_log
    def get_user_by_id(self, id):
        """
        Gets the user information based on id
        """
        logger.debug("Fetching user id - {} ".format(id))
        return self.api_object.get(self.end_point + "{}".format(id))

    @exec_log
    def is_email_present(self, email):
        """
        Confirms whether email address is present in application
        """
        resp = self.api_object.get("users")
        logger.debug("Checking if email {} is present?".format(email))
        for record in resp.get("response_body").get('data'):
            if record.get('email') == email.strip():
                logger.debug("Email address {} is present".format(email))
                return True
        logger.debug("Email address {} is NOT present".format(email))
        return False

    @exec_log
    def is_first_name_present(self, first_name):
        """
        Confirms whether first name is present in application
        """
        resp = self.api_object.get("users")
        logger.debug("Checking if first name {} is present?".format(first_name))
        for record in resp.get("response_body").get('data'):
            if record.get('first_name') == first_name.strip():
                logger.debug("First name {} is present".format(first_name))
                return True
        logger.debug("First name {} is NOT present".format(first_name))
        return False

    @exec_log
    def is_last_name_present(self, last_name):
        """
        Confirms whether last name is present in application
        """
        resp = self.api_object.get("users")
        logger.debug("Checking if last name {} is present?".format(last_name))
        for record in resp.get("response_body").get('data'):
            if record.get('last_name') == last_name.strip():
                logger.debug("Last name {} is present".format(last_name))
                return True
        logger.debug("Last name {} is NOT present".format(last_name))
        return False

