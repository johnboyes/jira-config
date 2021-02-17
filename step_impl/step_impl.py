from getgauge.python import step
from step_impl.bot import Bot, INTERNAL_EMPLOYEES_GROUP


@step("An internal employee can see all projects")
def an_internal_employee_can_see_all_projects():
    assert len(Bot.internal_employee.projects()) == len(Bot.jira_admin.projects())


@step("An internal employee is a member of the internal employees group")
def an_internal_employee_is_a_member_of_the_internal_employees_group():
    assert Bot.jira_admin.is_user_in_group(
        Bot.internal_employee.username, INTERNAL_EMPLOYEES_GROUP
    )


@step("There is a jira-internal-employee-users group")
def there_is_a_jira_internal_employee_users_group():
    assert Bot.jira_admin.has_group(INTERNAL_EMPLOYEES_GROUP)


@step("Not implemented yet")
def not_implemented_yet():
    assert False, "Add implementation code"
