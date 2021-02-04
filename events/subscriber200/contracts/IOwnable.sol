// SPDX-License-Identifier: MIT

pragma solidity >=0.5.0 <0.6.0;


/**
 * @dev Abstract contract of the Ownable contract.
 *
 * References:
 *
 * - openzeppelin-solidity/contracts/access/Ownable.sol
 */
contract IOwnable {
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner, uint8 level);

    /**
     * @dev Returns the level of the owner.
     */
    function levelOf(
        address owner
    ) public view returns (uint8);

    /**
     * @dev Returns the validation of the owner.
     */
    function isValid(
        address owner,
        uint8 level
    ) public view returns (bool);

    /**
     * @dev Throws if called by any account other than the owner.
     */
    modifier onlyOwner (
        uint8 level
    ) { _; }
}
