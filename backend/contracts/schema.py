from typing import Union, Dict

GenericSchema = Dict[str, Union[str, int, float, bool, None]]

CompraSchema: GenericSchema = {
    "ean": int,
    "price": float,
    "store": int,
    "dateTime": str
}