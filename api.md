# Accounts

Types:

```python
from meorphis_test_40.types import AccountAccountGetResponse
```

Methods:

- <code title="get /account">client.accounts.<a href="./src/meorphis_test_40/resources/accounts/accounts.py">account_get</a>() -> <a href="./src/meorphis_test_40/types/account_account_get_response.py">AccountAccountGetResponse</a></code>

## Addresses

Types:

```python
from meorphis_test_40.types.accounts import (
    AddressUpdateResponse,
    AddressAccountAddressCreateResponse,
)
```

Methods:

- <code title="put /account/addresses/{id}">client.accounts.addresses.<a href="./src/meorphis_test_40/resources/accounts/addresses.py">update</a>(id, \*\*<a href="src/meorphis_test_40/types/accounts/address_update_params.py">params</a>) -> <a href="./src/meorphis_test_40/types/accounts/address_update_response.py">AddressUpdateResponse</a></code>
- <code title="delete /account/addresses/{id}">client.accounts.addresses.<a href="./src/meorphis_test_40/resources/accounts/addresses.py">delete</a>(id) -> None</code>
- <code title="post /account/addresses">client.accounts.addresses.<a href="./src/meorphis_test_40/resources/accounts/addresses.py">account_address_create</a>(\*\*<a href="src/meorphis_test_40/types/accounts/address_account_address_create_params.py">params</a>) -> <a href="./src/meorphis_test_40/types/accounts/address_account_address_create_response.py">AddressAccountAddressCreateResponse</a></code>

## Exists

Methods:

- <code title="get /account/exists">client.accounts.exists.<a href="./src/meorphis_test_40/resources/accounts/exists.py">list</a>(\*\*<a href="src/meorphis_test_40/types/accounts/exist_list_params.py">params</a>) -> None</code>

## PaymentMethods

Types:

```python
from meorphis_test_40.types.accounts import PaymentMethodAccountAddPaymentMethodResponse
```

Methods:

- <code title="delete /account/payment-methods/{id}">client.accounts.payment_methods.<a href="./src/meorphis_test_40/resources/accounts/payment_methods.py">delete</a>(id) -> None</code>
- <code title="post /account/payment-methods">client.accounts.payment_methods.<a href="./src/meorphis_test_40/resources/accounts/payment_methods.py">account_add_payment_method</a>(\*\*<a href="src/meorphis_test_40/types/accounts/payment_method_account_add_payment_method_params.py">params</a>) -> <a href="./src/meorphis_test_40/types/accounts/payment_method_account_add_payment_method_response.py">PaymentMethodAccountAddPaymentMethodResponse</a></code>

# Payments

Types:

```python
from meorphis_test_40.types import PaymentCreateResponse
```

Methods:

- <code title="post /payments">client.payments.<a href="./src/meorphis_test_40/resources/payments.py">create</a>(\*\*<a href="src/meorphis_test_40/types/payment_create_params.py">params</a>) -> <a href="./src/meorphis_test_40/types/payment_create_response.py">PaymentCreateResponse</a></code>

# Guests

## Payments

Types:

```python
from meorphis_test_40.types.guests import PaymentGuestPaymentsInitializeResponse
```

Methods:

- <code title="post /guest/payments">client.guests.payments.<a href="./src/meorphis_test_40/resources/guests/payments.py">guest_payments_initialize</a>(\*\*<a href="src/meorphis_test_40/types/guests/payment_guest_payments_initialize_params.py">params</a>) -> <a href="./src/meorphis_test_40/types/guests/payment_guest_payments_initialize_response.py">PaymentGuestPaymentsInitializeResponse</a></code>

# Merchants

## Callbacks

Types:

```python
from meorphis_test_40.types.merchants import (
    CallbackListResponse,
    CallbackMerchantCallbacksUpdateResponse,
)
```

Methods:

- <code title="get /merchant/callbacks">client.merchants.callbacks.<a href="./src/meorphis_test_40/resources/merchants/callbacks.py">list</a>() -> <a href="./src/meorphis_test_40/types/merchants/callback_list_response.py">CallbackListResponse</a></code>
- <code title="patch /merchant/callbacks">client.merchants.callbacks.<a href="./src/meorphis_test_40/resources/merchants/callbacks.py">merchant_callbacks_update</a>(\*\*<a href="src/meorphis_test_40/types/merchants/callback_merchant_callbacks_update_params.py">params</a>) -> <a href="./src/meorphis_test_40/types/merchants/callback_merchant_callbacks_update_response.py">CallbackMerchantCallbacksUpdateResponse</a></code>

## Identifiers

Types:

```python
from meorphis_test_40.types.merchants import IdentifierListResponse
```

Methods:

- <code title="get /merchant/identifiers">client.merchants.identifiers.<a href="./src/meorphis_test_40/resources/merchants/identifiers.py">list</a>() -> <a href="./src/meorphis_test_40/types/merchants/identifier_list_response.py">IdentifierListResponse</a></code>

# Webhooks

Types:

```python
from meorphis_test_40.types import (
    WebhookCreateResponse,
    WebhookRetrieveResponse,
    WebhookListResponse,
)
```

Methods:

- <code title="put /webhooks">client.webhooks.<a href="./src/meorphis_test_40/resources/webhooks.py">create</a>(\*\*<a href="src/meorphis_test_40/types/webhook_create_params.py">params</a>) -> <a href="./src/meorphis_test_40/types/webhook_create_response.py">WebhookCreateResponse</a></code>
- <code title="get /webhooks/{id}">client.webhooks.<a href="./src/meorphis_test_40/resources/webhooks.py">retrieve</a>(id) -> <a href="./src/meorphis_test_40/types/webhook_retrieve_response.py">WebhookRetrieveResponse</a></code>
- <code title="get /webhooks">client.webhooks.<a href="./src/meorphis_test_40/resources/webhooks.py">list</a>() -> <a href="./src/meorphis_test_40/types/webhook_list_response.py">WebhookListResponse</a></code>
- <code title="delete /webhooks/{id}">client.webhooks.<a href="./src/meorphis_test_40/resources/webhooks.py">delete</a>(id) -> None</code>

# Testings

## Accounts

Types:

```python
from meorphis_test_40.types.testings import AccountTestingAccountCreateResponse
```

Methods:

- <code title="post /testing/accounts">client.testings.accounts.<a href="./src/meorphis_test_40/resources/testings/accounts.py">testing_account_create</a>(\*\*<a href="src/meorphis_test_40/types/testings/account_testing_account_create_params.py">params</a>) -> <a href="./src/meorphis_test_40/types/testings/account_testing_account_create_response.py">AccountTestingAccountCreateResponse</a></code>

## CreditCards

Types:

```python
from meorphis_test_40.types.testings import CreditCardListResponse
```

Methods:

- <code title="get /testing/credit-cards">client.testings.credit_cards.<a href="./src/meorphis_test_40/resources/testings/credit_cards.py">list</a>() -> <a href="./src/meorphis_test_40/types/testings/credit_card_list_response.py">CreditCardListResponse</a></code>

## Shipments

Methods:

- <code title="post /testing/shipments">client.testings.shipments.<a href="./src/meorphis_test_40/resources/testings/shipments.py">testing_shipment_tracking_create</a>(\*\*<a href="src/meorphis_test_40/types/testings/shipment_testing_shipment_tracking_create_params.py">params</a>) -> None</code>
