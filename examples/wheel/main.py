# Copyright 2018 The Bazel Authors. All rights reserved.
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

import examples.wheel.lib.module_with_data as module_with_data
import examples.wheel.lib.module_with_type_annotations as module_with_type_annotations
import examples.wheel.lib.simple_module as simple_module


def function():
    return "baz"


def main():
    print(function())
    print(module_with_data.function())
    print(module_with_type_annotations.function())
    print(simple_module.function())


if __name__ == "__main__":
    main()
