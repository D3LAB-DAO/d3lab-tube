## `MultiOwnable`



Contract module which provides a basic access control mechanism, where
there are accounts (owners group) that can be granted exclusive access to
specific functions.

By default, the owner account will be the one that deploys the contract.
This can later be changed with {transferOwnership} and {addOwnership} or
{deleteOwnership}.

This module is used through inheritance. It will make available the modifier
`onlyOwner(n)`, which can be applied to your functions to restrict their use
to the owner and owner's access level.

There are multiple levels (0~) and the higher level takes more accessability.
Zero means no accessability.

References:

- openzeppelin-solidity/contracts/access/Ownable.sol

### `onlyOwner(uint8 level)`



Throws if called by any account other than the owner.


### `constructor()` (internal)



Initializes the contract setting the deployer as the initial owner.

### `levelOf(address owner) → uint8` (public)



Returns the level of the owner.

### `isValid(address owner, uint8 level) → bool` (public)



Returns the validation of the owner.

### `_addOwnership(address account, uint8 level)` (internal)



Adds the ownership.

### `_deleteOwnership(address account)` (internal)



Leaves the contract. It will not be possible to call `onlyOwner`
functions anymore if there are no other owners.

NOTE: Renouncing ownership can cause removing any functionality that
is only available to the owners.

### `_transferOwnership(address oldOwner, address newOwner)` (internal)



Transfers ownership of the contract to a new account (`newOwner`).

### `_changeOwnershipLevel(address account, uint8 level)` (internal)



Changes ownership level.


