import sys
import re

COMMIT_MSG_REGEX = r'^(feat|fix|docs|style|refactor|perf|test|chore|build|ci|revert|merge)(\(.+\))?: .{1,50}'

def main():
    commit_msg_filepath = sys.argv[1]
    with open(commit_msg_filepath, 'r') as file:
        commit_msg = file.read().strip()

    if not re.match(COMMIT_MSG_REGEX, commit_msg):
        print(f"Commit message '{commit_msg}' does not match the required format.")
        print("Format: <type>(<scope>): <subject>")
        print("Example: feat(parser): add ability to parse arrays")
        sys.exit(1)

if __name__ == '__main__':
    raise SystemExit(main())