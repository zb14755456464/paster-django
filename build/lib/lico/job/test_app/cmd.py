# Copyright 2019-present Lenovo
# Confidential and Proprietary

import os
import sys
from collections import defaultdict

import six
from django.apps import apps
from django.core.management import (
    ManagementUtility, find_commands, get_commands,
)
from django.core.management.color import color_style
from paste.deploy import loadapp


class LicoManagementUtility(ManagementUtility):
    def main_help_text(self, commands_only=False):
        """
        Returns the script's main help text, as a string.
        """
        if commands_only:
            usage = sorted(get_commands().keys())
        else:
            usage = [
                "",
                "Type '%s help <subcommand>' for "
                "help on a specific subcommand." % self.prog_name,
                "",
                "Available subcommands:",
            ]

            commands = {}
            for app_config in reversed(list(apps.get_app_configs())):
                path = os.path.join(app_config.path, 'management')
                if app_config.name.startswith('lico'):
                    commands.update(
                        {name: app_config for name in find_commands(path)}
                    )

            commands_dict = defaultdict(lambda: [])
            for name, app_config in six.iteritems(commands):
                commands_dict[app_config.verbose_name].append(name)

            style = color_style()
            for app in sorted(commands_dict.keys()):
                usage.append("")
                usage.append(style.NOTICE("[%s]" % app))
                for name in sorted(commands_dict[app]):
                    usage.append("    %s" % name)
            # Output an extra note if settings are not properly configured
            if self.settings_exception is not None:
                usage.append(style.NOTICE(
                    "Note that only Django core commands are listed "
                    "as settings are not properly configured (error: %s)."
                    % self.settings_exception))

        return '\n'.join(usage)


def main():
    try:
        subcommand = sys.argv[1]
    except IndexError:
        subcommand = 'help'

    if subcommand == 'version' or sys.argv[1:] == ['--version']:
        from pkg_resources import get_distribution
        six.print_(get_distribution('deploy').version)
        exit()

    loadapp(
        'config:config.ini#main',
        relative_to='/home/roo/Desktop/projects/paster-django/etc',
    )
    LicoManagementUtility(sys.argv).execute()
