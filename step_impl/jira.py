from jira import JIRA
import os


class Jira:
    def __init__(self, username, password):
        self.jira = JIRA(
            auth=(username, password),
            options={"server": os.getenv("JIRA_BASE_URL")},
        )

    def has_group(self, group_name):
        return len(self.jira.group_members(group_name)) >= 0

    def projects(self):
        return self.jira.projects()

    def is_internal_employee_in_internal_employees_group(self):
        internal_employees = self.jira.group_members("jira-internal-employee_users")
        return bool(
            [
                emp
                for emp in internal_employees.values()
                if (emp["name"] == os.getenv("INTERNAL_EMPLOYEE_USERNAME"))
            ]
        )
