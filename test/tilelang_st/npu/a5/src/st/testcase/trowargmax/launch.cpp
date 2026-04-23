// Copyright (c) 2026 Huawei Technologies Co., Ltd.
// This program is free software, you can redistribute it and/or modify it under the terms and conditions of
// CANN Open Software License Agreement Version 2.0 (the "License").
// Please refer to the License for details. You may not use this file except in compliance with the License.
// THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR IMPLIED,
// INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT, MERCHANTABILITY, OR FITNESS FOR A PARTICULAR PURPOSE.
// See LICENSE in the root of the software repository for the full text of the License.

#include <stdint.h>

#ifndef AICORE
#define AICORE [aicore]
#endif

extern "C" __global__ AICORE void TROWARGMAX_f32_127x64_valid127x63(__gm__ float *src, __gm__ uint32_t *dst);

void LaunchTROWARGMAX_f32_127x64_valid127x63(float *src, uint32_t *dst, void *stream) {
    TROWARGMAX_f32_127x64_valid127x63<<<1, nullptr, stream>>>((__gm__ float *)src, (__gm__ uint32_t *)dst);
}