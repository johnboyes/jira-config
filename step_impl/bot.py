from getgauge.python import before_suite
from step_impl.jira import Jira
import os


class Bot(object):
    jira_admin = None
    internal_employee = None

    @before_suite
    def init(self):
        Bot.jira_admin = Jira(
            os.getenv("JIRA_ADMIN_USERNAME"), os.getenv("JIRA_ADMIN_PASSWORD")
        )
        Bot.internal_employee = Jira(
            os.getenv("INTERNAL_EMPLOYEE_USERNAME"),
            os.getenv("INTERNAL_EMPLOYEE_PASSWORD"),
        )
