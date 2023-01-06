import os

import click
import django
import uvicorn



os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'

django.setup()

from django.core import management  # noqa: E402


@click.command()
@click.option(
    '--collect-static/--no-collect-static',
    is_flag=True,
    default=True,
    help='Collect Django static',
)
@click.option(
    '--uvicorn-debug/--no-uvicorn-debug',
    is_flag=True,
    default=True,
    help='Enable/Disable debug and auto-reload',
)
@click.option(
    '--migrate/--no-migrate',
    is_flag=True,
    default=True,
    help='Make django migrate',
)
def web(collect_static: bool, uvicorn_debug: bool, migrate: bool):
    import config.asgi
    app = config.asgi.application

    if uvicorn_debug:
        # Автоперезапуск при изменении кода: uvicorn.config.Config.should_reload
        # Удобно при локальной разработке
        app = 'config.asgi:application'

    if collect_static:
        management.call_command('collectstatic', '--no-input', '--clear')

    if migrate:
        management.call_command('migrate', '--no-input')

    uvicorn.run(
        app,
        host='0.0.0.0',
        port=8000,
        reload=uvicorn_debug,
        # access_log=False,
        # log_config=None,
        lifespan='off',
    )


if __name__ == '__main__':
    web()
