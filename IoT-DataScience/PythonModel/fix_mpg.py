#
# Copyright 2014-2015 the original author or authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import glob
import json

source_dir = "/opt/pivotal/data/"
target_dir = "/opt/pivotal/data/test/"

filenames = glob.glob(source_dir + "*.out")

for filename in filenames:
    with open(filename) as f:
        trip = [json.loads(line) for line in f]

        for i in range(0, len(trip)):
            trip[i]['mpg_instantaneous'] = ""

    new_filename = target_dir + filename.split('/')[-1]
    jlist = [json.dumps(record) + "\n" for record in trip]
    open(new_filename, "w").writelines(jlist)
