## `IBet`



Abstarct contract of the Bet.


### `bet(uint24 amount, uint8 percentage) → bool` (public)



Consumes `amount` LPTs and runs the betting system with the probability
`percentage` .

Returns a boolean value indicating whether the betting succeeded.

Emits {Bet} and {Result} events.


### `Bet(address who, uint24 amount, uint8 percentage)`



Emitted when `who` bets `amount` LPTs with the probability `percentage`

### `Result(address who, bool success, uint256 reward)`



Emitted when `who` wins/loses random game with indicator 'success' and
amount of `reward`s.

