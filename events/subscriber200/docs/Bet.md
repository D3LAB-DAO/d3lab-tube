## `Bet`



Implementation of the {IBet} abstract contract.


### `constructor(address initialLPTAddress, address initialRandomAddress)` (public)



Sets the 'LPT' and 'Random' contracts.

Requirements:

- the `LPTAddress` MUST be a contract address.
- the `initialRandomAddress` MUST be a contract address.

### `bet(uint24 amount, uint8 percentage) → bool success` (public)



Consumes `amount` LPTs and runs the betting system with the probability
`percentage` .

Returns a boolean value indicating whether the betting succeeded.

Emits {Bet} and {Result} events.

Requirements:

- `percentage` < 100

### `claimWinner() → bool` (public)





### `getEndState() → bool` (public)



Returns the {ENDSTATE}.

### `setEndState(bool newENDSTATE)` (public)



Sets {ENDSTATE} to a value.

### `getTargetPrice() → uint256` (public)



Returns the {_targetPrice}.

### `setTargetPrice(uint256 newTargetPrice)` (public)



Sets {_targetPrice} to a value other than the default one of 200000.

### `getWinner() → address` (public)



Returns the {WINNER}.

### `getFeeConst() → uint8` (public)



Returns the number of {_feeconst}.

### `setFeeConst(uint8 newFeeConst)` (public)



Sets {_feeconst} to a value other than the default one of 8.

### `getLPTAddress() → address` (public)



Returns the address of 'LPT' contract.

### `setLPTAddress(address newLPTAddress)` (public)



Sets the 'LPT' via an address.
{newLPTAddress}.

Requirements:

- the `newLPTAddress` MUST be contract address.

### `getRandomAddress() → address` (public)



Returns the address of 'Random' contract.

### `setRandomAddress(address newRandomAddress)` (public)



Sets the 'Random' contract via an address.
{newRandomAddress}.

Requirements:

- the `newRandomAddress` MUST be contract address.

### `addOwnership(address account, uint8 level) → bool` (public)



Calls {_addOwnership}.

### `deleteOwnership(address account) → bool` (public)



Calls {_deleteOwnership}.

### `transferOwnership(address oldOwner, address newOwner) → bool` (public)



Calls {_transferOwnership}.

### `changeOwnershipLevel(address account, uint8 level) → bool` (public)



Calls {_changeOwnershipLevel}.


