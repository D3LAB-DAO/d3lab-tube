## `Address`



Collection of functions related to the address type

References:

- openzeppelin-solidity/contracts/utils/Address.sol


### `isContract(address account) → bool` (internal)



Returns true if `account` is a contract.

[IMPORTANT]
====
It is unsafe to assume that an address for which this function returns
false is an externally-owned account (EOA) and not a contract.

Among others, `isContract` will return false for the following
types of addresses:

 - an externally-owned account
- a contract in construction
- an address where a contract will be created
- an address where a contract lived, but was destroyed
====


