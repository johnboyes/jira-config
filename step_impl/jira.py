from jira import JIRA


class Jira:
    def __init__(self, base_url, username, password):
        self.jira = JIRA(
            auth=(username, password),
            options={"server": base_url},
        )
        self.username = username

    def has_group(self, group_name):
        return len(self.jira.group_members(group_name)) >= 0

    def projects(self):
        return self.jira.projects()

    def is_user_in_group(self, user, group):
        group_members = self.jira.group_members(group)
        return bool([emp for emp in group_members.values() if (emp["name"] == user)])
