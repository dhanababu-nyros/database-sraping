#!/usr/bin/env python
from models import FieldData, RecordData


def save_field(ms, table_id):
    for c in ms.columns:
        field = FieldData(table=table_id, name=c.name, data_type=c.type, nullable=c.nullable,
                          primary_key=c.primary_key, foreign_key=c.foreign_keys, decription='')
        field.save()


def save_record(ms, table_id, session):
    take = []
    for c in session.query(ms):
        take.append(c)
    record = RecordData(table=table_id, record=take)
    record.save()

