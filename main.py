import argparse
from helvers.github import get_github_repositories, json_parser
from helvers.writter_csv import writefile

parser = argparse.ArgumentParser()
parser.add_argument("-q", dest="query")
parser.add_argument("-p", dest="page")
parser.add_argument("-pr", dest="per_page")


args = parser.parse_args()

story = get_github_repositories(args.query, args.page, args.per_page)
repositories = json_parser(story)
writefile(repositories)
print("Done!")