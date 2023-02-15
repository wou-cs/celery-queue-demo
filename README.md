# Celery and Redis Demo - Task Queues for Python

## Calling the `add` method

Interact with the `add` function by opening a Python console within your Pipenv shell:

```sh
>>> from tasks import add
>>> add(3,4)
7
>>> add.delay(3,4)
<AsyncResult: bf044d84-c509-4dfa-9b3c-add1d51fc923>
>>>
```

When you call `add` with the `delay` modifier, you won't see the result show up in the console.

## Running a worker

To see the results, we need to start up a worker to process the results.

```sh
❯ celery -A tasks worker --loglevel=info

celery@MacBook-Pro-3.local v5.2.7 (dawn-chorus)
macOS-13.2-x86_64-i386-64bit 2023-02-15 08:40:40

[config]
.> app:         tasks:0x10d13a8f0
.> transport:   redis://localhost:6379//
.> results:     redis://localhost/
.> concurrency: 12 (prefork)
.> task events: OFF (enable -E to monitor tasks in this worker)

[queues]
.> celery           exchange=celery(direct) key=celery


[tasks]
  . tasks.add

[2023-02-15 08:40:40,483: INFO/MainProcess] Connected to redis://localhost:6379//
[2023-02-15 08:40:40,488: INFO/MainProcess] mingle: searching for neighbors
[2023-02-15 08:40:41,496: INFO/MainProcess] mingle: all alone
[2023-02-15 08:40:41,508: INFO/MainProcess] celery@MacBook-Pro-3.local ready.
[2023-02-15 08:40:41,511: INFO/MainProcess] Task tasks.add[bf044d84-c509-4dfa-9b3c-add1d51fc923] received
[2023-02-15 08:40:46,524: INFO/ForkPoolWorker-8] Task tasks.add[bf044d84-c509-4dfa-9b3c-add1d51fc923] succeeded in 5.011491307988763s: 7

```

This is verbose monitoring but helps see how the worker functions. At the end you can see the add method succeeded and returned the value 7.