// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC20/ERC20.sol";

contract ERC20Example is ERC20("ERC20Example", "TEST") {
    function mint(address account_, uint256 amount_) public {
        _mint(account_, amount_);
    }
}
