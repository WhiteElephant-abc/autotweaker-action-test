# autotweaker-action-test

Scratch repository for exercising [AutoTweaker/action](https://github.com/AutoTweaker/action)
end to end.

`.github/workflows/test.yml` runs on `workflow_dispatch` with a `prompt` input. The agent works
on the checked-out tree; if it leaves anything behind, a following step commits it to a branch
and opens a pull request.

`temperature.py` and `test_temperature.py` exist only to give the agent something real to
change.

## Running the tests

```bash
python3 -m unittest discover -v
```
