from getgauge.python import step, before_scenario, Messages
from jira import JIRA
import os


def jira_admin():
    return jira(os.getenv("JIRA_ADMIN_USERNAME"), os.getenv("JIRA_ADMIN_PASSWORD"))


def internal_employee():
    return jira(
        os.getenv("INTERNAL_EMPLOYEE_USERNAME"), os.getenv("INTERNAL_EMPLOYEE_PASSWORD")
    )


def jira(username, password):
    return JIRA(
        auth=(username, password),
        options={"server": os.getenv("JIRA_BASE_URL")},
    )


def is_group(group_name):
    return len(jira_admin().group_members(group_name)) >= 0


def is_internal_employee_in_internal_employees_group():
    internal_employees = jira_admin().group_members("jira-internal-employee_users")
    return bool(
        [
            emp
            for emp in internal_employees.values()
            if (emp["name"] == os.getenv("INTERNAL_EMPLOYEE_USERNAME"))
        ]
    )


@step("An internal employee can see all projects")
def an_internal_employee_can_see_all_projects():
    assert len(jira_admin().projects()) == len(internal_employee().projects())


@step("An internal employee is a member of the internal employees group")
def an_internal_employee_is_a_member_of_the_internal_employees_group():
    assert is_internal_employee_in_internal_employees_group()


@step("There is a jira-internal-employee-users group")
def there_is_a_jira_internal_employee_users_group():
    assert is_group("jira-internal-employee_users")


@step("Not implemented yet")
def not_implemented_yet():
    assert False, "Add implementation code"
