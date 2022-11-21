from invoke import task



@task
def start(ctx):
    ctx.run("python3 src/main.py", pty=True)
    
@task
def test(ctx):
    ctx.run("coverage run --branch -m pytest", pty=True)

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage report -m", pty=True)
    ctx.run("coverage html", pty=True)
    
