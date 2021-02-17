from getgauge.python import step
from step_impl.jira import Jira
import os


def jira_admin():
    return Jira(os.getenv("JIRA_ADMIN_USERNAME"), os.getenv("JIRA_ADMIN_PASSWORD"))


def internal_employee():
    return Jira(
        os.getenv("INTERNAL_EMPLOYEE_USERNAME"), os.getenv("INTERNAL_EMPLOYEE_PASSWORD")
    )


@step("An internal employee can see all projects")
def an_internal_employee_can_see_all_projects():
    assert len(jira_admin().projects()) == len(internal_employee().projects())


@step("An internal employee is a member of the internal employees group")
def an_internal_employee_is_a_member_of_the_internal_employees_group():
    assert jira_admin().is_internal_employee_in_internal_employees_group()


@step("There is a jira-internal-employee-users group")
def there_is_a_jira_internal_employee_users_group():
    assert jira_admin().has_group("jira-internal-employee_users")


@step("Not implemented yet")
def not_implemented_yet():
    assert False, "Add implementation code"
