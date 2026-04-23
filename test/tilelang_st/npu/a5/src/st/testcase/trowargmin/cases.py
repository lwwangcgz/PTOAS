#!/usr/bin/python3
# Copyright (c) 2026 Huawei Technologies Co., Ltd.
# This program is free software, you can redistribute it and/or modify it under the terms and conditions of
# CANN Open Software License Agreement Version 2.0 (the "License").
# Please refer to the License for details. You may not use this file except in compliance with the License.
# THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT, MERCHANTABILITY, OR FITNESS FOR A PARTICULAR PURPOSE.
# See LICENSE in the root of the software repository for the full text of the License.

# coding=utf-8

"""Single source of truth for trowargmin ST test cases."""

import numpy as np

CASES = [
    # f32 cases
    {
        "name": "f32_127x64_valid127x63",
        "dtype": np.float32,
        "dst_dtype": np.uint32,
        "shape": (127, 64),
        "valid_shape": (127, 63),
        "eps": 0,
    },
    {
        "name": "f32_63x64",
        "dtype": np.float32,
        "dst_dtype": np.uint32,
        "shape": (63, 64),
        "valid_shape": (63, 64),
        "eps": 0,
    },
    {
        "name": "f32_31x128_valid31x127",
        "dtype": np.float32,
        "dst_dtype": np.uint32,
        "shape": (31, 128),
        "valid_shape": (31, 127),
        "eps": 0,
    },
    {
        "name": "f32_15x192",
        "dtype": np.float32,
        "dst_dtype": np.uint32,
        "shape": (15, 192),
        "valid_shape": (15, 192),
        "eps": 0,
    },
    {
        "name": "f32_7x448_valid7x447",
        "dtype": np.float32,
        "dst_dtype": np.uint32,
        "shape": (7, 448),
        "valid_shape": (7, 447),
        "eps": 0,
    },
    # f16 case
    {
        "name": "f16_256x16_valid256x15",
        "dtype": np.float16,
        "dst_dtype": np.uint32,
        "shape": (256, 16),
        "valid_shape": (256, 15),
        "eps": 0,
    },
    # f32 more cases
    {
        "name": "f32_30x216",
        "dtype": np.float32,
        "dst_dtype": np.uint32,
        "shape": (30, 216),
        "valid_shape": (30, 216),
        "eps": 0,
    },
    {
        "name": "f32_30x216_valid30x24",
        "dtype": np.float32,
        "dst_dtype": np.uint32,
        "shape": (30, 216),
        "valid_shape": (30, 24),
        "eps": 0,
    },
    {
        "name": "f32_30x216_valid11x216",
        "dtype": np.float32,
        "dst_dtype": np.uint32,
        "shape": (30, 216),
        "valid_shape": (11, 216),
        "eps": 0,
    },
    {
        "name": "f32_30x216_valid11x24",
        "dtype": np.float32,
        "dst_dtype": np.uint32,
        "shape": (30, 216),
        "valid_shape": (11, 24),
        "eps": 0,
    },
    {
        "name": "f32_238x40",
        "dtype": np.float32,
        "dst_dtype": np.uint32,
        "shape": (238, 40),
        "valid_shape": (238, 40),
        "eps": 0,
    },
    {
        "name": "f32_238x40_valid238x16",
        "dtype": np.float32,
        "dst_dtype": np.uint32,
        "shape": (238, 40),
        "valid_shape": (238, 16),
        "eps": 0,
    },
    {
        "name": "f32_238x40_valid121x40",
        "dtype": np.float32,
        "dst_dtype": np.uint32,
        "shape": (238, 40),
        "valid_shape": (121, 40),
        "eps": 0,
    },
    {
        "name": "f32_238x40_valid121x16",
        "dtype": np.float32,
        "dst_dtype": np.uint32,
        "shape": (238, 40),
        "valid_shape": (121, 16),
        "eps": 0,
    },
    {
        "name": "f32_64x128",
        "dtype": np.float32,
        "dst_dtype": np.uint32,
        "shape": (64, 128),
        "valid_shape": (64, 128),
        "eps": 0,
    },
    {
        "name": "f32_32x256",
        "dtype": np.float32,
        "dst_dtype": np.uint32,
        "shape": (32, 256),
        "valid_shape": (32, 256),
        "eps": 0,
    },
    {
        "name": "f32_16x512",
        "dtype": np.float32,
        "dst_dtype": np.uint32,
        "shape": (16, 512),
        "valid_shape": (16, 512),
        "eps": 0,
    },
    {
        "name": "f32_8x1024",
        "dtype": np.float32,
        "dst_dtype": np.uint32,
        "shape": (8, 1024),
        "valid_shape": (8, 1024),
        "eps": 0,
    },
]
