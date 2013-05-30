#!/usr/bin/env python

# Copyright 2013, Institute for Bioninformatics and Evolutionary Studies
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import time
from random import randint

class TestRunner:
  def __init__(self):
    self.error = None
    self.next = []

  def start(self):
    self.cpu_intensive()
    if randint(0,10) > 8:
      self.next = [{'runner': TestRunner(), 'name': 'Added Runner' }]

  def cpu_intensive(self):
    a, b = 0, 1
    for i in range(100000):
      a, b = b, a + b
    time.sleep(randint(2,9))