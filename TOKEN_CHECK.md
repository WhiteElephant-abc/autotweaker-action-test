# GitHub Token Availability Check

Investigated on the GitHub Actions runner (`run-34673318069`) to determine
whether the agent process can obtain a usable GitHub token.

## Conclusion

**No. The GitHub token is not reachable from the agent's environment.**

None of the checked surfaces expose `GITHUB_TOKEN` or any equivalent
credential. This appears to be intentional: the workflow is written to keep the
token away from the agent step.

## Evidence

### 1. Environment variables

`env` was dumped in full (127 variables). Relevant results:

| Check | Result |
| --- | --- |
| `GITHUB_TOKEN` | UNSET |
| `ACTIONS_RUNTIME_TOKEN` | UNSET |
| `ACTIONS_ID_TOKEN_REQUEST_TOKEN` | UNSET |
| `GH_TOKEN` | UNSET |
| Any var matching `token`/`secret`/`passw`/`cred` | None (only `INPUT_PROMPT`, which merely contains the word "token" in the task text) |

The environment does contain `INPUT_API_KEY` (`sk-...`), which is the
AUTOTWEAKER/DeepSeek API key passed into the action — **not** a GitHub token.
It is a live secret and is visible to the agent, but it grants no GitHub access.

Other `GITHUB_*` variables (`GITHUB_REPOSITORY`, `GITHUB_SHA`, `GITHUB_REF`,
`GITHUB_ACTOR`, etc.) are metadata only; none are credentials.

### 2. `git config`

- `git config --list --show-origin`: only `/etc/gitconfig` (safe.directory,
  LFS filters) and `.git/config` (remote URL, fetch refspec, branch tracking).
- No `credential.helper` configured (`git config --get credential.helper` -> exit 1).
- No `http.*` entries at all, in particular no `http.https://github.com/.extraheader`
  (`git config --local --get-regexp http` -> exit 1).
- `~/.gitconfig` / `~/.config/git` do not exist, so no global credentials.

### 3. `.git/config`

```
[core]
	repositoryformatversion = 0
	filemode = true
	bare = false
	logallrefupdates = true
[remote "origin"]
	url = https://github.com/WhiteElephant-abc/autotweaker-action-test
	fetch = +refs/heads/*:refs/remotes/origin/*
[gc]
	auto = 0
[branch "main"]
	remote = origin
	merge = refs/heads/main
```

The remote URL is plain HTTPS with **no embedded `user:token@` credentials**.
`.git/config.worktree` only holds sparse-checkout flags. No credential files
exist: `~/.git-credentials` and `~/.netrc` are both absent.

### 4. `git remote -v`

```
origin	https://github.com/WhiteElephant-abc/autotweaker-action-test (fetch)
origin	https://github.com/WhiteElephant-abc/autotweaker-action-test (push)
```

No token in the URL. `FETCH_HEAD` likewise records the anonymous HTTPS URL.

## Important caveat on the reachability test

`git ls-remote origin` **succeeds** without any credentials, but this is *not*
evidence of a token: the repository is public (`"private": false` in the event
payload), so anonymous read access works. A successful fetch therefore proves
nothing about token availability. Writing (push / PR) would still require the
token, which is not present here.

## Why the token is unreachable (workflow design)

From `.github/workflows/test.yml`:

- `actions/checkout` runs with `persist-credentials: false`, so checkout does
  **not** write the token into `.git/config` as an extraheader.
- The job has `permissions: contents: write, pull-requests: write`, but the
  token itself (`GH_TOKEN: ${{ github.token }}`) is scoped to the single
  "Create PR" step and exported only there.
- The "Create PR" step authenticates its push via a one-off
  `git -c http...extraheader=...` argument, which never lands in config.

So the credential exists for the PR step only and is never handed to the agent
step, whose environment and git config are checked above.

## Summary

The agent cannot retrieve a GitHub token: it is absent from the environment,
from `git config`, from `.git/config`, and from `git remote -v`/`FETCH_HEAD`.
The only secret present is the non-GitHub `INPUT_API_KEY`.
