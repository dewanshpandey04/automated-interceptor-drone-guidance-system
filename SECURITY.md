# Security and Repository Hygiene

This repository is intentionally public.

Do not commit:

- API keys, tokens, passwords, SSH keys, or private certificates
- camera usernames/passwords or private stream URLs
- customer or company data
- private datasets or footage
- proprietary trained model weights
- internal network addresses or deployment secrets
- proprietary company source code

If a secret is committed accidentally, revoke it immediately and remove it from Git history rather than only deleting it in a later commit.
