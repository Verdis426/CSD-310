# ERD Project Workspace

This workspace is set up for an Entity Relationship Diagram (ERD) project.

## Included files
- `schema.sql` — SQL DDL for a simple retail database
- `erd.md` — Mermaid ERD diagram and notes
- `.gitignore` — common ignores for local tooling

## Suggested workflow
1. Review the entity relationships in `erd.md`.
2. Apply the schema in `schema.sql` to your database.
3. Extend the design with additional tables or attributes as needed.

## Example database domain
This sample schema models a simple order-management system with:
- customers
- products
- orders
- order items

## Run SQL
Use any SQL client or database engine to execute:

```sql
SOURCE schema.sql;
```

Or paste the contents of `schema.sql` directly into your database tool.
