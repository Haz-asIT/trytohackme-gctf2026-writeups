
# Ghost in the Repo 1

The challenge asks for a database password that had been committed and later removed from a local Git repository.

![Challenge](./images/fig-01.png)

## 1. Extract and inspect history

```bash
unzip repo.zip
cd repo
git log --oneline --all --graph
git reflog --all
```

![Repository extraction](./images/fig-02.png)

![Git history](./images/fig-03.png)

A historical commit named `fix: added db password` was inspected:

```bash
git show 7e70e9c
```

The diff reveals:

```python
password = 'db_p4ss_qw3r1234!'
```

![Recovered password](./images/fig-04.png)

## Flag

```text
gctf26{db_p4ss_qw3r1234!}
```
