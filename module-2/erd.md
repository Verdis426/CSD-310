# Entity Relationship Diagram

## Mermaid ERD

```mermaid
erDiagram
    CUSTOMER ||--o{ ORDER : places
    CUSTOMER ||--o{ SHIPPING_ADDRESS : has
    ORDER ||--o{ ORDER_ITEM : contains
    PRODUCT ||--o{ ORDER_ITEM : includes
    ORDER ||--o| PAYMENT : paid_by

    CUSTOMER {
        int customer_id PK
        string first_name
        string last_name
        string email
        string phone
        timestamp created_at
    }

    ORDER {
        int order_id PK
        int customer_id FK
        timestamp order_date
        string status
        decimal total_amount
    }

    PRODUCT {
        int product_id PK
        string product_name
        string description
        decimal unit_price
        int stock_quantity
    }

    ORDER_ITEM {
        int order_item_id PK
        int order_id FK
        int product_id FK
        int quantity
        decimal unit_price
    }

    PAYMENT {
        int payment_id PK
        int order_id FK
        timestamp payment_date
        decimal amount
        string payment_method
    }

    SHIPPING_ADDRESS {
        int address_id PK
        int customer_id FK
        string street_address
        string city
        string state
        string postal_code
        string country
    }
```

## Relationship summary
- One customer can place many orders.
- One order can contain many order items.
- One product can appear in many order items.
- One order may have one payment record.
- One customer can have multiple shipping addresses.

## Notes
This design is suitable for a basic e-commerce or retail management database.
