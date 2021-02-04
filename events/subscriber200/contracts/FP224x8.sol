// SPDX-License-Identifier: MIT

pragma solidity >=0.5.0 <0.6.0;

/**
 * @title FP224x8
 * @dev A library for handling binary fixed point numbers
 * 
 * Refers Uniswap UQ112x112 library:
 * 
 * https://github.com/Uniswap/uniswap-v2-core/blob/master/
 * contracts/libraries/UQ112x112.sol
 * 
 * Range: [0, 2**8 - 1]
 * Resolution: 1 / 2**224
 */
library FP224x8 {
    uint232 public constant MAX224 = 2**224;

    // encodes a uint8 as a FP224x8
    function encode(uint8 y) internal pure returns (uint232 z) {
        z = uint232(y) * MAX224;  // never overflows
    }

    // divides a FP224x8 by a uint8, returning a FP224x8
    function fpdiv(uint232 x, uint8 y) internal pure returns (uint232 z) {
        z = x / uint232(y);
    }
}
