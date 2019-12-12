from datetime import datetime
from datetime import timedelta
from typing import List
import sys

"""
Script to group timestamps by week. 
Give it a list of timestamps, and it will give you a list of list of timestamps, grouped by week starting 
from the first timestamp:
```python timestamps.py 2019-01-01 2019-01-02 2019-01-08 2019-02-01 2019-02-02 2019-02-05 ```
returns:

```[['2019-01-01', '2019-01-02'], ['2019-01-08'], ['2019-02-01', '2019-02-02', '2019-02-05']]```
"""

def add_week(date: datetime) -> datetime:
    week = timedelta(days=7)
    return date + week

def group_weeks(timestamps: List[str], grouped_ts: List[List[str]]):

    if len(timestamps) == 0:
        return grouped_ts

    group = []
    week_later = None

    for index, ts in enumerate(timestamps):
        date = datetime.fromisoformat(ts)

        if index == 0:
            week_later = add_week(date)

        if date < week_later:
            group.append(ts)
        else:
            break

    grouped_ts.append(group)
    del timestamps[:len(group)]
    return group_weeks(timestamps, grouped_ts)

def main(stamps):

    groups = group_weeks(stamps, list())
    print(groups)

if __name__ == "__main__":
    stamps = sys.argv[1:]
    main(stamps)
