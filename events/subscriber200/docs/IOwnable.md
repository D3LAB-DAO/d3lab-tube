## `IOwnable`



Abstract contract of the Ownable contract.

References:

- openzeppelin-solidity/contracts/access/Ownable.sol

### `onlyOwner(uint8 level)`



Throws if called by any account other than the owner.


### `levelOf(address owner) → uint8` (public)



Returns the level of the owner.

### `isValid(address owner, uint8 level) → bool` (public)



Returns the validation of the owner.


### `OwnershipTransferred(address previousOwner, address newOwner, uint8 level)`





