from abc import abstractmethod
from typing import Any

from boa3.model.symbol import ISymbol
from boa3.neo.vm.type.AbiType import AbiType


class IType(ISymbol):
    """
    An interface used to represent types

    :ivar identifier: the name identifier of the type
    """
    def __init__(self, identifier: str):
        self.identifier: str = identifier

    @property
    def abi_type(self) -> AbiType:
        """
        Get the type representation for the abi

        :return: the representation for the abi. Any by default.
        """
        return AbiType.Any

    @classmethod
    @abstractmethod
    def is_type_of(cls, value: Any):
        """
        Creates a type instance with the given value

        :param value: value to build the type
        :return: The built type if the value is valid. None otherwise
        :rtype: bool
        """
        pass

    @classmethod
    @abstractmethod
    def build(cls, value: Any):
        """
        Creates a type instance with the given value

        :param value: value to build the type
        :return: The built type if the value is valid. None otherwise
        :rtype: IType or None
        """
        pass
