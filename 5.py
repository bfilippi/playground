from prefect import task, Flow


@task
def say_hello():
    print("Hello, world!")


with Flow("My First Flow") as flow:
    say_hello()

flow.run()  # "Hello, world!"
