# coding=utf8
"""
CLI entry
"""
import os
import click

plugin_folder = os.path.join(os.path.dirname(__file__), 'commands')


class MyCLI(click.MultiCommand):
    def list_commands(self, ctx):
        rv = []
        for filename in os.listdir(plugin_folder):
            # Exclude private module
            if not filename.startswith('_') and filename.endswith('.py'):
                rv.append(filename.lstrip('_')[:-3])
        rv.sort()
        return rv

    def get_command(self, ctx, name):
        ns = {}
        fn = os.path.join(plugin_folder, name + '.py')
        with open(fn) as f:
            code = compile(f.read(), fn, 'exec')
            eval(code, ns, ns)
        return ns['cli']


@click.command(cls=MyCLI)
def cli():
    pass


if __name__ == '__main__':
    cli()
