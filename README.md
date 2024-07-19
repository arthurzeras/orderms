# Order MS (microservice)

A python application to consume a RabbitMQ queue, save data and expose a REST API in order to get some information about the saved data.

## Stack 

- Django
- Django Rest Framework
- PostgreSQL
- Pika

## Example of the message sent on RabbitMQ queue

```json
{
  "order_code": 1001,
  "customer_code": 1,
  "items": [
    {
      "product": "Beer",
      "quantity": 100,
      "price": 1.10
    },
    {
      "product": "Bread",
      "quantity": 10,
      "price": 1.00
    }
  ]
}
```