from prefect import Flow, task


# ------------------------------------
# define some tasks


@task
def numbers_task():
    return [1, 2, 3]


@task
def map_task(x):
    return x + 1


@task
def reduce_task(x):
    return sum(x)


# ------------------------------------
# build a flow

with Flow("Map / Reduce 🤓") as flow:
    numbers = numbers_task()
    first_map = map_task.map(numbers)
    print(first_map)
    second_map = map_task.map(first_map)
    reduction = reduce_task(second_map)


def main():
    state = flow.run()


# ------------------------------------
# run the flow
if __name__ == "__main__":
    main()
