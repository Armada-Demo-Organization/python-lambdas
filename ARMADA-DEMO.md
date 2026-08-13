# Armada demo estate

This repository is part of the **Armada** demo estate: the set of projects the
Armada Master Template is built from, so that `armada create` hands you a
SonarQube with real projects, real findings and real history already in it.

- **Copied from:** [`SonarSource-Demos/python-lambdas`](https://github.com/SonarSource-Demos/python-lambdas) — public at the time of copying.
- **Copied, not forked.** A fork would tie this estate to the source
  organisation's network. This is a plain push of the default branch's history
  into a fresh repository, so no fork relationship exists.
- **What came across:** the default branch and its tags. The source carried
  branches of personal work-in-progress; those were left behind.

## What this one demonstrates

**Python** serverless handlers — SAM and Serverless Framework layouts side
by side, with compliant/non-compliant pairs for individual rules. Useful
for monorepo and multi-root analysis questions as much as for Python ones.

## Please do not "fix" this code

The findings are the product. Every issue Sonar reports here is either
deliberate or inherited on purpose, and a cleanup would empty the demo.

## Pull requests

`demo/new-issue` is open as a pull request against `main`. It exists so that a
demo can show pull-request decoration: it introduces a finding that `main` does
not have, which is what gives the New Code quality gate something to fail on.
