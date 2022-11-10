/*
 * Copyright (c) 2022 Samsung Electronics Co., Ltd. All Rights Reserved
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#ifndef __ONE_SERVICE_NPUD_CORE_CORE_H__
#define __ONE_SERVICE_NPUD_CORE_CORE_H__

#include <vector>
#include <string>

namespace npud
{
namespace core
{

// TODO Define error status

class Core
{
public:
  Core() noexcept = default;
  ~Core() noexcept = default;

  Core(const Core &) = delete;
  Core &operator=(const Core &) = delete;

  void init();
  void deinit();

  int getAvailableDeviceList(std::vector<std::string> &list) const;
};

} // namespace core
} // namespace npud

#endif // __ONE_SERVICE_NPUD_CORE_CORE_H__