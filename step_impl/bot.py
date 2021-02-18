from getgauge.python import before_suite
from step_impl.jira import Jira
import os

JIRA_BASE_URL = os.getenv("JIRA_BASE_URL")
JIRA_ADMIN_USERNAME = os.getenv("JIRA_ADMIN_USERNAME")
JIRA_ADMIN_PASSWORD = os.getenv("JIRA_ADMIN_PASSWORD")
INTERNAL_EMPLOYEE_USERNAME = os.getenv("INTERNAL_EMPLOYEE_USERNAME")
INTERNAL_EMPLOYEE_PASSWORD = os.getenv("INTERNAL_EMPLOYEE_PASSWORD")
INTERNAL_EMPLOYEES_GROUP = "jira-internal-employee_users"


class Bot(object):
    jira_admin = None
    internal_employee = None

    @before_suite
    def init(self):
        Bot.jira_admin = Jira(JIRA_BASE_URL, JIRA_ADMIN_USERNAME, JIRA_ADMIN_PASSWORD)
        Bot.internal_employee = Jira(
            JIRA_BASE_URL,
            INTERNAL_EMPLOYEE_USERNAME,
            INTERNAL_EMPLOYEE_PASSWORD,
        )
