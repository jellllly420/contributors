"""This module contains the functions needed to write the output to markdown files."""


def write_to_markdown(collaborators, filename, start_date, end_date):
    """
    This function writes a list of collaborators to a markdown file in table format.
    Each collaborator is represented as a dictionary with keys 'username', 'contribution_count', 'new_contributor', and 'commits'.

    Args:
        collaborators (list): A list of dictionaries, where each dictionary represents a collaborator.
                              Each dictionary should have the keys 'username', 'contribution_count', and 'commits'.
        filename (str): The path of the markdown file to which the table will be written.

    """
    if start_date and end_date:
        headers = "| Username | Contribution Count | New Contributor | Commits |\n| --- | --- | --- | --- |\n"
    else:
        headers = "| Username | Contribution Count | Commits |\n| --- | --- | --- |\n"

    table = headers

    for repo in collaborators:
        for collaborator in repo:
            username = collaborator.username
            contribution_count = collaborator.contribution_count
            commit_url = collaborator.commit_url
            new_contributor = collaborator.new_contributor

            if start_date and end_date:
                row = f"| {username} | {contribution_count} | {new_contributor} | {commit_url} |\n"
            else:
                row = f"| {username} | {contribution_count} | {commit_url} |\n"

            table += row

    with open(filename, "w", encoding="utf-8") as markdown_file:
        markdown_file.write("# Contributors\n\n")
        markdown_file.write(table)
        markdown_file.write(
            "\n _this file was generated by the [Contributors GitHub Action](https://github.com/github/contributors)\n"
        )
