#!/usr/bin/env python

import re

in_str = '"Included are FN, VZ, XB, AY, 2HN & RS."'

out_str = re.findall(r'\d?[A-Z]{2}', in_str)

print(out_str)

