# tutorial.md — Using IDSA shared workflows

## Overview

This package is meant to be committed into:
`https://github.com/International-Data-Spaces-Association/.github`

It provides:

- PR checks: markdown lint (blocking), lychee link check (non-blocking), cspell (non-blocking)
- Release export: build PDF/DOCX from GitBook-style SUMMARY.md with pandoc; upload as release assets

## Consumer repo setup

1. Add two caller workflows from `examples/consumer-repo`.
2. Set repo variables:
   - CONTENT_DIR (e.g., docs)
   - SUMMARY_PATH (e.g., docs/SUMMARY.md)
3. Configure branch protection for `main`:
   - Require PR
   - Require 2 approvals
   - Include admins
   - Require status checks: only `markdown_lint` initially

## Central assets to replace

Replace these with the Knowledge Base versions:

- assets/markdownlint/.markdownlint.jsonc
- assets/lychee/lychee.toml
- assets/reference.docx
