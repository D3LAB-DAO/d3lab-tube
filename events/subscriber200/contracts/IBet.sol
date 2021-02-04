// SPDX-License-Identifier: MIT

pragma solidity >=0.5.0 <0.6.0;


/**
 * @dev Abstarct contract of the Bet.
 */
contract IBet {
    /**
     * @dev Consumes `amount` LPTs and runs the betting system with the probability
     * `percentage` .
     *
     * Returns a boolean value indicating whether the betting succeeded.
     *
     * Emits {Bet} and {Result} events.
     */
    function bet(
        uint24 amount,
        uint8 percentage
    ) public returns (bool);

    /**
     * @dev Emitted when `who` bets `amount` LPTs with the probability `percentage`
     */
    event Bet(address indexed who, uint24 amount, uint8 percentage);

    /**
     * @dev Emitted when `who` wins/loses random game with indicator 'success' and
     * amount of `reward`s.
     */
    event Result(address indexed who, bool success, uint256 reward);
}
