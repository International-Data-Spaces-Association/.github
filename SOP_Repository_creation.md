# SOP — New repo setup (IDSA)

## Mandatory content
- README.md
- LICENSE.md (usually CC BY 4.0)
- CODE_OF_CONDUCT.md
- CONTRIBUTING.md

## Workflows
Add caller workflows:
- .github/workflows/pr.yml
- .github/workflows/release.yml

## Repo variables
- CONTENT_DIR
- SUMMARY_PATH

## Branch protection (`main`)
- Require PR before merging
- Require **2** approvals
- Dismiss stale approvals
- Include administrators
- Require linear history
- Block force pushes & deletions
- Required status checks: markdown_lint
- Optional informational checks: link_check, spell_check
