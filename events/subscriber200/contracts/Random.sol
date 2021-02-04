// SPDX-License-Identifier: MIT

pragma solidity >=0.5.0 <0.6.0;


// WARNING: This contract is the temporary implementation of random.
// Using trustable random process for real uses.
contract Random  {
    uint256 private seed;

    event RandomNumber(uint256 randomNumber_);

    function random(
        // ...
    ) public returns (
        uint256 randomNumber
    ) {
        randomNumber = uint256(keccak256(abi.encodePacked(
            block.timestamp,
            block.difficulty,
            seed
        )));

        emit RandomNumber(randomNumber);

        seed += 1;
    }
}
