import subprocess

def add_pushurl(user_name, github_repo_name, gitbook_repo_name):
    """Add GitHub pushurl & Gitbook pushurl to remote origin in file .git/config"""

    github_repo_url = "https://github.com/{name}/{repo}.git".format(name=user_name, repo=github_repo_name)
    gitbook_repo_url = "https://git.gitbook.com/{name}/{repo}.git".format(name=user_name, repo=gitbook_repo_name)

    # add pushurl to git remote origin using shell command
    subprocess.call("git remote set-url --add --push origin "+github_repo_url, shell=True)
    print "> Add pushurl {} to remote origin".format(github_repo_url)
    subprocess.call("git remote set-url --add --push origin "+gitbook_repo_url, shell=True)
    print "> Add pushurl {} to remote origin".format(gitbook_repo_url)
    print "> Mission Complete"

if __name__ == "__main__":
    name_input = raw_input("Please enter your name for GitHub & Gitbook.\n>>>")

    prompt_github = "Please enter the name of your GitHub repo.\nif it's 'OMOOC2py', just hit enter.\n>>>"
    github_repo_name_input = raw_input(prompt_github)
    if not github_repo_name_input: github_repo_name_input = "OMOOC2py"

    prompt_gitbook = "Please enter the name of your Gitbook repo.\nif it's 'OMOOC2py', just hit enter.\n>>>"
    gitbook_repo_name_input = raw_input(prompt_gitbook)
    if not gitbook_repo_name_input: gitbook_repo_name_input = "OMOOC2py"

    add_pushurl(name_input, github_repo_name_input, gitbook_repo_name_input)

