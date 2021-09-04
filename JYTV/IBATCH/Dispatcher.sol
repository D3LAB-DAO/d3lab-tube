// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

/// Inspired by multicall
/// https://github.com/makerdao/multicall/blob/master/src/Multicall.sol

contract Dispatcher {
    struct Call {
        address account; // caller
        address target; // callee (contract)
        bytes callData; // func and args
        uint8 v; bytes32 r; bytes32 s; // sig
    }

    function dispatch(Call[] memory calls, bytes memory bmsgSign) public returns (uint256 blockNumber, bytes[] memory returnData) {
        blockNumber = block.number;
        returnData = new bytes[](calls.length);
        
        for(uint256 i = 0; i < calls.length; i++) {
            (bool success, bytes memory ret) = calls[i].target.call(calls[i].callData);
            require(success);
            returnData[i] = ret;
            
            bytes32 digest = keccak256(
                abi.encodePacked(
                    '\x19Ethereum Signed Message:\n32',
                    keccak256(abi.encode(bmsgSign))
                )
            );
            address recoveredAddress = ecrecover(digest, calls[i].v, calls[i].r, calls[i].s);
            require(recoveredAddress != address(0) && recoveredAddress == calls[i].account, 'INVALID_SIGNATURE');
        }
    }
}
