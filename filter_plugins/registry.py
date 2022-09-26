# python 3 headers, required if submitting to Ansible

from __future__ import (absolute_import, print_function)
__metaclass__ = type

import re

from ansible.utils.display import Display

display = Display()


class FilterModule(object):
    """
        Ansible file jinja2 tests
    """

    def filters(self):
        return {
            'registry_checksum': self.checksum,
        }

    def checksum(self, data, os, arch):
        """
        """
        checksum = None

        if isinstance(data, list):
            # filter OS
            # linux = [x for x in data if re.search(r".*prometheus-.*.{}.*.tar.gz".format(os), x)]
            # filter OS and ARCH
            checksum = [x for x in data if re.search(r".*registry-.*.{}-{}.tar.gz".format(os, arch), x)][0]

        if isinstance(checksum, str):
            checksum = checksum.split(" ")[0]

        # display.v("= checksum: {}".format(checksum))

        return checksum